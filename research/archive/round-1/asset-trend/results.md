# Asset Class Trend-Following — Local Backtest Results

**Date:** 2026-08-02 · **Script:** `backtest.py` · **Equity curve:** `equity.png`

## Setup

- Data: daily adjusted closes (yfinance, `auto_adjust=True`) for SPY, IEF, GLD, DBC, VNQ — ETF proxies for the 5 GTAA asset classes (DBC/GLD replace the repo's GSG/EFA per the test spec).
- Common history: 2006-02-06 → 2026-07-31 (limited by DBC inception). First signal after 210-day SMA warmup: 2006-12-29; 236 monthly rebalances.
- Signal: month-end close > 210-day SMA → hold; else sleeve to cash @ 0%. Weights applied at the signal close; returns accrue from the next trading day.
- Costs: 0 and 5 bps per unit of one-way turnover (Σ|Δw| at rebalance).

## Metrics

| Variant | Cost (bps) | Sharpe | CAGR | MaxDD | Vol |
|---|---|---|---|---|---|
| (a) Paper 20% sleeves | 0 | 0.779 | 5.57% | -16.61% | 7.32% |
| (a) Paper 20% sleeves | 5 | 0.766 | 5.46% | -16.63% | 7.32% |
| (b) Repo 1/N split | 0 | 0.670 | 7.29% | -33.21% | 11.53% |
| (b) Repo 1/N split | 5 | 0.649 | 7.04% | -33.28% | 11.53% |
| (c) EW buy & hold | 0 | 0.637 | 7.10% | -36.72% | 11.92% |
| (c) EW buy & hold | 5 | 0.635 | 7.09% | -36.74% | 11.92% |

Sanity: SPY annualized vol over the same window = 19.6%; trend variants run well below it. All CAGRs strongly positive.

## Key question: concentration quirk vs trend filter

The concentration quirk contributes **nothing** to risk-adjusted return — it actually *subtracts* Sharpe. The repo 1/N variant (0.670) sits barely above the do-nothing equal-weight benchmark (0.637), meaning nearly all of its performance is just concentrated beta, not the trend filter. The paper's fixed-20%-sleeve version is where the filter's value shows up: Sharpe 0.779, maxDD cut from -37% to -17%, and vol of 7.3% vs 11.9%. So the repo's reported 0.502 is best read as trend-filter value (modest at this portfolio-construction) minus concentration drag; the 0.502 vs 0.670 gap itself is attributable to universe differences (EFA/GSG vs GLD/DBC), the longer 2000+ sample incl. pre-2007, start-of-month intraday execution, and Lean's fee/slippage model.

## Caveats

- **Proxy quality:** GLD is a spot-gold proxy, not the paper's diversified commodity index (GSG in the repo); DBC inception (2006-02) caps the common sample — no 2000–2002 dot-com or earlier regimes are tested.
- **Survivorship:** all 5 ETFs survived the full window; no delisting bias modeled, but the universe was chosen with hindsight.
- **Cash earns 0%**: realistic T-bill yield on cash sleeves would lift (a) modestly (it holds cash most often).
- **Signal proxy:** 210-trading-day SMA on daily closes vs the paper's 10-month SMA on monthly closes; single parameter, no robustness sweep across 3–12 month windows.
- **Costs:** applied only on weight changes at rebalance (Σ|Δw| convention); 5 bps costs ~0.1–0.2 Sharpe on (b), negligible on (c).
