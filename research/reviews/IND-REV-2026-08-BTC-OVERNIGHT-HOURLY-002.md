# Independent Read-Only Review — BTC Overnight Hourly .002

- **experiment_id:** EXP-2026-08-BTC-OVERNIGHT-HOURLY-002
- **artifact:** `research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002/`
- **review_date:** 2026-08-02
- **reviewer:** independent machine-agent read-only reviewer (nemotron-3-ultra) — not the integrator; no experiment re-run, no artifact modification; not a human audit
- **review_summary_sha256:** `3f005cfc143d7b999c1c1041dcbc6fb729cc2054056454198e8acfd5553ae763` — digest of the reviewer's returned summary (provenance fingerprint only; the external summary is not retained in this repository and this record is self-contained)
- **scope:** artifact trust / integrity only
- **provenance note:** this record was transcribed into the repository by the integrator from the independent reviewer's returned verdict; the reviewer itself is read-only and did not author repository files. Citations such as `metrics.csv` or `checks.json` are relative to the experiment directory named above.

## Verdict

`artifact_accepted_with_limitations`

- **defects:** `[]`
- **source_cache_sha256:** `417e6b4a96c0b2c31daca1905eeae56b5789a11e90f55b57df8284d0bfd4ce72`

## Checks performed

- SHA-256 of source cache, local file, and manifest all match the hash above.
- Exact clock semantics: entry at 22:00 UTC open, exit at 00:00 UTC open (entry + 2 h); hold = 2.0 h confirmed from `trades.csv` rows against `data.csv` open prices.
- Trade count and dates: n = 697 completed trade days; entries 2024-08-30 → 2026-07-29; last exit 2026-07-30T00:00:00Z.
- Cost units: `fee_bps_per_fill` ∈ {0, 1, 5, 10, 20} × 2 fills per round trip on primary and placebos; buy-and-hold is gross-only.
- Fee arithmetic: `net_return_Xbps = gross_return - 2·X/10000` for all tiers (spot-checked; consistent across all 697 rows).
- Metrics recalculated to machine precision: mean = −2.8926127e−05, ann. vol = 0.1183696, Sharpe = −0.0891955, CAGR = −1.74% — all match `period_metrics.csv` and `metrics.csv`.
- Annualization factor 365 on daily observations; vol = std(daily)·√365; Sharpe = mean·365/ann_vol.
- Placebo windows: 11 non-overlapping 2 h windows + primary = 12; primary ranks 9/12 at 0 bps.
- Incomplete-bar exclusion: frozen cache 2024-08-30 00:00 → 2026-07-30 23:00 UTC; no live retrieval; no wall-clock filtering.
- No look-ahead: entry/exit at exact bar opens; return = exit/entry − 1.
- Timezone explicit: UTC open-time labels throughout.
- Provenance: code_commit 8104683, run_git_commit 2fcd741, git_dirty_at_start = false, not_cached = true.

## Evidence citations

- `data_manifest.json` source_cache_sha256 matches local SHA-256.
- `trades.csv` row 1: entry 59041.44140625 (2024-08-30 22:00 open) → exit 59119.34765625 (2024-08-31 00:00 open); row 697: entry 63778.4296875 (2026-07-29 22:00 open) → exit 63893.421875 (2026-07-30 00:00 open).
- `trades.csv` net-return tiers consistent with gross − 2·fee/10 000 on all 697 rows.
- `period_metrics.csv` row 1: mean_return −2.892612721276676e−05, vol 0.11836960467529596, sharpe −0.08919550303155954, n_obs 697.
- `metrics.csv` primary_22_00_fee_0bps sharpe −0.08919550303155954, cagr −0.017410563416605296; buyhold_gross sharpe 0.31516406141930225; placebo rank 9/12 at fee 0 bps.
- `checks.json` all 6 checks passed.
- `verdict.json` evidence_level E2, result_verdict inconclusive, reproduction_status partial.
- `REVIEW.md` integrator audit passed; local point estimates unfavorable to the hypothesis; non-claims listed.

## Limitations

- Yahoo/yfinance hourly venue proxy (not Gemini/Bitfinex per paper).
- Sample wholly post-paper (2024-08-30 → 2026-07-30); cannot reproduce the 2015–2021 study window.
- Exact open-time labels assumed; exchange clock/print quality unknown.
- No spread/slippage/funding modeled beyond the fee_bps_per_fill grid.
- Placebo windows descriptive only; primary window pre-specified.
- Buy-and-hold comparison is full-day 00:00 open-to-open, not a matched 2 h hold.
- Offline cache only; no live download.
- E2 diagnostic ceiling; not source-faithful reproduction.

## Explicit non-claims

This review establishes **artifact integrity only**. It does **not** constitute strategy validation, paper reproduction, or live-readiness approval, and it authorizes **no** vault promotion or evidence-level change. The artifact's local point estimates are *unfavorable* to the diagnostic hypothesis (negative gross mean, underperforms buy-and-hold, placebo rank 9/12); acceptance refers to artifact trust, not favorable evidence.

## Frozen-state note

The frozen artifact's internal `reviewer_status: pending` reflects its immutable pre-review state. This record lives outside the frozen experiment directory, which is intentionally unchanged.
