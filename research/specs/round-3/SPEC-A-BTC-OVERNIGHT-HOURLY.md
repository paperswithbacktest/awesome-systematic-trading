# SPEC-A — BTC Overnight Seasonality (Hourly Window)

**Experiment ID:** `EXP-2026-08-BTC-OVERNIGHT-HOURLY-001`  
**Strategy ID:** `STRAT-CRYPTO-BTC-OVERNIGHT`  
**Strategy title:** Overnight Seasonality in Bitcoin  
**Worker write root (only):** `research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/`  
**Evidence target:** E2 (partial E3 only if venue-faithful data is obtained)  
**experiment_class:** `diagnostic`  
**source_repo_commit baseline:** `1ce1eb2` (update `code_commit` to harness baseline after commit)

## Hypothesis

A fixed long BTC position held only from **22:00 UTC to 00:00 UTC** each day has positive expected return after realistic all-in trading costs, relative to buy-and-hold and to other non-overlapping two-hour UTC windows.

## What this is / is not

- **Is:** a clock-window test of the paper/repo rule on hourly (or finer) bars with explicit UTC timestamps.
- **Is not:** another daily close→open proxy. Round-1 daily results are archival only.
- **Is not:** a claim that Yahoo/Binance equals Gemini/Bitfinex. Venue mismatch must be stated.

## Data requirements

Priority order:
1. Venue-specific UTC hourly/minute bars (Gemini preferred; Bitfinex acceptable as repo-aligned).
2. Public exchange hourly (e.g. Binance) if (1) unavailable — label as venue proxy.
3. yfinance hourly only as short-window fallback — label as limited proxy.

Required metadata in `data_manifest.json`:
- provider, instruments, frequency, timezone (`UTC`), start, end
- sha256 for every cached file
- `not_cached: true` + retrieval recipe if raw bars are local-only
- note on candle label semantics (open-time vs close-time)

Exclude incomplete/current bars.

## Signal & execution

- Entry: first bar at/after **22:00 UTC** — go long 100% BTC.
- Exit: first bar at/after **00:00 UTC** — flatten.
- One trade return observation per calendar day (when both legs exist).
- Flat all other hours.
- No leverage in the primary variant (ignore repo `SetLeverage(10)` unless a labeled secondary).

## Cost model

```yaml
costs:
  fee_unit: bps_per_fill
  fee_bps_per_fill: [0, 1, 5, 10, 20]
  n_fills_per_round_trip: 2
  spread_bps: [0]          # optional secondary grid if data supports
  slippage_bps: [0]
  funding_mode: excluded   # spot; state if using perps
  borrow_mode: not_applicable
```

Charge costs **once per entry and once per exit** on active trade days only.

## Metrics & annualization

- Return observation frequency: **daily** (one P&L per trade day)
- `annualization_factor: 365`  (**not** 8760)
- Metrics: Sharpe, CAGR, vol, max_dd, total_return, mean daily trade return, hit rate
- Required variants:
  - 22:00–00:00 window at each fee level
  - Buy & hold over same calendar
  - Placebo: other non-overlapping 2-hour UTC windows (full 12-slot grid if feasible)
- Period splits: full sample; if history allows, pre-paper-end vs post-paper-end (paper ~2015–2021)

## Structural checks (must pass in checks.json)

- no_lookahead
- timezone_explicit (UTC)
- data_hash_verified
- cost_units_verified (per fill, 2 fills/RT)
- annualization_verified (365)
- incomplete_bar_excluded

## Verdict constraints

- `reviewer_status: pending` (worker cannot approve)
- Default `evidence_level: E2` unless venue-faithful long history justifies partial E3
- `reproduction_status: partial` at best under free proxies; `not-attempted` if only daily data available
- Must list promotion blockers (venue, sample length, costs, multiple-testing on window selection)
- Forbidden phrases at E2: "validated", "dead on arrival", "confirmed edge", "production ready"

## Required outputs

Full experiment contract files under the write root only.  
Do **not** edit vault notes, MOCs, `research/common`, `research/contracts`, or other experiment dirs.

## Reproduction command (template)

```bash
.venv/Scripts/python research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/run.py
.venv/Scripts/python -m research.common.validate research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001
```
