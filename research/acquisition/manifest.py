"""Immutable retrieval manifests and quarantine records."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
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
    missing_intervals: list[Any] | None,
    known_limitations: list[str],
    license_note: str,
    status: str,
    path_root: str | Path | None = None,
    missing_intervals_assessment: str | None = None,
) -> dict[str, Any]:
    if status == "ok" and row_count == 0:
        raise ValueError("status=ok is invalid for a dataset with zero rows")

    raw = Path(raw_path)
    normalized = Path(normalized_path)
    if path_root is None:
        raw_file = str(raw)
        normalized_file = str(normalized)
    else:
        root = Path(path_root).resolve()
        try:
            raw_file = raw.resolve().relative_to(root).as_posix()
            normalized_file = normalized.resolve().relative_to(root).as_posix()
        except ValueError as exc:
            raise ValueError("manifest file is outside path_root") from exc
    manifest: dict[str, Any] = {
        "dataset_id": dataset_id,
        "provider": provider,
        "instrument": instrument,
        "venue": venue,
        "frequency": frequency,
        "timezone": timezone,
        "candle_label": candle_label,
        "adjusted": adjusted,
        "retrieved_at_utc": retrieved_at_utc,
        "raw_file": raw_file,
        "raw_file_sha256": file_sha256(raw),
        "raw_file_bytes": raw.stat().st_size,
        "normalized_file": normalized_file,
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
    if missing_intervals_assessment is not None:
        manifest["missing_intervals_assessment"] = missing_intervals_assessment
    return manifest


def write_manifest_once(path: str | Path, manifest: dict[str, Any]) -> Path:
    """Atomically publish a manifest exactly once, or fail before any write.

    Contract:
    - Failure before publication raises with the destination absent (or an
      existing/foreign destination left byte-identical) and no .tmp left.
    - Success returns normally with the destination present; callers that
      track ownership (e.g. _persist_symbol) may rely on "returned without
      raising" meaning this invocation created the file.
    - Write-once: publishing onto an existing destination raises
      FileExistsError without truncating it. Hard-link publication (not
      os.replace) is what guarantees we never clobber a foreign manifest.
    """
    destination = Path(path)
    # Serialize before any filesystem mutation; non-serializable input fails here.
    payload = json.dumps(manifest, indent=2) + "\n"

    destination.parent.mkdir(parents=True, exist_ok=True)
    # Unique per-invocation temp: a foreign/in-flight temp file can never be
    # collided with or deleted by this invocation.
    fd, temp_name = tempfile.mkstemp(
        prefix=destination.name + ".",
        suffix=".tmp",
        dir=destination.parent,
    )
    temporary = Path(temp_name)
    published = False
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        # Exclusive publication: FileExistsError if destination already exists.
        os.link(temporary, destination)
        published = True
        return destination
    finally:
        if published:
            # Publish already succeeded; a temp-cleanup failure must not flip
            # success into an exception (callers key ownership off "returned
            # without raising").
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
        else:
            temporary.unlink(missing_ok=True)


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
