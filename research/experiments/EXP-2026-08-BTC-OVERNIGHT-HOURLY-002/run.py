#!/usr/bin/env python3
"""EXP-2026-08-BTC-OVERNIGHT-HOURLY-002 — offline exact-clock BTC overnight diagnostic.

Offline only. Uses cached Yahoo hourly BTC-USD bars.
Primary: exact 22:00 UTC open -> entry+2h open (00:00 next day).
Placebos: same rule for other non-overlapping 2h UTC windows via entry_ts + 2h.
B&H: gross only (no daily churn fees).
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from research.common.costs import round_trip_cost  # noqa: E402
from research.common.io import ensure_dir, write_csv, write_json, write_text  # noqa: E402
from research.common.metrics import equity_curve, metrics_from_returns  # noqa: E402
from research.common.provenance import file_sha256, git_state, utc_now_iso  # noqa: E402

try:
    import yaml  # type: ignore  # noqa: E402
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("PyYAML required for read-only config load") from exc

EXP = Path(__file__).resolve().parent
DATA = ensure_dir(EXP / "data")
CACHE_SRC = (
    ROOT
    / "research/archive/round-3-failed/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/data/btc_usd_hourly_yfinance.csv"
)
LOCAL_CACHE = DATA / "btc_usd_hourly_yfinance.csv"
FEE_GRID = [0, 1, 5, 10, 20]
ANN = 365
N_FILLS = 2
PAPER_URL = "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4081000"
HARNESS_BASELINE = "35e0ac0a96da66cec194eeaf3eda4016554d8748"
# Frozen sample bounds (must match offline cache)
CFG_START = pd.Timestamp("2024-08-30", tz="UTC")
CFG_END = pd.Timestamp("2026-07-30 23:00:00", tz="UTC")


def ensure_local_cache() -> str:
    """Copy offline source cache by SHA-256; return source sha."""
    if not CACHE_SRC.exists():
        raise FileNotFoundError(f"missing offline cache: {CACHE_SRC}")
    src_sha = file_sha256(CACHE_SRC)
    if (not LOCAL_CACHE.exists()) or file_sha256(LOCAL_CACHE) != src_sha:
        shutil.copy2(CACHE_SRC, LOCAL_CACHE)
    if file_sha256(LOCAL_CACHE) != src_sha:
        raise RuntimeError("local cache sha mismatch after copy")
    return src_sha


def load_config() -> dict:
    """Read-only config load. Never write config.yaml."""
    cfg = yaml.safe_load((EXP / "config.yaml").read_text(encoding="utf-8"))
    if not isinstance(cfg, dict):
        raise RuntimeError("config.yaml must be a mapping")
    return cfg


def load_hourly() -> pd.DataFrame:
    ensure_local_cache()
    df = pd.read_csv(LOCAL_CACHE, index_col=0, parse_dates=True)
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    else:
        df.index = df.index.tz_convert("UTC")
    df = df.sort_index()
    df.columns = [c.lower() for c in df.columns]
    need = ["open", "high", "low", "close", "volume"]
    missing = [c for c in need if c not in df.columns]
    if missing:
        raise ValueError(f"missing columns {missing}; have {df.columns.tolist()}")
    df = df[need].dropna(subset=["open", "close"])
    # Assert frozen cache matches configured sample (no wall-clock trim)
    first = df.index[0]
    last = df.index[-1]
    if first != CFG_START:
        raise RuntimeError(f"cache start {first} != configured {CFG_START}")
    if last != CFG_END:
        raise RuntimeError(f"cache end {last} != configured {CFG_END}")
    return df


def window_returns(df: pd.DataFrame, entry_hour: int) -> pd.DataFrame:
    """Exact entry_hour open -> entry+2h open. Works for same-day and cross-midnight."""
    opens = df["open"]
    # normalize to exact hour stamps only
    hour_index = opens.index[opens.index.minute == 0]
    opens = opens.loc[hour_index]
    open_map = {ts: float(px) for ts, px in opens.items()}

    rows = []
    # candidate entry days from unique dates that have the entry hour
    dates = sorted({ts.date() for ts in opens.index if ts.hour == entry_hour})
    for d in dates:
        entry_ts = pd.Timestamp(year=d.year, month=d.month, day=d.day, hour=entry_hour, tz="UTC")
        exit_ts = entry_ts + pd.Timedelta(hours=2)
        if entry_ts not in open_map or exit_ts not in open_map:
            continue
        entry_px = open_map[entry_ts]
        exit_px = open_map[exit_ts]
        if entry_px <= 0 or exit_px <= 0:
            continue
        if (exit_ts - entry_ts) != pd.Timedelta(hours=2):
            continue
        rows.append(
            {
                "date": pd.Timestamp(d),
                "entry_time": entry_ts.isoformat(),
                "exit_time": exit_ts.isoformat(),
                "entry_price": entry_px,
                "exit_price": exit_px,
                "gross_return": (exit_px / entry_px) - 1.0,
                "hold_hours": 2.0,
            }
        )
    return pd.DataFrame(rows)


def mean_bps(s: pd.Series) -> float:
    s = s.dropna().astype(float)
    return float(s.mean() * 1e4) if len(s) else float("nan")


def tstat(s: pd.Series) -> float:
    s = s.dropna().astype(float)
    if len(s) < 3:
        return float("nan")
    se = s.std(ddof=1) / np.sqrt(len(s))
    return float(s.mean() / se) if se > 0 else float("nan")


def metrics_row(name: str, window: str, fee, rets: pd.Series) -> dict:
    m = metrics_from_returns(rets, ANN)
    m.update(
        {
            "variant": name,
            "window": window,
            "fee_bps_per_fill": "" if fee is None else fee,
            "hit_rate": float((rets > 0).mean()) if len(rets) else float("nan"),
            "mean_return_bps": mean_bps(rets),
            "tstat_mean": tstat(rets),
        }
    )
    return m


def buyhold_daily_open_to_open(df: pd.DataFrame, trade_dates: pd.DatetimeIndex) -> pd.Series:
    """Gross B&H: 00:00 open -> next 00:00 open, aligned to primary trade dates."""
    opens = df["open"]
    hour0 = opens[(opens.index.minute == 0) & (opens.index.hour == 0)]
    # map date -> midnight open
    midnight = {}
    for ts, px in hour0.items():
        midnight[ts.date()] = float(px)
    rets = []
    idx = []
    for d in trade_dates:
        dd = d.date() if hasattr(d, "date") else d
        nxt = (pd.Timestamp(dd) + pd.Timedelta(days=1)).date()
        if dd not in midnight or nxt not in midnight:
            continue
        a, b = midnight[dd], midnight[nxt]
        if a <= 0 or b <= 0:
            continue
        rets.append(b / a - 1.0)
        idx.append(pd.Timestamp(dd))
    return pd.Series(rets, index=pd.DatetimeIndex(idx), name="return")


def main() -> int:
    print("EXP-2026-08-BTC-OVERNIGHT-HOURLY-002 offline")
    cfg = load_config()
    source_tree_commit = str(cfg.get("code_commit") or "")
    if not source_tree_commit or source_tree_commit == "PENDING_SOURCE_COMMIT":
        raise RuntimeError(
            "config.code_commit must be stamped to source-freeze commit S before run"
        )
    gs = git_state(ROOT)
    run_git_commit = gs.get("commit")
    dirty = bool(gs.get("dirty"))
    if dirty:
        raise RuntimeError("refusing to run with dirty git tree")
    print("source_tree_commit", source_tree_commit)
    print("run_git_commit", run_git_commit, "dirty", dirty)
    src_sha = ensure_local_cache()
    df = load_hourly()
    actual_start = str(df.index[0].date())
    actual_end = str(df.index[-1].date())
    print(f"cache bars={len(df)} {actual_start} -> {actual_end} sha={src_sha[:16]}")

    primary = window_returns(df, 22)
    if primary.empty:
        raise RuntimeError("no exact 22:00->00:00 trades found")
    # sanity: all holds exactly 2h
    if not np.allclose(primary["hold_hours"].values, 2.0):
        raise RuntimeError("primary holds not exactly 2h")
    primary_rets = pd.Series(
        primary["gross_return"].to_numpy(dtype=float),
        index=pd.DatetimeIndex(primary["date"]),
        name="return",
    )
    print(f"primary trades={len(primary_rets)}")

    bh = buyhold_daily_open_to_open(df, primary_rets.index)
    common = primary_rets.index.intersection(bh.index)
    if len(common) < 30:
        raise RuntimeError(f"too few common B&H days: {len(common)}")
    primary_rets = primary_rets.loc[common]
    bh = bh.loc[common]
    primary = primary[primary["date"].isin(common)].reset_index(drop=True)
    print(f"aligned trades={len(primary_rets)}")

    # placebos: all other entry hours 0,2,...,20
    placebo = {}
    for h in range(0, 24, 2):
        if h == 22:
            continue
        blot = window_returns(df, h)
        if blot.empty:
            print(f"  placebo {h:02d}: EMPTY")
            continue
        s = pd.Series(blot["gross_return"].to_numpy(dtype=float), index=pd.DatetimeIndex(blot["date"]))
        s = s.reindex(common).dropna()
        end_h = (h + 2) % 24
        key = f"{h:02d}-{end_h:02d}"
        placebo[key] = s
        print(f"  placebo {key}: {len(s)}")

    if len(placebo) < 8:
        raise RuntimeError(f"placebo grid too thin: {list(placebo)}")

    rows = []
    # fee arithmetic check on primary
    gmean = float(primary_rets.mean())
    for fee in FEE_GRID:
        cost = round_trip_cost(fee, N_FILLS)
        net = primary_rets - cost
        # exact fee arithmetic
        if abs(float(net.mean()) - (gmean - cost)) > 1e-12:
            raise RuntimeError("fee arithmetic failed")
        rows.append(metrics_row(f"primary_22_00_fee_{fee}bps", "22-00", fee, net))

    rows.append(metrics_row("buyhold_gross", "buyhold", None, bh))

    for wname, s in sorted(placebo.items()):
        for fee in FEE_GRID:
            cost = round_trip_cost(fee, N_FILLS)
            rows.append(metrics_row(f"placebo_{wname}_fee_{fee}bps", wname, fee, s - cost))

    metrics_df = pd.DataFrame(rows)
    preferred = [
        "variant",
        "window",
        "fee_bps_per_fill",
        "n_obs",
        "total_return",
        "cagr",
        "vol",
        "sharpe",
        "max_dd",
        "mean_return",
        "mean_return_bps",
        "hit_rate",
        "tstat_mean",
        "annualization_factor",
        "risk_free_rate",
    ]
    cols = [c for c in preferred if c in metrics_df.columns] + [
        c for c in metrics_df.columns if c not in preferred
    ]
    metrics_df = metrics_df[cols]
    write_csv(EXP / "metrics.csv", metrics_df)

    trades = primary.copy()
    for fee in FEE_GRID:
        trades[f"net_return_{fee}bps"] = trades["gross_return"] - round_trip_cost(fee, N_FILLS)
    write_csv(EXP / "trades.csv", trades)

    eq = pd.DataFrame(
        {
            "primary_22_00_fee_0bps": equity_curve(primary_rets),
            "buyhold_gross": equity_curve(bh),
        }
    )
    write_csv(EXP / "equity.csv", eq, index=True)

    period_rows = []
    for fee in FEE_GRID:
        net = primary_rets - round_trip_cost(fee, N_FILLS)
        m = metrics_row(f"primary_22_00_fee_{fee}bps", "22-00", fee, net)
        m["period"] = "full_sample_post_paper"
        period_rows.append(m)
    write_csv(EXP / "period_metrics.csv", pd.DataFrame(period_rows))

    local_sha = file_sha256(LOCAL_CACHE)
    if local_sha != src_sha:
        raise RuntimeError("local cache sha drifted from source cache")
    write_json(
        EXP / "data_manifest.json",
        {
            "manifest_generated_at_utc": utc_now_iso(),
            "retrieved_at_utc": None,
            "retrieval_note": "Original Yahoo retrieval timestamp unknown; offline copy only.",
            "provider": "yfinance",
            "instruments": ["BTC-USD"],
            "frequency": "hourly",
            "timezone": "UTC",
            "start": actual_start,
            "end": actual_end,
            "query": {
                "mode": "offline_copy",
                "source_cache": str(CACHE_SRC.relative_to(ROOT)).replace("\\", "/"),
                "source_cache_sha256": src_sha,
                "interval": "1h",
                "candle_label": "open-time",
            },
            "files": {
                "data/btc_usd_hourly_yfinance.csv": {
                    "sha256": local_sha,
                    "bytes": LOCAL_CACHE.stat().st_size,
                    "not_cached": True,
                    "local_path": "data/btc_usd_hourly_yfinance.csv",
                    "source_cache_sha256": src_sha,
                }
            },
            "notes": [
                "Offline recovery from archived worker cache; no live download.",
                "Exact entry_hour open and entry+2h open only.",
                "Sample is post-paper; cannot reproduce 2015-2021 window.",
                "Yahoo venue proxy only.",
                "B&H is gross open-to-open daily; no recurring fees.",
            ],
        },
    )

    write_json(
        EXP / "checks.json",
        {
            "passed": True,
            "checks": {
                "no_lookahead": {
                    "passed": True,
                    "detail": "entry at exact hour open; exit at entry+2h open; return=exit/entry-1",
                },
                "timezone_explicit": {"passed": True, "detail": "UTC open-time labels"},
                "data_hash_verified": {
                    "passed": True,
                    "detail": f"source={src_sha[:16]} local={local_sha[:16]}",
                },
                "cost_units_verified": {
                    "passed": True,
                    "detail": "primary/placebo: 2 fills/RT on trade days; B&H gross_only",
                },
                "annualization_verified": {
                    "passed": True,
                    "detail": "365 on daily trade observations",
                },
                "incomplete_bar_excluded": {
                    "passed": True,
                    "detail": (
                        "Frozen cache asserted exactly "
                        "2024-08-30 00:00 UTC through 2026-07-30 23:00 UTC; "
                        "no wall-clock-dependent filtering; no live retrieval"
                    ),
                },
            },
        },
    )

    m0 = metrics_df[(metrics_df["window"] == "22-00") & (metrics_df["fee_bps_per_fill"] == 0)].iloc[0]
    bh0 = metrics_df[metrics_df["variant"] == "buyhold_gross"].iloc[0]
    p0 = metrics_df[(metrics_df["fee_bps_per_fill"] == 0) & (metrics_df["window"] != "buyhold")]
    sharpes = p0.set_index("window")["sharpe"].dropna().sort_values(ascending=False)
    rank = int(list(sharpes.index).index("22-00") + 1) if "22-00" in sharpes.index else None

    summary = (
        f"Offline Yahoo hourly proxy {actual_start}→{actual_end}: exact 22:00–00:00 UTC "
        f"gross Sharpe={float(m0['sharpe']):.3f}, CAGR={float(m0['cagr']):.3%}, "
        f"mean={float(m0['mean_return_bps']):.2f}bps/day, n={int(m0['n_obs'])}. "
        f"B&H gross Sharpe={float(bh0['sharpe']):.3f}. "
        f"Primary 0bps placebo rank={rank}/{len(sharpes)}. "
        "Post-paper venue proxy only; inconclusive for source paper."
    )

    write_json(
        EXP / "verdict.json",
        {
            "experiment_id": "EXP-2026-08-BTC-OVERNIGHT-HOURLY-002",
            "strategy_id": "STRAT-CRYPTO-BTC-OVERNIGHT",
            "hypothesis": str(cfg["hypothesis"]),
            "experiment_class": "diagnostic",
            "evidence_level": "E2",
            "result_verdict": "inconclusive",
            "reproduction_status": "partial",
            "summary": summary,
            "key_metrics": {
                "primary_sharpe_0bps": float(m0["sharpe"]),
                "primary_cagr_0bps": float(m0["cagr"]),
                "primary_mean_bps_0bps": float(m0["mean_return_bps"]),
                "primary_tstat_0bps": float(m0["tstat_mean"]),
                "buyhold_sharpe_gross": float(bh0["sharpe"]),
                "n_trade_days": int(m0["n_obs"]),
                "data_start": actual_start,
                "data_end": actual_end,
                "placebo_rank_0bps": rank,
                "n_windows_ranked": int(len(sharpes)),
                "n_placebo_windows": int(len(placebo)),
                "input_cache_sha256": src_sha,
            },
            "promotion_blockers": [
                "Yahoo hourly venue proxy, not Gemini/Bitfinex",
                "Sample is post-paper (~2y); cannot reproduce 2015-2021 study window",
                "No spread/slippage/funding beyond fee grid",
                "Placebo comparisons are descriptive only",
                "E2 diagnostic ceiling; not source-faithful reproduction",
            ],
            "reviewer_status": "pending",
            "reproduction_command": (
                ".venv/Scripts/python.exe research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002/run.py"
            ),
            "sample_start": actual_start,
            "sample_end": actual_end,
            "data_frequency": "hourly",
            "code_commit": source_tree_commit,
            "run_git_commit": run_git_commit,
            "git_dirty_at_start": dirty,
            "harness_baseline_commit": HARNESS_BASELINE,
            "supersedes": "EXP-2026-08-BTC-OVERNIGHT-HOURLY-001",
            "source_paper_url": PAPER_URL,
        },
    )

    shutil.copy2(ROOT / "requirements-lock.txt", EXP / "requirements-lock.txt")
    # Config is frozen; runtime provenance lives only in verdict/manifest.

    write_text(
        EXP / "README.md",
        f"""# EXP-2026-08-BTC-OVERNIGHT-HOURLY-002

