# Evidence Levels & Workflow Statuses

## Evidence levels (quality of proof)

| Code | Name | Meaning |
|------|------|---------|
| **E0** | Source claim | README/paper reported metric only |
| **E1** | Code inspection | Rules + implementation deltas documented |
| **E2** | Proxy / diagnostic | Related hypothesis tested via **contract-compliant** experiment artifact |
| **E3** | Reproduction | Materially faithful implementation of source rules |
| **E4** | Robustness | Survives periods, costs, params, universe checks |
| **E5** | Forward evidence | Paper-trade or genuine OOS after freeze |

## Workflow status (process state)

| Status | Meaning |
|--------|---------|
| `stub` | Captured from catalog; brief only |
| `researched` | Method + deltas documented |
| `experimented` | ≥1 **contract-compliant** experiment under `research/experiments/` |
| `reproduced` | E3+ source-faithful test completed |
| `validated` | E4+ and adversarial review approved |
| `live-candidate` | Ops/risk/execution approvals complete |
| `rejected` | Explicitly discarded with reason |

Deprecated: bare `backtested` (ambiguous; use `experimented` + evidence_level).

Round-1 vault scratchpads and `research/archive/round-1/` scripts are **legacy exploratory proxies**. They do **not** qualify a strategy for `status: experimented` or evidence ≥ E2.

## Round-1 archival classification (frozen)

| Strategy | Workflow status | Evidence | Legacy classification |
|----------|-----------------|----------|------------------------|
| Overnight Seasonality in Bitcoin | `researched` | E1 | exploratory resolution-mismatched daily proxy |
| Rebalancing Premium in Cryptocurrencies | `researched` | E1 | exploratory static-survivor allocation proxy |
| Asset Class Trend-Following | `researched` | E1 | exploratory paper-informed ETF proxy |

## Strategy note YAML fields (target)

```yaml
status: researched | experimented | reproduced | validated | rejected
reported_sharpe_ratio: 0.892
reported_sharpe_source: awesome-systematic-trading
sharpe_ratio: 0.892                 # compatibility alias = reported only
local_sharpe_ratio: null            # filled only from accepted experiment
evidence_level: E1
legacy_experiment_class: exploratory-proxy   # optional
legacy_result_status: not-promotable         # optional
best_experiment: null
backtest_class: resolution-mismatched-diagnostic | static-survivor-allocation-proxy | paper-informed-etf-proxy | replication
reproduction_status: not-attempted | partial | faithful | failed
live_eligibility: blocked | candidate
promotion_blockers: []
```

Rules:
- `reported_sharpe_ratio` is immutable source claim.
- `local_sharpe_ratio` is only populated from an accepted experiment artifact.
- `sharpe_ratio` is a compatibility alias for MOCs/Dataview; never overwrite with local results.
- Local metrics live on experiment notes / `verdict.json`.
