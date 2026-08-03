"""End-to-end contracts for the deliberately narrow GTAA ETF workflow."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from research.acquisition.core import EmptyDataError, RateLimitError
from research.acquisition.manifest import file_sha256
from research.acquisition.providers.stooq import StooqResponseError
from research.acquisition.providers.yahoo import yahoo_daily_request_kwargs
from research.acquisition.workflows.etf_gtaa import (
    DATASET_ID,
    GTAA_SYMBOLS,
    WorkflowIntegrityError,
    acquire_gtaa_etf_daily,
)


def frame(offset: float = 0.0) -> pd.DataFrame:
    index = pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"])
    return pd.DataFrame(
        {
            "open": [100.0 + offset, 101.0 + offset, 102.0 + offset],
            "high": [102.0 + offset, 103.0 + offset, 104.0 + offset],
            "low": [99.0 + offset, 100.0 + offset, 101.0 + offset],
            "close": [101.0 + offset, 102.0 + offset, 103.0 + offset],
            "adjusted_close": [98.0 + offset, 99.0 + offset, 100.0 + offset],
            "volume": [1000, 1100, 1200],
        },
        index=index,
    ).rename_axis("session_date")


class DeterministicYahoo:
    """Stable per-symbol frames independent of call order — required for the
    rematerialize contract, where re-fetched bytes must hash-match the frozen
    manifest."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, ...]] = []

    def fetch(self, recipe):
        self.calls.append(recipe.required_instruments)
        symbol = recipe.required_instruments[0]
        return {symbol: frame(float(GTAA_SYMBOLS.index(symbol) + 1))}


class RecordingYahoo:
    def __init__(self, *, empty_symbol: str | None = None) -> None:
        self.calls: list[tuple[str, ...]] = []
        self.empty_symbol = empty_symbol

    def fetch(self, recipe):  # type intentionally matches provider protocol
        self.calls.append(recipe.required_instruments)
        symbol = recipe.required_instruments[0]
        if symbol == self.empty_symbol:
            return {symbol: pd.DataFrame()}
        return {symbol: frame(float(len(self.calls)))}


class MatchingStooq:
    def fetch(self, symbols):
        return {
            symbol: frame(float(index + 1)).drop(columns=["adjusted_close"])
            for index, symbol in enumerate(symbols)
        }


class UnavailableStooq:
    def fetch(self, _symbols):
        raise StooqResponseError("Stooq response appears to be HTML, not CSV")


class BuggyStooq:
    def fetch(self, _symbols):
        raise TypeError("internal programming defect, not source unavailability")


class RateLimitedOnceYahoo(RecordingYahoo):
    def __init__(self) -> None:
        super().__init__()
        self.rate_limited = False

    def fetch(self, recipe):
        symbol = recipe.required_instruments[0]
        if symbol == "SPY" and not self.rate_limited:
            self.rate_limited = True
            self.calls.append(recipe.required_instruments)
            raise RateLimitError("429")
        return super().fetch(recipe)


def run(tmp_path: Path, yahoo, stooq=None):
    return acquire_gtaa_etf_daily(
        repo_root=tmp_path,
        retrieved_at_utc="2026-08-03T02:30:00+00:00",
        yahoo_provider=yahoo,
        stooq_provider=stooq,
    )


def _long_frame() -> pd.DataFrame:
    """Business-day coverage spanning nearly the full frozen request window
    (2007-01-03 → 2026-07-31): genuinely sufficient, not a 750-day stub."""
    index = pd.date_range("2007-01-03", "2026-07-31", freq="B", name="session_date")
    base = pd.Series(range(len(index)), index=index, dtype="float64")
    return pd.DataFrame(
        {
            "open": 100.0 + base,
            "high": 102.0 + base,
            "low": 99.0 + base,
            "close": 101.0 + base,
            "adjusted_close": 98.0 + base,
            "volume": pd.Series(1000, index=index, dtype="int64"),
        },
        index=index,
    )


