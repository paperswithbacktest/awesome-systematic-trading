# Review: EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002

**Reviewer role:** Hermes integrator (same agent that authored the recovery runner)  
**Date (UTC):** 2026-08-02  
**Artifact:** `research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002/`  
**Source freeze (S):** `8104683e74be96f53f2564d7aa24908ea0687dc4`  
**Run base:** `ebab7bf52c28eb320f2cfe1b6a461756a69fee31`  
**Harness baseline:** `35e0ac0a96da66cec194eeaf3eda4016554d8748`  
**Input cache SHA-256:** `84a1db1b2e703dc4fb12b664d058024e3e440fb7c61296fa5f71686317d68a57`

## Disposition

| Field | Value |
|--------|--------|
| Mechanical validator | **PASS** |
| Integrator semantic audit | **PASS** |
| Independent external review | **PENDING** |
| `reviewer_status` | **pending** |
| `result_verdict` | **inconclusive** (runner-default) |
| `evidence_level` | **E2** (candidate record only) |
| `reproduction_status` | **partial** |
| Vault promotion | **blocked** until independent review |

This is an **integrator audit**, not an independent acceptance. A separate audit script is evidence hygiene; it does **not** create a second reviewer.

## What was checked (integrator)

1. **Offline only** — Round-1 Yahoo static-survivor `prices.csv`; no live download.
2. **Frozen cutoff** — `ANALYSIS_END=2026-08-01`; no wall-clock filtering.
3. **Primary sample honesty** — cached panel `2018-01-01 → 2026-08-01`; primary `full_common_12` return sample `2020-08-21 → 2026-08-01` (`n=2172`, starts when DOT joins; DOT first valid `2020-08-20`).
4. **Four cohorts** — `full_common_12`, `start_2018_no_dot`, `start_2020_no_dot`, `exclude_dot_same_window`.
5. **Timing** — prior-close decision; earn close-to-close return t; daily EW gross == cross-sectional mean return (reconstructed identity check).
6. **Costs** — `risky_traded_notional` cash-excluded; initial cash→EW establishment = 1.0; no terminal liquidation; fee grid `{0,5,10,20,50}` bps; CAGR nonincreasing in fees for fixed cohort/freq.
7. **Artifact shape** — 80 metrics rows, 80 comparisons, 16 period rows, 4 cohorts; comparisons reproduce primary CAGR deltas.
8. **Provenance** — `code_commit=S`, `run_git_commit=ebab7bf`, `git_dirty_at_start=false`; source/local/manifest SHA match; `not_cached: true` (raw bars gitignored).
9. **Daily contiguous** — full_common_12 return index is daily-contiguous after longest-segment trim.

## Local point estimates (proxy only — not paper reproduction)

**Primary cohort `full_common_12`, 0 bps:**

| Variant | Sharpe | CAGR vs B&H |
|---------|--------|-------------|
| Buy&Hold (drift) | **0.710** | baseline |
| Daily EW | **0.761** | **+5.88%** CAGR |
| Monthly EW | **0.815** | **+11.65%** CAGR |

At **20 bps** fee (primary cohort): daily CAGR **31.76%**, monthly CAGR **38.81%**.

Local point estimates on this frozen static-survivor Yahoo long-only proxy **favor periodic rebalancing** (especially monthly) over drifted EW B&H after the stated cost model. Fees reduce levels but do not reverse the monthly-over-daily / monthly-over-B&H ordering on the primary cohort at 0 and 20 bps in the committed tables.

Committed `result_verdict` remains **`inconclusive`** so it stays consistent with the deterministic runner output on re-run. Favorable local point estimates are the integrator’s reading of the metrics, not independent acceptance of a source claim.

## Explicit non-claims / promotion blockers

- **Not** the paper’s 27-coin PIT Bitfinex universe (static 12-asset Yahoo survivor only).
- **Not** long-rebalanced / short-drifting (70% short leg omitted).
- **Not** venue-faithful execution (Yahoo composite closes; fee grid only).
- Longest-contiguous-segment cleaning is post-hoc data hygiene, not PIT eligibility.
- Source-reported Sharpe (`0.698` in repo README table) remains a separate E0/E1 claim and must **not** be overwritten by local Sharpes.
- E2 ceiling; no E3+, validated, reproduced, or live-candidate.

## Supersedes

`EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001` (archived incomplete: live Yahoo rate-limit → zero instruments → empty-DF crash).

## Vault guidance (until independent review)

- Do **not** set strategy `status: experimented` yet.
- Do **not** move pipeline stages.
- Do **not** overwrite source Sharpe with local Sharpe.
- Optional later fields only after external review: `latest_experiment_id`, candidate E2 link, separate `local_sharpe_ratio`.
