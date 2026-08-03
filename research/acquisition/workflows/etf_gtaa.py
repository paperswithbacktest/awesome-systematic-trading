"""Fixed-universe acquisition workflow for the five GTAA ETFs."""

from __future__ import annotations

import json
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from research.acquisition.core import (
    AcquisitionRecipe,
    EmptyDataError,
    RateLimitError,
    acquire_with_retries_result,
)
from research.acquisition.manifest import (
    build_manifest,
    file_sha256,
    write_manifest_once,
)
from research.acquisition.providers.stooq import (
    StooqDailyCrossCheck,
    StooqResponseError,
)
from research.acquisition.providers.yahoo import (
    YahooDailyProvider,
    yahoo_daily_request_kwargs,
)


DATASET_ID = "DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001"
GTAA_SYMBOLS = ("SPY", "EFA", "IEF", "VNQ", "GSG")
_SOURCE_DIR = "etf_gtaa_daily_001"
_COLUMNS = ("open", "high", "low", "close", "adjusted_close", "volume")
_YAHOO_START = "2007-01-01"
_YAHOO_END = "2026-08-02"
_YAHOO_TIMEOUT = 20
# Broad coverage policy (inequalities, not exact session dates — no exchange
# calendar is applied; real Yahoo edge sessions must not false-fail).
_COVERAGE_MIN_ROWS = 4500
_COVERAGE_START_ON_OR_BEFORE = "2007-01-31"
_COVERAGE_END_ON_OR_AFTER = "2026-06-01"
_COVERAGE_POLICY = (
    "Coverage thresholds check observed span/row floor only; "
    "missing_intervals not assessed (no exchange calendar)."
)
_STOOQ_CLOSE_TOLERANCE = 0.02
_STOOQ_SOURCE_FAILURES = (
    EmptyDataError,
    RateLimitError,
    StooqResponseError,
    OSError,
)
_MISSING_INTERVALS_ASSESSMENT = "not_assessed_no_exchange_calendar"
_MISSING_INTERVALS_LIMITATION = (
    "missing_intervals not assessed: no exchange holiday calendar applied; "
    "null means unknown, not zero."
)
_LIMITATIONS = [
    "The source snapshot is a source snapshot after adapter parsing, not an untouched vendor payload.",
    "Yahoo adjusted close is a provider-adjusted close proxy.",
    "Total return was not independently reconstructed from distributions and split events.",
    _MISSING_INTERVALS_LIMITATION,
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


def _validated_daily_bars(frame: pd.DataFrame, symbol: str) -> pd.DataFrame:
    """Fail closed on economically incoherent daily OHLCV bars.

    Returns the SAME frame object (validated, unmodified). Numeric coercion is
    used only for the checks; the persisted/QA'd bytes must remain the
    provider's own, otherwise rematerialization cannot hash-match a frozen
    manifest. Raises ValueError with the symbol in the message. Never writes.
    """
    missing = [column for column in _COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"{symbol} missing required columns: {missing}")
    if frame.empty:
        raise ValueError(f"{symbol} has zero bars")

    # Session-date index contract. Checked in an order that names the actual
    # violated invariant; never sort, dedupe, localize, or normalize here.
    index = frame.index
    if not isinstance(index, pd.DatetimeIndex):
        raise ValueError(f"{symbol} session_date index must be a DatetimeIndex")
    if index.hasnans:
        raise ValueError(f"{symbol} session_date index contains NaT entries")
    if index.tz is not None:
        raise ValueError(
            f"{symbol} session_date index must be timezone-naive exchange session dates"
        )
    if not index.equals(index.normalize()):
        raise ValueError(
            f"{symbol} session_date index must be midnight-normalized session dates"
        )
    if not index.is_unique:
        raise ValueError(f"{symbol} session_date index contains duplicate dates")
    if not index.is_monotonic_increasing:
        raise ValueError(f"{symbol} session_date index must be monotonic increasing")

    numeric = frame.loc[:, list(_COLUMNS)].apply(pd.to_numeric, errors="coerce")

    for column in ("open", "high", "low", "close", "adjusted_close"):
        values = numeric[column].to_numpy(dtype="float64")
        if not np.isfinite(values).all():
            raise ValueError(f"{symbol} {column} has non-finite or non-numeric values")
        if not (values > 0).all():
            raise ValueError(f"{symbol} {column} must be strictly positive on every bar")

    volume = numeric["volume"].to_numpy(dtype="float64")
    if not np.isfinite(volume).all():
        raise ValueError(f"{symbol} volume has non-finite or non-numeric values")
    if not (volume >= 0).all():
        raise ValueError(f"{symbol} volume must be nonnegative on every bar")

    oc_max = numeric[["open", "close"]].max(axis=1)
    oc_min = numeric[["open", "close"]].min(axis=1)
    if not (numeric["high"] >= oc_max).all():
        raise ValueError(f"{symbol} high is below open/close on at least one bar")
    if not (numeric["low"] <= oc_min).all():
        raise ValueError(f"{symbol} low is above open/close on at least one bar")
    if not (numeric["high"] >= numeric["low"]).all():
        raise ValueError(f"{symbol} high is below low on at least one bar")

    return frame


def _stage_csv(frame: pd.DataFrame, destination: Path) -> Path:
    """Serialize a frame to its sibling .tmp path; never to the final path."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + ".tmp")
    if temporary.exists():
        raise WorkflowIntegrityError(f"stale partial file exists: {temporary.name}")
    try:
        frame.to_csv(temporary, index=True, index_label="session_date")
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return temporary


def _write_csv_atomic(frame: pd.DataFrame, destination: Path) -> None:
    temporary = _stage_csv(frame, destination)
    try:
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


_STATE_ABSENT = "absent"
_STATE_VERIFIED = "verified"
_STATE_REMATERIALIZE = "rematerialize"


def _read_valid_manifest(manifest_path: Path, symbol: str) -> dict[str, Any]:
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - malformed evidence must fail closed
        raise WorkflowIntegrityError(f"{symbol} manifest is unreadable: {exc}") from exc
    if manifest.get("dataset_id") != DATASET_ID or manifest.get("instrument") != symbol:
        raise WorkflowIntegrityError(f"{symbol} manifest identity mismatch")
    return manifest


def _classify_symbol(root: Path, symbol: str) -> tuple[str, dict[str, Any] | None]:
    """Classify existing artifacts before any network access.

    States:
      absent        — no source, no normalized, no manifest: full acquisition.
      verified      — all three present and hash-consistent: resume without fetch.
      rematerialize — committed manifest present, BOTH gitignored data files
                      absent (normal clean-clone state): re-fetch and rewrite
                      local files only, hash-checked against the frozen manifest.
    Every other combination is corruption/orphan evidence and hard-fails.
    """
    source, normalized, manifest_path = _artifact_paths(root, symbol)
    has_source = source.exists()
    has_normalized = normalized.exists()
    has_manifest = manifest_path.exists()

    if not (has_source or has_normalized or has_manifest):
        return _STATE_ABSENT, None
    if not has_manifest:
        raise WorkflowIntegrityError(
            f"{symbol} has incomplete existing artifacts; quarantine or restore them before resuming"
        )

    manifest = _read_valid_manifest(manifest_path, symbol)
    if has_source and has_normalized:
        expected = {
            "source": (source, manifest.get("raw_file_sha256")),
            "normalized": (normalized, manifest.get("normalized_file_sha256")),
        }
        for label, (path, recorded_hash) in expected.items():
            if not recorded_hash or file_sha256(path) != recorded_hash:
                raise WorkflowIntegrityError(f"{symbol} {label} hash mismatch")
        return _STATE_VERIFIED, manifest
    if not has_source and not has_normalized:
        return _STATE_REMATERIALIZE, manifest
    raise WorkflowIntegrityError(
        f"{symbol} has incomplete existing artifacts; quarantine or restore them before resuming"
    )


def _load_normalized(root: Path, symbol: str) -> pd.DataFrame:
    _, normalized, _ = _artifact_paths(root, symbol)
    frame = pd.read_csv(normalized, parse_dates=["session_date"], index_col="session_date")
    frame.index.name = "session_date"
    return _validated_daily_bars(frame, symbol)


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
    """First-time persistence as a compensating transaction.

    Stage both CSVs, publish them while tracking what was published, then
    write the manifest. On any failure, delete the manifest this invocation
    created and every published CSV in reverse order, and clean up .tmp
    files — so the next run classifies the symbol as 'absent', not
    corruption/orphan evidence. The manifest records final repo-relative
    paths (built from published bytes via path_root), never .tmp paths.
    """
    source, normalized, manifest_path = _artifact_paths(root, symbol)
    if source.exists() or normalized.exists() or manifest_path.exists():
        raise WorkflowIntegrityError(
            f"{symbol} first-time persistence found pre-existing artifacts"
        )
    selected = frame.loc[:, list(_COLUMNS)].copy()
    selected.index.name = "session_date"

    tmp_source: Path | None = None
    tmp_normalized: Path | None = None
    published: list[Path] = []
    manifest_owned = False
    try:
        tmp_source = _stage_csv(selected, source)
        try:
            tmp_normalized = _stage_csv(selected, normalized)
        except Exception:
            tmp_source.unlink(missing_ok=True)
            tmp_source = None
            raise

        tmp_source.replace(source)
        published.append(source)
        tmp_normalized.replace(normalized)
        published.append(normalized)

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
            query_parameters=yahoo_daily_request_kwargs(
                # Exact yf.download wire kwargs from the single source of
                # truth in the provider module. End exclusivity is frozen in
                # the committed recipe, not folded into wire kwargs. This
                # describes the fixed production Yahoo request; injected test
                # doubles are contract fakes, not introspected.
                start=_YAHOO_START,
                end=_YAHOO_END,
                timeout=_YAHOO_TIMEOUT,
            ),
            rate_limit_events=rate_limit_events,
            missing_intervals=None,
            missing_intervals_assessment=_MISSING_INTERVALS_ASSESSMENT,
            known_limitations=list(_LIMITATIONS),
            license_note="Verify Yahoo Finance terms before redistribution; local research use only.",
            status="ok",
            path_root=root,
        )
        write_manifest_once(manifest_path, manifest)
        manifest_owned = True
    except Exception:
        # Only delete the manifest if THIS invocation successfully created it.
        # On FileExistsError (exclusive-create raced a foreign manifest),
        # manifest_owned stays False and the foreign file is preserved.
        if manifest_owned:
            manifest_path.unlink(missing_ok=True)
        for path in reversed(published):
            path.unlink(missing_ok=True)
        raise
    finally:
        for staged in (tmp_source, tmp_normalized):
            if staged is not None and staged.exists():
                staged.unlink()


def _rematerialize_symbol(
    *,
    root: Path,
    symbol: str,
    frame: pd.DataFrame,
    manifest: dict[str, Any],
) -> None:
    """Rewrite local gitignored data files against a frozen committed manifest.

    Transactional: both files are staged and hash-checked before either is
    published. On any mismatch both staged files are deleted, the final files
    stay absent, and the committed manifest is never touched. A hash mismatch
    means the vendor data drifted from the frozen manifest — that requires a
    new dataset ID, not a silent manifest rewrite.
    """
    source, normalized, manifest_path = _artifact_paths(root, symbol)
    del manifest_path  # rematerialization must never write the manifest
    selected = frame.loc[:, list(_COLUMNS)].copy()
    selected.index.name = "session_date"

    tmp_source: Path | None = None
    tmp_normalized: Path | None = None
    published: list[Path] = []
    try:
        tmp_source = _stage_csv(selected, source)
        try:
            tmp_normalized = _stage_csv(selected, normalized)
        except Exception:
            tmp_source.unlink(missing_ok=True)
            tmp_source = None
            raise
        for label, staged, recorded in (
            ("source", tmp_source, manifest.get("raw_file_sha256")),
            ("normalized", tmp_normalized, manifest.get("normalized_file_sha256")),
        ):
            if not recorded or file_sha256(staged) != recorded:
                raise WorkflowIntegrityError(
                    f"{symbol} {label} hash mismatch during rematerialization; "
                    "vendor data diverged from the frozen manifest"
                )
        if source.exists() or normalized.exists():
            raise WorkflowIntegrityError(
                f"{symbol} artifact reappeared during rematerialization"
            )
        tmp_source.replace(source)
        published.append(source)
        tmp_normalized.replace(normalized)
        published.append(normalized)
    except Exception:
        for path in reversed(published):
            if path.exists():
                path.unlink()
        raise
    finally:
        for staged in (tmp_source, tmp_normalized):
            if staged is not None and staged.exists():
                staged.unlink()


def _compare_stooq(
    yahoo_frames: dict[str, pd.DataFrame], stooq_provider: Any
) -> dict[str, Any]:
    try:
        stooq_frames = stooq_provider.fetch(GTAA_SYMBOLS)
    except _STOOQ_SOURCE_FAILURES as exc:
        # Genuine source failures (HTML challenge, empty data, rate limit,
        # transport) are recorded as unavailable evidence. Programming defects
        # (TypeError/KeyError/AttributeError/AssertionError) propagate.
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
        passed = bool((relative <= _STOOQ_CLOSE_TOLERANCE).mean() >= 0.95)
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
        "tolerance": _STOOQ_CLOSE_TOLERANCE,
        "overlap_rows_by_symbol": {
            symbol: int(instrument_results[symbol].get("overlap_rows", 0))
            for symbol in GTAA_SYMBOLS
        },
        "reason": None,
        "instruments": list(GTAA_SYMBOLS),
        "details": instrument_results,
    }


def _coverage_by_symbol(frames: dict[str, pd.DataFrame]) -> dict[str, dict[str, Any]]:
    """Stable per-symbol coverage facts from the validated frames, in fixed
    universe order. Derived facts only — no expectations."""
    coverage: dict[str, dict[str, Any]] = {}
    for symbol in GTAA_SYMBOLS:
        frame = frames[symbol]
        coverage[symbol] = {
            "row_count": int(len(frame)),
            "start": frame.index.min().date().isoformat(),
            "end": frame.index.max().date().isoformat(),
        }
    return coverage


def _experiment_readiness(
    coverage: dict[str, dict[str, Any]],
    cross_source: dict[str, Any],
) -> tuple[bool, list[str]]:
    """Deterministic readiness verdict with named blockers.

    Gates: per-symbol row floor + span boundaries (broad, no calendar), plus
    a passing Stooq unadjusted-close sanity check. Ready iff no blockers."""
    blockers: list[str] = []
    for symbol in GTAA_SYMBOLS:
        entry = coverage[symbol]
        if entry["row_count"] < _COVERAGE_MIN_ROWS:
            blockers.append(
                f"coverage: {symbol} row_count {entry['row_count']} below floor {_COVERAGE_MIN_ROWS}"
            )
        if entry["start"] > _COVERAGE_START_ON_OR_BEFORE:
            blockers.append(
                f"coverage: {symbol} starts {entry['start']}, later than {_COVERAGE_START_ON_OR_BEFORE}"
            )
        if entry["end"] < _COVERAGE_END_ON_OR_AFTER:
            blockers.append(
                f"coverage: {symbol} ends {entry['end']}, earlier than {_COVERAGE_END_ON_OR_AFTER}"
            )
    if not cross_source["passed"]:
        reason = cross_source.get("reason")
        suffix = f" ({reason})" if reason else ""
        blockers.append(f"stooq: {cross_source['status']}{suffix}")
    return (not blockers, blockers)


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
    blockers = report["experiment_readiness_blockers"]
    blocker_lines = (
        ["none"]
        if not blockers
        else [f"- {blocker}" for blocker in blockers]
    )
    coverage_lines = [
        f"- {symbol}: {entry['row_count']} rows, {entry['start']} → {entry['end']}"
        for symbol, entry in report["coverage_by_symbol"].items()
    ]
    return "\n".join(
        [
            f"# GTAA ETF Data QA — {DATASET_ID}",
            "",
            f"Status: **{report['status']}** (Yahoo acquisition completed for all five symbols; "
            "this is not an experiment-readiness claim)",
            "",
            f"Experiment ready: **{'yes' if report['experiment_ready'] else 'no'}**",
            "",
            "Readiness blockers:",
            *blocker_lines,
            "",
            "Per-symbol coverage (observed span/row floor only; no exchange calendar applied, "
            "missing_intervals not assessed):",
            *coverage_lines,
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
        yahoo_provider = YahooDailyProvider(
            start=_YAHOO_START,
            end=_YAHOO_END,
            timeout=_YAHOO_TIMEOUT,
        )
    if stooq_provider is None:
        if not allow_live:
            raise PermissionError("live providers require allow_live=True")
        stooq_provider = StooqDailyCrossCheck()

    # Phase A: integrity-preflight every symbol before ANY provider request.
    # An orphan, stale partial, unreadable manifest, or hash mismatch on any
    # symbol (including later ones) must hard-fail with zero network calls.
    preflight: dict[str, tuple[str, dict[str, Any] | None]] = {}
    for symbol in GTAA_SYMBOLS:
        _ensure_no_stale_partials(root, symbol)
        preflight[symbol] = _classify_symbol(root, symbol)

    # Phase B: resume verified symbols, fetch missing ones serially.
    resumed: list[str] = []
    frames: dict[str, pd.DataFrame] = {}
    for symbol in GTAA_SYMBOLS:
        state, frozen_manifest = preflight[symbol]
        if state == _STATE_VERIFIED:
            resumed.append(symbol)
            frames[symbol] = _load_normalized(root, symbol)
            continue
        if state not in (_STATE_ABSENT, _STATE_REMATERIALIZE):
            raise AssertionError(f"unexpected artifact state for {symbol}: {state}")
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
        frame = _validated_daily_bars(fetched[symbol], symbol)
        if state == _STATE_REMATERIALIZE:
            if frozen_manifest is None:
                raise AssertionError(f"{symbol} rematerialization lacks frozen manifest")
            _rematerialize_symbol(
                root=root,
                symbol=symbol,
                frame=frame,
                manifest=frozen_manifest,
            )
            # QA downstream uses the exact serialized canonical artifact whose
            # hash was verified against the frozen manifest.
            frames[symbol] = _load_normalized(root, symbol)
        else:
            _persist_symbol(
                root=root,
                symbol=symbol,
                frame=frame,
                retrieved_at_utc=retrieved_at_utc,
                rate_limit_events=acquisition.rate_limit_events,
            )
            frames[symbol] = frame

    cross_source = _compare_stooq(frames, stooq_provider)
    coverage = _coverage_by_symbol(frames)
    experiment_ready, readiness_blockers = _experiment_readiness(coverage, cross_source)
    qa_report = {
        "dataset_id": DATASET_ID,
        "status": "complete",
        "instruments": list(GTAA_SYMBOLS),
        "timezone": "America/New_York",
        "candle_label": "session-close",
        "adjustment": "yahoo-adjusted-close-proxy",
        "coverage_by_symbol": coverage,
        "coverage_policy": {
            "minimum_rows": _COVERAGE_MIN_ROWS,
            "start_on_or_before": _COVERAGE_START_ON_OR_BEFORE,
            "end_on_or_after": _COVERAGE_END_ON_OR_AFTER,
            "note": _COVERAGE_POLICY,
        },
        "experiment_ready": experiment_ready,
        "experiment_readiness_blockers": readiness_blockers,
        "cross_source_check": cross_source,
        "known_limitations": list(_LIMITATIONS),
    }
    _write_qa(root, qa_report)
    return {
        **qa_report,
        "resumed": resumed,
        "retrieved_at_utc": retrieved_at_utc,
    }
