"""Tests for committed YAML acquisition recipes."""

from __future__ import annotations

from pathlib import Path

import pytest

from research.acquisition.recipes import RecipeError, load_recipe


REQUIRED = """
dataset_id: DATA-TEST-001
provider: fixture
endpoint: https://example.invalid/data
instruments: [TEST-USD]
venue: fixture
quote_asset: USD
frequency: 1h
timezone: UTC
candle_label: open-time
adjustment: null
start: '2020-01-01T00:00:00Z'
end: null
pagination: {mode: cursor}
rate_limit: {requests_per_second: 1}
max_attempts: 3
backoff_seconds: [1, 2]
empty_response_policy: hard_fail
raw_output_path: research/data/raw/fixture/test.csv
normalized_output_path: research/data/normalized/DATA-TEST-001/test.csv
manifest_path: research/data/manifests/DATA-TEST-001.json
license_note: verify before redistribution
known_limitations: [fixture only]
"""


def test_recipe_loader_accepts_explicit_contract(tmp_path: Path) -> None:
    path = tmp_path / "recipe.yaml"
    path.write_text(REQUIRED, encoding="utf-8")

    recipe = load_recipe(path)

    assert recipe["empty_response_policy"] == "hard_fail"
    assert recipe["timezone"] == "UTC"
    assert recipe["max_attempts"] == 3


def test_recipe_loader_rejects_missing_fields(tmp_path: Path) -> None:
    path = tmp_path / "recipe.yaml"
    path.write_text("dataset_id: DATA-X\nprovider: fixture\n", encoding="utf-8")

    with pytest.raises(RecipeError, match="missing fields"):
        load_recipe(path)


def test_recipe_loader_rejects_non_hard_fail_empty_policy(tmp_path: Path) -> None:
    path = tmp_path / "recipe.yaml"
    path.write_text(
        REQUIRED.replace("empty_response_policy: hard_fail", "empty_response_policy: ignore"),
        encoding="utf-8",
    )

    with pytest.raises(RecipeError, match="hard_fail"):
        load_recipe(path)


def test_recipe_loader_rejects_ambiguous_intraday_crypto_semantics(
    tmp_path: Path,
) -> None:
    path = tmp_path / "recipe.yaml"
    text = REQUIRED.replace("DATA-TEST-001", "DATA-CRYPTO-BTCUSD-TEST-1H-001")
    text = text.replace("timezone: UTC", "timezone: America/New_York")
    path.write_text(text, encoding="utf-8")

    with pytest.raises(RecipeError, match="UTC"):
        load_recipe(path)
