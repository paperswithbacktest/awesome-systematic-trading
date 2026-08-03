"""Behavioral tests for the provider-neutral acquisition boundary."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from research.acquisition.core import (
    AcquisitionRecipe,
    AmbiguousTimestampError,
    EmptyDataError,
    MissingInstrumentError,
    RateLimitError,
    acquire_with_retries,
    acquire_with_retries_result,
    validate_frames,
)


class SequenceProvider:
    """Deterministic provider used to exercise retry behavior without a network."""

    def __init__(self, outcomes: list[object]) -> None:
        self.outcomes = list(outcomes)
        self.calls = 0

    def fetch(self, recipe: AcquisitionRecipe) -> dict[str, pd.DataFrame]:
        del recipe
        outcome = self.outcomes[self.calls]
        self.calls += 1
        if isinstance(outcome, Exception):
            raise outcome
        return outcome  # type: ignore[return-value]


def daily_frame(rows: int = 2) -> pd.DataFrame:
    index = pd.date_range("2024-01-02", periods=rows, freq="B", tz="UTC")
    return pd.DataFrame({"close": range(100, 100 + rows)}, index=index)


def recipe(**overrides: object) -> AcquisitionRecipe:
    values: dict[str, object] = {
        "dataset_id": "DATA-ETF-GTAA-DAILY-001",
        "provider": "fake",
        "required_instruments": ("SPY", "EFA"),
        "frequency": "1d",
        "timezone": "UTC",
        "candle_label": "session-close",
        "adjustment": "provider-adjusted-close",
        "max_attempts": 3,
        "backoff_seconds": (1.0, 2.0),
    }
    values.update(overrides)
    return AcquisitionRecipe(**values)


def test_empty_provider_response_fails_at_acquisition_boundary() -> None:
    provider = SequenceProvider([{}])

    with pytest.raises(EmptyDataError, match="zero instruments"):
        acquire_with_retries(provider, recipe(), sleeper=lambda _: None)

    assert provider.calls == 1


def test_zero_row_frame_fails_at_acquisition_boundary() -> None:
    provider = SequenceProvider([{"SPY": daily_frame(0), "EFA": daily_frame()}])

    with pytest.raises(EmptyDataError, match="SPY"):
        acquire_with_retries(provider, recipe(), sleeper=lambda _: None)


def test_missing_required_instrument_fails_instead_of_shrinking_universe() -> None:
    frames = {"SPY": daily_frame()}

    with pytest.raises(MissingInstrumentError, match="EFA"):
        validate_frames(frames, recipe())


def test_rate_limit_retries_are_bounded_without_real_sleep() -> None:
    sleeps: list[float] = []
    provider = SequenceProvider(
        [RateLimitError("429"), RateLimitError("429"), RateLimitError("429")]
    )

    with pytest.raises(RateLimitError, match="after 3 attempts"):
        acquire_with_retries(provider, recipe(), sleeper=sleeps.append)

    assert provider.calls == 3
    assert sleeps == [1.0, 2.0]


def test_rate_limited_provider_can_recover_within_budget() -> None:
    sleeps: list[float] = []
    expected = {"SPY": daily_frame(), "EFA": daily_frame()}
    provider = SequenceProvider([RateLimitError("429"), expected])

    result = acquire_with_retries(provider, recipe(), sleeper=sleeps.append)

    assert set(result) == {"SPY", "EFA"}
    assert provider.calls == 2
    assert sleeps == [1.0]


def test_retry_result_reports_first_attempt_success() -> None:
    provider = SequenceProvider([{"SPY": daily_frame(), "EFA": daily_frame()}])

    result = acquire_with_retries_result(provider, recipe(), sleeper=lambda _: None)

    assert set(result.frames) == {"SPY", "EFA"}
    assert result.attempts == 1
    assert result.rate_limit_events == 0


def test_retry_result_counts_recovered_rate_limit_events() -> None:
    sleeps: list[float] = []
    provider = SequenceProvider(
        [RateLimitError("429"), {"SPY": daily_frame(), "EFA": daily_frame()}]
    )

    result = acquire_with_retries_result(provider, recipe(), sleeper=sleeps.append)

    assert result.attempts == 2
    assert result.rate_limit_events == 1
    assert sleeps == [1.0]


def test_retry_exhaustion_exposes_attempt_and_event_counts() -> None:
    provider = SequenceProvider(
        [RateLimitError("429"), RateLimitError("429"), RateLimitError("429")]
    )

    with pytest.raises(RateLimitError) as caught:
        acquire_with_retries_result(provider, recipe(), sleeper=lambda _: None)

    assert caught.value.attempts == 3
    assert caught.value.rate_limit_events == 3


def test_crypto_recipe_rejects_ambiguous_candle_label() -> None:
    with pytest.raises(AmbiguousTimestampError, match="candle_label"):
        recipe(
            dataset_id="DATA-CRYPTO-BTCUSD-COINBASE-1H-001",
            required_instruments=("BTC-USD",),
            frequency="1h",
            candle_label="unknown",
            adjustment=None,
        )


def test_recipe_rejects_non_utc_intraday_crypto() -> None:
    with pytest.raises(AmbiguousTimestampError, match="UTC"):
        recipe(
            dataset_id="DATA-CRYPTO-BTCUSD-COINBASE-1H-001",
            required_instruments=("BTC-USD",),
            frequency="1h",
            timezone="America/New_York",
            candle_label="open-time",
            adjustment=None,
        )


def test_recipe_rejects_unbounded_retry_configuration() -> None:
    with pytest.raises(ValueError, match="max_attempts"):
        recipe(max_attempts=0)


def test_validate_frames_rejects_duplicate_or_non_monotonic_timestamps() -> None:
    frame = daily_frame()
    duplicate = pd.concat([frame, frame.iloc[[0]]])
    with pytest.raises(ValueError, match="duplicate timestamps"):
        validate_frames({"SPY": duplicate, "EFA": frame}, recipe())

    reversed_frame = frame.iloc[::-1]
    with pytest.raises(ValueError, match="monotonic"):
        validate_frames({"SPY": reversed_frame, "EFA": frame}, recipe())
