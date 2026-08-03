"""Tests for immutable acquisition manifests and quarantine records."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from research.acquisition.manifest import (
    build_manifest,
    file_sha256,
    quarantine_file,
    write_manifest_once,
)


def test_manifest_links_raw_and_normalized_files_by_sha256(tmp_path: Path) -> None:
    raw = tmp_path / "raw.csv"
    normalized = tmp_path / "normalized.csv"
    raw.write_bytes(b"timestamp,close\n2024-01-01,100\n")
    normalized.write_bytes(b"timestamp,close\n2024-01-01T00:00:00Z,100\n")

    manifest = build_manifest(
        dataset_id="DATA-TEST-001",
        provider="fixture",
        instrument="TEST-USD",
        venue="fixture",
        frequency="1h",
        timezone="UTC",
        candle_label="open-time",
        adjusted=None,
        retrieved_at_utc="2026-08-03T00:00:00+00:00",
        raw_path=raw,
        normalized_path=normalized,
        row_count=1,
        start="2024-01-01T00:00:00+00:00",
        end="2024-01-01T00:00:00+00:00",
        query_parameters={"limit": 1000},
        rate_limit_events=0,
        missing_intervals=[],
        known_limitations=["fixture"],
        license_note="test fixture",
        status="ok",
    )

    assert manifest["raw_file_sha256"] == file_sha256(raw)
    assert manifest["normalized_file_sha256"] == file_sha256(normalized)
    assert manifest["row_count"] == 1
    assert manifest["status"] == "ok"


def test_manifest_can_store_privacy_safe_paths_relative_to_root(tmp_path: Path) -> None:
    raw = tmp_path / "research" / "data" / "raw" / "test.csv"
    normalized = tmp_path / "research" / "data" / "normalized" / "test.csv"
    raw.parent.mkdir(parents=True)
    normalized.parent.mkdir(parents=True)
    raw.write_text("session_date,close\n2024-01-01,100\n", encoding="utf-8")
    normalized.write_text("session_date,adjusted_close\n2024-01-01,99\n", encoding="utf-8")

    manifest = build_manifest(
        dataset_id="DATA-TEST-RELATIVE-001",
        provider="fixture",
        instrument="TEST",
        venue="fixture",
        frequency="1d",
        timezone="America/New_York",
        candle_label="session-close",
        adjusted="fixture-adjusted",
        retrieved_at_utc="2026-08-03T00:00:00+00:00",
        raw_path=raw,
        normalized_path=normalized,
        path_root=tmp_path,
        row_count=1,
        start="2024-01-01",
        end="2024-01-01",
        query_parameters={},
        rate_limit_events=0,
        missing_intervals=[],
        known_limitations=[],
        license_note="fixture",
        status="ok",
    )

    assert manifest["raw_file"] == "research/data/raw/test.csv"
    assert manifest["normalized_file"] == "research/data/normalized/test.csv"
    assert str(tmp_path) not in str(manifest)


def test_manifest_rejects_files_outside_path_root(tmp_path: Path) -> None:
    approved = tmp_path / "repo"
    approved.mkdir()
    raw = tmp_path / "outside.csv"
    normalized = approved / "normalized.csv"
    raw.write_text("session_date,close\n2024-01-01,100\n", encoding="utf-8")
    normalized.write_text("session_date,adjusted_close\n2024-01-01,99\n", encoding="utf-8")

    try:
        build_manifest(
            dataset_id="DATA-TEST-OUTSIDE-001",
            provider="fixture",
            instrument="TEST",
            venue="fixture",
            frequency="1d",
            timezone="America/New_York",
            candle_label="session-close",
            adjusted=None,
            retrieved_at_utc="2026-08-03T00:00:00+00:00",
            raw_path=raw,
            normalized_path=normalized,
            path_root=approved,
            row_count=1,
            start="2024-01-01",
            end="2024-01-01",
            query_parameters={},
            rate_limit_events=0,
            missing_intervals=[],
            known_limitations=[],
            license_note="fixture",
            status="ok",
        )
    except ValueError as exc:
        assert "outside path_root" in str(exc)
    else:
        raise AssertionError("expected outside-root manifest path to fail")


def test_manifest_rejects_ok_status_with_zero_rows(tmp_path: Path) -> None:
    raw = tmp_path / "raw.csv"
    normalized = tmp_path / "normalized.csv"
    raw.write_text("timestamp,close\n", encoding="utf-8")
    normalized.write_text("timestamp,close\n", encoding="utf-8")

    try:
        build_manifest(
            dataset_id="DATA-TEST-EMPTY-001",
            provider="fixture",
            instrument="TEST-USD",
            venue="fixture",
            frequency="1h",
            timezone="UTC",
            candle_label="open-time",
            adjusted=None,
            retrieved_at_utc="2026-08-03T00:00:00+00:00",
            raw_path=raw,
            normalized_path=normalized,
            row_count=0,
            start=None,
            end=None,
            query_parameters={},
            rate_limit_events=0,
            missing_intervals=[],
            known_limitations=[],
            license_note="test fixture",
            status="ok",
        )
    except ValueError as exc:
        assert "zero rows" in str(exc)
    else:
        raise AssertionError("expected zero-row manifest to fail")


def test_manifest_is_write_once(tmp_path: Path) -> None:
    path = tmp_path / "manifest.json"
    manifest = {"dataset_id": "DATA-TEST-001", "status": "ok"}
    write_manifest_once(path, manifest)
    try:
        write_manifest_once(path, manifest)
    except FileExistsError:
        pass
    else:
        raise AssertionError("expected immutable manifest write to fail")

    assert json.loads(path.read_text(encoding="utf-8")) == manifest


def test_write_manifest_once_is_crash_atomic_on_serialization_failure(tmp_path: Path) -> None:
    """If json.dumps raises (non-serializable manifest), no final file and no
    temporary file may remain. The write must be staged and atomic."""
    path = tmp_path / "manifest.json"
    bad_manifest = {"dataset_id": "DATA-TEST-001", "bad": object()}

    with pytest.raises((TypeError, ValueError)):
        write_manifest_once(path, bad_manifest)

    assert not path.exists()
    assert list(tmp_path.iterdir()) == []


def test_write_manifest_once_second_write_preserves_existing(tmp_path: Path) -> None:
    """A second write must raise FileExistsError and leave the original bytes
    completely intact (no truncation, no partial overwrite)."""
    path = tmp_path / "manifest.json"
    original = {"dataset_id": "DATA-TEST-001", "status": "ok", "n": 1}
    write_manifest_once(path, original)
    original_bytes = path.read_bytes()

    with pytest.raises(FileExistsError):
        write_manifest_once(path, {"dataset_id": "DATA-TEST-001", "status": "different"})

    assert path.read_bytes() == original_bytes


def test_write_manifest_once_never_deletes_foreign_temp(tmp_path: Path) -> None:
    """A pre-existing foreign/in-flight temporary file must never be deleted
    by another invocation, and this invocation must still publish normally.

    The shared fixed `.tmp` name is the defect: with it, open("x") collides
    with the foreign file and the unconditional finally deletes it. The fixed
    behavior uses a unique per-invocation temp: publish succeeds and the
    foreign file is left byte-identical."""
    destination = tmp_path / "manifest.json"
    foreign = tmp_path / "manifest.json.tmp"
    foreign.write_bytes(b"foreign-in-flight\n")
    payload = {"dataset_id": "DATA-TEST-001", "status": "ok"}

    write_manifest_once(destination, payload)

    assert json.loads(destination.read_text(encoding="utf-8")) == payload
    assert foreign.read_bytes() == b"foreign-in-flight\n"
    # No temporary file owned by this invocation remains.
    leftovers = [p for p in tmp_path.iterdir() if p != destination and p != foreign]
    assert leftovers == []


def test_partial_file_moves_to_quarantine_with_failure_record(tmp_path: Path) -> None:
    partial = tmp_path / "cache" / "batch.partial.csv"
    partial.parent.mkdir()
    partial.write_text("partial", encoding="utf-8")
    quarantine = tmp_path / "quarantine"

    destination, record = quarantine_file(
        partial,
        quarantine,
        dataset_id="DATA-TEST-001",
        reason="rate_limit_exhausted",
        recorded_at_utc="2026-08-03T00:00:00+00:00",
    )

    assert not partial.exists()
    assert destination.exists()
    assert destination.parent == quarantine
    assert record["status"] == "quarantined"
    assert record["sha256"] == file_sha256(destination)
    assert record["reason"] == "rate_limit_exhausted"
