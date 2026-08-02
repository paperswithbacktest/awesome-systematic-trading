# EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002

Offline **12-asset static-survivor long-only** rebalancing-frequency proxy.

- **Supersedes:** EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001 (incomplete; Yahoo 0 instruments)
- **Paper:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3982120
- **Cached panel:** offline Round-1 `prices.csv` only (2018-01-01 → 2026-08-01)
- **Primary full_common_12 sample:** 2020-08-21 → 2026-08-01 (n=2172; starts when DOT joins)
- **Universe:** BTC ETH XRP LTC BCH ADA DOGE DOT LINK XLM TRX ETC
- **Cohorts:** full_common_12, start_2018_no_dot, start_2020_no_dot, exclude_dot_same_window
- **Variants:** buyhold drift, daily, weekly, monthly EW
- **Costs:** risky_traded_notional; fees [0, 5, 10, 20, 50] bps; establishment 1.0; no terminal liq
- **Evidence:** E2 / partial / inconclusive

## Key (full_common_12, 0 bps)

| Variant | Sharpe | CAGR | Avg ann traded notional |
|---------|--------|------|-------------------------|
| Buy&Hold | 0.710 | 27.61% | 0.17 |
| Daily | 0.761 | 33.49% | 6.51 |
| Monthly | 0.815 | 39.26% | 1.63 |

## Reproduce

```bash
.venv/Scripts/python.exe research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002/run.py
.venv/Scripts/python.exe -m research.common.validate research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002
```

## Limitations

Not the paper construction. Survivorship and Yahoo venue effects remain. No short leg.
