"""Deterministic, non-destructive inventory of existing local data caches."""

from __future__ import annotations

import json
import re
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import pandas as pd

from research.acquisition.manifest import file_sha256

_EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
}
_DATETIME_COLUMNS = ("timestamp", "datetime", "date", "time")
_TZ_SUFFIX = re.compile(r"(?:Z|[+-]\d{2}:?\d{2})$", re.IGNORECASE)


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _discover_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return
    for candidate in root.rglob("*"):
        if not candidate.is_file():
            continue
        if any(part in _EXCLUDED_DIRS for part in candidate.parts):
            continue
        yield candidate


def _csv_metadata(path: Path) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "parse_status": "not_csv",
        "row_count": None,
        "columns": None,
        "datetime_column": None,
        "index_start": None,
        "index_end": None,
        "timezone_detected": None,
        "parse_error": None,
    }
    if path.suffix.lower() != ".csv":
        return metadata

    try:
        frame = pd.read_csv(path)
        metadata.update(
            parse_status="ok",
            row_count=int(len(frame)),
            columns=[str(column) for column in frame.columns],
        )
        by_lower = {str(column).strip().lower(): str(column) for column in frame.columns}
        date_column = next(
            (by_lower[name] for name in _DATETIME_COLUMNS if name in by_lower), None
        )
        if date_column is None or frame.empty:
            return metadata

        source = frame[date_column].dropna().astype(str).str.strip()
        if source.empty:
            return metadata
        explicitly_zoned = bool(source.map(lambda value: bool(_TZ_SUFFIX.search(value))).all())
        parsed = pd.to_datetime(source, errors="coerce", utc=explicitly_zoned).dropna()
        if parsed.empty:
            return metadata

        start = parsed.min()
        end = parsed.max()
        metadata["datetime_column"] = date_column
        metadata["index_start"] = start.isoformat()
        metadata["index_end"] = end.isoformat()
        if explicitly_zoned:
            metadata["timezone_detected"] = "UTC"
        return metadata
    except Exception as exc:  # noqa: BLE001 - inventory must continue after bad files
        metadata["parse_status"] = "error"
        metadata["parse_error"] = f"{type(exc).__name__}: {exc}"
        return metadata


def inventory_paths(
    roots: Iterable[str | Path] | Mapping[str, str | Path],
    *,
    repo_root: str | Path,
    redact_absolute_paths: bool = False,
) -> dict[str, Any]:
    """Hash and describe files under roots without copying or changing them."""
    repository = Path(repo_root).resolve()
    if isinstance(roots, Mapping):
        root_items = [(str(alias), Path(path).resolve()) for alias, path in roots.items()]
    else:
        root_items = [
            (f"ROOT_{index}", Path(path).resolve())
            for index, path in enumerate(roots, start=1)
        ]

    root_records: list[dict[str, Any]] = []
    discovered: dict[Path, tuple[str, Path]] = {}

    for alias, root in root_items:
        exists = root.exists()
        root_records.append(
            {
                "alias": alias,
                "path": None if redact_absolute_paths else str(root),
                "exists": exists,
                "status": "available" if exists else "missing",
            }
        )
        if exists:
            for candidate in _discover_files(root):
                discovered.setdefault(candidate.resolve(), (alias, root))

    files: list[dict[str, Any]] = []
    for path in sorted(discovered, key=lambda item: str(item).lower()):
        alias, source_root = discovered[path]
        repo_owned = _is_within(path, repository)
        relative_path = path.relative_to(repository).as_posix() if repo_owned else None
        path_from_root = path.relative_to(source_root).as_posix()
        record: dict[str, Any] = {
            "absolute_path": None if redact_absolute_paths else str(path),
            "relative_path": relative_path,
            "root_alias": alias,
            "path_from_root": path_from_root,
            "repo_owned": repo_owned,
            "redistribution_status": (
                "repository-policy-applies" if repo_owned else "local-only-unverified"
            ),
            "bytes": path.stat().st_size,
            "sha256": file_sha256(path),
            "retrieved_at_utc": None,
        }
        record.update(_csv_metadata(path))
        if redact_absolute_paths and record.get("parse_error"):
            error = str(record["parse_error"])
            for private_path, replacement in (
                (str(path), f"{alias}/{path_from_root}"),
                (str(source_root), alias),
                (str(repository), "REPO"),
            ):
                error = error.replace(private_path, replacement)
            record["parse_error"] = error
        files.append(record)

    return {
        "inventory_version": 1,
        "repo_root": None if redact_absolute_paths else str(repository),
        "roots": root_records,
        "file_count": len(files),
        "files": files,
    }


def write_inventory_reports(
    report: dict[str, Any], json_path: str | Path, markdown_path: str | Path
) -> tuple[Path, Path]:
    """Write a machine report and a compact human summary; never copy source data."""
    json_destination = Path(json_path)
    markdown_destination = Path(markdown_path)
    json_destination.parent.mkdir(parents=True, exist_ok=True)
    markdown_destination.parent.mkdir(parents=True, exist_ok=True)
    json_destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Local Data Cache Inventory",
        "",
        f"Files discovered: **{report.get('file_count', len(report.get('files', [])))}**",
        "",
        "| Path | SHA-256 | Rows | Coverage | Parse |",
        "|------|----------|------|----------|-------|",
    ]
    for entry in report.get("files", []):
        display_path = entry.get("relative_path")
        if not display_path and entry.get("root_alias") and entry.get("path_from_root"):
            display_path = f"{entry['root_alias']}/{entry['path_from_root']}"
        display_path = display_path or entry.get("path_from_root") or "<redacted>"
        coverage = ""
        if entry.get("index_start") or entry.get("index_end"):
            coverage = f"{entry.get('index_start') or '?'} → {entry.get('index_end') or '?'}"
        rows = "" if entry.get("row_count") is None else str(entry["row_count"])
        lines.append(
            f"| `{display_path}` | `{entry['sha256']}` | {rows} | {coverage} | "
            f"{entry.get('parse_status', '')} |"
        )
    markdown_destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_destination, markdown_destination
