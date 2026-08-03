"""Tests for deterministic, non-destructive local cache inventory."""

from __future__ import annotations

from pathlib import Path

from research.acquisition.inventory import inventory_paths, write_inventory_reports
from research.acquisition.manifest import file_sha256


def test_inventory_hashes_csv_and_extracts_coverage(tmp_path: Path) -> None:
    csv_path = tmp_path / "raw" / "btc.csv"
    csv_path.parent.mkdir()
    csv_path.write_text(
        "timestamp,open,close\n"
        "2024-01-01T00:00:00Z,100,101\n"
        "2024-01-01T01:00:00Z,101,102\n",
        encoding="utf-8",
    )

    report = inventory_paths([tmp_path], repo_root=tmp_path)
    entry = report["files"][0]

    assert entry["relative_path"] == "raw/btc.csv"
    assert entry["sha256"] == file_sha256(csv_path)
    assert entry["row_count"] == 2
    assert entry["columns"] == ["timestamp", "open", "close"]
    assert entry["datetime_column"] == "timestamp"
    assert entry["index_start"] == "2024-01-01T00:00:00+00:00"
    assert entry["index_end"] == "2024-01-01T01:00:00+00:00"
    assert entry["timezone_detected"] == "UTC"
    assert entry["retrieved_at_utc"] is None
    assert entry["parse_status"] == "ok"


def test_inventory_does_not_abort_on_malformed_csv(tmp_path: Path) -> None:
    bad = tmp_path / "broken.csv"
    bad.write_bytes(b'"unterminated\n')
    good = tmp_path / "good.csv"
    good.write_text("date,close\n2024-01-01,1\n", encoding="utf-8")

    report = inventory_paths([tmp_path], repo_root=tmp_path)
    by_name = {Path(item["absolute_path"]).name: item for item in report["files"]}

    assert by_name["broken.csv"]["parse_status"] == "error"
    assert by_name["broken.csv"]["sha256"] == file_sha256(bad)
    assert by_name["good.csv"]["parse_status"] == "ok"


def test_inventory_records_missing_configured_root(tmp_path: Path) -> None:
    missing = tmp_path / "missing"

    report = inventory_paths([missing], repo_root=tmp_path)

    assert report["files"] == []
    assert report["roots"][0]["exists"] is False
    assert report["roots"][0]["status"] == "missing"


def test_inventory_deduplicates_same_file_reached_through_nested_roots(
    tmp_path: Path,
) -> None:
    nested = tmp_path / "archive"
    nested.mkdir()
    source = nested / "prices.csv"
    source.write_text("date,close\n2024-01-01,1\n", encoding="utf-8")

    report = inventory_paths([tmp_path, nested], repo_root=tmp_path)

    assert len(report["files"]) == 1


def test_inventory_writes_json_and_markdown_without_raw_copy(tmp_path: Path) -> None:
    source = tmp_path / "cache.csv"
    source.write_text("date,close\n2024-01-01,1\n", encoding="utf-8")
    report = inventory_paths([tmp_path], repo_root=tmp_path)
    output = tmp_path / "reports"

    json_path, markdown_path = write_inventory_reports(
        report,
        output / "inventory.json",
        output / "inventory.md",
    )

    assert json_path.exists()
    assert markdown_path.exists()
    assert "cache.csv" in markdown_path.read_text(encoding="utf-8")
    assert not (output / "cache.csv").exists()


def test_inventory_marks_external_paths_as_local_only(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    external = tmp_path / "vault"
    repo.mkdir()
    external.mkdir()
    (external / "prices.csv").write_text(
        "date,close\n2024-01-01,1\n", encoding="utf-8"
    )

    report = inventory_paths([external], repo_root=repo)
    entry = report["files"][0]

    assert entry["repo_owned"] is False
    assert entry["redistribution_status"] == "local-only-unverified"
    assert entry["relative_path"] is None


def test_redacted_inventory_uses_root_alias_without_absolute_paths(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    external = tmp_path / "vault"
    repo.mkdir()
    nested = external / "60-Trading" / "Backtests"
    nested.mkdir(parents=True)
    source = nested / "prices.csv"
    source.write_text("date,close\n2024-01-01,1\n", encoding="utf-8")

    report = inventory_paths(
        {"OBSIDIAN_VAULT": external},
        repo_root=repo,
        redact_absolute_paths=True,
    )
    entry = report["files"][0]

    assert report["repo_root"] is None
    assert report["roots"][0]["path"] is None
    assert report["roots"][0]["alias"] == "OBSIDIAN_VAULT"
    assert entry["absolute_path"] is None
    assert entry["root_alias"] == "OBSIDIAN_VAULT"
    assert entry["path_from_root"] == "60-Trading/Backtests/prices.csv"
    serialized = str(report)
    assert str(tmp_path) not in serialized
