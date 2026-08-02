# REJECTED — EXP-2026-08-BTC-OVERNIGHT-HOURLY-001

**Status:** reviewer-rejected (structurally complete, methodologically invalid for promotion)  
**Date (UTC):** 2026-08-02  
**Review:** `research/reviews/REV-2026-08-BTC-HOURLY-001.md`

## Why rejected

1. Buy-and-hold charged full round-trip fees every day (invalid benchmark).
2. Config/manifest claimed 2016–2026; actual data is ~2024-08-30 → 2026-07-30.
3. Soft entry rule ("first bar at/after") can shift the window.
4. Source URL was Quantpedia, not SSRN paper.

## Recovery

`EXP-2026-08-BTC-OVERNIGHT-HOURLY-002` — offline correction from the same cached hourly CSV.
