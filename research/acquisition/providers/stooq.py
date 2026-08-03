"""Stooq daily OHLCV cross-check provider."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from io import StringIO
from urllib.request import Request, urlopen

import pandas as pd

from research.acquisition.core import EmptyDataError, RateLimitError


_REQUIRED_COLUMNS = ("Date", "Open", "High", "Low", "Close", "Volume")
_RENAMED_COLUMNS = {
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Volume": "volume",
}


def _default_get_text(url: str, timeout: int) -> str:
    request = Request(url, headers={"User-Agent": "awesome-systematic-trading-research/1.0"})
    with urlopen(request, timeout=timeout) as response:  # noqa: S310
        return response.read().decode("utf-8")


def _looks_rate_limited(exc: BaseException) -> bool:
    message = str(exc).lower()
    return "rate limit" in message or "too many requests" in message or "429" in message


class StooqDailyCrossCheck:
    """Fetch unadjusted Stooq OHLCV for sanity checking only."""

    def __init__(
        self,
        *,
        get_text: Callable[[str, int], str] | None = None,
        timeout: int = 20,
    ) -> None:
        self.get_text = get_text or _default_get_text
        self.timeout = timeout

    def fetch(self, symbols: Iterable[str]) -> dict[str, pd.DataFrame]:
        frames: dict[str, pd.DataFrame] = {}
        for symbol in symbols:
            url = f"https://stooq.com/q/d/l/?s={symbol.lower()}.us&i=d"
            try:
                text = self.get_text(url, self.timeout)
            except Exception as exc:
                if _looks_rate_limited(exc):
                    raise RateLimitError(f"Stooq rate limit for {symbol}: {exc}") from exc
                raise
            frames[symbol] = self._normalize(text, symbol)
        return frames

    @staticmethod
    def _normalize(text: str, symbol: str) -> pd.DataFrame:
        if not text.strip() or text.strip().lower().startswith("no data"):
            raise EmptyDataError(f"Stooq returned zero rows for {symbol}")
        try:
            raw = pd.read_csv(StringIO(text))
        except Exception as exc:
            raise ValueError(f"Stooq response for {symbol} is not valid CSV: {exc}") from exc
        if raw.empty:
            raise EmptyDataError(f"Stooq returned zero rows for {symbol}")
        missing = [column for column in _REQUIRED_COLUMNS if column not in raw.columns]
        if missing:
            raise ValueError(f"Stooq response for {symbol} missing required columns: {missing}")

        frame = raw.loc[:, list(_REQUIRED_COLUMNS)].copy()
        frame["Date"] = pd.to_datetime(frame["Date"], errors="coerce")
        frame = frame.dropna(subset=["Date"]).set_index("Date").sort_index()
        frame = frame.rename(columns=_RENAMED_COLUMNS)
        frame.index.name = "session_date"
        if frame.empty:
            raise EmptyDataError(f"Stooq returned zero usable rows for {symbol}")
        return frame
