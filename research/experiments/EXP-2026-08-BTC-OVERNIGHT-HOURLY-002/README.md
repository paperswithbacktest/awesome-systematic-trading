# EXP-2026-08-BTC-OVERNIGHT-HOURLY-002

Offline exact-clock diagnostic of BTC overnight seasonality.

- **Supersedes:** EXP-2026-08-BTC-OVERNIGHT-HOURLY-001 (reviewer-rejected)
- **Paper:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4081000
- **Data:** offline Yahoo BTC-USD hourly open-time cache, 2024-08-30 → 2026-07-30
- **Rule:** exact entry hour open → entry+2h open (primary 22:00→00:00)
- **Annualization:** 365 (one observation per completed trade day)
- **Costs:** fee grid [0, 1, 5, 10, 20] bps/fill × 2 fills on primary/placebos; B&H is **gross only**
- **Evidence:** E2 diagnostic / partial / inconclusive

## Key results (primary 0 bps)

| Metric | Value |
|--------|-------|
| Sharpe | -0.089 |
| CAGR | -1.74% |
| Mean | -0.29 bps/day |
| t-stat | -0.12 |
| N | 697 |
| B&H Sharpe (gross) | 0.315 |
| Placebo rank (0 bps Sharpe) | 9/12 |
| Placebo windows produced | 11 |

## Reproduce

```bash
.venv/Scripts/python.exe research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002/run.py
.venv/Scripts/python.exe -m research.common.validate research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002
```

## Limitations

Yahoo venue proxy; post-paper sample only; no microstructure costs beyond fee grid.
This does **not** validate or reject the original paper.
