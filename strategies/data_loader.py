"""
Data loader module.
"""
from datetime import date, datetime, timedelta
import os

import pandas as pd
from tqdm import tqdm
from trading.data.client import Client


def load_futures_hist_prices(ticker: str) -> pd.DataFrame:
    """
    Load futures history prices.

    Parameters
    ----------
        ticker: str
            Future ticker.
    """
    file_path = os.path.join(
        os.getenv("HOME"),
        ".trading",
        "data",
        "futures",
        ticker,
        f"hist_prices.{date.today()}.csv",
    )
    if os.path.exists(file_path):
        return pd.read_csv(file_path, index_col="Date")
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    client = Client()
    chain, _ = client.get_expiry_calendar(ticker)
    frames = []
    for _, row in tqdm(chain.iterrows(), total=chain.shape[0]):
        is_recent_ric = datetime.now() - datetime.strptime(
            row.YearMonth, "%Y-%m"
        ) < timedelta(days=365)
        active_ric = row.RIC
        if is_recent_ric and not Client().get_health_ric(row.RIC)[0]:
            active_ric = row.RIC.split("^")[0]
        dfm, _ = client.get_daily_ohlcv(
            ric=active_ric,
            start_date=datetime.strptime(row.FTD, "%Y-%m-%d").date(),
            end_date=datetime.strptime(row.LTD, "%Y-%m-%d").date(),
        )
        if dfm is None:
            continue
        dfm = dfm[["Close"]]
        dfm.rename(
            columns={"Close": row.RIC},
            inplace=True,
        )
        dfm.index = dfm.index.map(lambda x: x[0])
        dfm.index.rename("Date", inplace=True)
        dfm = dfm.loc[~dfm.index.duplicated(keep="first")]
        frames.append(dfm)
    dfm = pd.concat(frames, axis=1).sort_index(ascending=True)
    dfm.to_csv(file_path, index=True, sep=",")
    return dfm


def load_futures_meta(ticker: str) -> dict:
    """
    Load futures meta

    Parameters
    ----------
        ticker: str
            Future ticker.

    Returns
    -------
        dict: Future meta data
    """
    client = Client()
    futures, _ = client.get_tickers()
    return futures[ticker]
