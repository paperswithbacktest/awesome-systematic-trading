"""Provider-neutral acquisition boundary and bounded retry policy."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable, Protocol

import pandas as pd


class AcquisitionError(RuntimeError):
    """Base error for controlled acquisition failures."""


class RateLimitError(AcquisitionError):
    """The provider rejected a request because of a rate limit."""


class EmptyDataError(AcquisitionError):
    """The provider returned no usable observations."""


class MissingInstrumentError(AcquisitionError):
    """A required instrument was absent from a provider response."""


class AmbiguousTimestampError(AcquisitionError):
    """Time-zone or candle-label semantics are not explicit."""


_ALLOWED_CANDLE_LABELS = {"open-time", "close-time", "session-close"}


@dataclass(frozen=True)
class AcquisitionRecipe:
    dataset_id: str
    provider: str
    required_instruments: tuple[str, ...]
    frequency: str
    timezone: str
    candle_label: str
    adjustment: str | None
    max_attempts: int
    backoff_seconds: tuple[float, ...]

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        if len(self.backoff_seconds) < self.max_attempts - 1:
            raise ValueError("backoff_seconds must cover every retry")
        if self.candle_label not in _ALLOWED_CANDLE_LABELS:
            raise AmbiguousTimestampError(
                "candle_label must explicitly be open-time, close-time, or session-close"
            )
        is_crypto_intraday = self.dataset_id.startswith("DATA-CRYPTO-") and _is_intraday(
            self.frequency
        )
        if is_crypto_intraday and self.timezone != "UTC":
            raise AmbiguousTimestampError("intraday crypto acquisition must use UTC")


def _is_intraday(frequency: str) -> bool:
    value = frequency.strip().lower()
    return value.endswith("h") or value.endswith("m") or value.endswith("min")


class Provider(Protocol):
    def fetch(self, recipe: AcquisitionRecipe) -> dict[str, pd.DataFrame]: ...


def validate_frames(
    frames: dict[str, pd.DataFrame], recipe: AcquisitionRecipe
) -> dict[str, pd.DataFrame]:
    if not frames:
        raise EmptyDataError("provider returned zero instruments")

    missing = [symbol for symbol in recipe.required_instruments if symbol not in frames]
    if missing:
        raise MissingInstrumentError(
            "missing required instruments: " + ", ".join(sorted(missing))
        )

    for symbol in recipe.required_instruments:
        frame = frames[symbol]
        if frame.empty:
            raise EmptyDataError(f"provider returned zero rows for {symbol}")
        if not isinstance(frame.index, pd.DatetimeIndex):
            raise ValueError(f"{symbol} index must be a DatetimeIndex")
        if frame.index.has_duplicates:
            raise ValueError(f"{symbol} has duplicate timestamps")
        if not frame.index.is_monotonic_increasing:
            raise ValueError(f"{symbol} timestamps must be monotonic increasing")
        if _is_intraday(recipe.frequency) and frame.index.tz is None:
            raise AmbiguousTimestampError(f"{symbol} intraday timestamps must be timezone-aware")

    return frames


def acquire_with_retries(
    provider: Provider,
    recipe: AcquisitionRecipe,
    *,
    sleeper: Callable[[float], None] = time.sleep,
) -> dict[str, pd.DataFrame]:
    for attempt in range(1, recipe.max_attempts + 1):
        try:
            return validate_frames(provider.fetch(recipe), recipe)
        except RateLimitError as exc:
            if attempt == recipe.max_attempts:
                raise RateLimitError(
                    f"rate limit exhausted after {recipe.max_attempts} attempts: {exc}"
                ) from exc
            sleeper(recipe.backoff_seconds[attempt - 1])

    raise AssertionError("bounded retry loop exited unexpectedly")
