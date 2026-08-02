# Review: EXP-2026-08-BTC-OVERNIGHT-HOURLY-001

**Reviewer:** Hermes (integrator, post-worker)  
**Date (UTC):** 2026-08-02  
**Harness baseline:** `35e0ac0`  
**Worker batch:** `deleg_89f7dcab` (timeout)  
**Artifact path:** `research/archive/round-3-failed/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/`  
**Reviewer status:** **rejected** (do not promote; leave immutable)

## Structural state

- Mechanical validator: **OK** (files/schema present)
- Research validity: **FAIL**

Validator success is **not** acceptance.

## Material defects

1. **Buy-and-hold cost model is wrong.** Round-trip fees are applied to every daily B&H return, turning the benchmark into a daily-churn strategy. B&H must be zero recurring cost (or one entry + optional terminal exit only).
2. **Declared date range is false.** Config/manifest claim `2016-01-01 → 2026-07-31`; actual cached sample is ~`2024-08-30 → 2026-07-30` (~699 trade days).
3. **History claims overstate coverage** ("from ~2014") while the artifact only holds ~2 years of hourly bars.
4. **Source paper URL** points at Quantpedia rather than the strategy note's SSRN paper.
5. **Entry rule softens the clock:** "first bar at/after 22:00" can silently shift the holding window; exact 22:00 / next-day 00:00 is required.
6. Worker self-reported `reviewer_status: pending` is correct; must not become approved.

## Soft finding (not a paper rejection)

Primary 22:00–00:00 window on this Yahoo hourly proxy is roughly flat/negative gross (Sharpe ≈ −0.11 at 0 bps). That is an **E2 sample observation only**, not evidence the paper is false.

## Disposition

- Archived under `research/archive/round-3-failed/` as an attempted, reviewer-rejected artifact.
- Recovery path: mint `EXP-2026-08-BTC-OVERNIGHT-HOURLY-002` offline from the cached CSV only.
- No vault promotion from `.001`.