class LongYahoo:
    """Full-window per-symbol frames."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, ...]] = []

    def fetch(self, recipe):
        symbol = recipe.required_instruments[0]
        self.calls.append(recipe.required_instruments)
        return {symbol: _long_frame()}


class LongStooq:
    """Unadjusted-close mirror of the long Yahoo frames."""

    def fetch(self, symbols):
        return {symbol: _long_frame().drop(columns=["adjusted_close"]) for symbol in symbols}


def _qa_for(run_root: Path, yahoo, stooq) -> dict:
    result = acquire_gtaa_etf_daily(
        repo_root=run_root,
        retrieved_at_utc="2026-08-03T02:30:00+00:00",
        yahoo_provider=yahoo,
        stooq_provider=stooq,
    )
    assert result["status"] == "complete"
    qa_path = run_root / "research/data/quality-reports" / f"{DATASET_ID}.json"
    return json.loads(qa_path.read_text(encoding="utf-8"))


def _bad_index_frame(kind: str) -> pd.DataFrame:
    dates = pd.to_datetime(["2024-01-02", "2024-01-03", "2024-01-04"])
    if kind == "nat":
        index = pd.DatetimeIndex([dates[0], pd.NaT, dates[2]])
    elif kind == "duplicate":
        index = pd.to_datetime(["2024-01-02", "2024-01-02", "2024-01-04"])
    elif kind == "unordered":
        index = pd.to_datetime(["2024-01-02", "2024-01-04", "2024-01-03"])
    elif kind == "tz_aware":
        index = dates.tz_localize("America/New_York")
    elif kind == "intraday":
        index = pd.to_datetime(
            ["2024-01-02 09:30", "2024-01-03 09:30", "2024-01-04 09:30"]
        )
    else:
        raise AssertionError(f"unknown bad-index kind: {kind}")
    return pd.DataFrame(
        {
            "open": [100.0, 101.0, 102.0],
            "high": [102.0, 103.0, 104.0],
            "low": [99.0, 100.0, 101.0],
            "close": [101.0, 102.0, 103.0],
            "adjusted_close": [98.0, 99.0, 100.0],
            "volume": [1000, 1100, 1200],
        },
        index=index,
    ).rename_axis("session_date")


@pytest.mark.parametrize(
    ("kind", "reason"),
    [
        ("nat", "NaT"),
        ("duplicate", "duplicate"),
        ("unordered", "monotonic"),
        ("tz_aware", "timezone-naive"),
        ("intraday", "midnight"),
    ],
)
def test_invalid_session_index_fails_before_any_write(
    tmp_path: Path, kind: str, reason: str
) -> None:
    """Session-date contract violations must hard-fail at the first fetch,
    before persistence and before any later-symbol network call:

    - NaT index entries (bad index, not bad rows)
    - duplicate session dates
    - non-monotonic index
    - timezone-aware index (session dates are tz-naive exchange dates)
    - intraday timestamps (session dates are midnight-normalized dates)

    The error names the symbol AND the violated invariant, so an accidental
    downstream ValueError cannot satisfy this test. The frame is never
    coerced (persist must write provider bytes for rematerialization)."""
    bad = _bad_index_frame(kind)

    class BadIndexYahoo:
        def __init__(self) -> None:
            self.calls: list[tuple[str, ...]] = []

        def fetch(self, recipe):
            symbol = recipe.required_instruments[0]
            self.calls.append(recipe.required_instruments)
            return {symbol: bad if symbol == "SPY" else frame()}

    yahoo = BadIndexYahoo()
    with pytest.raises(ValueError, match=rf"SPY.*{reason}"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == [("SPY",)], (
        "index violation must stop the run at the first symbol, before later fetches"
    )
    assert list(tmp_path.rglob("*.csv")) == []
    assert list(tmp_path.rglob("*.json")) == []
    assert list(tmp_path.rglob("*.tmp")) == []


def test_qa_marks_short_coverage_not_ready_even_when_stooq_passes(tmp_path: Path) -> None:
    """A 3-session fixture against a 2007–2026 request is grossly insufficient
    coverage, so a passing Stooq cross-check alone can NEVER mark the dataset
    experiment-ready. This is the anti-tautology case: readiness is gated on
    coverage, not just on the cross-check boolean."""
    qa = _qa_for(tmp_path / "run", RecordingYahoo(), MatchingStooq())

    coverage = qa["coverage_by_symbol"]
    assert list(coverage) == list(GTAA_SYMBOLS)
    for symbol in GTAA_SYMBOLS:
        entry = coverage[symbol]
        assert entry["row_count"] == 3
        assert entry["start"] == "2024-01-02"
        assert entry["end"] == "2024-01-04"

    assert qa["experiment_ready"] is False
    blockers = qa["experiment_readiness_blockers"]
    assert any("coverage" in blocker.lower() for blocker in blockers), (
        "insufficient coverage must be named as a readiness blocker even when Stooq passes"
    )
    # Stooq passed, so it must NOT be listed as a blocker here.
    assert not any("stooq" in blocker.lower() for blocker in blockers)


def test_qa_marks_stooq_unavailable_not_ready_with_named_blocker(tmp_path: Path) -> None:
    """Stooq unavailability is itself a blocker; combined with insufficient
    coverage both must be named. Stooq must never be silently treated as a
    pass to reach readiness."""
    qa = _qa_for(tmp_path / "run", RecordingYahoo(), UnavailableStooq())

    assert qa["experiment_ready"] is False
    blockers = qa["experiment_readiness_blockers"]
    assert any("stooq" in blocker.lower() for blocker in blockers)
    assert any("coverage" in blocker.lower() for blocker in blockers)


def test_qa_marks_full_window_coverage_and_passing_stooq_ready(tmp_path: Path) -> None:
    """The only path to experiment_ready=True: every symbol has full-window
    coverage (start/end boundaries + row floor from shared workflow constants)
    AND a passing Stooq cross-check AND no blockers. Frozen QA must exclude
    volatile invocation fields (resumed, retrieved_at_utc)."""
    from research.acquisition.workflows import etf_gtaa as workflow_module

    qa = _qa_for(tmp_path / "run", LongYahoo(), LongStooq())

    coverage = qa["coverage_by_symbol"]
    assert list(coverage) == list(GTAA_SYMBOLS)
    expected_rows = len(_long_frame())
    for symbol in GTAA_SYMBOLS:
        entry = coverage[symbol]
        assert entry["row_count"] == expected_rows
        assert entry["row_count"] >= workflow_module._COVERAGE_MIN_ROWS
        assert entry["start"] == "2007-01-03"
        assert entry["end"] == "2026-07-31"

    assert qa["experiment_ready"] is True
    assert qa["experiment_readiness_blockers"] == []
    assert "resumed" not in qa
    assert "retrieved_at_utc" not in qa


def test_manifest_declares_missing_intervals_not_assessed(tmp_path: Path) -> None:
    """Without an authoritative exchange calendar, the workflow CANNOT
    distinguish a missing trading session from a weekend/holiday/suspension.
    So it must never freeze missing_intervals=[] (a false completeness claim)
    nor fabricate dates. The honest contract: null = unknown, paired with an
    explicit assessment declaration and limitation — identical for every
    symbol, whether or not its index has visible discontinuities."""
    run(tmp_path, RecordingYahoo(), MatchingStooq())

    limitation = (
        "missing_intervals not assessed: no exchange holiday calendar applied; "
        "null means unknown, not zero."
    )
    for symbol in GTAA_SYMBOLS:
        manifest_path = tmp_path / "research/data/manifests" / DATASET_ID / f"{symbol}.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert manifest["missing_intervals"] is None, (
            f"{symbol} must not claim [] without an exchange calendar"
        )
        assert manifest["missing_intervals_assessment"] == "not_assessed_no_exchange_calendar"
        assert limitation in manifest["known_limitations"]


def test_manifest_query_parameters_match_yahoo_wire_kwargs_exactly(tmp_path: Path) -> None:
    """Manifest provenance must describe the request actually issued: the same
    kwargs YahooDailyProvider passes to yf.download, verbatim — never a
    renamed wire key, never dropped keys. End exclusivity lives in the
    committed recipe, not in wire parameters."""
    run(tmp_path, RecordingYahoo(), MatchingStooq())

    for symbol in GTAA_SYMBOLS:
        manifest_path = (
            tmp_path
            / "research/data/manifests"
            / DATASET_ID
            / f"{symbol}.json"
        )
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        # query_parameters holds the exact yf.download wire kwargs only — no
        # renamed keys, no dropped keys, no semantics folded in. End
        # exclusivity is frozen in the committed recipe, not repeated here.
        assert manifest["query_parameters"] == yahoo_daily_request_kwargs(
            start="2007-01-01",
            end="2026-08-02",
            timeout=20,
        ), f"{symbol} manifest query_parameters drifted from Yahoo wire kwargs"
        assert "end_semantics" not in manifest["query_parameters"]


def test_workflow_enforces_exact_universe_and_persists_each_symbol(tmp_path: Path) -> None:
    yahoo = RecordingYahoo()

    result = run(tmp_path, yahoo, MatchingStooq())

    assert GTAA_SYMBOLS == ("SPY", "EFA", "IEF", "VNQ", "GSG")
    assert yahoo.calls == [(symbol,) for symbol in GTAA_SYMBOLS]
    assert result["dataset_id"] == DATASET_ID
    assert result["status"] == "complete"
    assert result["instruments"] == list(GTAA_SYMBOLS)

    for symbol in GTAA_SYMBOLS:
        source = (
            tmp_path
            / "research/data/raw/yahoo/etf_gtaa_daily_001"
            / f"{symbol}.source_snapshot.csv"
        )
        normalized = (
            tmp_path / "research/data/normalized" / DATASET_ID / f"{symbol}.csv"
        )
        manifest_path = (
            tmp_path / "research/data/manifests" / DATASET_ID / f"{symbol}.json"
        )
        assert source.exists()
        assert normalized.exists()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert manifest["instrument"] == symbol
        assert manifest["raw_file_sha256"] == file_sha256(source)
        assert manifest["normalized_file_sha256"] == file_sha256(normalized)
        assert manifest["raw_file"].startswith("research/data/raw/")
        assert manifest["normalized_file"].startswith("research/data/normalized/")
        assert str(tmp_path) not in json.dumps(manifest)
        assert "source snapshot after adapter parsing" in " ".join(
            manifest["known_limitations"]
        )


def test_partial_failure_keeps_completed_symbols_but_never_marks_dataset_complete(
    tmp_path: Path,
) -> None:
    yahoo = RecordingYahoo(empty_symbol="EFA")

    with pytest.raises(EmptyDataError, match="EFA"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == [("SPY",), ("EFA",)]
    assert (
        tmp_path / "research/data/manifests" / DATASET_ID / "SPY.json"
    ).exists()
    assert not (
        tmp_path / "research/data/manifests" / DATASET_ID / "EFA.json"
    ).exists()
    assert not (
        tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.json"
    ).exists()


def test_verified_resume_skips_existing_symbols_without_network(tmp_path: Path) -> None:
    first = RecordingYahoo()
    run(tmp_path, first, MatchingStooq())
    second = RecordingYahoo()

    result = run(tmp_path, second, MatchingStooq())

    assert second.calls == []
    assert result["resumed"] == list(GTAA_SYMBOLS)
    qa = json.loads(
        (
            tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.json"
        ).read_text(encoding="utf-8")
    )
    assert "resumed" not in qa
    assert "retrieved_at_utc" not in qa


def test_resume_hash_mismatch_hard_fails_without_overwrite(tmp_path: Path) -> None:
    run(tmp_path, RecordingYahoo(), MatchingStooq())
    normalized = tmp_path / "research/data/normalized" / DATASET_ID / "EFA.csv"
    normalized.write_text("corrupted\n", encoding="utf-8")
    yahoo = RecordingYahoo()

    with pytest.raises(WorkflowIntegrityError, match="EFA.*hash"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == []
    assert normalized.read_text(encoding="utf-8") == "corrupted\n"


def test_manifest_only_state_rematerializes_files_locally(tmp_path: Path) -> None:
    """Clean-clone simulation: committed manifest exists, gitignored data files absent.

    This is the normal state on a fresh checkout after manifests were committed.
    It must NOT be treated as corruption. The workflow re-materializes the local
    raw/normalized files (no Yahoo network needed if provider returns data) but
    must never rewrite the committed manifest under the same dataset ID.
    """
    first = DeterministicYahoo()
    run(tmp_path, first, MatchingStooq())

    # Simulate clean clone: delete the gitignored local data files, keep manifests.
    manifest_dir = tmp_path / "research/data/manifests" / DATASET_ID
    for symbol in GTAA_SYMBOLS:
        (tmp_path / "research/data/raw/yahoo/etf_gtaa_daily_001"
         / f"{symbol}.source_snapshot.csv").unlink()
        (tmp_path / "research/data/normalized" / DATASET_ID
         / f"{symbol}.csv").unlink()

    frozen_manifests = {
        symbol: (manifest_dir / f"{symbol}.json").read_text(encoding="utf-8")
        for symbol in GTAA_SYMBOLS
    }

    second = DeterministicYahoo()
    result = run(tmp_path, second, MatchingStooq())

    # Every symbol was missing locally, so all five are re-fetched.
    assert second.calls == [(symbol,) for symbol in GTAA_SYMBOLS]

    # Data files re-materialized locally; committed manifests untouched.
    for symbol in GTAA_SYMBOLS:
        assert (tmp_path / "research/data/normalized" / DATASET_ID
                / f"{symbol}.csv").exists()
        assert (manifest_dir / f"{symbol}.json").read_text(encoding="utf-8") \
            == frozen_manifests[symbol]
    assert result["status"] == "complete"


def test_manifest_hash_mismatch_on_rematerialize_hard_fails(tmp_path: Path) -> None:
    """If a re-materialized file's hash no longer matches the frozen manifest,
    the vendor data has drifted. That is a provenance divergence, not corruption:
    hard-fail and require a new dataset ID rather than silently overwriting
    the committed manifest or local file."""
    run(tmp_path, DeterministicYahoo(), MatchingStooq())

    normalized = tmp_path / "research/data/normalized" / DATASET_ID / "SPY.csv"
    raw = tmp_path / "research/data/raw/yahoo/etf_gtaa_daily_001" / "SPY.source_snapshot.csv"
    normalized.unlink()
    raw.unlink()

    # Provider returns DIFFERENT data than the frozen manifest records.
    class DriftedYahoo:
        def fetch(self, recipe):
            return {recipe.required_instruments[0]: frame(999.0)}

    with pytest.raises(WorkflowIntegrityError, match="SPY.*hash"):
        run(tmp_path, DriftedYahoo(), MatchingStooq())

    # Manifest must not have been overwritten.
    manifest = tmp_path / "research/data/manifests" / DATASET_ID / "SPY.json"
    assert manifest.exists()


def test_unavailable_stooq_is_recorded_as_limitation_not_crosscheck_pass(
    tmp_path: Path,
) -> None:
    result = run(tmp_path, RecordingYahoo(), UnavailableStooq())

    assert result["cross_source_check"]["status"] == "unavailable"
    qa_json = json.loads(
        (
            tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.json"
        ).read_text(encoding="utf-8")
    )
    qa_md = (
        tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.md"
    ).read_text(encoding="utf-8")
    assert qa_json["cross_source_check"]["status"] == "unavailable"
    assert qa_json["cross_source_check"]["passed"] is False
    assert "HTML" in qa_json["cross_source_check"]["reason"]
    assert "No independent price cross-check passed" in qa_md
    assert "provider-adjusted close proxy" in qa_md
    assert "not independently reconstructed total return" in qa_md
    assert "America/New_York" in qa_md
    assert "session-close" in qa_md
    assert str(tmp_path) not in qa_md


def test_matching_stooq_checks_unadjusted_close_only(tmp_path: Path) -> None:
    result = run(tmp_path, RecordingYahoo(), MatchingStooq())

    check = result["cross_source_check"]
    assert check["status"] == "passed_unadjusted_sanity_check"
    assert check["passed"] is True
    assert check["series"] == "unadjusted_close"
    assert set(check["instruments"]) == set(GTAA_SYMBOLS)
    assert check["overlap_rows_by_symbol"]["SPY"] > 0
    assert check["tolerance"] == 0.02


def test_recovered_rate_limit_is_recorded_in_symbol_manifest(tmp_path: Path) -> None:
    yahoo = RateLimitedOnceYahoo()

    acquire_gtaa_etf_daily(
        repo_root=tmp_path,
        retrieved_at_utc="2026-08-03T02:30:00+00:00",
        yahoo_provider=yahoo,
        stooq_provider=MatchingStooq(),
        sleeper=lambda _: None,
    )

    manifest_dir = tmp_path / "research/data/manifests" / DATASET_ID
    spy = json.loads((manifest_dir / "SPY.json").read_text(encoding="utf-8"))
    efa = json.loads((manifest_dir / "EFA.json").read_text(encoding="utf-8"))
    assert spy["rate_limit_events"] == 1
    assert efa["rate_limit_events"] == 0


def test_qa_is_write_once_and_divergent_resume_hard_fails(tmp_path: Path) -> None:
    run(tmp_path, RecordingYahoo(), MatchingStooq())
    qa = tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.json"
    original = qa.read_text(encoding="utf-8")

    with pytest.raises(WorkflowIntegrityError, match="quality report.*different content"):
        acquire_gtaa_etf_daily(
            repo_root=tmp_path,
            retrieved_at_utc="2026-08-03T03:30:00+00:00",
            yahoo_provider=RecordingYahoo(),
            stooq_provider=UnavailableStooq(),
        )

    assert qa.read_text(encoding="utf-8") == original


def test_orphaned_artifact_hard_fails_before_network(tmp_path: Path) -> None:
    source = (
        tmp_path
        / "research/data/raw/yahoo/etf_gtaa_daily_001"
        / "SPY.source_snapshot.csv"
    )
    source.parent.mkdir(parents=True)
    source.write_text("orphan\n", encoding="utf-8")
    yahoo = RecordingYahoo()

    with pytest.raises(WorkflowIntegrityError, match="SPY.*incomplete"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == []
    assert source.read_text(encoding="utf-8") == "orphan\n"


def test_failed_manifest_write_leaves_no_orphaned_artifacts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """If manifest publication fails after CSVs were staged, first-time
    persistence must roll back: no final source, no final normalized, no
    manifest, and no leftover .tmp files. The next run must see 'absent',
    not corruption."""
    import research.acquisition.workflows.etf_gtaa as wf

    def boom(_path, _manifest):
        raise OSError("simulated manifest-write failure")

    monkeypatch.setattr(wf, "write_manifest_once", boom)
    with pytest.raises(OSError, match="manifest-write failure"):
        run(tmp_path, RecordingYahoo(), MatchingStooq())

    source = (
        tmp_path / "research/data/raw/yahoo/etf_gtaa_daily_001"
        / "SPY.source_snapshot.csv"
    )
    normalized = tmp_path / "research/data/normalized" / DATASET_ID / "SPY.csv"
    manifest = tmp_path / "research/data/manifests" / DATASET_ID / "SPY.json"
    assert not source.exists()
    assert not normalized.exists()
    assert not manifest.exists()
    leftovers = list(tmp_path.rglob("*.tmp"))
    assert leftovers == []


def test_failed_persist_never_deletes_manifest_it_did_not_create(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """If a manifest already exists at the target path (e.g., created by a
    concurrent process after our pre-existence guard ran), write_manifest_once
    raises FileExistsError from its exclusive create. Rollback must NOT delete
    that manifest — we don't own it. Published CSVs are still rolled back."""
    import research.acquisition.workflows.etf_gtaa as wf

    real_write = wf.write_manifest_once
    manifest_dir = tmp_path / "research/data/manifests" / DATASET_ID

    def interfering_write(path, manifest):
        # Simulate another process winning the race: create a manifest we do
        # not own, then invoke the real exclusive create (which must raise).
        manifest_dir.mkdir(parents=True, exist_ok=True)
        foreign = manifest_dir / "SPY.json"
        foreign.write_text('{"dataset_id": "foreign-owner"}\n', encoding="utf-8")
        return real_write(path, manifest)

    monkeypatch.setattr(wf, "write_manifest_once", interfering_write)
    with pytest.raises(FileExistsError):
        run(tmp_path, RecordingYahoo(), MatchingStooq())

    foreign = manifest_dir / "SPY.json"
    assert foreign.read_text(encoding="utf-8") == '{"dataset_id": "foreign-owner"}\n'
    source = (
        tmp_path / "research/data/raw/yahoo/etf_gtaa_daily_001"
        / "SPY.source_snapshot.csv"
    )
    normalized = tmp_path / "research/data/normalized" / DATASET_ID / "SPY.csv"
    assert not source.exists()
    assert not normalized.exists()
    assert list(tmp_path.rglob("*.tmp")) == []


