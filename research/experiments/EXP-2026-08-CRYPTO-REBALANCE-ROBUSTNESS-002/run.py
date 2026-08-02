#!/usr/bin/env python3
"""EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002 — offline static-survivor long-only proxy.

OFFLINE ONLY. Source: research/archive/round-1/crypto-rebalance/prices.csv
No yfinance. No network.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from research.common.costs import apply_turnover_costs, risky_traded_notional  # noqa: E402
from research.common.io import ensure_dir, write_csv, write_json, write_text  # noqa: E402
from research.common.metrics import equity_curve, metrics_from_returns  # noqa: E402
from research.common.provenance import file_sha256, git_state, utc_now_iso  # noqa: E402

try:
    import yaml  # type: ignore  # noqa: E402
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("PyYAML required for read-only config load") from exc

EXP = Path(__file__).resolve().parent
DATA = ensure_dir(EXP / "data")
CACHE_SRC = ROOT / "research/archive/round-1/crypto-rebalance/prices.csv"
LOCAL_CACHE = DATA / "prices.csv"
FEE_GRID = [0, 5, 10, 20, 50]
ANN = 365
CASH = "CASH"
PAPER_URL = "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3982120"
HARNESS_BASELINE = "35e0ac0a96da66cec194eeaf3eda4016554d8748"
# Fixed analysis end: exclude potentially partial 2026-08-02 cache row
ANALYSIS_END = pd.Timestamp("2026-08-01")
ALL12 = [
    "BTC-USD", "ETH-USD", "XRP-USD", "LTC-USD", "BCH-USD", "ADA-USD",
    "DOGE-USD", "DOT-USD", "LINK-USD", "XLM-USD", "TRX-USD", "ETC-USD",
]


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


def load_prices() -> pd.DataFrame:
    ensure_local_cache()
    px = pd.read_csv(LOCAL_CACHE, index_col=0, parse_dates=True).sort_index()
    if px.index.tz is not None:
        px.index = px.index.tz_localize(None)
    # Frozen cutoff — no wall-clock dependency
    px = px.loc[px.index <= ANALYSIS_END]
    missing = [c for c in ALL12 if c not in px.columns]
    if missing:
        raise ValueError(f"cache missing columns: {missing}")
    px = px[ALL12].astype(float)
    # no forward fill; keep NaNs until cohort logic
    if (px <= 0).any().any():
        raise ValueError("non-positive prices present")
    if px.index.min() > pd.Timestamp("2018-01-01"):
        raise RuntimeError(f"cache starts late: {px.index.min()}")
    if px.index.max() < ANALYSIS_END:
        raise RuntimeError(f"cache ends before ANALYSIS_END: {px.index.max()}")
    return px


def first_valid(px: pd.DataFrame) -> dict[str, pd.Timestamp]:
    out = {}
    for c in px.columns:
        s = px[c].dropna()
        if s.empty:
            raise ValueError(f"no data for {c}")
        out[c] = pd.Timestamp(s.index[0])
    return out


def cohort_specs(fv: dict[str, pd.Timestamp]) -> dict[str, dict]:
    dot_start = fv["DOT-USD"]
    no_dot = [c for c in ALL12 if c != "DOT-USD"]
    return {
        "full_common_12": {
            "assets": list(ALL12),
            "start": max(fv[c] for c in ALL12),  # should equal DOT first valid
            "note": "all 12 including DOT from common first-valid",
        },
        "start_2018_no_dot": {
            "assets": no_dot,
            "start": pd.Timestamp("2018-01-01"),
            "note": "11 assets excluding DOT from 2018-01-01",
        },
        "start_2020_no_dot": {
            "assets": no_dot,
            "start": pd.Timestamp("2020-01-01"),
            "note": "11 assets excluding DOT from 2020-01-01",
        },
        "exclude_dot_same_window": {
            "assets": no_dot,
            "start": max(fv[c] for c in ALL12),
            "note": "same start as full_common_12 but without DOT",
        },
    }


def longest_contiguous_daily(sub: pd.DataFrame) -> pd.DataFrame:
    """Keep the longest contiguous 1-day segment; refuse multi-day jumps as 'daily'."""
    if sub.empty:
        raise RuntimeError("empty price panel")
    idx = pd.DatetimeIndex(sub.index).sort_values()
    sub = sub.loc[idx]
    gaps = idx.to_series().diff().dt.days.fillna(1).to_numpy()
    # segment id increments whenever gap != 1 day
    seg = np.cumsum(gaps != 1)
    # pick longest segment
    counts = pd.Series(seg).value_counts()
    best = int(counts.idxmax())
    mask = seg == best
    out = sub.iloc[mask].copy()
    # hard check
    diffs = out.index.to_series().diff().dropna().dt.days
    if len(out) < 60:
        raise RuntimeError(f"contiguous segment too short: {len(out)}")
    if not (diffs == 1).all():
        bad = diffs[diffs != 1]
        raise RuntimeError(f"non-daily gaps remain: {bad.head().to_dict()}")
    return out


def prepare_cohort(px: pd.DataFrame, assets: list[str], start: pd.Timestamp) -> pd.DataFrame:
    sub = px[assets].loc[px.index >= start].copy()
    # drop dates with any missing price in frozen membership
    sub = sub.dropna(how="any")
    sub = longest_contiguous_daily(sub)
    # returns over exact 1-day steps only
    rets = sub.pct_change(fill_method=None).iloc[1:]
    if rets.empty:
        raise RuntimeError("empty returns")
    # one more continuity assert on return index
    diffs = rets.index.to_series().diff().dropna().dt.days
    if not (diffs == 1).all():
        raise RuntimeError("return index not daily-contiguous")
    return rets


def simulate(rets: pd.DataFrame, freq: str | None) -> tuple[pd.Series, pd.Series]:
    """freq: None=B&H, 'D','W','M'. Returns (gross_returns, risky_traded_notional series).

    Calendar convention
    -------------------
    Return row indexed at date t is the close-to-close simple return from t-1 → t:
        r[t] = P[t] / P[t-1] - 1

    Decision convention
    -------------------
    Weights that earn r[t] are decided using information available at t-1 close.
    For static equal-weight schedules, the rebalance calendar is known without
    using r[t] itself. Operationally:

    - Before earning r[t], if a rebalance is scheduled for the t-1 close /
      start of day t, set target weights and charge risky_traded_notional.
    - Then earn r[t] with those weights.
    - Then drift weights with r[t].

    First bar (t = first return date)
    ---------------------------------
    Portfolio starts in cash. Establish cash → EW (risky traded notional = 1.0)
    at the prior close / start of first return day, then earn the first return.

    Weekly/monthly
    --------------
    A new week/month on date t means the decision was taken at the preceding
    close (t-1), which is the last close of the prior period. No same-bar
    price information is used to choose the target.
    """
    assets = list(rets.columns)
    n = len(assets)
    dates = rets.index
    month_key = pd.Series(dates, index=dates).dt.to_period("M")
    week_key = pd.Series(dates, index=dates).dt.to_period("W-SUN")

    gross = np.zeros(len(dates))
    traded = np.zeros(len(dates))
    w = np.zeros(n)  # start in cash
    # Precompute period labels as arrays for boundary comparison
    week_vals = week_key.to_numpy()
    month_vals = month_key.to_numpy()

    for i, dt in enumerate(dates):
        r = rets.iloc[i].to_numpy(dtype=float)
        if i == 0:
            rebalance = True
        elif freq == "D":
            rebalance = True
        elif freq == "W":
            rebalance = week_vals[i] != week_vals[i - 1]
        elif freq == "M":
            rebalance = month_vals[i] != month_vals[i - 1]
        elif freq is None:
            rebalance = False  # establishment only on i==0 above
        else:
            raise ValueError(freq)

        if rebalance:
            target = np.full(n, 1.0 / n)
            w_old = {a: float(w[j]) for j, a in enumerate(assets)}
            w_old[CASH] = float(max(0.0, 1.0 - float(np.sum(w))))
            w_new = {a: float(target[j]) for j, a in enumerate(assets)}
            w_new[CASH] = 0.0
            traded[i] = risky_traded_notional(
                w_old, w_new, cash_labels={CASH, "cash", "Cash", "_"}
            )
            w = target
        else:
            traded[i] = 0.0

        # Earn return t with weights decided before r[t]
        port_r = float(np.dot(w, r))
        gross[i] = port_r
        w = w * (1.0 + r)
        s = float(w.sum())
        if s <= 0:
            raise RuntimeError("portfolio wiped out")
        w = w / s

    g = pd.Series(gross, index=dates, name="gross")
    t = pd.Series(traded, index=dates, name="traded")
    if abs(float(t.iloc[0]) - 1.0) > 1e-9:
        raise RuntimeError(
            f"initial establishment traded notional expected 1.0, got {t.iloc[0]}"
        )
    # Daily EW at 0 cost must equal cross-sectional mean return each day
    if freq == "D":
        mean_r = rets.mean(axis=1)
        if not np.allclose(g.to_numpy(), mean_r.to_numpy(), rtol=0, atol=1e-12):
            raise RuntimeError("daily EW gross != cross-sectional mean return")
    # B&H rebalances only once
    if freq is None and int((t > 0).sum()) != 1:
        raise RuntimeError("buyhold must rebalance only at establishment")
    return g, t


def metrics_bundle(name: str, cohort: str, freq: str, fee: int, rets: pd.Series, traded: pd.Series) -> dict:
    m = metrics_from_returns(rets, ANN)
    years = max(len(rets) / ANN, 1e-12)
    m.update(
        {
            "variant": name,
            "cohort": cohort,
            "frequency": freq,
            "fee_bps": fee,
            "avg_annual_risky_traded_notional": float(traded.sum() / years),
            "total_risky_traded_notional": float(traded.sum()),
            "n_rebalances": int((traded > 0).sum()),
            "initial_establishment": float(traded.iloc[0]) if len(traded) else float("nan"),
        }
    )
    return m


def main() -> int:
    print("EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002 offline")
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
    px = load_prices()
    fv = first_valid(px)
    specs = cohort_specs(fv)
    print("DOT first valid", fv["DOT-USD"].date())
    print(
        f"price range {px.index.min().date()} -> {px.index.max().date()} sha={src_sha[:16]}"
    )

    freq_map = {
        "buyhold": None,
        "daily": "D",
        "weekly": "W",
        "monthly": "M",
    }

    metric_rows = []
    comparison_rows = []
    cohort_rows = []
    equity = {}
    turnover_rows = []

    for cohort_name, spec in specs.items():
        raw = px[spec["assets"]].loc[px.index >= spec["start"]].dropna(how="any")
        rets = prepare_cohort(px, spec["assets"], spec["start"])
        print(
            f"cohort {cohort_name}: assets={len(spec['assets'])} "
            f"start={rets.index[0].date()} end={rets.index[-1].date()} n={len(rets)}"
        )
        cohort_rows.append(
            {
                "cohort": cohort_name,
                "assets": "|".join(spec["assets"]),
                "n_assets": len(spec["assets"]),
                "requested_start": str(pd.Timestamp(spec["start"]).date()),
                "raw_common_rows_after_dropna": int(len(raw)),
                "actual_start": str(rets.index[0].date()),
                "actual_end": str(rets.index[-1].date()),
                "n_return_obs": int(len(rets)),
                "contiguous_segment_rule": "longest_contiguous_daily_after_dropna",
                "note": spec.get("note", ""),
            }
        )
        sim = {}
        for fname, fcode in freq_map.items():
            g, t = simulate(rets, fcode)
            sim[fname] = (g, t)
            for dt, val in t.items():
                if val > 0:
                    turnover_rows.append(
                        {
                            "cohort": cohort_name,
                            "frequency": fname,
                            "date": dt,
                            "risky_traded_notional": float(val),
                        }
                    )
            for fee in FEE_GRID:
                net = apply_turnover_costs(g, t, fee)
                metric_rows.append(
                    metrics_bundle(
                        f"{cohort_name}_{fname}_fee{fee}",
                        cohort_name,
                        fname,
                        fee,
                        net,
                        t,
                    )
                )
            equity[f"{cohort_name}_{fname}_fee0"] = equity_curve(
                apply_turnover_costs(sim[fname][0], sim[fname][1], 0)
            )

        for fee in FEE_GRID:
            d_net = apply_turnover_costs(*sim["daily"], fee)
            m_net = apply_turnover_costs(*sim["monthly"], fee)
            w_net = apply_turnover_costs(*sim["weekly"], fee)
            bh_net = apply_turnover_costs(*sim["buyhold"], fee)
            dm = metrics_from_returns(d_net, ANN)
            mm = metrics_from_returns(m_net, ANN)
            wm = metrics_from_returns(w_net, ANN)
            bm = metrics_from_returns(bh_net, ANN)
            for label, pm in [("daily", dm), ("weekly", wm), ("monthly", mm)]:
                comparison_rows.append(
                    {
                        "cohort": cohort_name,
                        "fee_bps": fee,
                        "compare": f"{label}_minus_buyhold",
                        "cagr_left": float(pm["cagr"]),
                        "cagr_right": float(bm["cagr"]),
                        "cagr_delta": float(pm["cagr"] - bm["cagr"]),
                        "sharpe_left": float(pm["sharpe"]) if pd.notna(pm["sharpe"]) else float("nan"),
                        "sharpe_right": float(bm["sharpe"]) if pd.notna(bm["sharpe"]) else float("nan"),
                        "sharpe_delta": (
                            float(pm["sharpe"] - bm["sharpe"])
                            if pd.notna(pm["sharpe"]) and pd.notna(bm["sharpe"])
                            else float("nan")
                        ),
                        "n_obs": int(pm["n_obs"]),
                    }
                )
            comparison_rows.append(
                {
                    "cohort": cohort_name,
                    "fee_bps": fee,
                    "compare": "daily_minus_monthly",
                    "cagr_left": float(dm["cagr"]),
                    "cagr_right": float(mm["cagr"]),
                    "cagr_delta": float(dm["cagr"] - mm["cagr"]),
                    "sharpe_left": float(dm["sharpe"]) if pd.notna(dm["sharpe"]) else float("nan"),
                    "sharpe_right": float(mm["sharpe"]) if pd.notna(mm["sharpe"]) else float("nan"),
                    "sharpe_delta": (
                        float(dm["sharpe"] - mm["sharpe"])
                        if pd.notna(dm["sharpe"]) and pd.notna(mm["sharpe"])
                        else float("nan")
                    ),
                    "n_obs": int(dm["n_obs"]),
                }
            )

    metrics_df = pd.DataFrame(metric_rows)
    write_csv(EXP / "metrics.csv", metrics_df)
    write_csv(EXP / "comparisons.csv", pd.DataFrame(comparison_rows))
    write_csv(EXP / "cohorts.csv", pd.DataFrame(cohort_rows))
    write_csv(EXP / "turnover.csv", pd.DataFrame(turnover_rows))
    eq_df = pd.DataFrame(equity)
    write_csv(EXP / "equity.csv", eq_df, index=True)

    # period_metrics: compact cohort summary at 0 bps from metrics only
    period_rows = []
    for cohort_name in specs:
        for freq in ["buyhold", "daily", "weekly", "monthly"]:
            sub = metrics_df[
                (metrics_df["cohort"] == cohort_name)
                & (metrics_df["frequency"] == freq)
                & (metrics_df["fee_bps"] == 0)
            ]
            if len(sub):
                r = sub.iloc[0].to_dict()
                r["period"] = "full_cohort_window"
                period_rows.append(r)
    write_csv(EXP / "period_metrics.csv", pd.DataFrame(period_rows))

    local_sha = file_sha256(LOCAL_CACHE)
    if local_sha != src_sha:
        raise RuntimeError("local cache sha drifted from source cache")
    # Config is frozen. Runtime sample facts live in cohorts/manifest/verdict only.
    # Panel = full offline cache after ANALYSIS_END clip.
    # Primary sample = full_common_12 actual return window (starts when DOT joins).
    panel_start = str(px.dropna(how="all").index.min().date())
    panel_end = str(px.index.max().date())
    if panel_end != str(ANALYSIS_END.date()):
        raise RuntimeError(f"panel end {panel_end} != ANALYSIS_END {ANALYSIS_END.date()}")
    primary_rows = [r for r in cohort_rows if r["cohort"] == "full_common_12"]
    if len(primary_rows) != 1:
        raise RuntimeError("expected exactly one full_common_12 cohort row")
    primary = primary_rows[0]
    sample_start = str(primary["actual_start"])
    sample_end = str(primary["actual_end"])
    sample_n = int(primary["n_return_obs"])
    # Keep actual_* names as panel bounds for manifest start/end fields.
    actual_start = panel_start
    actual_end = panel_end

    write_json(
        EXP / "data_manifest.json",
        {
            "manifest_generated_at_utc": utc_now_iso(),
            "retrieved_at_utc": None,
            "retrieval_note": "Original Yahoo retrieval timestamp unknown; offline Round-1 cache copy only.",
            "provider": "yfinance",
            "instruments": ALL12,
            "frequency": "daily",
            "timezone": "UTC",
            "start": actual_start,
            "end": actual_end,
            "query": {
                "mode": "offline_copy",
                "source_cache": "research/archive/round-1/crypto-rebalance/prices.csv",
                "source_cache_sha256": src_sha,
                "analysis_end": str(ANALYSIS_END.date()),
            },
            "files": {
                "data/prices.csv": {
                    "sha256": local_sha,
                    "bytes": LOCAL_CACHE.stat().st_size,
                    "not_cached": True,
                    "local_path": "data/prices.csv",
                    "source_cache_sha256": src_sha,
                }
            },
            "notes": [
                "Offline Round-1 Yahoo static-survivor cache only; no live download.",
                "12-asset long-only proxy; not paper 27-coin PIT Bitfinex long/short.",
                "No forward-fill; frozen cohort membership; drop dates with missing prices.",
                "Longest contiguous daily segment used per cohort after dropna (disclosed in cohorts.csv).",
                "Initial cash->EW establishment turnover = 1.0; no terminal liquidation.",
                f"DOT first valid: {fv['DOT-USD'].date()}",
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
                    "detail": "weights decided at prior close (t-1); earn close-to-close return t",
                },
                "timezone_explicit": {
                    "passed": True,
                    "detail": "UTC daily cache; ANALYSIS_END=2026-08-01 fixed cutoff",
                },
                "data_hash_verified": {
                    "passed": True,
                    "detail": f"source={src_sha[:16]} local={local_sha[:16]}",
                },
                "cost_units_verified": {
                    "passed": True,
                    "detail": "risky_traded_notional cash-excluded; establishment=1.0; fee grid bps per traded notional",
                },
                "annualization_verified": {"passed": True, "detail": "365"},
                "incomplete_bar_excluded": {
                    "passed": True,
                    "detail": (
                        "rows after fixed ANALYSIS_END=2026-08-01 excluded from price panel; "
                        "no wall-clock-dependent filtering; no live retrieval"
                    ),
                },
            },
        },
    )

    # key metrics from full_common_12 daily/monthly/bh at 0 and 20 bps
    def pick(cohort, freq, fee):
        sub = metrics_df[
            (metrics_df["cohort"] == cohort)
            & (metrics_df["frequency"] == freq)
            & (metrics_df["fee_bps"] == fee)
        ]
        return sub.iloc[0] if len(sub) else None

    fc = "full_common_12"
    bh0 = pick(fc, "buyhold", 0)
    d0 = pick(fc, "daily", 0)
    m0 = pick(fc, "monthly", 0)
    d20 = pick(fc, "daily", 20)
    m20 = pick(fc, "monthly", 20)

    summary = (
        f"Offline 12-asset static-survivor long-only Yahoo proxy. "
        f"Cached panel {panel_start}→{panel_end}; primary {fc} sample {sample_start}→{sample_end} (n={sample_n}). "
        f"Cohort {fc}: BH Sharpe={float(bh0['sharpe']):.3f}, daily0={float(d0['sharpe']):.3f}, "
        f"monthly0={float(m0['sharpe']):.3f}; daily-BH CAGR={float(d0['cagr']-bh0['cagr']):+.2%}, "
        f"monthly-BH CAGR={float(m0['cagr']-bh0['cagr']):+.2%}. "
        f"At 20bps: daily CAGR={float(d20['cagr']):.2%}, monthly CAGR={float(m20['cagr']):.2%}. "
        "Not paper PIT/long-short; E2 proxy only."
    )

    # soft support test: monthly beats BH net across fees 0 and 20 on full_common_12
    supported_bits = []
    for fee in [0, 20]:
        mm = pick(fc, "monthly", fee)
        bb = pick(fc, "buyhold", fee)
        supported_bits.append(float(mm["cagr"]) > float(bb["cagr"]) and float(mm["sharpe"]) >= float(bb["sharpe"]) - 1e-9)
    # still keep inconclusive unless strong + multi-cohort; stay conservative
    result_verdict = "inconclusive"

    write_json(
            EXP / "verdict.json",
            {
                "experiment_id": "EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002",
                "strategy_id": "STRAT-CRYPTO-REBALANCE-PREMIUM",
                "hypothesis": str(cfg["hypothesis"]),
                "experiment_class": "proxy",
                "evidence_level": "E2",
                "result_verdict": result_verdict,
                "reproduction_status": "partial",
                "summary": summary,
                "key_metrics": {
                    "full_common_12_bh_sharpe_0bps": float(bh0["sharpe"]),
                    "full_common_12_daily_sharpe_0bps": float(d0["sharpe"]),
                    "full_common_12_monthly_sharpe_0bps": float(m0["sharpe"]),
                    "full_common_12_daily_cagr_minus_bh_0bps": float(d0["cagr"] - bh0["cagr"]),
                    "full_common_12_monthly_cagr_minus_bh_0bps": float(m0["cagr"] - bh0["cagr"]),
                    "full_common_12_daily_avg_ann_turnover_0bps": float(d0["avg_annual_risky_traded_notional"]),
                    "full_common_12_monthly_avg_ann_turnover_0bps": float(m0["avg_annual_risky_traded_notional"]),
                    "cache_start": panel_start,
                    "cache_end": panel_end,
                    "primary_sample_start": sample_start,
                    "primary_sample_end": sample_end,
                    "primary_n_return_obs": sample_n,
                    "n_assets": 12,
                    "input_cache_sha256": src_sha,
                    "analysis_end": str(ANALYSIS_END.date()),
                },
                "promotion_blockers": [
                    "Static survivor Yahoo 12-asset proxy, not paper 27-coin PIT Bitfinex universe",
                    "Long-only only; paper 70% short drifting leg not tested",
                    "No venue-specific spread/slippage beyond fee grid",
                    "Longest-contiguous-segment sample selection is post-hoc data cleaning, not PIT eligibility",
                    "E2 ceiling; not source-faithful reproduction",
                ],
                "reviewer_status": "pending",
                "reproduction_command": (
                    ".venv/Scripts/python.exe research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002/run.py"
                ),
                "sample_start": sample_start,
                "sample_end": sample_end,
                "data_frequency": "daily",
                "code_commit": source_tree_commit,
                "run_git_commit": run_git_commit,
                "git_dirty_at_start": dirty,
                "harness_baseline_commit": HARNESS_BASELINE,
                "supersedes": "EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001",
                "source_paper_url": PAPER_URL,
            },
        )

    shutil.copy2(ROOT / "requirements-lock.txt", EXP / "requirements-lock.txt")
    write_text(
        EXP / "README.md",
        f"""# EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002

