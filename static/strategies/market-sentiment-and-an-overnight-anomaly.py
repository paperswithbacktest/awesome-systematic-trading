# https://quantpedia.com/strategies/market-sentiment-and-an-overnight-anomaly/
#
# The investment universe consists of SPY ETF, and the price of SPY, price of VIX and Brain Market Sentiment (BMS) indicator
# are used to identify the market sentiment. The investor buys SPY ETF and holds it overnight; when the price of SPY is above its 20-day moving average,
# the price of VIX is below its moving average, and the value of the BMS indicator is greater than its 20-day moving average.
# Note that the authors suggest using this strategy as an overlay when deciding whether to make a trade rather than using this system on its own.
#
# QC Implementation:

# region imports
from AlgorithmImports import *

# endregion


class MarketSentimentAndAnOvernightAnomaly(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.period: int = 20  # sma period

        self.weight: float = 0
        self.price_data: dict = {}

        self.spy_symbol: Symbol = self.AddEquity("SPY", Resolution.Minute).Symbol
        self.vix_symbol: Symbol = self.AddData(
            QuandlVix, "CBOE/VIX", Resolution.Daily
        ).Symbol  # starts in 2004
        self.bms_symbol: Symbol = self.AddData(
            QuantpediaBMS, "BMS_GLOBAL", Resolution.Daily
        ).Symbol  # starts in 2018

        for symbol in [self.spy_symbol, self.vix_symbol, self.bms_symbol]:
            self.price_data[symbol] = RollingWindow[float](self.period)

    def OnData(self, data: Slice):
        # calculate signal from SPY 16 minutes before close
        if (
            self.spy_symbol in data
            and data[self.spy_symbol]
            and self.Time.hour == 15
            and self.Time.minute == 44
        ):
            weight: float = 0.0

            for symbol in [self.spy_symbol, self.vix_symbol, self.bms_symbol]:
                # trade only sub-strategies with underlying data available
                if (
                    self.Securities[symbol].GetLastData()
                    and (
                        self.Time.date()
                        - self.Securities[symbol].GetLastData().Time.date()
                    ).days
                    <= 3
                ):
                    price: float = self.Securities[symbol].GetLastData().Price
                    rolling_window: RollingWindow = self.price_data[symbol]
                    if rolling_window.IsReady and self.GetSignal(
                        price,
                        rolling_window,
                        True if symbol != self.vix_symbol else False,
                    ):
                        weight += 1 / 3

                    rolling_window.Add(price)

            q: int = int(
                (self.Portfolio.TotalPortfolioValue * weight)
                / data[self.spy_symbol].Value
            )
            if q != 0:
                self.MarketOnCloseOrder(self.spy_symbol, q)
                self.MarketOnOpenOrder(self.spy_symbol, -q)

    def GetSignal(
        self, curr_value: float, rolling_window: RollingWindow, signal_above_sma: bool
    ) -> bool:
        prices: list[float] = [x for x in rolling_window]
        moving_average: float = sum(prices) / len(prices)

        result: bool = False
        if signal_above_sma and (curr_value > moving_average):
            result = True
        elif not signal_above_sma and (curr_value < moving_average):
            result = True

        return result


# Quantpedia data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaBMS(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource(
            "data.quantpedia.com/backtesting_data/index/{0}.csv".format(
                config.Symbol.Value
            ),
            SubscriptionTransportMedium.RemoteFile,
            FileFormat.Csv,
        )

    def Reader(self, config, line, date, isLiveMode):
        data: QuantpediaBMS = QuantpediaBMS()
        data.Symbol = config.Symbol

        if not line[0].isdigit():
            return None

        split: list = line.split(",")

        data.Time = datetime.strptime(split[0], "%Y-%m-%d") + timedelta(days=1)
        data.Value = float(split[2])

        return data


class QuandlVix(PythonQuandl):
    def __init__(self):
        self.ValueColumnName = "VIX Close"
