# Round-1 Archive (exploratory — not contract-compliant)

**Status:** frozen historical snapshot  
**Date:** 2026-08-02  
**Evidence ceiling:** E1 research context only (legacy scratchpads)

## What this is

The first three local backtests written under the Obsidian vault:

| Folder | Strategy | Class |
|--------|----------|-------|
| `btc-overnight/` | Overnight Seasonality in Bitcoin | Resolution-mismatched daily diagnostic |
| `crypto-rebalance/` | Rebalancing Premium in Cryptocurrencies | Static-survivor allocation/frequency proxy |
| `asset-trend/` | Asset Class Trend-Following | Paper-informed ETF proxy |

These are **not** contract-compliant experiments and must not be labeled `validated`, bare `backtested`, or `experimented`.

## Correct labels

| Strategy | status | evidence_level | reproduction_status | legacy_result_status |
|----------|--------|----------------|---------------------|----------------------|
| BTC Overnight | researched | E1 | not-attempted | not-promotable |
| Crypto Rebalance | researched | E1 | not-attempted | not-promotable |
| Asset Trend | researched | E1 | not-attempted | not-promotable |

## Soft conclusions (do not overclaim)

- **BTC:** daily close→open does **not** test the paper’s 22:00–00:00 UTC window. Fee-sensitive null on daily bars is not evidence against the intraday hypothesis.
- **Crypto rebalance:** monthly > daily on a present-day survivor cohort. Does **not** establish a point-in-time rebalancing premium.
- **Asset trend:** fixed 20% sleeves beat repo 1/N on this ETF proxy. Not a full GTAA source validation.

## Reproducibility

- Committed: `backtest.py`, `metrics.csv`, `results.md`, this README, `ARCHIVE_MANIFEST.json`
- Local-only (gitignored): raw CSVs, PNGs
- See `research/contracts/DATA_ARTIFACT_POLICY.md`

## Supersession

Round-3 contract experiments under `research/experiments/` and frozen specs under `research/specs/round-3/` supersede these for promotion decisions. E2 is awarded only after a contract-compliant artifact exists.