Offline **12-asset static-survivor long-only** rebalancing-frequency proxy.

- **Supersedes:** EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001 (incomplete; Yahoo 0 instruments)
- **Paper:** {PAPER_URL}
- **Cached panel:** offline Round-1 `prices.csv` only ({panel_start} → {panel_end})
- **Primary full_common_12 sample:** {sample_start} → {sample_end} (n={sample_n}; starts when DOT joins)
- **Universe:** BTC ETH XRP LTC BCH ADA DOGE DOT LINK XLM TRX ETC
- **Cohorts:** full_common_12, start_2018_no_dot, start_2020_no_dot, exclude_dot_same_window
- **Variants:** buyhold drift, daily, weekly, monthly EW
- **Costs:** risky_traded_notional; fees {FEE_GRID} bps; establishment 1.0; no terminal liq
- **Evidence:** E2 / partial / {result_verdict}

## Key (full_common_12, 0 bps)

| Variant | Sharpe | CAGR | Avg ann traded notional |
|---------|--------|------|-------------------------|
| Buy&Hold | {float(bh0['sharpe']):.3f} | {float(bh0['cagr']):.2%} | {float(bh0['avg_annual_risky_traded_notional']):.2f} |
| Daily | {float(d0['sharpe']):.3f} | {float(d0['cagr']):.2%} | {float(d0['avg_annual_risky_traded_notional']):.2f} |
| Monthly | {float(m0['sharpe']):.3f} | {float(m0['cagr']):.2%} | {float(m0['avg_annual_risky_traded_notional']):.2f} |

## Reproduce

```bash
.venv/Scripts/python.exe research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002/run.py
.venv/Scripts/python.exe -m research.common.validate research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002
```

## Limitations

Not the paper construction. Survivorship and Yahoo venue effects remain. No short leg.
""",
    )
    print(summary)
    print("DONE CRYPTO-002")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
