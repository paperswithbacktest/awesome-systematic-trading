"""Strict loader for committed acquisition recipes."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from research.acquisition.core import AcquisitionRecipe, AcquisitionError


class RecipeError(ValueError):
    """A recipe is incomplete or violates the acquisition contract."""


REQUIRED_FIELDS = {
    "dataset_id",
    "provider",
    "endpoint",
    "instruments",
    "venue",
    "quote_asset",
    "frequency",
    "timezone",
    "candle_label",
    "adjustment",
    "start",
    "end",
    "pagination",
    "rate_limit",
    "max_attempts",
    "backoff_seconds",
    "empty_response_policy",
    "raw_output_path",
    "normalized_output_path",
    "manifest_path",
    "license_note",
    "known_limitations",
}


def load_recipe(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        loaded = yaml.safe_load(source.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise RecipeError(f"recipe is not valid YAML: {exc}") from exc
    if not isinstance(loaded, dict):
        raise RecipeError("recipe must parse to a mapping")

    missing = sorted(REQUIRED_FIELDS - set(loaded))
    if missing:
        raise RecipeError(f"recipe missing fields: {missing}")
    if loaded["empty_response_policy"] != "hard_fail":
        raise RecipeError("empty_response_policy must be hard_fail")
    instruments = loaded["instruments"]
    if not isinstance(instruments, list) or not instruments:
        raise RecipeError("instruments must be a non-empty list")
    backoff = loaded["backoff_seconds"]
    if not isinstance(backoff, list):
        raise RecipeError("backoff_seconds must be a list")

    try:
        AcquisitionRecipe(
            dataset_id=str(loaded["dataset_id"]),
            provider=str(loaded["provider"]),
            required_instruments=tuple(str(item) for item in instruments),
            frequency=str(loaded["frequency"]),
            timezone=str(loaded["timezone"]),
            candle_label=str(loaded["candle_label"]),
            adjustment=(
                None if loaded["adjustment"] is None else str(loaded["adjustment"])
            ),
            max_attempts=int(loaded["max_attempts"]),
            backoff_seconds=tuple(float(value) for value in backoff),
        )
    except (AcquisitionError, TypeError, ValueError) as exc:
        raise RecipeError(str(exc)) from exc
    return loaded
