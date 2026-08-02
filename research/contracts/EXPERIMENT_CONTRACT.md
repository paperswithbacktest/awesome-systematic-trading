# Experiment Contract v1

Every experiment directory under `research/experiments/` MUST satisfy this contract before review or vault integration.

## Required files

```text
EXP-<YYYY>-<MM>-<SLUG>-<NNN>/
├── README.md              # human summary + how to reproduce
├── config.yaml            # frozen run config
├── run.py                 # entrypoint
├── requirements-lock.txt  # pip freeze or equivalent
├── data_manifest.json     # inputs + hashes + provider metadata
├── metrics.csv            # primary table (variant × metric)
├── period_metrics.csv     # optional subperiod splits
├── equity.csv             # optional equity curve(s)
├── trades.csv             # optional trade blotter
├── checks.json            # structural QA results
├── verdict.json           # machine-readable conclusion
└── figures/               # optional plots
```

## config.yaml required keys

```yaml
experiment_id: EXP-2026-08-BTC-OVERNIGHT-HOURLY-001
strategy_id: STRAT-CRYPTO-BTC-OVERNIGHT
strategy_title: Overnight Seasonality in Bitcoin
experiment_class: replication | proxy | diagnostic | robustness
hypothesis: ""
source_paper_url: ""
source_repo_path: ""          # e.g. static/strategies/...
source_repo_commit: ""
code_commit: ""
run_timestamp_utc: ""
data:
  provider: ""
  instruments: []
  frequency: ""               # minute|hourly|daily|monthly
  timezone: UTC
  start: ""
  end: ""
  adjusted: true|false
universe:
  requested: []
  actual: []
  eligibility_rule: ""
signal:
  description: ""
  formation_timestamp: ""     # when signal is known
  execution_timestamp: ""     # when trade is allowed
costs:
  fee_bps_per_fill: []
  spread_bps: []
  slippage_bps: []
  cash_return: ""             # e.g. 0 | tbill | none
metrics:
  annualization_factor: 252|365|other
  risk_free_rate: 0.0
known_limitations: []
```

## verdict.json required keys

```json
{
  "experiment_id": "",
  "strategy_id": "",
  "hypothesis": "",
  "experiment_class": "proxy",
  "evidence_level": "E2",
  "result_verdict": "supported | unsupported | inconclusive",
  "reproduction_status": "not-attempted | partial | faithful | failed",
  "summary": "",
  "key_metrics": {},
  "promotion_blockers": [],
  "reviewer_status": "pending | approved | rejected",
  "reproduction_command": ""
}
```

## Structural checks (checks.json)

Workers must assert and record:

1. No same-bar look-ahead (signal available before execution).
2. Data timezone explicit and consistent with signal clock.
3. Incomplete current bar excluded if live/partial.
4. Annualization matches frequency (crypto 365, equities 252 unless justified).
5. Fee units consistent with turnover definition.
6. Input file SHA-256 present for every cached dataset.
7. Code commit / dirty-tree note recorded.
8. Benchmark and sample dates present.
9. Experiment class labeled honestly (`replication` only if materially faithful).
10. Known limitations non-empty when using free/proxy data.

## Promotion gates

| Target evidence | Minimum bar |
|-----------------|-------------|
| E2 proxy | Contract complete + costs grid + limitations |
| E3 reproduction | Source-faithful rules + matching resolution + venue notes |
| E4 robustness | ≥2 periods + cost sweep + param or universe sensitivity |
| E5 forward | Frozen config + out-of-sample live/paper window |

No experiment alone can set strategy `status: validated`. Integrator only.

## Forbidden worker actions

- Editing Obsidian vault notes or MOCs
- Editing another experiment directory
- Editing `research/common` or `research/contracts`
- Overwriting Round-1 archive files
- Claiming "validated" or "dead strategy" from a resolution-mismatched proxy
