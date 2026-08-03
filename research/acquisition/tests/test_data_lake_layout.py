"""Structural tests for local-only Round-4 data-lake paths."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def test_raw_normalized_and_quarantine_are_gitignored() -> None:
    ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "research/data/raw/**" in ignore
    assert "research/data/normalized/**" in ignore
    assert "research/data/quarantine/**" in ignore


def test_committed_metadata_directories_have_placeholders() -> None:
    for name in ("registry", "recipes", "manifests", "inventory", "quality-reports"):
        assert (ROOT / "research" / "data" / name / ".gitkeep").exists()
