"""
Future tools module.
"""
from datetime import date
import os

import pandas as pd
from trading.data.client import Client


def get_futures_chain(ticker: str, asofdate: date) -> pd.DataFrame:
    """
    Get futures chain

    Parameters
    ----------
        ticker: str
            Future ticker.

        asofdate: date
            Current date. Will return only the live futures.
    """
    file_path = os.path.join(
        os.getenv("HOME"),
        ".trading",
        "data",
        "futures",
        ticker,
        f"chain.{date.today()}.csv",
    )
    if os.path.exists(file_path):
        chain = pd.read_csv(file_path, index_col="RIC")
    else:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        chain, _ = Client().get_expiry_calendar(ticker)
        chain.set_index("RIC", drop=True, inplace=True)
        chain.to_csv(file_path, index=True, sep=",")
    chain.FTD = pd.to_datetime(chain.FTD)
    chain.LTD = pd.to_datetime(chain.LTD)
    index = pd.to_datetime(chain.LTD) >= asofdate
    chain = chain.loc[index, :]
    return chain
