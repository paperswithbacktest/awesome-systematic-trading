# Local Backtest — Overnight Seasonality in Bitcoin

**Date:** 2026-08-02
**Strategy note:** [[Overnight Seasonality in Bitcoin]]
**Script:** `backtest.py` (this directory) · **Data cache:** `btc_usd_daily.csv` · **Equity curve:** `equity.png`

## Data

- Source: yfinance `BTC-USD` daily OHLC, `auto_adjust=True`, maximum history.
- Range: **2014-09-17 → 2026-08-02**, 4,338 daily bars (BTC trades 24/7; 365 bars/year used for annualization).
- Daily return decomposition: overnight leg = prev close → open; intraday leg = open → close.
- yfinance daily bars are UTC-stamped, so the overnight leg approximates the note's 22:00→00:00 UTC window only loosely (it is a ~24h→24h close/open gap, not the paper's specific two-hour clock window).

## Results (2014-09-17 → 2026-08-02)

| Variant | Sharpe | CAGR | Max DD | Total Return |
|---|---|---|---|---|
| Buy & Hold | 0.959 | 51.4% | -83.4% | 13,672.4% |
| Intraday-only (0 bps) | 0.928 | 48.2% | -84.0% | 10,618.7% |
| Overnight-only (0 bps/fill) | 0.563 | 2.0% | -7.6% | 26.1% |
| Overnight-only (5 bps/fill) | -9.631 | -29.2% | -98.4% | -98.4% |
| Overnight-only (10 bps/fill) | -19.826 | -50.9% | -100.0% | -100.0% |
| Overnight-only (20 bps/fill) | -40.216 | -76.4% | -100.0% | -100.0% |

Leg decomposition (gross): overnight mean **+0.55 bps/day** (total +26% over ~12 years); intraday mean **+16.83 bps/day** (total +10,619%).

## Key Question: does the overnight edge survive realistic taker fees?

**No — there is no overnight edge at daily resolution to begin with, and any fee level annihilates the strategy.** The gross overnight leg earns only ~0.55 bps per day on average (2.0% CAGR, +26% total over ~12 years); the entire BTC return stream sits in the intraday (open→close) leg. A round trip costs 2 fills × fee, so even 5 bps/fill (10 bps/round trip ≈ 36.5%/yr of drag) turns the strategy sharply negative (-98% total), and 10–20 bps/fill wipes out the account. Unlike equities, BTC shows no close→open premium on UTC daily bars — consistent with a 24/7 market having no true "close" — so the paper's 22:00–00:00 UTC two-hour effect does not generalize to the daily overnight leg.

## Caveats

- **Window mismatch:** the paper's edge is a specific 2-hour clock window (22:00–00:00 UTC) measured on minute data from Gemini; this test uses daily OHLC, where "overnight" is a UTC midnight boundary with effectively zero time gap. A null result here does not refute the minute-resolution claim, but it does show the effect cannot be harvested with daily bars.
- **Data quality:** yfinance BTC-USD is a Yahoo composite, not a single exchange; open/close prints may embed small timing inconsistencies vs. Gemini/Bitfinex.
- **No survivorship bias** (single asset), but regime dependence is real: the sample covers multiple BTC halving cycles and the post-2024 ETF era.
- **Cost model:** flat bps per fill, no slippage/spread modeled — real taker costs would be worse, strengthening the negative conclusion.
- Sharpe computed on daily returns, annualized with √365.
