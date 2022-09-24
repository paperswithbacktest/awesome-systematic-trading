# region imports
from AlgorithmImports import *

# endregion
# https://quantpedia.com/strategies/asset-class-momentum-rotational-system/
#
# Use 5 ETFs (SPY - US stocks, EFA - foreign stocks, IEF - bonds, VNQ - REITs, GSG - commodities).
# Pick 3 ETFs with strongest 12 month momentum into your portfolio and weight them equally.
# Hold for 1 month and then rebalance.


class MomentumAssetAllocationStrategy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.data = {}
        period = 12 * 21
        self.SetWarmUp(period)
        self.symbols = ["SPY", "EFA", "IEF", "VNQ", "GSG"]

        for symbol in self.symbols:
            self.AddEquity(symbol, Resolution.Daily)
            self.data[symbol] = self.ROC(symbol, period, Resolution.Daily)

        self.recent_month = -1

    def OnData(self, data):
        if self.IsWarmingUp:
            return

        # monthly rebalance
        if self.Time.month == self.recent_month:
            return
        self.recent_month = self.Time.month

        sorted_by_momentum = sorted(
            [
                x
                for x in self.data.items()
                if x[1].IsReady and x[0] in data and data[x[0]]
            ],
            key=lambda x: x[1].Current.Value,
            reverse=True,
        )
        count = 3
        long = [x[0] for x in sorted_by_momentum][:count]

        invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
        for symbol in invested:
            if symbol not in long:
                self.Liquidate(symbol)

        for symbol in long:
            self.SetHoldings(symbol, 1 / len(long))
