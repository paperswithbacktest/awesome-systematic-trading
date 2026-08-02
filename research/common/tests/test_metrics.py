"""Unit tests for shared metrics and costs."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Allow `python research/common/tests/test_metrics.py` from repo root
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from research.common.costs import (  # noqa: E402
    apply_turnover_costs,
    conventional_one_way_turnover,
    gross_traded_notional,
    portfolio_l1_weight_change,
    risky_traded_notional,
    round_trip_cost,
)
from research.common.metrics import (  # noqa: E402
    VOL_EPS,
    cagr,
    max_drawdown,
    metrics_from_returns,
    sharpe,
    total_return,
    volatility,
)


def test_constant_positive_returns():
    r = pd.Series([0.01] * 252)
    m = metrics_from_returns(r, annualization_factor=252)
    assert m["total_return"] > 0
    assert m["cagr"] > 0
    assert m["vol"] == 0.0
    assert np.isnan(m["sharpe"])
    assert m["max_dd"] == 0.0


def test_all_zero_returns():
    r = pd.Series([0.0] * 100)
    m = metrics_from_returns(r, annualization_factor=252)
    assert m["total_return"] == 0.0
    assert m["cagr"] == 0.0
    assert m["max_dd"] == 0.0
    assert m["vol"] == 0.0
    assert np.isnan(m["sharpe"])


def test_first_observation_drawdown():
    r = pd.Series([-0.10, 0.0, 0.05])
    dd = max_drawdown(r)
    # equity: 1.0 -> 0.9 -> 0.9 -> 0.945; min dd = -10%
    assert abs(dd - (-0.10)) < 1e-12


def test_drawdown_mid_path():
    r = pd.Series([0.10, -0.50, 0.0])
    dd = max_drawdown(r)
    # equity: 1.0, 1.1, 0.55, 0.55 -> dd = 0.55/1.1 - 1 = -0.5
    assert abs(dd - (-0.5)) < 1e-12


def test_total_loss_cagr_and_return():
    r = pd.Series([0.05, -1.0])
    assert total_return(r) == -1.0
    assert cagr(r, 252) == -1.0
    assert abs(max_drawdown(r) - (-1.0)) < 1e-12


def test_invalid_return_below_minus_one():
    r = pd.Series([0.01, -1.5])
    try:
        total_return(r)
        raise AssertionError("expected ValueError for r < -1")
    except ValueError as exc:
        assert "invalid simple returns" in str(exc)


def test_near_zero_vol_sharpe_is_nan():
    # Floating noise around a constant
    r = pd.Series([0.01 + 1e-16, 0.01 - 1e-16, 0.01, 0.01] * 50)
    s = sharpe(r, 252)
    # Either exactly constant after float ops, or near-constant — must not explode
    assert np.isnan(s) or abs(s) < 1e6
    # Force true near-zero path via VOL_EPS contract
    r2 = pd.Series([0.0 + VOL_EPS / 10] * 100)
    assert np.isnan(sharpe(r2, 252))


def test_equity_annualization_252():
    daily = (1.10) ** (1 / 252) - 1
    r = pd.Series([daily] * 252)
    assert abs(cagr(r, 252) - 0.10) < 1e-6
    assert abs(total_return(r) - 0.10) < 1e-6


def test_crypto_annualization_365():
    daily = (1.20) ** (1 / 365) - 1
    r = pd.Series([daily] * 365)
    assert abs(cagr(r, 365) - 0.20) < 1e-6


def test_sharpe_positive():
    rng = np.random.default_rng(0)
    r = pd.Series(rng.normal(0.001, 0.01, size=1000))
    s = sharpe(r, 252)
    assert s > 0


def test_turnover_costs_once_and_index_preserved():
    idx = pd.date_range("2020-01-01", periods=3, freq="D")
    gross = pd.Series([0.01, 0.01, 0.01], index=idx, name="ret")
    traded = pd.Series([1.0, 0.0, 0.0], index=idx)
    net = apply_turnover_costs(gross, traded, fee_bps_per_traded_notional=10)
    assert abs(net.iloc[0] - (0.01 - 0.001)) < 1e-12
    assert abs(net.iloc[1] - 0.01) < 1e-12
    assert list(net.index) == list(idx)
    assert net.name == "ret"


def test_misaligned_turnover_index_raises():
    idx_a = pd.date_range("2020-01-01", periods=3, freq="D")
    idx_b = pd.date_range("2020-01-02", periods=3, freq="D")
    gross = pd.Series([0.01, 0.01, 0.01], index=idx_a)
    traded = pd.Series([1.0, 0.0, 0.0], index=idx_b)
    try:
        apply_turnover_costs(gross, traded, fee_bps_per_traded_notional=10)
        raise AssertionError("expected ValueError for misaligned indexes")
    except ValueError as exc:
        assert "do not match exactly" in str(exc)


def test_full_switch_turnover_is_two():
    # 100% A -> 100% B: gross traded notional = 2.0; one-way = 1.0
    w_old = pd.Series({"A": 1.0, "B": 0.0})
    w_new = pd.Series({"A": 0.0, "B": 1.0})
    gtn = gross_traded_notional(w_old, w_new)
    owt = conventional_one_way_turnover(w_old, w_new)
    assert abs(gtn - 2.0) < 1e-15
    assert abs(owt - 1.0) < 1e-15
    # Cost at 10 bps per traded notional = 20 bps total drag on full switch
    gross = pd.Series([0.0])
    traded = pd.Series([gtn])
    net = apply_turnover_costs(gross, traded, fee_bps_per_traded_notional=10)
    assert abs(net.iloc[0] - (-0.002)) < 1e-15


def test_cash_to_asset_risky_notional_is_one():
    # Cash → 100% A: fee-bearing notional = 1.0 (buy A); portfolio L1 = 2.0
    w_old = {"CASH": 1.0, "A": 0.0}
    w_new = {"CASH": 0.0, "A": 1.0}
    assert abs(risky_traded_notional(w_old, w_new) - 1.0) < 1e-15
    assert abs(portfolio_l1_weight_change(w_old, w_new) - 2.0) < 1e-15
    assert abs(gross_traded_notional(w_old, w_new) - 1.0) < 1e-15  # default excludes cash


def test_asset_to_cash_risky_notional_is_one():
    w_old = {"CASH": 0.0, "A": 1.0}
    w_new = {"CASH": 1.0, "A": 0.0}
    assert abs(risky_traded_notional(w_old, w_new) - 1.0) < 1e-15
    assert abs(portfolio_l1_weight_change(w_old, w_new) - 2.0) < 1e-15


def test_partial_sleeve_to_cash():
    # 20% A → cash: risky traded = 0.2; portfolio L1 = 0.4
    w_old = {"CASH": 0.8, "A": 0.2}
    w_new = {"CASH": 1.0, "A": 0.0}
    assert abs(risky_traded_notional(w_old, w_new) - 0.2) < 1e-15
    assert abs(portfolio_l1_weight_change(w_old, w_new) - 0.4) < 1e-15


def test_cash_only_has_zero_risky_traded_notional():
    w_old = {"CASH": 1.0}
    w_new = {"CASH": 1.0}
    assert abs(risky_traded_notional(w_old, w_new) - 0.0) < 1e-15
    assert abs(gross_traded_notional(w_old, w_new) - 0.0) < 1e-15
    # Portfolio L1 still reflects bookkeeping identity (0 change)
    assert abs(portfolio_l1_weight_change(w_old, w_new) - 0.0) < 1e-15


def test_unlabeled_array_treated_as_risky():
    # No cash labels → entire vector is fee-bearing
    w_old = np.array([1.0, 0.0])
    w_new = np.array([0.0, 1.0])
    assert abs(risky_traded_notional(w_old, w_new) - 2.0) < 1e-15


def test_round_trip_not_double_count_units():
    # 5 bps/fill * 2 fills = 10 bps total = 0.001
    assert abs(round_trip_cost(5.0, n_fills=2) - 0.001) < 1e-15


def test_volatility_nonneg_and_zero_on_constant():
    r = pd.Series([0.01, -0.02, 0.015, -0.005])
    assert volatility(r, 252) >= 0
    assert volatility(pd.Series([0.02] * 50), 252) == 0.0


def test_no_lookahead_toy():
    """Toy rule: signal at t uses only data <= t; trade earns return t->t+1."""
    prices = pd.Series([100.0, 101.0, 99.0, 102.0, 103.0])
    # Signal: long if today's close > yesterday's close (known at close)
    signal = (prices > prices.shift(1)).astype(float)
    # Execute next period: position at t is signal[t-1]
    position = signal.shift(1).fillna(0.0)
    rets = prices.pct_change().fillna(0.0)
    strat = position * rets
    # First bar must be flat (no prior signal)
    assert strat.iloc[0] == 0.0
    # No same-bar: when signal flips on bar i, bar i return is not earned by new pos
    # bar 1: price up, signal becomes 1 at end of bar 1; position still 0 on bar 1
    assert position.iloc[1] == 0.0
    assert position.iloc[2] == 1.0  # signal from bar 1 active on bar 2


def main():
    tests = [
        test_constant_positive_returns,
        test_all_zero_returns,
        test_first_observation_drawdown,
        test_drawdown_mid_path,
        test_total_loss_cagr_and_return,
        test_invalid_return_below_minus_one,
        test_near_zero_vol_sharpe_is_nan,
        test_equity_annualization_252,
        test_crypto_annualization_365,
        test_sharpe_positive,
        test_turnover_costs_once_and_index_preserved,
        test_misaligned_turnover_index_raises,
        test_full_switch_turnover_is_two,
        test_cash_to_asset_risky_notional_is_one,
        test_asset_to_cash_risky_notional_is_one,
        test_partial_sleeve_to_cash,
        test_cash_only_has_zero_risky_traded_notional,
        test_unlabeled_array_treated_as_risky,
        test_round_trip_not_double_count_units,
        test_volatility_nonneg_and_zero_on_constant,
        test_no_lookahead_toy,
    ]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL {t.__name__}: {exc}")
    if failed:
        raise SystemExit(f"{failed} tests failed")
    print(f"OK {len(tests)} tests passed")


if __name__ == "__main__":
    main()
