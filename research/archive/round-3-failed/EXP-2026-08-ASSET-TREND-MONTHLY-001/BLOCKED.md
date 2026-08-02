# BLOCKED — EXP-2026-08-ASSET-TREND-MONTHLY-001

**Status:** blocked  
**Date (UTC):** 2026-08-02  
**Harness baseline:** `35e0ac0`  
**Review:** `research/reviews/REV-2026-08-ASSET-TREND-001.md`

## Why blocked

1. Yahoo/yfinance rate-limited during worker acquisition; no usable live download completed.
2. Required/preferred SPEC universe cannot be assembled from local cache:

| Sleeve | Required | Offline available |
|--------|----------|-------------------|
| US equities | SPY | yes (Round-1) |
| Intl equities | EFA | **no** |
| Bonds | IEF | yes |
| REITs | VNQ | yes |
| Commodities | GSG (DBC only with explicit sub) | GSG **no**; DBC yes |

3. Available offline set is `SPY, IEF, GLD, DBC, VNQ`.  
   **GLD is not an allowed substitute for EFA.** Using it would silently redefine the strategy.

## What was not produced

- No valid metrics, verdict, checks, or data_manifest for a completed experiment.
- Empty/stub CSVs under `data/` are not evidence.
- No evidence-level promotion; strategy note stays `researched` / E1.

## Future path

- Acquire/cache `EFA` + `GSG` (or mint a **new** experiment ID with an explicitly titled alternate universe).
- Do not “finish” this ID with a silent substitution.
