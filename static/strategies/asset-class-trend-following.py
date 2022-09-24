# region imports
from AlgorithmImports import *

# endregion
# https://quantpedia.com/strategies/asset-class-trend-following/
#
# Use 5 ETFs (SPY - US stocks, EFA - foreign stocks, IEF - bonds, VNQ - REITs,
# GSG - commodities), equal weight the portfolio. Hold asset class ETF only when
# it is over its 10 month Simple Moving Average, otherwise stay in cash.
#
# QC implementation:
#   - SMA with period of 210 days is used.


class AssetClassTrendFollowing(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.sma = {}
        period = 10 * 21
        self.SetWarmUp(period, Resolution.Daily)

        self.symbols = ["SPY", "EFA", "IEF", "VNQ", "GSG"]
        self.rebalance_flag = False

        self.tracked_symbol = None
        for symbol in self.symbols:
            self.AddEquity(symbol, Resolution.Minute)
            self.sma[symbol] = self.SMA(symbol, period, Resolution.Daily)

        self.recent_month = -1

    def OnData(self, data):
        # rebalance once a month
        if self.Time.month == self.recent_month:
            return
        if self.Time.hour != 9 and self.Time.minute != 31:
            return
        self.recent_month = self.Time.month

        long = [
            symbol
            for symbol in self.symbols
            if symbol in data
            and data[symbol]
            and self.sma[symbol].IsReady
            and data[symbol].Value > self.sma[symbol].Current.Value
        ]

        # trade execution
        invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
        for symbol in invested:
            if symbol not in long:
                self.Liquidate(symbol)

        for symbol in long:
            self.SetHoldings(symbol, 1 / len(long))
