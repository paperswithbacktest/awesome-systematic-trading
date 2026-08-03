"""Contracts for the committed GTAA registry row and acquisition recipe."""

from __future__ import annotations

from pathlib import Path

from research.acquisition.recipes import load_recipe
from research.acquisition.registry import load_registry
from research.acquisition.workflows.etf_gtaa import DATASET_ID, GTAA_SYMBOLS


ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = ROOT / "research/data/registry/datasets.csv"
RECIPE_PATH = (
    ROOT / "research/data/recipes/DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001.yaml"
)


def test_committed_registry_freezes_exact_gtaa_dataset_contract() -> None:
    registry = load_registry(REGISTRY_PATH)

    assert DATASET_ID in registry
    row = registry[DATASET_ID]
    assert row["asset_class"] == "etf"
    assert row["instrument"].split("|") == list(GTAA_SYMBOLS)
    assert row["venue"] == "US ETF consolidated daily"
    assert row["provider"] == "yahoo-yfinance"
    assert row["frequency"] == "1d"
    assert row["timezone"] == "America/New_York"
    assert row["candle_label"] == "session-close"
    assert row["adjusted"] == "yahoo-adjusted-close-proxy"
    assert row["status"] == "planned"
    assert row["recipe_path"] == (
        "research/data/recipes/DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001.yaml"
    )
    assert row["manifest_path"] == (
        "research/data/manifests/"
        "DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001/{symbol}.json"
    )


def test_committed_recipe_matches_workflow_and_is_privacy_safe() -> None:
    recipe = load_recipe(RECIPE_PATH)

    assert recipe["dataset_id"] == DATASET_ID
    assert recipe["provider"] == "yahoo-yfinance"
    assert recipe["endpoint"] == "yfinance.download"
    assert recipe["instruments"] == list(GTAA_SYMBOLS)
    assert recipe["venue"] == "US ETF consolidated daily"
    assert recipe["quote_asset"] == "USD"
    assert recipe["frequency"] == "1d"
    assert recipe["timezone"] == "America/New_York"
    assert recipe["candle_label"] == "session-close"
    assert recipe["adjustment"] == "yahoo-adjusted-close-proxy"
    assert recipe["start"] == "2007-01-01"
    assert recipe["end"] == "2026-08-02"
    assert recipe["end_semantics"] == "exclusive"
    assert recipe["request_parameters"] == {
        "start": "2007-01-01",
        "end": "2026-08-02",
        "interval": "1d",
        "auto_adjust": False,
        "actions": True,
        "threads": False,
        "multi_level_index": False,
        "progress": False,
        "timeout": 20,
    }
    assert recipe["pagination"] == {"mode": "none"}
    assert recipe["rate_limit"]["mode"] == "bounded_serial"
    assert recipe["rate_limit"]["provider_limit"] == "undocumented"
    assert recipe["max_attempts"] == 3
    assert recipe["backoff_seconds"] == [5, 20]
    assert recipe["empty_response_policy"] == "hard_fail"

    paths = [
        recipe["raw_output_path"],
        recipe["normalized_output_path"],
        recipe["manifest_path"],
    ]
    assert paths == [
        "research/data/raw/yahoo/etf_gtaa_daily_001/{symbol}.source_snapshot.csv",
        "research/data/normalized/"
        "DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001/{symbol}.csv",
        "research/data/manifests/"
        "DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001/{symbol}.json",
    ]
    assert all(not Path(value).is_absolute() for value in paths)

    cross = recipe["cross_check"]
    assert cross["provider"] == "stooq"
    assert cross["series"] == "unadjusted_close"
    assert cross["role"] == "sanity_evidence_only"
    assert cross["failure_policy"] == "record_runtime_unavailable"
    assert cross["substitution_allowed"] is False
    assert "current_status" not in cross
    assert "unavailability_reason" not in cross

    serialized = str(recipe).lower()
    assert "adapter parsing" in serialized
    assert "provider-adjusted close proxy" in serialized
    assert "not independently reconstructed" in serialized
    assert "stooq" in serialized and "unadjusted" in serialized
    # Runtime unavailability is a policy expectation, not a frozen observation.
    assert "unavailable" in serialized
    assert "html" not in serialized
    assert "never used to substitute" in serialized
    assert "verify yahoo finance terms before redistribution" in serialized
    assert "c:\\users\\" not in serialized
    assert "/users/" not in serialized
    assert "onedrive" not in serialized
    assert "appdata" not in serialized
