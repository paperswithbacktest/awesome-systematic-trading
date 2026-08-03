"""Tests for immutable acquisition manifests and quarantine records."""

from __future__ import annotations

import json
from pathlib import Path

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
