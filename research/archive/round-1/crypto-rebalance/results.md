# Rebalancing Premium in Cryptocurrencies — Local Backtest Results

- **Date:** 2026-08-02
- **Script:** `backtest.py` (this directory); data cached in `prices.csv`
- **Data:** yfinance daily adjusted closes (`auto_adjust=True`), 12 large-cap USD pairs:
  BTC, ETH, XRP, LTC, BCH, ADA, DOGE, DOT, LINK, XLM, TRX, ETC
- **Sample:** 2020-08-20 → 2026-08-02 (2,174 days). Start is gated by DOT-USD
  (listed 2020-08); no tickers dropped for data errors (spike-and-revert check passed
  for all 12). All cryptos trade 7 days/week; annualization uses 365 days, rf = 0.
- **Setup:** equal weight 1/N across the 12 names. Rebalance variants: none (buy & hold),
  daily, weekly (Mondays), monthly (first trading day of month). Costs charged per unit
  of one-sided turnover (sum of |Δweight|) at rebalance.

## Metrics per variant × cost level

| Variant | Fee (bps) | CAGR | Vol | Sharpe | MaxDD |
|---|---|---|---|---|---|
| Buy & Hold | 0/5/10/20 | 27.8% | 86.5% | 0.71 | −88.4% |
| Daily | 0 | 33.9% | 75.1% | 0.77 | −80.6% |
| Daily | 5 | 33.5% | 75.1% | 0.76 | −80.7% |
| Daily | 10 | 33.1% | 75.1% | 0.76 | −80.8% |
| Daily | 20 | 32.2% | 75.1% | 0.75 | −81.0% |
| Weekly | 0 | 36.8% | 75.8% | 0.79 | −80.8% |
| Weekly | 5 | 36.6% | 75.8% | 0.79 | −80.8% |
| Weekly | 10 | 36.4% | 75.8% | 0.79 | −80.8% |
| Weekly | 20 | 36.0% | 75.8% | 0.79 | −80.9% |
| Monthly | 0 | 39.7% | 76.7% | 0.82 | −81.3% |
| Monthly | 5 | 39.6% | 76.7% | 0.82 | −81.3% |
| Monthly | 10 | 39.5% | 76.7% | 0.82 | −81.3% |
| Monthly | 20 | 39.3% | 76.7% | 0.81 | −81.3% |

(Buy & Hold trades only once at inception, so fees are negligible for it.)

**Rebalancing premium (gross, vs buy-and-hold CAGR):** daily **+6.1%/yr**,
weekly +9.0%/yr, monthly +11.9%/yr.

**Daily vs monthly net CAGR by fee (fine sweep):**

| Fee | Daily | Monthly | Diff |
|---|---|---|---|
| 0 bps | 33.9% | 39.7% | −5.8% |
| 5 bps | 33.5% | 39.6% | −6.1% |
| 10 bps | 33.1% | 39.5% | −6.4% |
| 20 bps | 32.2% | 39.3% | −7.1% |
| 50 bps | 29.7% | 38.7% | −9.0% |

Average annual turnover: daily ≈ 634%/yr, monthly ≈ 146%/yr.

## Key question

Gross of costs, the daily-rebalancing premium over buy-and-hold is **+6.1%/yr** in CAGR
(Sharpe 0.77 vs 0.71) — real but modest, and it is the *weakest* of the three rebalancing
frequencies: monthly rebalancing earns +11.9%/yr gross, because in this sample the crypto
cross-section trends at short horizons, so daily rebalancing sells winners too early.
Consequently **daily rebalancing already underperforms monthly at 0 bps — there is no
positive fee crossover**; every additional bp of fees just widens the gap
(≈ −0.6%/yr per 10 bps, driven by daily's ~4.3× higher turnover). Daily rebalancing only
beats buy-and-hold net of costs: it stays ahead of B&H even at 50 bps
(29.7% vs 27.8% CAGR), so the premium itself is robust to realistic taker fees —
it just isn't maximized at daily frequency.

## Caveats

- **Survivorship bias:** basket is today's large caps with long history; dead/delisted
  2018-vintage coins (the paper's universe included several) are excluded, flattering
  all variants roughly equally. The relative premium between variants is less affected
  than the level.
- **Sample window:** starts 2020-08 (gated by DOT). Extending to 2018 requires dropping
  DOT from the basket; not done here.
- **Proxy quality:** yfinance closes are composite quotes, not a single venue; daily
  close-to-close ignores intraday execution and spread, which matters at 634%/yr turnover.
- **Fee model:** cost per unit of one-sided turnover, no slippage, no borrow costs
  (this test is long-only, unlike the paper's long/short implementation).
- Annualization uses 365 days and rf = 0; last bar (2026-08-02) may be a partial day.
- The note's QuantConnect implementation (daily rebalance, 70% drifting short leg,
  0.5 bp fee) is a different construction; this test isolates the rebalancing premium
  itself per the local TEST spec.

## Files

- `backtest.py` — self-contained script (caches `prices.csv`, reruns use cache)
- `prices.csv` — raw daily closes for the 12 tickers, 2018-01-01 onward
- `metrics.csv` — the variant × fee metrics table
- `equity.png` — daily-rebalance (gross) vs buy-and-hold equity curves
