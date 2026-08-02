"""Rebalancing Premium in Cryptocurrencies - local backtest.

TEST: equal-weight crypto portfolio under buy-and-hold / daily / weekly / monthly
rebalancing, swept over transaction costs of 0, 5, 10, 20 bps per unit of turnover.
Data: daily adjusted closes from yfinance, cached as CSV on first download.
"""

import os
import sys
import time

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yfinance as yf

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_CSV = os.path.join(HERE, "prices.csv")

TICKERS = [
    "BTC-USD", "ETH-USD", "XRP-USD", "LTC-USD", "BCH-USD", "ADA-USD",
    "DOGE-USD", "DOT-USD", "LINK-USD", "XLM-USD", "TRX-USD", "ETC-USD",
]
START = "2018-01-01"
MIN_HISTORY_DAYS = 365 * 3  # drop tickers with less history than this
FEES_BPS = [0, 5, 10, 20]  # per unit of turnover traded
DAYS_PER_YEAR = 365  # crypto trades every day


def download_data():
    """Download daily adjusted closes, retry once on failure; cache to CSV."""
    for attempt in (1, 2):
        try:
            df = yf.download(
                TICKERS, start=START, auto_adjust=True, progress=False
            )["Close"]
            if df.empty:
                raise RuntimeError("yfinance returned an empty dataframe")
            break
        except Exception as exc:
            if attempt == 2:
                print(f"ERROR: download failed twice: {exc}", file=sys.stderr)
                sys.exit(1)
            print(f"Download attempt {attempt} failed ({exc}); retrying in 5s...")
            time.sleep(5)
    # Flatten possible MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.reindex(columns=TICKERS)
    df.to_csv(DATA_CSV)
    return df


def load_data():
    if os.path.exists(DATA_CSV):
        print(f"Loading cached data from {DATA_CSV}")
        df = pd.read_csv(DATA_CSV, index_col=0, parse_dates=True)
    else:
        print("Downloading data from yfinance...")
        df = download_data()
    return df


def clean_data(df):
    """Drop tickers with too-short history or obvious data errors."""
    keep, dropped = [], []
    for t in df.columns:
        s = df[t].dropna()
        if len(s) < MIN_HISTORY_DAYS:
            dropped.append((t, f"only {len(s)} days of history"))
            continue
        if (s <= 0).any():
            dropped.append((t, "non-positive prices"))
            continue
        r = s.pct_change().dropna()
        # obvious data error = a huge one-day spike that immediately reverts
        # (bad print). Real mania moves (DOGE 2021, TRX 2018/2024) hold their
        # new level, so they must not be dropped.
        rev = (r.abs() > 0.80) & (r.shift(-1) * r < -0.25)
        if rev.any():
            dropped.append((t, "spike-and-revert bad print"))
            continue
        keep.append(t)
    for t, why in dropped:
        print(f"  DROPPED {t}: {why}")
    df = df[keep]
    # common window: earliest date where all kept tickers have data
    df = df.dropna()
    return df


def simulate(rets, freq):
    """Simulate equal-weight portfolio. freq: None (B&H), 1 (daily), 7 (weekly),
    or 'M' (monthly). Returns daily net returns per fee level and gross turnover."""
    n = rets.shape[1]
    w = np.full(n, 1.0 / n)  # start equal-weight
    dates = rets.index
    month_starts = dates.to_series().groupby(
        [dates.year, dates.month]).min().values
    gross_rets = np.zeros(len(dates))
    turnovers = np.zeros(len(dates))
    port_growth = 1.0
    for i, (dt, row) in enumerate(rets.iterrows()):
        r = row.values
        # rebalance at the START of day i (based on previous close weights),
        # then earn today's returns
        rebalance = False
        if i > 0:
            if freq == 1:
                rebalance = True
            elif freq == 7 and dt.weekday() == 0:
                rebalance = True
            elif freq == "M" and dt in month_starts:
                rebalance = True
        if rebalance:
            target = np.full(n, 1.0 / n)
            to = np.abs(target - w).sum()  # one-sided turnover in weight units
            turnovers[i] = to
            w = target
        port_r = float(w @ r)
        gross_rets[i] = port_r
        # weights drift with returns
        w = w * (1.0 + r)
        w = w / w.sum()
        port_growth *= 1.0 + port_r
    out = {}
    for fee in FEES_BPS:
        out[fee] = gross_rets - turnovers * (fee / 1e4)
    return out, turnovers


