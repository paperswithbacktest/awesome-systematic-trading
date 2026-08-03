"""Fixed-universe acquisition workflow for the five GTAA ETFs."""

from __future__ import annotations

import json
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pandas as pd

from research.acquisition.core import (
    AcquisitionRecipe,
    acquire_with_retries_result,
)
from research.acquisition.manifest import (
    build_manifest,
    file_sha256,
    write_manifest_once,
)
from research.acquisition.providers.stooq import StooqDailyCrossCheck
from research.acquisition.providers.yahoo import YahooDailyProvider


DATASET_ID = "DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001"
GTAA_SYMBOLS = ("SPY", "EFA", "IEF", "VNQ", "GSG")
_SOURCE_DIR = "etf_gtaa_daily_001"
_COLUMNS = ("open", "high", "low", "close", "adjusted_close", "volume")
_LIMITATIONS = [
    "The source snapshot is a source snapshot after adapter parsing, not an untouched vendor payload.",
    "Yahoo adjusted close is a provider-adjusted close proxy.",
    "Total return was not independently reconstructed from distributions and split events.",
]


class WorkflowIntegrityError(RuntimeError):
    """Existing workflow artifacts cannot be trusted or safely resumed."""


def _artifact_paths(root: Path, symbol: str) -> tuple[Path, Path, Path]:
    source = (
        root
        / "research"
        / "data"
        / "raw"
        / "yahoo"
        / _SOURCE_DIR
        / f"{symbol}.source_snapshot.csv"
    )
    normalized = (
        root / "research" / "data" / "normalized" / DATASET_ID / f"{symbol}.csv"
    )
    manifest = (
        root / "research" / "data" / "manifests" / DATASET_ID / f"{symbol}.json"
    )
    return source, normalized, manifest


