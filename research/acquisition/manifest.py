"""Immutable retrieval manifests and quarantine records."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


def file_sha256(path: str | Path) -> str:
    source = Path(path)
    digest = hashlib.sha256()
    with source.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(
    *,
    dataset_id: str,
    provider: str,
    instrument: str,
    venue: str,
    frequency: str,
    timezone: str,
    candle_label: str,
    adjusted: str | None,
    retrieved_at_utc: str,
    raw_path: str | Path,
    normalized_path: str | Path,
    row_count: int,
    start: str | None,
    end: str | None,
    query_parameters: dict[str, Any],
    rate_limit_events: int,
    missing_intervals: list[Any],
    known_limitations: list[str],
    license_note: str,
    status: str,
) -> dict[str, Any]:
    if status == "ok" and row_count == 0:
        raise ValueError("status=ok is invalid for a dataset with zero rows")

    raw = Path(raw_path)
    normalized = Path(normalized_path)
    return {
        "dataset_id": dataset_id,
        "provider": provider,
        "instrument": instrument,
        "venue": venue,
        "frequency": frequency,
        "timezone": timezone,
        "candle_label": candle_label,
        "adjusted": adjusted,
        "retrieved_at_utc": retrieved_at_utc,
        "raw_file": str(raw),
        "raw_file_sha256": file_sha256(raw),
        "raw_file_bytes": raw.stat().st_size,
        "normalized_file": str(normalized),
        "normalized_file_sha256": file_sha256(normalized),
        "normalized_file_bytes": normalized.stat().st_size,
        "row_count": row_count,
        "start": start,
        "end": end,
        "query_parameters": query_parameters,
        "rate_limit_events": rate_limit_events,
        "missing_intervals": missing_intervals,
        "known_limitations": known_limitations,
        "license_note": license_note,
        "status": status,
    }


def write_manifest_once(path: str | Path, manifest: dict[str, Any]) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")
    return destination


def quarantine_file(
    partial_path: str | Path,
    quarantine_dir: str | Path,
    *,
    dataset_id: str,
    reason: str,
    recorded_at_utc: str,
) -> tuple[Path, dict[str, Any]]:
    source = Path(partial_path)
    destination_dir = Path(quarantine_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / source.name
    if destination.exists():
        raise FileExistsError(f"quarantine destination already exists: {destination}")
    shutil.move(str(source), str(destination))
    record = {
        "dataset_id": dataset_id,
        "status": "quarantined",
        "reason": reason,
        "recorded_at_utc": recorded_at_utc,
        "path": str(destination),
        "bytes": destination.stat().st_size,
        "sha256": file_sha256(destination),
    }
    return destination, record