def metrics(daily_rets):
    eq = (1.0 + daily_rets).cumprod()
    years = len(daily_rets) / DAYS_PER_YEAR
    cagr = eq.iloc[-1] ** (1.0 / years) - 1.0
    vol = daily_rets.std() * np.sqrt(DAYS_PER_YEAR)
    sharpe = (daily_rets.mean() * DAYS_PER_YEAR) / vol if vol > 0 else np.nan
    dd = (eq / eq.cummax() - 1.0).min()
    return {"CAGR": cagr, "Vol": vol, "Sharpe": sharpe, "MaxDD": dd}


def main():
    raw = load_data()
    print(f"Raw data: {raw.shape[0]} rows, {raw.shape[1]} tickers")
    px = clean_data(raw)
    print(f"Clean data: {px.shape[0]} days "
          f"({px.index[0].date()} to {px.index[-1].date()}), "
          f"tickers: {list(px.columns)}")
    rets = px.pct_change().dropna()

    variants = [("Buy & Hold", None), ("Daily", 1), ("Weekly", 7), ("Monthly", "M")]
    results, turns = {}, {}
    for name, freq in variants:
        results[name], turns[name] = simulate(rets, freq)

    rows = []
    for name, _ in variants:
        for fee in FEES_BPS:
            m = metrics(pd.Series(results[name][fee], index=rets.index))
            rows.append({
                "Variant": name, "Fee (bps)": fee,
                "CAGR": f"{m['CAGR']*100:.1f}%",
                "Vol": f"{m['Vol']*100:.1f}%",
                "Sharpe": f"{m['Sharpe']:.2f}",
                "MaxDD": f"{m['MaxDD']*100:.1f}%",
            })
    table = pd.DataFrame(rows)
    print("\n" + table.to_string(index=False))

    # Rebalancing premium: gross-of-costs CAGR vs buy-and-hold
    def cagr_of(r):
        r = pd.Series(r)
        return (1 + r).prod() ** (DAYS_PER_YEAR / len(r)) - 1
    bh = cagr_of(results["Buy & Hold"][0])
    print(f"\nBuy-and-hold gross CAGR: {bh*100:.2f}%")
    prem = {}
    for name in ("Daily", "Weekly", "Monthly"):
        p = cagr_of(results[name][0]) - bh
        prem[name] = p
        print(f"Rebalancing premium ({name}, gross): {p*100:+.2f}%/yr")

    # Fee crossover: fine sweep, daily net CAGR vs monthly net CAGR
    print("\nDaily vs Monthly net CAGR by fee (fine sweep):")
    d_gross = results["Daily"][0]
    mo_gross = results["Monthly"][0]
    crossover = None
    for fee in [0, 2, 4, 6, 8, 10, 12, 15, 20, 30, 50]:
        d = cagr_of(d_gross - turns["Daily"] * fee / 1e4)
        mo = cagr_of(mo_gross - turns["Monthly"] * fee / 1e4)
        tag = ""
        if crossover is None and d < mo and fee > 0:
            crossover = fee
            tag = "  <-- first fee where daily < monthly"
        print(f"  {fee:>2} bps: daily {d*100:7.2f}%  monthly {mo*100:7.2f}%  "
              f"diff {(d-mo)*100:+6.2f}%{tag}")
    # average daily turnover for context
    print(f"\nAvg annual turnover: daily {turns['Daily'].sum()*100/ (len(rets)/DAYS_PER_YEAR):.0f}%/yr, "
          f"monthly {turns['Monthly'].sum()*100/ (len(rets)/DAYS_PER_YEAR):.0f}%/yr")

    # Equity curve PNG: daily rebalance (gross) vs buy-and-hold
    eq_daily = (1.0 + pd.Series(results["Daily"][0], index=rets.index)).cumprod()
    eq_bh = (1.0 + pd.Series(results["Buy & Hold"][0], index=rets.index)).cumprod()
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(eq_daily.index, eq_daily.values, label="Daily rebalance (gross)", lw=1.2)
    ax.plot(eq_bh.index, eq_bh.values, label="Buy & Hold", lw=1.2)
    ax.set_yscale("log")
    ax.set_title("Rebalancing Premium in Crypto: Daily Rebalance vs Buy & Hold")
    ax.set_ylabel("Growth of $1 (log scale)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "equity.png"), dpi=130)
    print("\nSaved equity.png")

    # persist machine-readable results for the report step
    table.to_csv(os.path.join(HERE, "metrics.csv"), index=False)


if __name__ == "__main__":
    main()