def _write_csv_atomic(frame: pd.DataFrame, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + ".tmp")
    if temporary.exists():
        raise WorkflowIntegrityError(f"stale partial file exists: {temporary.name}")
    try:
        frame.to_csv(temporary, index=True, index_label="session_date")
        temporary.replace(destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def _write_text_atomic(destination: Path, text: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + ".tmp")
    if temporary.exists():
        raise WorkflowIntegrityError(f"stale partial file exists: {temporary.name}")
    try:
        temporary.write_text(text, encoding="utf-8")
        temporary.replace(destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def _ensure_no_stale_partials(root: Path, symbol: str) -> None:
    for destination in _artifact_paths(root, symbol):
        temporary = destination.with_name(destination.name + ".tmp")
        if temporary.exists():
            raise WorkflowIntegrityError(
                f"stale partial file exists for {symbol}: {temporary.name}"
            )


def _verify_or_absent(root: Path, symbol: str) -> bool:
    source, normalized, manifest_path = _artifact_paths(root, symbol)
    present = (source.exists(), normalized.exists(), manifest_path.exists())
    if not any(present):
        return False
    if not all(present):
        raise WorkflowIntegrityError(
            f"{symbol} has incomplete existing artifacts; quarantine or restore them before resuming"
        )

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - malformed evidence must fail closed
        raise WorkflowIntegrityError(f"{symbol} manifest is unreadable: {exc}") from exc
    if manifest.get("dataset_id") != DATASET_ID or manifest.get("instrument") != symbol:
        raise WorkflowIntegrityError(f"{symbol} manifest identity mismatch")
    expected = {
        "source": (source, manifest.get("raw_file_sha256")),
        "normalized": (normalized, manifest.get("normalized_file_sha256")),
    }
    for label, (path, recorded_hash) in expected.items():
        if not recorded_hash or file_sha256(path) != recorded_hash:
            raise WorkflowIntegrityError(f"{symbol} {label} hash mismatch")
    return True


def _load_normalized(root: Path, symbol: str) -> pd.DataFrame:
    _, normalized, _ = _artifact_paths(root, symbol)
    frame = pd.read_csv(normalized, parse_dates=["session_date"], index_col="session_date")
    frame.index.name = "session_date"
    return frame


def _single_symbol_recipe(symbol: str) -> AcquisitionRecipe:
    return AcquisitionRecipe(
        dataset_id=DATASET_ID,
        provider="yahoo-yfinance",
        required_instruments=(symbol,),
        frequency="1d",
        timezone="America/New_York",
        candle_label="session-close",
        adjustment="yahoo-adjusted-close-proxy",
        max_attempts=3,
        backoff_seconds=(5.0, 20.0),
    )


def _persist_symbol(
    *,
    root: Path,
    symbol: str,
    frame: pd.DataFrame,
    retrieved_at_utc: str,
    rate_limit_events: int,
) -> None:
    source, normalized, manifest_path = _artifact_paths(root, symbol)
    selected = frame.loc[:, list(_COLUMNS)].copy()
    selected.index.name = "session_date"
    _write_csv_atomic(selected, source)
    _write_csv_atomic(selected, normalized)

    manifest = build_manifest(
        dataset_id=DATASET_ID,
        provider="yahoo-yfinance",
        instrument=symbol,
        venue="US ETF consolidated daily",
        frequency="1d",
        timezone="America/New_York",
        candle_label="session-close",
        adjusted="yahoo-adjusted-close-proxy",
        retrieved_at_utc=retrieved_at_utc,
        raw_path=source,
        normalized_path=normalized,
        row_count=len(selected),
        start=selected.index.min().date().isoformat(),
        end=selected.index.max().date().isoformat(),
        query_parameters={
            "start": "2007-01-01",
            "end_exclusive": "2026-08-02",
            "interval": "1d",
            "auto_adjust": False,
            "actions": True,
            "threads": False,
        },
        rate_limit_events=rate_limit_events,
        missing_intervals=[],
        known_limitations=list(_LIMITATIONS),
        license_note="Verify Yahoo Finance terms before redistribution; local research use only.",
        status="ok",
        path_root=root,
    )
    write_manifest_once(manifest_path, manifest)


def _compare_stooq(
    yahoo_frames: dict[str, pd.DataFrame], stooq_provider: Any
) -> dict[str, Any]:
    try:
        stooq_frames = stooq_provider.fetch(GTAA_SYMBOLS)
    except Exception as exc:  # noqa: BLE001 - unavailability is evidence, not dataset failure
        return {
            "status": "unavailable",
            "passed": False,
            "provider": "stooq",
            "series": "unadjusted_close",
            "reason": str(exc),
            "instruments": [],
        }

    instrument_results: dict[str, Any] = {}
    all_passed = True
    for symbol in GTAA_SYMBOLS:
        if symbol not in stooq_frames or stooq_frames[symbol].empty:
            instrument_results[symbol] = {"passed": False, "reason": "missing or empty"}
            all_passed = False
            continue
        joined = pd.concat(
            [
                yahoo_frames[symbol]["close"].rename("yahoo_close"),
                stooq_frames[symbol]["close"].rename("stooq_close"),
            ],
            axis=1,
            join="inner",
        ).dropna()
        if joined.empty:
            instrument_results[symbol] = {"passed": False, "reason": "no overlap"}
            all_passed = False
            continue
        relative = (
            (joined["yahoo_close"] - joined["stooq_close"]).abs()
            / joined["yahoo_close"].abs().clip(lower=1e-12)
        )
        passed = bool((relative <= 0.02).mean() >= 0.95)
        instrument_results[symbol] = {
            "passed": passed,
            "overlap_rows": int(len(joined)),
            "median_absolute_relative_difference": float(relative.median()),
        }
        all_passed = all_passed and passed

    return {
        "status": (
            "passed_unadjusted_sanity_check"
            if all_passed
            else "failed_unadjusted_sanity_check"
        ),
        "passed": all_passed,
        "provider": "stooq",
        "series": "unadjusted_close",
        "reason": None,
        "instruments": list(GTAA_SYMBOLS),
        "details": instrument_results,
    }


def _qa_markdown(report: dict[str, Any]) -> str:
    cross = report["cross_source_check"]
    if cross["passed"]:
        cross_text = (
            "Stooq passed an unadjusted-close sanity check. This does not validate Yahoo "
            "adjusted-close or total-return semantics."
        )
    else:
        cross_text = (
            "No independent price cross-check passed. "
            f"Stooq status: {cross['status']}; reason: {cross.get('reason') or 'comparison failed'}."
        )
    return "\n".join(
        [
            f"# GTAA ETF Data QA — {DATASET_ID}",
            "",
            f"Status: **{report['status']}**",
            "",
            "Exact universe: `SPY`, `EFA`, `IEF`, `VNQ`, `GSG`.",
            "",
            "Daily observations are exchange session dates using `America/New_York` and "
            "`session-close` semantics; no fabricated UTC intraday timestamps were added.",
            "",
            "Yahoo `adjusted_close` is a provider-adjusted close proxy, not independently "
            "reconstructed total return.",
            "",
            cross_text,
            "",
            "The persisted source snapshot is after adapter parsing and is not an untouched "
            "vendor payload.",
            "",
        ]
    )


def _write_qa(root: Path, report: dict[str, Any]) -> None:
    directory = root / "research" / "data" / "quality-reports"
    payloads = {
        directory / f"{DATASET_ID}.json": json.dumps(report, indent=2) + "\n",
        directory / f"{DATASET_ID}.md": _qa_markdown(report),
    }
    for destination, content in payloads.items():
        if destination.exists() and destination.read_text(encoding="utf-8") != content:
            raise WorkflowIntegrityError(
                f"quality report has different content: {destination.name}"
            )
    for destination, content in payloads.items():
        if not destination.exists():
            _write_text_atomic(destination, content)


def acquire_gtaa_etf_daily(
    *,
    repo_root: str | Path,
    retrieved_at_utc: str,
    yahoo_provider: Any | None = None,
    stooq_provider: Any | None = None,
    allow_live: bool = False,
    sleeper: Callable[[float], None] = time.sleep,
) -> dict[str, Any]:
    """Acquire exactly five GTAA ETFs and write QA only after full completion."""
    root = Path(repo_root).resolve()
    if yahoo_provider is None:
        if not allow_live:
            raise PermissionError("live providers require allow_live=True")
        yahoo_provider = YahooDailyProvider(start="2007-01-01", end="2026-08-02")
    if stooq_provider is None:
        if not allow_live:
            raise PermissionError("live providers require allow_live=True")
        stooq_provider = StooqDailyCrossCheck()

    resumed: list[str] = []
    frames: dict[str, pd.DataFrame] = {}
    for symbol in GTAA_SYMBOLS:
        _ensure_no_stale_partials(root, symbol)
        if _verify_or_absent(root, symbol):
            resumed.append(symbol)
            frames[symbol] = _load_normalized(root, symbol)
            continue
        recipe = _single_symbol_recipe(symbol)
        acquisition = acquire_with_retries_result(
            yahoo_provider,
            recipe,
            sleeper=sleeper,
        )
        fetched = acquisition.frames
        if set(fetched) != {symbol}:
            raise WorkflowIntegrityError(
                f"{symbol} provider response must contain exactly one requested instrument"
            )
        frame = fetched[symbol]
        _persist_symbol(
            root=root,
            symbol=symbol,
            frame=frame,
            retrieved_at_utc=retrieved_at_utc,
            rate_limit_events=acquisition.rate_limit_events,
        )
        frames[symbol] = frame

    cross_source = _compare_stooq(frames, stooq_provider)
    qa_report = {
        "dataset_id": DATASET_ID,
        "status": "complete",
        "instruments": list(GTAA_SYMBOLS),
        "timezone": "America/New_York",
        "candle_label": "session-close",
        "adjustment": "yahoo-adjusted-close-proxy",
        "cross_source_check": cross_source,
        "known_limitations": list(_LIMITATIONS),
    }
    _write_qa(root, qa_report)
    return {
        **qa_report,
        "resumed": resumed,
        "retrieved_at_utc": retrieved_at_utc,
    }
