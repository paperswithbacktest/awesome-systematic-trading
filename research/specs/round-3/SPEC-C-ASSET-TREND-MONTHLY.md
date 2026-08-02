# SPEC-C — Asset Class Trend-Following (Monthly ETF Proxy)

**Experiment ID:** `EXP-2026-08-ASSET-TREND-MONTHLY-001`  
**Strategy ID:** `STRAT-MULTI-ASSET-TREND`  
**Strategy title:** Asset Class Trend-Following  
**Worker write root (only):** `research/experiments/EXP-2026-08-ASSET-TREND-MONTHLY-001/`  
**Evidence target:** E2  
**experiment_class:** `proxy`  
**backtest_class label:** `paper-informed-etf-proxy`  
**source_repo_commit baseline:** `1ce1eb2`

## Hypothesis

A monthly trend filter that holds each asset-class sleeve only when price is above its 10-month moving average improves risk-adjusted returns versus a monthly equal-weight buy-and-hold benchmark. The paper-style fixed 20% sleeve (cash residual) differs materially from the repo-style 1/N among active sleeves.

## What this is / is not

- **Is:** paper-informed monthly ETF proxy with next-period execution.
- **Is not:** a 1900–present Faber original reproduction.
- **Is not:** unlabeled use of GLD/DBC as GSG without declaring the substitution.

## Universe (freeze)

Primary investable proxy set (repo-aligned names preferred):

| Sleeve | Primary ticker | Notes |
|--------|----------------|-------|
| US equities | SPY | required |
| Intl equities | EFA | preferred over omitting |
| Bonds | IEF | required |
| REITs | VNQ | required |
| Commodities | GSG | if history too short/empty, DBC with explicit substitution note |

Common-inception sample only after SMA warmup. No backfill.

## Signal & execution (no look-ahead)

- Use **monthly closes** (resample daily adjusted closes to month-end).
- Signal: month-end close > 10-month SMA of month-end closes.
- SMA requires 10 completed monthly observations before a sleeve can go long.
- **Execution:** signal known at month-end close T; weights apply to returns of the **next** month (T→T+1). No same-month return capture from the signal bar.
- Cash residual earns 0% in primary variant; optional secondary with a T-bill proxy if free data allows (label clearly).

## Portfolio variants (all required)

1. **Paper fixed sleeves:** each qualifying sleeve gets 20% weight; non-qualifying → cash. Max invested 100%.
2. **Repo 1/N active:** qualifying sleeves split 100% equally; cash only if none qualify.
3. **EW buy & hold benchmark:** 20% each sleeve, monthly rebalanced (or static EW with declared drift policy — prefer monthly rebalanced EW for clean comparison).

## Cost model

```yaml
costs:
  turnover_definition: risky_traded_notional   # cash excluded; A→cash = |ΔA| only
  fee_unit: bps_per_traded_notional
  fee_bps_per_traded_notional: [0, 5, 10]
  cash_labels: [CASH]
  spread_bps: [0]
  slippage_bps: [0]
  cash_return: "0"
  borrow_mode: not_applicable
```

Charge on rebalance dates including initial establishment.
Use `research.common.costs.risky_traded_notional` — do **not** charge the cash bookkeeping leg.

## Metrics & annualization

- Daily equity path preferred; annualize daily returns with **252** (weekday ETFs)
- If using pure monthly returns, annualize with **12** and state it
- Metrics per variant × cost: Sharpe, CAGR, vol, max_dd, total_return, average cash weight
- Period splits (calendar, non-overlapping as available): pre-2015 (if any), 2015–2019, 2020+
- Sanity: report SPY vol over same window

## Structural checks

- no_lookahead (month-end signal → next month returns)
- timezone_explicit (America/New_York or UTC with conversion note for US ETFs)
- data_hash_verified
- cost_units_verified
- annualization_verified
- incomplete_bar_excluded
- Additional: common_inception_enforced; sma_warmup_enforced

## Verdict constraints

- `reviewer_status: pending`
- `evidence_level: E2`
- `reproduction_status: partial`
- Must declare ETF substitutions and sample start gated by youngest asset
- Do not claim full GTAA validation
- Compare paper vs repo vs EW explicitly; do not collapse into one “trend works” slogan

## Required outputs

Full contract under write root only. No vault / shared harness edits.

## Reproduction command (template)

```bash
.venv/Scripts/python research/experiments/EXP-2026-08-ASSET-TREND-MONTHLY-001/run.py
.venv/Scripts/python -m research.common.validate research/experiments/EXP-2026-08-ASSET-TREND-MONTHLY-001
```