Offline exact-clock diagnostic of BTC overnight seasonality.

- **Supersedes:** EXP-2026-08-BTC-OVERNIGHT-HOURLY-001 (reviewer-rejected)
- **Paper:** {PAPER_URL}
- **Data:** offline Yahoo BTC-USD hourly open-time cache, {actual_start} → {actual_end}
- **Rule:** exact entry hour open → entry+2h open (primary 22:00→00:00)
- **Annualization:** 365 (one observation per completed trade day)
- **Costs:** fee grid {FEE_GRID} bps/fill × 2 fills on primary/placebos; B&H is **gross only**
- **Evidence:** E2 diagnostic / partial / inconclusive

## Key results (primary 0 bps)

| Metric | Value |
|--------|-------|
| Sharpe | {float(m0['sharpe']):.3f} |
| CAGR | {float(m0['cagr']):.2%} |
| Mean | {float(m0['mean_return_bps']):.2f} bps/day |
| t-stat | {float(m0['tstat_mean']):.2f} |
| N | {int(m0['n_obs'])} |
| B&H Sharpe (gross) | {float(bh0['sharpe']):.3f} |
| Placebo rank (0 bps Sharpe) | {rank}/{len(sharpes)} |
| Placebo windows produced | {len(placebo)} |

## Reproduce

```bash
.venv/Scripts/python.exe research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002/run.py
.venv/Scripts/python.exe -m research.common.validate research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002
```

## Limitations

Yahoo venue proxy; post-paper sample only; no microstructure costs beyond fee grid.
This does **not** validate or reject the original paper.
""",
    )
    print(summary)
    print("DONE BTC-002")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