def bad_frame(**overrides: float) -> pd.DataFrame:
    values = {
        "open": 100.0,
        "high": 102.0,
        "low": 99.0,
        "close": 101.0,
        "adjusted_close": 98.0,
        "volume": 1000.0,
    }
    values.update(overrides)
    index = pd.to_datetime(["2024-01-02"])
    return pd.DataFrame(
        {column: [value] for column, value in values.items()}, index=index
    ).rename_axis("session_date")


class BadFrameYahoo:
    def __init__(self, bad: pd.DataFrame) -> None:
        self.bad = bad

    def fetch(self, recipe):
        return {recipe.required_instruments[0]: self.bad}


@pytest.mark.parametrize(
    "overrides",
    [
        {"close": 0.0},
        {"close": -5.0},
        {"close": float("nan")},
        {"open": float("inf")},
        {"volume": -1.0},
        {"high": 100.5},  # high < close(101): high must cover open/close
        {"low": 100.5},  # low > open(100): low must not exceed open/close
        {"adjusted_close": float("nan")},
        {"adjusted_close": 0.0},
    ],
    ids=[
        "close-zero",
        "close-negative",
        "close-nan",
        "open-infinite",
        "volume-negative",
        "high-below-close",
        "low-above-open",
        "adjusted-close-nan",
        "adjusted-close-zero",
    ],
)
def test_economically_incoherent_bars_fail_before_any_persistence(
    tmp_path: Path, overrides: dict
) -> None:
    yahoo = BadFrameYahoo(bad_frame(**overrides))

    with pytest.raises((ValueError, WorkflowIntegrityError), match="SPY"):
        run(tmp_path, yahoo, MatchingStooq())

    base = tmp_path / "research/data"
    assert list(base.rglob("SPY*")) == []


