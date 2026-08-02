# Review: EXP-2026-08-BTC-OVERNIGHT-HOURLY-002

**Reviewer role:** Hermes integrator (same agent that authored the recovery runner)  
**Date (UTC):** 2026-08-02  
**Artifact:** `research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002/`  
**Source freeze (S):** `8104683e74be96f53f2564d7aa24908ea0687dc4`  
**Run base (P):** `2fcd7415605e9af8758237b85a957126823e4dcd`  
**Harness baseline:** `35e0ac0a96da66cec194eeaf3eda4016554d8748`  
**Input cache SHA-256:** `417e6b4a96c0b2c31daca1905eeae56b5789a11e90f55b57df8284d0bfd4ce72`

## Disposition

| Field | Value |
|--------|--------|
| Mechanical validator | **PASS** |
| Integrator semantic audit | **PASS** |
| Independent external review | **PENDING** |
| `reviewer_status` | **pending** |
| `result_verdict` | **inconclusive** (runner-default; local point estimates unfavorable) |
| `evidence_level` | **E2** (candidate record only) |
| `reproduction_status` | **partial** |
| Vault promotion | **blocked** until independent review |

This is an **integrator audit**, not an independent acceptance. A separate audit script is useful evidence hygiene; it does **not** create a second reviewer.

## What was checked (integrator)

1. Offline only — archived Yahoo hourly cache; no live download.
2. Exact clock — entry `22:00 UTC` open → exit `00:00 UTC` open; hold always 2.0h; `n=697`.
3. Trade window — entries `2024-08-30` → `2026-07-29`; last exit `2026-07-30 00:00 UTC`. Cache bars cover through `2026-07-30 23:00 UTC` (coverage end ≠ last entry date).
4. Gross identity — `gross = exit/entry - 1`.
5. Fee arithmetic — `2 × fee_bps` exact on primary/placebos for `{0,1,5,10,20}`; means nonincreasing in fees.
6. B&H — single **gross-only** row; no daily fee churn (fixes rejected `.001`).
7. Placebos — 11 other 2h windows + primary = 12 at 0 bps; primary rank **9/12**.
8. Provenance — `code_commit=S`, `run_git_commit=P`, `git_dirty_at_start=false`; source/local/manifest SHA match; `not_cached: true` (raw bars gitignored).

## Local point estimates (not a paper verdict)

| Metric | Primary 0 bps |
|--------|----------------|
| Sharpe | **−0.089** |
| CAGR | **−1.74%** |
| Mean | **−0.29 bps/day** |
| t-stat | **−0.12** |
| N | **697** |
| B&H Sharpe (gross) | **0.315** |
| Placebo rank (0 bps) | **9/12** |

Local point estimates on this frozen Yahoo post-paper proxy **do not support** the diagnostic hypothesis (negative gross mean; underperforms B&H; weak placebo rank). Fees only worsen primary performance.

Committed `result_verdict` remains **`inconclusive`** so it stays consistent with the deterministic runner output on re-run. The unfavorable local point estimates are the integrator’s reading of the metrics, not an independent acceptance of a stronger claim.

## Explicit non-claims

- Does **not** reject or confirm SSRN `abstract_id=4081000`.
- Does **not** establish Gemini/Bitfinex venue fidelity.
- Does **not** cover the paper’s ~2015–2021 window.
- Source-reported Sharpe (`0.892` in repo README table) remains a separate E0/E1 claim.

## Supersedes

`EXP-2026-08-BTC-OVERNIGHT-HOURLY-001` (archived; reviewer-rejected for B&H fee churn, false dates, soft clock, wrong URL).

## Vault guidance (until independent review)

- Do **not** set strategy `status: experimented` yet.
- Do **not** move pipeline stages.
- Do **not** overwrite source Sharpe with local Sharpe.
- Optional later fields only after external review: `latest_experiment_id`, candidate E2 link, separate `local_sharpe_ratio`.
