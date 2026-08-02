"""Shared performance metrics.

Conventions
-----------
- Inputs are simple returns (not log returns), as a pandas Series indexed by time.
- annualization_factor:
    * equities / ETFs trading weekdays: 252
    * crypto 24/7 daily bars: 365
    * hourly crypto: 24 * 365 = 8760  (caller must pass explicitly)
- risk_free_rate is annualized decimal (0.0 default). Converted to per-period
  by dividing by annualization_factor.
- Sharpe uses population std (ddof=0) by default for short-sample stability.
  Document if you prefer sample std (ddof=1).
- Near-zero volatility is treated as zero via VOL_EPS to avoid absurd Sharpes
  from floating-point noise on constant returns.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

# Period-return std below this is treated as zero for Sharpe purposes.
VOL_EPS = 1e-12


def _clean(ret: pd.Series, *, allow_total_loss: bool = True) -> pd.Series:
    if not isinstance(ret, pd.Series):
        ret = pd.Series(ret)
    r = ret.replace([np.inf, -np.inf], np.nan).dropna().astype(float)
    if (r < -1.0).any():
        bad = r[r < -1.0]
        raise ValueError(
            f"invalid simple returns < -100% at {len(bad)} observations "
            f"(min={float(bad.min()):.6f}); check cost model / leverage"
        )
    if not allow_total_loss and (r <= -1.0).any():
        raise ValueError("total-loss returns (r <= -1) not allowed in this context")
    return r


def total_return(ret: pd.Series) -> float:
    r = _clean(ret)
    if r.empty:
        return float("nan")
    growth = float((1.0 + r).prod())
    # Exact wipeout
    if growth <= 0.0:
        return -1.0
    return growth - 1.0


def cagr(ret: pd.Series, annualization_factor: float) -> float:
    """Compound annual growth rate from a return series."""
    r = _clean(ret)
    if r.empty or annualization_factor <= 0:
        return float("nan")
    n = len(r)
    years = n / float(annualization_factor)
    if years <= 0:
        return float("nan")
    growth = float((1.0 + r).prod())
    if growth < 0.0:
        # Path went negative — invalid for unlevered simple-return compounding
        return float("nan")
    if growth == 0.0:
        return -1.0
    return float(growth ** (1.0 / years) - 1.0)


def volatility(ret: pd.Series, annualization_factor: float, ddof: int = 0) -> float:
    r = _clean(ret)
    if len(r) < 2 or annualization_factor <= 0:
        return float("nan")
    period_vol = float(r.std(ddof=ddof))
    if period_vol < VOL_EPS:
        return 0.0
    return float(period_vol * np.sqrt(annualization_factor))


def sharpe(
    ret: pd.Series,
    annualization_factor: float,
    risk_free_rate: float = 0.0,
    ddof: int = 0,
) -> float:
    """Annualized Sharpe ratio.

    excess_period = ret - rf / annualization_factor
    Sharpe = mean(excess) / std(excess) * sqrt(annualization_factor)

    Near-zero period vol (< VOL_EPS) => NaN (undefined risk-adjusted return).
    """
    r = _clean(ret)
    if len(r) < 2 or annualization_factor <= 0:
        return float("nan")
    excess = r - (float(risk_free_rate) / float(annualization_factor))
    vol = float(excess.std(ddof=ddof))
    if vol < VOL_EPS:
        return float("nan")
    return float(excess.mean() / vol * np.sqrt(annualization_factor))


def max_drawdown(ret: pd.Series) -> float:
    """Most negative peak-to-trough drawdown (negative number or 0).

    Initial capital of 1.0 is included as the starting peak so a loss on the
    first observation is measured correctly. Uses a positional integer index
    to avoid mixed-index / None-index pandas edge cases.
    """
    r = _clean(ret)
    if r.empty:
        return float("nan")
    growth = (1.0 + r).cumprod().reset_index(drop=True)
    wealth = pd.concat([pd.Series([1.0]), growth], ignore_index=True)
    peaks = wealth.cummax()
    with np.errstate(divide="ignore", invalid="ignore"):
        dd = wealth / peaks - 1.0
    val = float(dd.min())
    if np.isnan(val):
        return float("nan")
    return val


def metrics_from_returns(
    ret: pd.Series,
    annualization_factor: float,
    risk_free_rate: float = 0.0,
) -> dict[str, Any]:
    """Standard metric bundle used by all experiments."""
    r = _clean(ret)
    return {
        "n_obs": int(len(r)),
        "total_return": total_return(r),
        "cagr": cagr(r, annualization_factor),
        "vol": volatility(r, annualization_factor),
        "sharpe": sharpe(r, annualization_factor, risk_free_rate),
        "max_dd": max_drawdown(r),
        "mean_return": float(r.mean()) if len(r) else float("nan"),
        "annualization_factor": float(annualization_factor),
        "risk_free_rate": float(risk_free_rate),
        "vol_eps": VOL_EPS,
        "sharpe_ddof": 0,
    }


def equity_curve(ret: pd.Series, start_value: float = 1.0) -> pd.Series:
    r = _clean(ret)
    if r.empty:
        return r
    return start_value * (1.0 + r).cumprod()
