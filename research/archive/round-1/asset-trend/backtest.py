"""
Asset Class Trend-Following (Meb Faber GTAA) — local backtest.

Variants:
  (a) paper GTAA: fixed 20% sleeve per qualifying asset, rest in cash @ 0%
  (b) repo-code version: qualifying sleeves split 100% equally (1/N)
  (c) buy-and-hold equal-weight benchmark (20% each, monthly rebalanced)

Signal: month-end close > 210-day SMA (daily data). Rebalance at month-end
close; new weights earn returns from the next trading day.
Costs: 0 and 5 bps per unit of one-way turnover (sum |delta w|).
"""

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
TICKERS = ["SPY", "IEF", "GLD", "DBC", "VNQ"]
SMA_PERIOD = 210
COST_LEVELS = [0.0, 0.0005]


def load_data() -> pd.DataFrame:
    """Download adjusted closes via yfinance, caching per-ticker CSVs."""
    frames = {}
    for t in TICKERS:
        csv = HERE / f"data_{t}.csv"
        if csv.exists():
            df = pd.read_csv(csv, index_col=0, parse_dates=True)
            frames[t] = df["Close"]
            print(f"[cache] {t}: {len(df)} rows, {df.index[0].date()} -> {df.index[-1].date()}")
            continue
        err = None
        for attempt in (1, 2):
            try:
                import yfinance as yf

                df = yf.download(t, period="max", auto_adjust=True, progress=False)
                if df is None or df.empty:
                    raise RuntimeError(f"empty download for {t}")
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)
                df = df[["Close"]].dropna()
                df.to_csv(csv)
                frames[t] = df["Close"]
                print(f"[download] {t}: {len(df)} rows, {df.index[0].date()} -> {df.index[-1].date()}")
                err = None
                break
            except Exception as e:  # noqa: BLE001
                err = e
                print(f"[retry] {t} attempt {attempt} failed: {e}")
                time.sleep(3)
        if err is not None:
            sys.exit(f"ERROR: could not download {t} after retry: {err}")
    prices = pd.DataFrame(frames).dropna()
    return prices


def month_end_weights(prices: pd.DataFrame) -> pd.DataFrame:
    """Binary trend signal at each month-end: 1 if close > 210d SMA else 0."""
    sma = prices.rolling(SMA_PERIOD).mean()
    signal = (prices > sma).astype(float)
    signal[sma.isna()] = np.nan
    me_dates = prices.groupby(prices.index.to_period("M")).apply(lambda g: g.index[-1])
    sig_me = signal.loc[me_dates.values]
    return sig_me.dropna()


def run_variant(sig_me: pd.DataFrame, rets: pd.DataFrame, mode: str, cost: float):
    """Simulate monthly rebalance. mode in {'paper', 'repo', 'bh'}."""
    dates = rets.index
    target = pd.DataFrame(0.0, index=sig_me.index, columns=sig_me.columns)
    for dt, row in sig_me.iterrows():
        q = row[row > 0].index.tolist()
        if mode == "paper":
            w = pd.Series(0.0, index=sig_me.columns)
            for s in q:
                w[s] = 0.20
        elif mode == "repo":
            w = pd.Series(0.0, index=sig_me.columns)
            if q:
                for s in q:
                    w[s] = 1.0 / len(q)
        elif mode == "bh":
            w = pd.Series(0.20, index=sig_me.columns)
        target.loc[dt] = w

    start = sig_me.index[0]
    r = rets.loc[dates[dates > start]]
    port_dates = [start] + list(r.index)

    w = target.loc[start].values.copy()  # weights applied at close of signal day
    equity = 1.0
    eq = [equity]
    total_cost = 0.0
    sig_set = set(sig_me.index)
    for dt, row in r.iterrows():
        gross = float(np.dot(w, row.values))
        # drift weights after the day's returns, back to portfolio fractions
        # (cash sleeve earns 0 and absorbs the residual weight)
        if 1 + gross != 0:
            w = w * (1 + row.values) / (1 + gross)
        day_ret = gross
        if dt in sig_set:
            new_w = target.loc[dt].values
            turnover = float(np.abs(new_w - w).sum())
            c = cost * turnover
            total_cost += c
            day_ret = gross - c
            w = new_w
        equity *= 1 + day_ret
        eq.append(equity)
    curve = pd.Series(eq, index=port_dates)
    return curve, total_cost


def metrics(curve: pd.Series):
    rets = curve.pct_change().dropna()
    years = (curve.index[-1] - curve.index[0]).days / 365.25
    cagr = curve.iloc[-1] ** (1 / years) - 1
    vol = rets.std() * np.sqrt(252)
    sharpe = (rets.mean() * 252) / vol if vol > 0 else np.nan
    dd = (curve / curve.cummax() - 1).min()
    return {"Sharpe": sharpe, "CAGR": cagr, "MaxDD": dd, "Vol": vol}


def main():
    prices = load_data()
    print(f"\nCommon history: {prices.index[0].date()} -> {prices.index[-1].date()} ({len(prices)} days)")
    rets = prices.pct_change().dropna()
    sig_me = month_end_weights(prices)
    print(f"First signal month-end: {sig_me.index[0].date()}  ({len(sig_me)} rebalances)")

    rows = []
    curves0 = {}
    for mode, label in [("paper", "(a) Paper 20% sleeves"), ("repo", "(b) Repo 1/N split"), ("bh", "(c) EW buy&hold")]:
        for cost in COST_LEVELS:
            curve, tcost = run_variant(sig_me, rets, mode, cost)
            m = metrics(curve)
            rows.append({
                "Variant": label, "Cost(bps)": int(cost * 1e4),
                "Sharpe": round(m["Sharpe"], 3), "CAGR": f"{m['CAGR']:.2%}",
                "MaxDD": f"{m['MaxDD']:.2%}", "Vol": f"{m['Vol']:.2%}",
            })
            if cost == 0.0:
                curves0[label] = curve

    res = pd.DataFrame(rows)
    print("\n" + res.to_string(index=False))

    # SPY vol sanity check over the same window
    spy_vol = rets["SPY"].loc[curves0["(c) EW buy&hold"].index].std() * np.sqrt(252)
    print(f"\n[sanity] SPY ann. vol over test window: {spy_vol:.2%}")

    fig, ax = plt.subplots(figsize=(10, 6))
    for label, curve in curves0.items():
        ax.plot(curve.index, curve.values, label=label)
    ax.set_yscale("log")
    ax.set_title("Asset Class Trend-Following: variants at 0 bps (log scale)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(HERE / "equity.png", dpi=120)
    print(f"\nSaved {HERE / 'equity.png'}")

    res.to_csv(HERE / "metrics.csv", index=False)


if __name__ == "__main__":
    main()
