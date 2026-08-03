"""Bounded, serial Yahoo daily-bar provider."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from research.acquisition.core import (
    AcquisitionRecipe,
    EmptyDataError,
    RateLimitError,
)


_REQUIRED_COLUMNS = ("Open", "High", "Low", "Close", "Adj Close", "Volume")
_RENAMED_COLUMNS = {
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Adj Close": "adjusted_close",
    "Volume": "volume",
}


def _default_downloader(symbol: str, **kwargs: object) -> pd.DataFrame:
    import yfinance as yf

    return yf.download(symbol, **kwargs)


def _looks_rate_limited(exc: BaseException) -> bool:
    message = str(exc).lower()
    return "rate limit" in message or "too many requests" in message or "429" in message


class YahooDailyProvider:
    """Fetch one ticker at a time while retaining raw and adjusted closes."""

    def __init__(
        self,
        *,
        start: str,
        end: str,
        downloader: Callable[..., pd.DataFrame] | None = None,
        timeout: int = 20,
    ) -> None:
        self.start = start
        self.end = end
        self.downloader = downloader or _default_downloader
        self.timeout = timeout

    def fetch(self, recipe: AcquisitionRecipe) -> dict[str, pd.DataFrame]:
        frames: dict[str, pd.DataFrame] = {}
        for symbol in recipe.required_instruments:
            try:
                raw = self.downloader(
                    symbol,
                    start=self.start,
                    end=self.end,
                    interval="1d",
                    auto_adjust=False,
                    actions=True,
                    threads=False,
                    progress=False,
                    timeout=self.timeout,
                    multi_level_index=False,
                )
            except Exception as exc:
                if _looks_rate_limited(exc):
                    raise RateLimitError(f"Yahoo rate limit for {symbol}: {exc}") from exc
                raise
            frames[symbol] = self._normalize(raw, symbol)
        return frames

    @staticmethod
    def _normalize(raw: pd.DataFrame | None, symbol: str) -> pd.DataFrame:
        if raw is None or raw.empty:
            raise EmptyDataError(f"Yahoo returned zero rows for {symbol}")
        if isinstance(raw.columns, pd.MultiIndex):
            raise ValueError(f"Yahoo response for {symbol} has unexpected MultiIndex columns")
        missing = [column for column in _REQUIRED_COLUMNS if column not in raw.columns]
        if missing:
            raise ValueError(f"Yahoo response for {symbol} missing columns: {missing}")

        frame = raw.loc[:, list(_REQUIRED_COLUMNS)].rename(columns=_RENAMED_COLUMNS).copy()
        frame.index = pd.to_datetime(frame.index, errors="coerce")
        frame = frame.loc[~frame.index.isna()].sort_index()
        frame.index.name = "session_date"
        if frame.empty:
            raise EmptyDataError(f"Yahoo returned zero usable rows for {symbol}")
        if frame["adjusted_close"].notna().sum() == 0:
            raise EmptyDataError(f"Yahoo adjusted close has zero usable rows for {symbol}")
        return frame
