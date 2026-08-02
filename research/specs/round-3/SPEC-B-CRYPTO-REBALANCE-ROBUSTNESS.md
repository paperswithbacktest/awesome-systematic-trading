# SPEC-B — Crypto Rebalancing Robustness

**Experiment ID:** `EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001`  
**Strategy ID:** `STRAT-CRYPTO-REBALANCE-PREMIUM`  
**Strategy title:** Rebalancing Premium in Cryptocurrencies  
**Worker write root (only):** `research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001/`  
**Evidence target:** E2 (E3/E4 only if true PIT eligibility becomes available)  
**experiment_class:** `robustness` (primary) / `proxy` for static-survivor legs  
**source_repo_commit baseline:** `1ce1eb2`

## Hypothesis

In a declared crypto universe, a periodically rebalanced equal-weight long portfolio outperforms a drifting buy-and-hold equal-weight portfolio on a risk-adjusted and/or return basis after costs. Frequency (daily/weekly/monthly) and universe eligibility materially change the result.

## What this is / is not

- **Is:** allocation / rebalance-frequency / eligibility sensitivity study.
- **Is not:** a claim that a 2026 survivor Yahoo basket equals the paper’s 27-coin Bitfinex universe.
- **Is not:** silent substitution of long-only for the paper’s long-rebalanced / short-drifting construction without labeling.

## Three questions to answer separately

1. Does daily EW rebalancing beat a drifting EW basket (gross and net)?
2. Does monthly/weekly beat daily after costs?
3. (Optional secondary) Does the paper-style long rebalanced / short drifting (70% short) construction work **if** shorts are modeled with explicit financing/tradability assumptions?

Primary deliverable is (1)+(2). (3) only if cleanly implementable; otherwise document as blocked.

## Universe policy (freeze before run)

Declare in config **before** seeing results:

```yaml
universe:
  policy: static_survivor_proxy | dynamic_eligibility | paper_list_proxy
  requested: [...]   # frozen list
  actual: [...]      # after data availability filter
  eligibility_rule: >
    Asset enters on first date with valid price and remains only while
    continuous history exists; no backfill before first observation.
```

Required cohort tests (at least):
- Full available common window
- 2018-start cohort (drop assets without 2018 history)
- 2020-start cohort
- Explicit exclude-late-listed (e.g. DOT) sensitivity

No forward-fill of missing prices across gaps. No silent survivorship.

## Portfolio construction

Primary long-only variants:
- Buy & hold EW (establish once; drift)
- Daily rebalance to EW
- Weekly rebalance to EW (e.g. Mondays UTC or first bar of week — declare)
- Monthly rebalance to EW (month-start or month-end — declare and stick)

Execution timing:
- Weights decided on bar close T
- Returns earned from T→T+1 after rebalance
- Initial establishment turnover must be charged on first invest day

## Cost model

```yaml
costs:
  turnover_definition: risky_traded_notional   # sum(|Δw|) on assets; A→B = 2.0
  fee_unit: bps_per_traded_notional
  fee_bps_per_traded_notional: [0, 5, 10, 20, 50]
  cash_labels: [CASH]
  spread_bps: [0]
  slippage_bps: [0]
  funding_mode: excluded          # unless perps used
  borrow_mode: excluded           # long-only primary
```

Do **not** call `sum(|Δw|)` “one-way turnover.” Use `risky_traded_notional` harness helper.

## Metrics & annualization

- Crypto daily bars: `annualization_factor: 365`
- Metrics per variant × fee × cohort: Sharpe, CAGR, vol, max_dd, total_return
- Report rebalancing premium vs B&H (CAGR and Sharpe deltas)
- Fee crossover table: daily vs monthly net CAGR
- Average annual gross traded notional

## Structural checks

- no_lookahead (rebalance decision before earning next return)
- timezone_explicit
- data_hash_verified
- cost_units_verified (`risky_traded_notional`; cash excluded)
- annualization_verified (365)
- incomplete_bar_excluded
- Additional recommended: initial_establishment_cost_applied; no_price_forward_fill

## Verdict constraints

- `reviewer_status: pending`
- Default `evidence_level: E2`
- Static survivor results must say **static survivor** in summary
- `reproduction_status: partial` at best without PIT coin universe
- Promotion blockers must include survivorship / eligibility / venue / short-leg tradability if omitted

## Required outputs

Full contract under write root only. No vault / shared harness edits.

## Reproduction command (template)

```bash
.venv/Scripts/python research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001/run.py
.venv/Scripts/python -m research.common.validate research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001
```
