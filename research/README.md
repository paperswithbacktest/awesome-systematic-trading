# Research Harness

Canonical home for systematic-trading experiments derived from this repo and the Obsidian vault.

## Rules

1. **Code + data + metrics live here**, not in Obsidian.
2. Obsidian notes hold summaries, links, decisions, and experiment IDs only.
3. Workers write **only** under `research/experiments/<experiment_id>/`.
4. No worker edits vault MOCs, strategy YAML, or shared harness files.
5. One integrator promotes accepted findings into the vault after review.
6. Never overwrite a completed experiment directory — mint a new ID.

## Layout

```text
research/
├── README.md
├── contracts/           # frozen schemas + promotion gates
├── common/              # shared metrics/costs/provenance helpers
├── experiments/         # one directory per experiment ID
├── data-manifests/      # optional shared dataset manifests
└── archive/             # immutable snapshots of prior rounds
```

## Evidence levels

See `contracts/evidence-levels.md`.

| Level | Meaning |
|-------|---------|
| E0 | Source claim only (README/paper Sharpe) |
| E1 | Code/method inspection |
| E2 | Proxy / diagnostic test |
| E3 | Materially faithful reproduction |
| E4 | Robustness across periods/costs/params |
| E5 | Forward / paper-trade evidence |

## Workflow statuses (strategy notes)

```text
stub → researched → experimented → reproduced → validated → live-candidate
                                                     ↘ rejected
```

`backtested` is deprecated as a primary status. Use `experimented` plus an evidence level.

## Canonical execution root

```text
C:\Users\Kyle\projects\awesome-systematic-trading
```

Create and use the local venv in this root. Do **not** run experiments against
code in this tree using the Orca worktree interpreter at
`orca/workspaces/awesome-systematic-trading/dace/.venv`.

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -U pip
.venv/Scripts/python -m pip install -r requirements-research.txt
.venv/Scripts/python -m pip freeze > requirements-lock.txt
.venv/Scripts/python research/common/tests/test_metrics.py
.venv/Scripts/python -m research.common.validate research/experiments/EXP-...
```

## Annualization contract

Annualization follows the **return observation frequency**, not merely the input
bar frequency.

| Series shape | annualization_factor |
|--------------|----------------------|
| Weekday equity/ETF daily returns | 252 |
| Crypto daily returns (24/7) | 365 |
| One strategy P&L observation per day (even if built from hourly bars) | 365 |
| One return per hour including inactive hours | 8760 |

For BTC overnight seasonality (one 2-hour trade per day), use 365 — not 8760.

Config should record both:

```yaml
data:
  frequency: hourly
metrics:
  return_observation_frequency: daily
  annualization_factor: 365
```

## Running experiments

```bash
.venv/Scripts/python research/experiments/EXP-.../run.py
```

## Round-1 archive

`archive/round-1/` holds the first exploratory scripts/results that lived under the vault. They are **not** validated replications. See each strategy note's promotion blockers.