def test_manifest_plus_one_data_file_hard_fails_before_network(tmp_path: Path) -> None:
    """manifest + exactly one data file (source present, normalized absent) is
    corruption/orphan evidence — not a clean clone — and must hard-fail with
    zero provider calls."""
    manifest_dir = tmp_path / "research/data/manifests" / DATASET_ID
    manifest_dir.mkdir(parents=True)
    (manifest_dir / "SPY.json").write_text(
        json.dumps({"dataset_id": DATASET_ID, "instrument": "SPY"}),
        encoding="utf-8",
    )
    source = (
        tmp_path / "research/data/raw/yahoo/etf_gtaa_daily_001"
        / "SPY.source_snapshot.csv"
    )
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("stray\n", encoding="utf-8")
    yahoo = RecordingYahoo()

    with pytest.raises(WorkflowIntegrityError, match="SPY.*incomplete"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == []
    assert source.read_text(encoding="utf-8") == "stray\n"


def test_stale_partial_file_hard_fails_without_overwrite(tmp_path: Path) -> None:
    temporary = (
        tmp_path
        / "research/data/raw/yahoo/etf_gtaa_daily_001"
        / "SPY.source_snapshot.csv.tmp"
    )
    temporary.parent.mkdir(parents=True)
    temporary.write_text("partial\n", encoding="utf-8")
    yahoo = RecordingYahoo()

    with pytest.raises(WorkflowIntegrityError, match="stale partial.*SPY"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == []
    assert temporary.read_text(encoding="utf-8") == "partial\n"


def test_failed_csv_serialization_leaves_no_tmp_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """If DataFrame.to_csv raises mid-staging (e.g., disk error, encoding),
    the .tmp file must be removed by the staging helper itself — the caller
    cannot clean a path that was never returned."""
    import research.acquisition.workflows.etf_gtaa as wf

    real_to_csv = pd.DataFrame.to_csv

    def exploding_to_csv(self, path_or_buf, *args, **kwargs):
        # Write partial garbage then raise, simulating an interrupted write.
        if str(path_or_buf).endswith(".tmp"):
            with open(path_or_buf, "w") as fh:
                fh.write("partial-garbage\n")
            raise OSError("simulated to_csv failure")
        return real_to_csv(self, path_or_buf, *args, **kwargs)

    monkeypatch.setattr(pd.DataFrame, "to_csv", exploding_to_csv)
    with pytest.raises(OSError, match="to_csv failure"):
        run(tmp_path, RecordingYahoo(), MatchingStooq())

    assert list(tmp_path.rglob("*.tmp")) == []


def test_later_symbol_orphan_blocks_all_network(tmp_path: Path) -> None:
    source = (
        tmp_path
        / "research/data/raw/yahoo/etf_gtaa_daily_001"
        / "GSG.source_snapshot.csv"
    )
    source.parent.mkdir(parents=True)
    source.write_text("orphan\n", encoding="utf-8")
    yahoo = RecordingYahoo()

    with pytest.raises(WorkflowIntegrityError, match="GSG.*incomplete"):
        run(tmp_path, yahoo, MatchingStooq())

    assert yahoo.calls == []


def test_stooq_internal_bug_is_not_marked_unavailable(tmp_path: Path) -> None:
    with pytest.raises(TypeError, match="internal programming defect"):
        run(tmp_path, RecordingYahoo(), BuggyStooq())

    qa_json_path = (
        tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.json"
    )
    assert not qa_json_path.exists() or (
        json.loads(qa_json_path.read_text(encoding="utf-8"))
        ["cross_source_check"]["status"]
        != "unavailable"
    )


class InternalValueErrorStooq:
    def fetch(self, _symbols):
        raise ValueError("off-by-one bug in my own comparison code")


def test_stooq_internal_value_error_is_not_marked_unavailable(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="off-by-one bug"):
        run(tmp_path, RecordingYahoo(), InternalValueErrorStooq())

    qa_json_path = (
        tmp_path / "research/data/quality-reports" / f"{DATASET_ID}.json"
    )
    assert not qa_json_path.exists() or (
        json.loads(qa_json_path.read_text(encoding="utf-8"))
        ["cross_source_check"]["status"]
        != "unavailable"
    )


def test_default_live_providers_require_explicit_allow_live(tmp_path: Path) -> None:
    with pytest.raises(PermissionError, match="allow_live"):
        acquire_gtaa_etf_daily(
            repo_root=tmp_path,
            retrieved_at_utc="2026-08-03T02:30:00+00:00",
        )
