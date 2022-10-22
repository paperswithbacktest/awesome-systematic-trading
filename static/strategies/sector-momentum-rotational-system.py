# region imports
from AlgorithmImports import *

# endregion
# https://quantpedia.com/strategies/sector-momentum-rotational-system/
#
# Use ten sector ETFs. Pick 3 ETFs with the strongest 12-month momentum into your portfolio and weight them equally. Hold them for one month and then rebalance.


class SectorMomentumAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        # Daily ROC data.
        self.data = {}

        self.period = 12 * 21
        self.SetWarmUp(self.period)

        self.symbols = [
            "VNQ",  # Vanguard Real Estate Index Fund
            "XLK",  # Technology Select Sector SPDR Fund
            "XLE",  # Energy Select Sector SPDR Fund
            "XLV",  # Health Care Select Sector SPDR Fund
            "XLF",  # Financial Select Sector SPDR Fund
            "XLI",  # Industrials Select Sector SPDR Fund
            "XLB",  # Materials Select Sector SPDR Fund
            "XLY",  # Consumer Discretionary Select Sector SPDR Fund
            "XLP",  # Consumer Staples Select Sector SPDR Fund
            "XLU",  # Utilities Select Sector SPDR Fund
        ]

        for symbol in self.symbols:
            data = self.AddEquity(symbol, Resolution.Daily)
            data.SetFeeModel(CustomFeeModel())
            data.SetLeverage(5)

            self.data[symbol] = self.ROC(symbol, self.period, Resolution.Daily)

        self.data[self.symbols[0]].Updated += self.OnROCUpdated
        self.recent_month = -1
        self.rebalance_flag = False

    def OnROCUpdated(self, sender, updated):
        # set rebalance flag
        if self.recent_month != self.Time.month:
            self.recent_month = self.Time.month
            self.rebalance_flag = True

    def OnData(self, data):
        if self.IsWarmingUp:
            return

        # rebalance once a month
        if self.rebalance_flag:
            self.rebalance_flag = False

            sorted_by_momentum = sorted(
                [
                    x
                    for x in self.data.items()
                    if x[1].IsReady and x[0] in data and data[x[0]]
                ],
                key=lambda x: x[1].Current.Value,
                reverse=True,
            )
            long = [x[0] for x in sorted_by_momentum[:3]]

            # Trade execution.
            invested = [x.Key for x in self.Portfolio if x.Value.Invested]
            for symbol in invested:
                if symbol not in long:
                    self.Liquidate(symbol)

            for symbol in long:
                self.SetHoldings(symbol, 1 / len(long))


# Custom fee model
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
