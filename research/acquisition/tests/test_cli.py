"""Tests for the reproducible acquisition command line."""

from __future__ import annotations

import json
from pathlib import Path

from research.acquisition.cli import main


def test_inventory_cli_requires_at_least_one_root(tmp_path: Path) -> None:
    rc = main(
        [
            "inventory",
            "--repo-root",
            str(tmp_path),
            "--out-json",
            str(tmp_path / "inventory.json"),
            "--out-md",
            str(tmp_path / "inventory.md"),
        ]
    )

    assert rc == 2
    assert not (tmp_path / "inventory.json").exists()


def test_inventory_cli_writes_json_and_markdown(tmp_path: Path) -> None:
    root = tmp_path / "cache"
    root.mkdir()
    source = root / "prices.csv"
    source.write_text("date,close\n2024-01-01,1\n", encoding="utf-8")
    output = tmp_path / "reports"

    rc = main(
        [
            "inventory",
            "--repo-root",
            str(tmp_path),
            "--root",
            str(root),
            "--out-json",
            str(output / "inventory.json"),
            "--out-md",
            str(output / "inventory.md"),
        ]
    )

    assert rc == 0
    report = json.loads((output / "inventory.json").read_text(encoding="utf-8"))
    assert report["file_count"] == 1
    assert report["files"][0]["relative_path"] == "cache/prices.csv"
    assert (output / "inventory.md").exists()
    assert not (output / "prices.csv").exists()


def test_inventory_cli_tolerates_missing_roots(tmp_path: Path) -> None:
    output = tmp_path / "reports"

    rc = main(
        [
            "inventory",
            "--repo-root",
            str(tmp_path),
            "--root",
            str(tmp_path / "missing"),
            "--out-json",
            str(output / "inventory.json"),
            "--out-md",
            str(output / "inventory.md"),
        ]
    )

    assert rc == 0
    report = json.loads((output / "inventory.json").read_text(encoding="utf-8"))
    assert report["file_count"] == 0
    assert report["roots"][0]["status"] == "missing"


def test_inventory_cli_redacts_paths_and_accepts_named_roots(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    vault = tmp_path / "vault"
    repo.mkdir()
    vault.mkdir()
    (vault / "prices.csv").write_text("date,close\n2024-01-01,1\n", encoding="utf-8")
    output = repo / "reports"

    rc = main(
        [
            "inventory",
            "--repo-root",
            str(repo),
            "--named-root",
            f"OBSIDIAN_VAULT={vault}",
            "--redact-absolute-paths",
            "--out-json",
            str(output / "inventory.json"),
            "--out-md",
            str(output / "inventory.md"),
        ]
    )

    assert rc == 0
    text = (output / "inventory.json").read_text(encoding="utf-8")
    report = json.loads(text)
    assert report["files"][0]["root_alias"] == "OBSIDIAN_VAULT"
    assert report["files"][0]["absolute_path"] is None
    assert str(tmp_path) not in text
