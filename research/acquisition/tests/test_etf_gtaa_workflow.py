"""End-to-end contracts for the deliberately narrow GTAA ETF workflow."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from research.acquisition.core import EmptyDataError, RateLimitError
from research.acquisition.manifest import file_sha256
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
        raise ValueError("Stooq response appears to be HTML, not CSV")


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


def test_default_live_providers_require_explicit_allow_live(tmp_path: Path) -> None:
    with pytest.raises(PermissionError, match="allow_live"):
        acquire_gtaa_etf_daily(
            repo_root=tmp_path,
            retrieved_at_utc="2026-08-03T02:30:00+00:00",
        )
