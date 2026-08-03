"""Contract tests for bounded, serial Yahoo ETF acquisition."""

from __future__ import annotations

import pandas as pd
import pytest

from research.acquisition.core import AcquisitionRecipe, EmptyDataError, RateLimitError, acquire_with_retries
from research.acquisition.providers.yahoo import YahooDailyProvider, yahoo_daily_request_kwargs


SYMBOLS = ("SPY", "EFA", "IEF", "VNQ", "GSG")


def recipe(*, max_attempts: int = 1) -> AcquisitionRecipe:
    return AcquisitionRecipe(
        dataset_id="DATA-ETF-GTAA-YAHOO-DAILY-ADJ-001",
        provider="yahoo-yfinance",
        required_instruments=SYMBOLS,
        frequency="1d",
        timezone="America/New_York",
        candle_label="session-close",
        adjustment="yahoo-adjusted-close-proxy",
        max_attempts=max_attempts,
        backoff_seconds=(0.0,) * max(0, max_attempts - 1),
    )


def yahoo_frame(symbol: str) -> pd.DataFrame:
    index = pd.to_datetime(["2024-01-02", "2024-01-03"])
    return pd.DataFrame(
        {
            "Open": [100.0, 101.0],
            "High": [102.0, 103.0],
            "Low": [99.0, 100.0],
            "Close": [101.0, 102.0],
            "Adj Close": [98.0, 99.0],
            "Volume": [1000, 1100],
        },
        index=index,
    ).rename_axis("Date")


def test_yahoo_fetches_exact_universe_serially_with_explicit_options() -> None:
    calls: list[tuple[str, dict[str, object]]] = []

    def downloader(symbol: str, **kwargs: object) -> pd.DataFrame:
        calls.append((symbol, kwargs))
        return yahoo_frame(symbol)

    provider = YahooDailyProvider(
        start="2007-01-01",
        end="2026-08-02",
        downloader=downloader,
    )
    frames = provider.fetch(recipe())

    assert list(frames) == list(SYMBOLS)
    assert [symbol for symbol, _ in calls] == list(SYMBOLS)
    # Exact wire kwargs, asserted against an independent literal so this test
    # fails if the canonical helper drifts from the intended request contract.
    expected_kwargs = {
        "start": "2007-01-01",
        "end": "2026-08-02",
        "interval": "1d",
        "auto_adjust": False,
        "actions": True,
        "threads": False,
        "progress": False,
        "timeout": 20,
        "multi_level_index": False,
    }
    # The canonical helper itself must equal the independent literal.
    assert yahoo_daily_request_kwargs(
        start="2007-01-01",
        end="2026-08-02",
        timeout=20,
    ) == expected_kwargs
    # The provider must issue exactly that dict for every symbol.
    for _, actual_kwargs in calls:
        assert actual_kwargs == expected_kwargs
    assert list(frames["SPY"].columns) == [
        "open",
        "high",
        "low",
        "close",
        "adjusted_close",
        "volume",
    ]
    assert frames["SPY"].index.name == "session_date"


def test_yahoo_empty_symbol_hard_fails_at_acquisition_boundary() -> None:
    def downloader(symbol: str, **_: object) -> pd.DataFrame:
        return pd.DataFrame() if symbol == "EFA" else yahoo_frame(symbol)

    provider = YahooDailyProvider(start="2007-01-01", end="2026-08-02", downloader=downloader)

    with pytest.raises(EmptyDataError, match="zero rows for EFA"):
        acquire_with_retries(provider, recipe())


def test_yahoo_all_nan_adjusted_close_is_empty_usable_data() -> None:
    def downloader(symbol: str, **_: object) -> pd.DataFrame:
        frame = yahoo_frame(symbol)
        if symbol == "GSG":
            frame["Adj Close"] = float("nan")
        return frame

    provider = YahooDailyProvider(start="2007-01-01", end="2026-08-02", downloader=downloader)

    with pytest.raises(EmptyDataError, match="adjusted close.*GSG"):
        provider.fetch(recipe())


def test_yahoo_rate_limit_is_translated_and_bounded() -> None:
    attempts = 0

    def downloader(symbol: str, **_: object) -> pd.DataFrame:
        nonlocal attempts
        attempts += 1
        raise RuntimeError("Too Many Requests. Rate limited. Try after a while.")

    provider = YahooDailyProvider(start="2007-01-01", end="2026-08-02", downloader=downloader)

    with pytest.raises(RateLimitError, match="exhausted after 2 attempts"):
        acquire_with_retries(provider, recipe(max_attempts=2), sleeper=lambda _: None)
    assert attempts == 2


def test_yahoo_rejects_missing_adjusted_close_column() -> None:
    def downloader(symbol: str, **_: object) -> pd.DataFrame:
        return yahoo_frame(symbol).drop(columns=["Adj Close"])

    provider = YahooDailyProvider(start="2007-01-01", end="2026-08-02", downloader=downloader)

    with pytest.raises(ValueError, match="Adj Close"):
        provider.fetch(recipe())


def test_yahoo_rejects_unexpected_multiindex_columns_loudly() -> None:
    def downloader(symbol: str, **_: object) -> pd.DataFrame:
        frame = yahoo_frame(symbol)
        frame.columns = pd.MultiIndex.from_product([frame.columns, [symbol]])
        return frame

    provider = YahooDailyProvider(start="2007-01-01", end="2026-08-02", downloader=downloader)

    with pytest.raises(ValueError, match="MultiIndex"):
        provider.fetch(recipe())


def test_yahoo_rejects_unparseable_timestamps() -> None:
    """Malformed vendor timestamps must hard-fail, never silently drop to NaT."""

    def downloader(symbol: str, **_: object) -> pd.DataFrame:
        frame = yahoo_frame(symbol)
        frame.index = pd.Index(["2024-01-02", "not-a-date"])
        return frame

    provider = YahooDailyProvider(
        start="2007-01-01",
        end="2026-08-02",
        downloader=downloader,
    )

    with pytest.raises(ValueError, match=r"SPY.*(NaT|unparseable)"):
        provider.fetch(recipe())
