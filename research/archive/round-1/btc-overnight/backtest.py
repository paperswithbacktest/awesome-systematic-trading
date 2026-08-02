"""Overnight seasonality in Bitcoin — local backtest.

Decomposes daily BTC-USD returns into the overnight leg (prev close -> open)
and the intraday leg (open -> close). Simulates:
  - overnight-only (buy at close, exit at next open) at 0/5/10/20 bps per fill
  - intraday-only (buy at open, exit at close)
  - buy-and-hold
and reports Sharpe, CAGR, max drawdown, total return.

Data: yfinance BTC-USD daily OHLC, auto_adjust=True, max history.
Cached to btc_usd_daily.csv; reruns load from cache.
"""

import os
import sys

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "btc_usd_daily.csv")
TRADING_DAYS = 365  # BTC trades 24/7


def load_data() -> pd.DataFrame:
    if os.path.exists(CACHE):
        df = pd.read_csv(CACHE, index_col=0, parse_dates=True)
        print(f"Loaded cached data: {df.index[0].date()} -> {df.index[-1].date()} ({len(df)} rows)")
        return df

    import yfinance as yf

    last_err = None
    for attempt in (1, 2):
        try:
            df = yf.download("BTC-USD", period="max", auto_adjust=True,
                             progress=False)
            if df is None or df.empty:
                raise RuntimeError("yfinance returned an empty dataframe")
            break
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            print(f"Download attempt {attempt} failed: {exc}")
    else:
        raise SystemExit(f"FATAL: could not download BTC-USD after 2 attempts: {last_err}")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close"]].dropna()
    df.to_csv(CACHE)
    print(f"Downloaded data: {df.index[0].date()} -> {df.index[-1].date()} ({len(df)} rows)")
    return df


def metrics(ret: pd.Series) -> dict:
    ret = ret.dropna()
    if len(ret) == 0:
        return {"Sharpe": np.nan, "CAGR": np.nan, "MaxDD": np.nan, "TotalReturn": np.nan}
    equity = (1.0 + ret).cumprod()
    n_years = len(ret) / TRADING_DAYS
    cagr = equity.iloc[-1] ** (1.0 / n_years) - 1.0
    vol = ret.std()
    sharpe = (ret.mean() / vol) * np.sqrt(TRADING_DAYS) if vol > 0 else np.nan
    maxdd = (equity / equity.cummax() - 1.0).min()
    return {
        "Sharpe": sharpe,
        "CAGR": cagr,
        "MaxDD": maxdd,
        "TotalReturn": equity.iloc[-1] - 1.0,
    }


def main() -> None:
    df = load_data()
    o, c = df["Open"], df["Close"]
    prev_c = c.shift(1)

    overnight_ret = o / prev_c - 1.0   # prev close -> open
    intraday_ret = c / o - 1.0         # open -> close
    bh_ret = c / prev_c - 1.0          # buy-and-hold

    cost_levels = [0, 5, 10, 20]  # bps per fill, 2 fills per round trip

    results = []

    def add_row(name, ret):
        m = metrics(ret)
        results.append({
            "Variant": name,
            "Sharpe": m["Sharpe"],
            "CAGR": m["CAGR"],
            "MaxDD": m["MaxDD"],
            "TotalReturn": m["TotalReturn"],
        })

    add_row("Buy & Hold", bh_ret)
    add_row("Intraday-only (0 bps)", intraday_ret)
    for bps in cost_levels:
        cost = 2.0 * (bps / 1e4)  # entry + exit per round trip
        add_row(f"Overnight-only ({bps} bps)", overnight_ret - cost)

    res = pd.DataFrame(results)
    res_fmt = res.copy()
    for col in ("CAGR", "MaxDD", "TotalReturn"):
        res_fmt[col] = res_fmt[col].map(lambda x: f"{x * 100:,.1f}%")
    res_fmt["Sharpe"] = res_fmt["Sharpe"].map(lambda x: f"{x:.3f}")
    print("\n=== Results ===")
    print(res_fmt.to_string(index=False))

    # Equity curves
    eq_0 = (1.0 + overnight_ret.dropna()).cumprod()
    eq_10 = (1.0 + overnight_ret.dropna() - 2.0 * 10 / 1e4).cumprod()
    eq_bh = (1.0 + bh_ret.dropna()).cumprod()

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(eq_bh.index, eq_bh.values, label="Buy & Hold", linewidth=1.2)
    ax.plot(eq_0.index, eq_0.values, label="Overnight-only (0 bps)", linewidth=1.2)
    ax.plot(eq_10.index, eq_10.values, label="Overnight-only (10 bps/fill)", linewidth=1.2)
    ax.set_yscale("log")
    ax.set_title("BTC-USD: Overnight-only vs Buy & Hold (log scale)")
    ax.set_ylabel("Equity (growth of $1, log)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    png_path = os.path.join(HERE, "equity.png")
    fig.savefig(png_path, dpi=130)
    print(f"\nEquity curve saved to {png_path}")

    res.to_csv(os.path.join(HERE, "metrics.csv"), index=False)

    # Extra decomposition stats for the report
    print("\n=== Leg decomposition (gross) ===")
    for name, r in (("Overnight", overnight_ret), ("Intraday", intraday_ret)):
        print(f"{name}: mean {r.mean() * 1e4:.2f} bps/day, "
              f"total {((1 + r.dropna()).prod() - 1) * 100:,.0f}%")
    print(f"Period: {df.index[0].date()} -> {df.index[-1].date()} ({len(df)} daily bars)")


if __name__ == "__main__":
    sys.exit(main())
