"""Shared research harness helpers for contract-compliant experiments."""

from .metrics import (
    cagr,
    max_drawdown,
    metrics_from_returns,
    sharpe,
    total_return,
    volatility,
)
from .costs import (
    apply_turnover_costs,
    conventional_one_way_turnover,
    gross_traded_notional,
    portfolio_l1_weight_change,
    risky_traded_notional,
    round_trip_cost,
)
from .provenance import (
    file_sha256,
    git_state,
    hash_dataframe,
    run_context,
    write_data_manifest,
)
from .io import ensure_dir, write_csv, write_json, write_text


def validate_experiment_dir(*args, **kwargs):
    """Lazy import so `python -m research.common.validate` stays clean."""
    from .validate import validate_experiment_dir as _validate

    return _validate(*args, **kwargs)


__all__ = [
    "cagr",
    "max_drawdown",
    "metrics_from_returns",
    "sharpe",
    "total_return",
    "volatility",
    "apply_turnover_costs",
    "conventional_one_way_turnover",
    "gross_traded_notional",
    "portfolio_l1_weight_change",
    "risky_traded_notional",
    "round_trip_cost",
    "file_sha256",
    "git_state",
    "hash_dataframe",
    "run_context",
    "write_data_manifest",
    "ensure_dir",
    "write_csv",
    "write_json",
    "write_text",
    "validate_experiment_dir",
]
