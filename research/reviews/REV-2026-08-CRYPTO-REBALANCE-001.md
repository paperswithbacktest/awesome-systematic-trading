# Review: EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001

**Reviewer:** Hermes (integrator, post-worker)  
**Date (UTC):** 2026-08-02  
**Harness baseline:** `35e0ac0`  
**Worker batch:** `deleg_89f7dcab` (timeout)  
**Artifact path:** `research/archive/round-3-failed/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001/`  
**Reviewer status:** **rejected / incomplete** (do not promote)

## Structural state

- Present: `config.yaml`, `run.py` only
- Missing: metrics, verdict, checks, data_manifest, README, lockfile
- Mechanical validator: **FAIL** (incomplete)
- Live Yahoo downloads: rate-limited; unfinished

## Material issues

1. Frozen config requests a large paper-like universe (~26 tickers) while the only offline cache has **12** Yahoo survivors.
2. Runner is live-download oriented; continuing it will re-trigger rate limits.
3. No completed cohort metrics; no establishment-cost audit trail.

## Terminal failure (post-timeout background process)

Live acquisition returned **zero instruments** after Yahoo rate limits:

```text
Got prices: (0, 0) (nan to nan)
Actual universe (0): []
AttributeError: 'float' object has no attribute 'date'
```

The runner then attempted `.date()` on NaN/float `data_start`. This is an **unhandled-empty-universe failure**, not an experiment result. No metrics, no E2 evidence, no vault promotion.

## Disposition

- Archived under `research/archive/round-3-failed/`.
- Do **not** re-run `.001`.
- Mint `EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002` as an explicit **static-survivor long-only proxy** using `research/archive/round-1/crypto-rebalance/prices.csv` only.
- No vault promotion from `.001`.
