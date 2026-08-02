# Data Artifact Policy

## Principle

Git stores **code, configs, manifests, metrics, and verdicts**.  
Raw market-data bars are **local-only** unless redistribution rights are explicit.

## What is committed

| Artifact | Commit? |
|----------|---------|
| `config.yaml`, `run.py`, `README.md` | Yes |
| `data_manifest.json` (provider, query, timestamps, sha256) | Yes |
| `metrics.csv`, `period_metrics.csv`, `verdict.json`, `checks.json` | Yes |
| `requirements-lock.txt` | Yes |
| Small synthetic fixtures under `research/common/tests/fixtures/` | Yes |
| Round-1 scripts + metrics + results.md + ARCHIVE_MANIFEST | Yes |
| Raw OHLCV CSVs / parquet / plots from vendors | **No** (local cache) |

## Manifest rules

Every cached input file must appear in `data_manifest.json` with:

```json
{
  "files": {
    "data/prices.csv": {
      "sha256": "...",
      "bytes": 12345,
      "not_cached": false
    }
  }
}
```

If the file is not in git:

```json
{
  "sha256": "...",
  "bytes": 12345,
  "not_cached": true,
  "local_path": "data/prices.csv",
  "retrieval": {
    "provider": "yfinance",
    "query": {"ticker": "BTC-USD", "interval": "1h"},
    "retrieved_at_utc": "..."
  }
}
```

The validator accepts missing-on-disk files only when `not_cached` or `external` is true (warning, not hard fail for external).

## Round-1 archive

`research/archive/round-1/` is a **frozen historical snapshot** of exploratory scripts/results, not a contract-compliant reproduction.

- Scripts, metrics.csv, results.md, and ARCHIVE_MANIFEST.json are committed.
- Raw vendor CSVs and PNGs are gitignored (local-only).
- ARCHIVE_MANIFEST hashes those local files for machines that still have them.
- Re-download may differ slightly from vendor revisions; treat hashes as provenance, not bit-identical forever guarantees.

## Preferred runtime cache location

```text
research/experiments/EXP-.../data/     # gitignored
research/experiments/EXP-.../cache/    # gitignored
research/experiments/EXP-.../figures/  # png gitignored; keep .gitkeep
```

## Licensing

Do not commit bulk Yahoo/exchange dumps to a public remote without checking ToS. Private local use + committed recipes/hashes is the default.
