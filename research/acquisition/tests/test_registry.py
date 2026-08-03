"""Tests for the committed flat data registry."""

from __future__ import annotations

from pathlib import Path

import pytest

from research.acquisition.registry import RegistryError, load_registry


def test_registry_loads_unique_dataset_rows(tmp_path: Path) -> None:
    registry = tmp_path / "datasets.csv"
    registry.write_text(
        "dataset_id,asset_class,instrument,venue,provider,frequency,timezone,"
        "candle_label,adjusted,status,recipe_path,manifest_path\n"
        "DATA-ETF-GTAA-DAILY-001,etf,SPY|EFA|IEF|VNQ|GSG,NYSE-Arca,"
        "yahoo,1d,UTC,session-close,provider-adjusted-close,planned,"
        "recipes/gtaa.yaml,manifests/gtaa.json\n",
        encoding="utf-8",
    )

    rows = load_registry(registry)

    assert rows["DATA-ETF-GTAA-DAILY-001"]["instrument"].split("|") == [
        "SPY",
        "EFA",
        "IEF",
        "VNQ",
        "GSG",
    ]


def test_registry_rejects_duplicate_dataset_ids(tmp_path: Path) -> None:
    registry = tmp_path / "datasets.csv"
    header = (
        "dataset_id,asset_class,instrument,venue,provider,frequency,timezone,"
        "candle_label,adjusted,status,recipe_path,manifest_path\n"
    )
    row = "DATA-DUP,crypto,BTC-USD,Coinbase,coinbase,1h,UTC,open-time,,planned,r,m\n"
    registry.write_text(header + row + row, encoding="utf-8")

    with pytest.raises(RegistryError, match="duplicate dataset_id"):
        load_registry(registry)


def test_registry_rejects_missing_required_columns(tmp_path: Path) -> None:
    registry = tmp_path / "datasets.csv"
    registry.write_text("dataset_id,provider\nDATA-X,fixture\n", encoding="utf-8")

    with pytest.raises(RegistryError, match="missing columns"):
        load_registry(registry)
