# Round-3 Failed Worker Attempts

**Date:** 2026-08-02  
**Harness baseline:** `35e0ac0`  
**Worker batch:** `deleg_89f7dcab` (all timed out on Yahoo rate limits)

These directories are **historical evidence only**. Do not run them again.
Corrections live under new experiment IDs in `research/experiments/`.

| Attempt | Disposition | Review |
|---------|-------------|--------|
| `EXP-2026-08-BTC-OVERNIGHT-HOURLY-001` | reviewer-rejected (B&H costs wrong; date claim false; soft clock) | `research/reviews/REV-2026-08-BTC-HOURLY-001.md` |
| `EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001` | incomplete (config+run only; live download stalled) | `research/reviews/REV-2026-08-CRYPTO-REBALANCE-001.md` |
| `EXP-2026-08-ASSET-TREND-MONTHLY-001` | blocked (missing EFA/GSG; no silent substitution) | `research/reviews/REV-2026-08-ASSET-TREND-001.md` |

## Recovery IDs

- BTC: `EXP-2026-08-BTC-OVERNIGHT-HOURLY-002` (offline from archived hourly CSV)
- Crypto: `EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002` (offline from Round-1 `prices.csv`)
- Asset trend: no `.002` this round — strategy stays researched/E1

## Data policy

Raw vendor bars under `data/` are gitignored. Manifests and reviews are committed.
