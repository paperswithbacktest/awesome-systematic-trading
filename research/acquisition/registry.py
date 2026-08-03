"""Strict loader for the committed flat dataset registry."""

from __future__ import annotations

import csv
from pathlib import Path


class RegistryError(ValueError):
    """The dataset registry violates its structural contract."""


REQUIRED_COLUMNS = {
    "dataset_id",
    "asset_class",
    "instrument",
    "venue",
    "provider",
    "frequency",
    "timezone",
    "candle_label",
    "adjusted",
    "status",
    "recipe_path",
    "manifest_path",
}


def load_registry(path: str | Path) -> dict[str, dict[str, str]]:
    source = Path(path)
    with source.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - columns)
        if missing:
            raise RegistryError(f"registry missing columns: {missing}")

        rows: dict[str, dict[str, str]] = {}
        for line_number, row in enumerate(reader, start=2):
            dataset_id = (row.get("dataset_id") or "").strip()
            if not dataset_id:
                raise RegistryError(f"empty dataset_id at line {line_number}")
            if dataset_id in rows:
                raise RegistryError(f"duplicate dataset_id: {dataset_id}")
            rows[dataset_id] = {key: value or "" for key, value in row.items()}
    return rows
