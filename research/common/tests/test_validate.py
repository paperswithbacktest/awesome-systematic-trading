"""Tests for experiment directory validator + fixtures."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from research.common.validate import validate_experiment_dir

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
VALID = FIXTURES / "valid_exp"
INVALID = FIXTURES / "invalid_exp"
SCHEMA = Path(__file__).resolve().parents[2] / "contracts" / "experiment.schema.json"


def test_valid_fixture_passes():
    result = validate_experiment_dir(VALID)
    assert result["ok"] is True, result["errors"]
    assert result["errors"] == []


def test_invalid_fixture_fails_with_expected_errors():
    result = validate_experiment_dir(INVALID)
    assert result["ok"] is False
    joined = " | ".join(result["errors"]).lower()
    assert "sha256 mismatch" in joined or "mismatch" in joined
    assert "checks.passed=true" in joined or "passed=true" in joined
    assert "experiment_id" in joined
    # empty metrics
    assert "no data rows" in joined or "metrics.csv" in joined


def test_jsonschema_accepts_valid_verdict():
    import jsonschema

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    verdict = json.loads((VALID / "verdict.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=verdict, schema=schema)


def test_missing_dir_fails():
    result = validate_experiment_dir(FIXTURES / "does-not-exist")
    assert result["ok"] is False
    assert any("not a directory" in e for e in result["errors"])
