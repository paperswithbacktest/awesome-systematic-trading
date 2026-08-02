"""Transaction cost helpers.

Turnover / traded-notional conventions
--------------------------------------
Two related quantities:

1. **portfolio_l1_weight_change** = sum(|Δw|) over the full portfolio
   including cash bookkeeping legs. Cash→100% A = 2.0 when cash is explicit.
2. **risky_traded_notional** = sum(|Δw|) over risky assets only (cash excluded).
   Cash→100% A = 1.0 (buy the asset). A→B = 2.0. 20% A→cash = 0.2.

**Default cost base is risky_traded_notional.** Cash is not a fee-bearing
instrument; charging the cash bookkeeping leg double-counts settlement.

`gross_traded_notional(...)` is an alias of `risky_traded_notional` for
backward compatibility (cash excluded by default).

Many portfolio libraries call "one-way turnover":

    conventional_one_way_turnover = 0.5 * gross_traded_notional

**Do not mix** portfolio L1, risky traded notional, and one-way turnover.

Cost application (default)
--------------------------
net_return = gross_return - risky_traded_notional * (fee_bps / 1e4)

Where fee_bps is the all-in cost charged **per dollar of risky notional traded**.
If you instead model per-fill costs on a single-name strategy that enters
and exits once, use `round_trip_cost`.

Config fields every experiment should declare
---------------------------------------------
- turnover_definition: risky_traded_notional | portfolio_l1 | conventional_one_way
- fee_unit: bps_per_traded_notional | bps_per_fill
- cash_labels: e.g. [CASH]
- whether spread, slippage, borrow, funding, impact are included
- whether cash is an explicit portfolio weight
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def bps_to_decimal(bps: float) -> float:
    return float(bps) / 1e4


def _as_weight_series(w: pd.Series | np.ndarray | dict) -> pd.Series:
    if isinstance(w, pd.Series):
        return w.astype(float)
    if isinstance(w, dict):
        return pd.Series(w, dtype=float)
    return pd.Series(np.asarray(w, dtype=float))


def portfolio_l1_weight_change(
    w_old: pd.Series | np.ndarray | dict,
    w_new: pd.Series | np.ndarray | dict,
) -> float:
    """Full-portfolio L1 change including cash bookkeeping legs.

    Cash → 100% A (cash explicit): 2.0
    100% A → 100% B: 2.0
    """
    a = _as_weight_series(w_old)
    b = _as_weight_series(w_new)
    a, b = a.align(b, fill_value=0.0)
    return float((b - a).abs().sum())


def risky_traded_notional(
    w_old: pd.Series | np.ndarray | dict,
    w_new: pd.Series | np.ndarray | dict,
    *,
    cash_labels: set[str] | frozenset[str] | None = None,
) -> float:
    """Fee-bearing traded notional on risky assets only.

    Cash is not a brokerage instrument. Moving 100% cash → 100% A costs 1.0
    (buy A), not 2.0. Moving 100% A → 100% B costs 2.0 (sell A + buy B).
    Moving 20% A → cash costs 0.2 (sell A only).

    Parameters
    ----------
    cash_labels
        Labels treated as non-fee-bearing cash sleeves. Default:
        {"CASH", "cash", "Cash", "_"}.
    """
    labels = cash_labels or {"CASH", "cash", "Cash", "_"}
    a = _as_weight_series(w_old)
    b = _as_weight_series(w_new)
    a, b = a.align(b, fill_value=0.0)
    has_explicit_cash = any(label in labels for label in a.index)
    risky = [i for i in a.index if i not in labels]
    if not risky:
        # Explicit cash-only book: no fee-bearing instruments.
        # Unlabeled arrays (no cash labels present): treat whole vector as risky.
        return 0.0 if has_explicit_cash else float((b - a).abs().sum())
    return float((b.loc[risky] - a.loc[risky]).abs().sum())


def gross_traded_notional(
    w_old: pd.Series | np.ndarray | dict,
    w_new: pd.Series | np.ndarray | dict,
    *,
    exclude_cash: bool = True,
    cash_labels: set[str] | frozenset[str] | None = None,
) -> float:
    """Default cost base: risky traded notional (cash excluded).

    Set exclude_cash=False to get full-portfolio L1 (bookkeeping) change.
    Prefer calling risky_traded_notional / portfolio_l1_weight_change by name
    in new code for clarity.
    """
    if exclude_cash:
        return risky_traded_notional(w_old, w_new, cash_labels=cash_labels)
    return portfolio_l1_weight_change(w_old, w_new)


def conventional_one_way_turnover(
    w_old: pd.Series | np.ndarray | dict,
    w_new: pd.Series | np.ndarray | dict,
    *,
    exclude_cash: bool = True,
    cash_labels: set[str] | frozenset[str] | None = None,
) -> float:
    """0.5 * gross_traded_notional under the same cash convention."""
    return 0.5 * gross_traded_notional(
        w_old, w_new, exclude_cash=exclude_cash, cash_labels=cash_labels
    )


def apply_turnover_costs(
    gross_returns: pd.Series | np.ndarray,
    gross_traded_notional_series: pd.Series | np.ndarray,
    fee_bps_per_traded_notional: float,
) -> pd.Series:
    """Subtract costs proportional to gross traded notional.

    Parameters
    ----------
    gross_traded_notional_series
        Per-period sum(|Δw|). Full portfolio switch = 2.0.
    fee_bps_per_traded_notional
        All-in bps charged per dollar traded (per side).

    If both inputs are pandas Series, indexes must match exactly after an
    inner align. Positional arrays are accepted only when both inputs are
    array-like without meaningful indexes (or plain ndarrays).
    """
    g_is_series = isinstance(gross_returns, pd.Series)
    t_is_series = isinstance(gross_traded_notional_series, pd.Series)

    if g_is_series and t_is_series:
        g_raw = gross_returns.astype(float)
        t_raw = gross_traded_notional_series.astype(float)
        g, t = g_raw.align(t_raw, join="inner")
        if len(g) != len(g_raw) or len(t) != len(t_raw):
            raise ValueError(
                "gross_returns and gross_traded_notional indexes do not match exactly "
                f"(gross={len(g_raw)}, traded={len(t_raw)}, aligned={len(g)})"
            )
        if not g.index.equals(t.index):
            raise ValueError("aligned indexes still differ after inner join")
        cost = t * bps_to_decimal(fee_bps_per_traded_notional)
        out = g - cost
        out.name = getattr(gross_returns, "name", None)
        return out

    # Positional path for plain arrays
    g = pd.Series(np.asarray(gross_returns, dtype=float))
    t = pd.Series(np.asarray(gross_traded_notional_series, dtype=float))
    if len(g) != len(t):
        raise ValueError(
            f"gross_returns length {len(g)} != gross_traded_notional length {len(t)}"
        )
    cost = t * bps_to_decimal(fee_bps_per_traded_notional)
    out = g - cost
    if g_is_series:
        out.index = gross_returns.index
        out.name = getattr(gross_returns, "name", None)
    return out


def round_trip_cost(fee_bps_per_fill: float, n_fills: int = 2) -> float:
    """Total decimal cost for n fills (default entry+exit)."""
    return n_fills * bps_to_decimal(fee_bps_per_fill)


def apply_fixed_round_trip_cost(
    gross_returns: pd.Series,
    fee_bps_per_fill: float,
    n_fills: int = 2,
    active_mask: pd.Series | None = None,
) -> pd.Series:
    """Subtract a fixed round-trip cost on active periods.

    If active_mask is None, every observation is charged (use carefully).
    """
    cost = round_trip_cost(fee_bps_per_fill, n_fills=n_fills)
    out = gross_returns.astype(float).copy()
    if active_mask is None:
        return out - cost
    mask = active_mask.reindex(out.index).fillna(False).astype(bool)
    out.loc[mask] = out.loc[mask] - cost
    return out
