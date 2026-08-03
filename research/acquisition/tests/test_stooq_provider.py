"""Contract tests for Stooq daily ETF sanity-check acquisition."""

from __future__ import annotations

import pandas as pd
import pytest

from research.acquisition.core import EmptyDataError, RateLimitError
from research.acquisition.providers.stooq import StooqDailyCrossCheck


CSV = """Date,Open,High,Low,Close,Volume
2024-01-03,101,103,100,102,1100
2024-01-02,100,102,99,101,1000
"""


def test_stooq_maps_us_etfs_and_normalizes_ascending_session_dates() -> None:
    urls: list[str] = []

    def get_text(url: str, timeout: int) -> str:
        urls.append(url)
        assert timeout == 20
        return CSV

    provider = StooqDailyCrossCheck(get_text=get_text)
    frames = provider.fetch(("SPY", "EFA", "IEF", "VNQ", "GSG"))

    assert urls == [
        "https://stooq.com/q/d/l/?s=spy.us&i=d",
        "https://stooq.com/q/d/l/?s=efa.us&i=d",
        "https://stooq.com/q/d/l/?s=ief.us&i=d",
        "https://stooq.com/q/d/l/?s=vnq.us&i=d",
        "https://stooq.com/q/d/l/?s=gsg.us&i=d",
    ]
    assert list(frames) == ["SPY", "EFA", "IEF", "VNQ", "GSG"]
    assert list(frames["SPY"].columns) == ["open", "high", "low", "close", "volume"]
    assert frames["SPY"].index.equals(pd.to_datetime(["2024-01-02", "2024-01-03"]))
    assert frames["SPY"].index.name == "session_date"


def test_stooq_empty_response_is_hard_failure_not_silent_degradation() -> None:
    provider = StooqDailyCrossCheck(get_text=lambda _url, _timeout: "No data")

    with pytest.raises(EmptyDataError, match="SPY"):
        provider.fetch(("SPY",))


def test_stooq_http_rate_limit_is_translated() -> None:
    def get_text(_url: str, _timeout: int) -> str:
        raise RuntimeError("HTTP Error 429: Too Many Requests")

    provider = StooqDailyCrossCheck(get_text=get_text)

    with pytest.raises(RateLimitError, match="Stooq.*SPY"):
        provider.fetch(("SPY",))


def test_stooq_rejects_malformed_csv() -> None:
    provider = StooqDailyCrossCheck(get_text=lambda _url, _timeout: "Date,Close\n2024-01-02,100\n")

    with pytest.raises(ValueError, match="required columns"):
        provider.fetch(("SPY",))
