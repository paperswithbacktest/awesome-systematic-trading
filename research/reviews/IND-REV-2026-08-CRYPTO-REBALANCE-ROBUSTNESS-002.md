# Independent Read-Only Review — Crypto Rebalance Robustness .002

- **experiment_id:** EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002
- **artifact:** `research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002/`
- **review_date:** 2026-08-02
- **reviewer:** independent machine-agent read-only reviewer (nemotron-3-ultra) — not the integrator; no experiment re-run, no artifact modification; not a human audit
- **review_summary_sha256:** `12482778beab3bfbf91730dfc498b94dbaddf216755475f6c9765085a55c2e2a` — digest of the reviewer's returned summary (provenance fingerprint only; the external summary is not retained in this repository and this record is self-contained)
- **scope:** artifact trust / integrity only
- **provenance note:** this record was transcribed into the repository by the integrator from the independent reviewer's returned verdict; the reviewer itself is read-only and did not author repository files. Citations such as `metrics.csv` or `checks.json` are relative to the experiment directory named above.

## Verdict

`artifact_accepted_with_limitations`

- **defects:** `[]`
- **source_cache_sha256:** `84a1db1b2e703dc4fb12b664d058024e3e440fb7c61296fa5f71686317d68a57`

## Checks performed

- Source cache SHA-256 consistent across `config.yaml`, `data_manifest.json`, `checks.json`, and `verdict.json`.
- Analysis end 2026-08-01 — frozen cutoff, no wall-clock dependency (`run.py` ANALYSIS_END fixed).
- Primary sample: `full_common_12` cohort, 2020-08-21 → 2026-08-01 (n = 2172; DOT first valid 2020-08-20).
- Lagged weight semantics: prior-close decision (t−1), earn close-to-close return t — validated by the daily equal-weight gross == cross-sectional mean return identity assertion.
- Cost model: `risky_traded_notional` cash-excluded; establishment = 1.0; no terminal liquidation; fee grid {0, 5, 10, 20, 50} bps.
- Turnover arithmetic: daily avg annual traded notional 6.51 (38.72 total / 5.95 y); monthly 1.63 (9.72 / 5.95 y) — matches metrics.
- Key metric recalculation: `full_common_12` buy-and-hold Sharpe 0.7100 (mean 0.00168231 × 365 / ann. vol 0.86479); daily Sharpe 0.7611; monthly Sharpe 0.8146; CAGR deltas vs B&H +5.88% (daily), +11.65% (monthly).
- Artifact shape: 81 metrics rows (4 cohorts × 4 freqs × 5 fees + 1), 80 comparisons, 4 cohorts, 16 period rows — internally consistent.
- Provenance: code_commit 8104683e, run_git_commit ebab7bf5, git_dirty_at_start = false, source/local/manifest SHA match, not_cached = true.
- Existing `REV-2026-08-CRYPTO-REBALANCE-002.md` identified as an integrator audit (same agent), with independent external review pending — which this record now provides.

## Evidence citations

- `config.yaml`, `data_manifest.json`, `checks.json`, `verdict.json`: source_cache_sha256 84a1db1b…68a57.
- `run.py`: ANALYSIS_END = 2026-08-01; simulate() prior-close (t−1) decision convention; daily EW identity assertion.
- `cohorts.csv`: full_common_12 actual_start 2020-08-21, actual_end 2026-08-01, n_return_obs 2172.
- `metrics.csv`: full_common_12_buyhold_fee0 sharpe 0.7100496575614557; full_common_12_daily_fee0 sharpe 0.7611288074343484; full_common_12_monthly_fee0 sharpe 0.8145931147381914.
- `comparisons.csv`: full_common_12 daily_minus_buyhold cagr_delta 0.05877575002865609; monthly_minus_buyhold cagr_delta 0.11649090142505969.
- `turnover.csv`: full_common_12 daily total traded notional 38.72076360102554; monthly 9.71570971082212.
- `verdict.json`: reviewer_status pending (frozen state), result_verdict inconclusive, evidence_level E2.
- `REV-2026-08-CRYPTO-REBALANCE-002.md`: independent external review PENDING, vault promotion blocked.

## Limitations

- Static 12-asset Yahoo survivor proxy — not the paper's 27-coin point-in-time Bitfinex universe.
- Long-only only; the paper's 70% short drifting leg is not tested.
- No venue-specific spread/slippage beyond the fee grid.
- Longest-contiguous-segment sample selection is post-hoc data cleaning, not point-in-time eligibility.
- E2 ceiling; not source-faithful reproduction.

## Explicit non-claims

This review establishes **artifact integrity only**. It does **not** constitute strategy validation, paper reproduction, or live-readiness approval, and it authorizes **no** vault promotion or evidence-level change. Apparent metric improvements over buy-and-hold are produced on a static survivor proxy without the paper's universe or short leg and cannot be treated as a source-faithful reproduction.

## Frozen-state note

The frozen artifact's internal `reviewer_status: pending` reflects its immutable pre-review state. This record lives outside the frozen experiment directory, which is intentionally unchanged.
