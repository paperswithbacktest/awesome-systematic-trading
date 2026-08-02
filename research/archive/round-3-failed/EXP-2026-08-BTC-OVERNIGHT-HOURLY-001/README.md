# EXP-2026-08-BTC-OVERNIGHT-HOURLY-001

## BTC Overnight Seasonality Hourly Diagnostic

**Experiment ID:** EXP-2026-08-BTC-OVERNIGHT-HOURLY-001  
**Strategy ID:** STRAT-CRYPTO-BTC-OVERNIGHT  
**Strategy Title:** Overnight Seasonality in Bitcoin  
**Experiment Class:** diagnostic  
**Evidence Level:** E2  
**Result Verdict:** inconclusive  
**Reviewer Status:** pending

## Hypothesis

A fixed long BTC position held only from **22:00 UTC to 00:00 UTC** each day has positive expected return after realistic all-in trading costs, relative to buy-and-hold and to other non-overlapping two-hour UTC windows.

## Data

- **Provider:** yfinance (venue proxy — not Gemini/Bitfinex)
- **Instrument:** BTC-USD
- **Frequency:** hourly
- **Timezone:** UTC
- **Date Range:** 2024-08-30 to 2026-07-30
- **Candle Convention:** open-time labels (yfinance)
- **Incomplete Bars:** Excluded

## Signal & Execution

- **Entry:** First bar at/after 22:00 UTC — go long 100% BTC at bar open
- **Exit:** First bar at/after 00:00 UTC next day — flatten at bar open
- **Frequency:** One trade observation per calendar day (when both legs exist)
- **Leverage:** None (unlevered primary variant)

## Cost Model

| Parameter | Value |
|-----------|-------|
| fee_bps_per_fill | [0, 1, 5, 10, 20] |
| n_fills_per_round_trip | 2 (entry + exit) |
| spread_bps | [0] |
| slippage_bps | [0] |
| cash_return | none |

Costs charged only on active trade days.

## Metrics & Annualization

- **Return observation frequency:** Daily (one P&L per trade day)
- **Annualization factor:** 365 (NOT 8760)
- **Metrics:** Sharpe, CAGR, vol, max_dd, total_return, mean daily trade return, hit rate

## Variants Tested

1. **Primary:** 22:00–00:00 window at each fee level
2. **Buy & Hold:** Over same calendar days at each fee level
3. **Placebo:** 11 other non-overlapping 2-hour UTC windows (0-2, 2-4, ..., 20-22) at each fee level

## Key Results (Primary Window, 0bps fees)

- **Sharpe:** -0.107
- **CAGR:** -0.019
- **Total Return:** -0.037
- **Trade Days:** 699
- **Hit Rate:** 0.471

## Reproduction

```bash
.venv/Scripts/python.exe research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/run.py
.venv/Scripts/python.exe -m research.common.validate research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001
```

## Known Limitations

1. yfinance hourly data is a venue proxy (not Gemini/Bitfinex); limited history from ~2014
2. No spread/slippage data available
3. Candle timestamp convention: yfinance uses open-time labels
4. Annualization factor = 365 (daily trade observations) not 8760
5. Only fee_bps_per_fill costs modeled; no spread, slippage, funding, or borrow costs
6. Multiple testing across placebo windows not corrected
7. Sample period may not match paper period (paper ~2015-2021)

## Promotion Blockers

- Venue proxy (yfinance) not source venue (Gemini/Bitfinex)
- Limited history (yfinance hourly from ~2014)
- No spread/slippage data available
- Multiple testing across 12 placebo windows not corrected
- Cost model only includes fee_bps_per_fill; no funding, borrow, or impact
- Sample period may not match paper period (paper ~2015-2021)
