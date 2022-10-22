# https://quantpedia.com/strategies/roa-effect-within-stocks/
#
# The investment universe contains all stocks on NYSE and AMEX and Nasdaq with Sales greater than 10 million USD. Stocks are then sorted into
# two halves based on market capitalization. Each half is then divided into deciles based on Return on assets (ROA) calculated as quarterly
# earnings (Compustat quarterly item IBQ – income before extraordinary items) divided by one-quarter-lagged assets (item ATQ – total assets).
# The investor then goes long the top three deciles from each market capitalization group and goes short bottom three deciles. The strategy is
# rebalanced monthly, and stocks are equally weighted.
#
# QC implementation changes:
#   - Instead of all listed stock, we select 500 most liquid stocks traded on NYSE, AMEX, or NASDAQ.

from AlgorithmImports import *


class ROAEffectWithinStocks(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.course_count = 500

        self.long = []
        self.short = []

        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(
            self.DateRules.MonthEnd(self.symbol),
            self.TimeRules.AfterMarketOpen(self.symbol),
            self.Selection,
        )

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(5)

    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged

        selected = sorted(
            [
                x
                for x in coarse
                if x.HasFundamentalData and x.Market == "usa" and x.Price > 5
            ],
            key=lambda x: x.DollarVolume,
            reverse=True,
        )

        return [x.Symbol for x in selected[: self.course_count]]

    def FineSelectionFunction(self, fine):
        fine = [
            x
            for x in fine
            if x.MarketCap != 0
            and x.ValuationRatios.SalesPerShare
            * x.EarningReports.DilutedAverageShares.Value
            > 10000000
            and x.OperationRatios.ROA.ThreeMonths != 0
            and (
                (x.SecurityReference.ExchangeId == "NYS")
                or (x.SecurityReference.ExchangeId == "NAS")
                or (x.SecurityReference.ExchangeId == "ASE")
            )
        ]

        # Sorting by market cap.
        sorted_by_market_cap = sorted(fine, key=lambda x: x.MarketCap, reverse=True)
        half = int(len(sorted_by_market_cap) / 2)
        top_mc = [x for x in sorted_by_market_cap[:half]]
        bottom_mc = [x for x in sorted_by_market_cap[half:]]

        if len(top_mc) >= 10 and len(bottom_mc) >= 10:
            # Sorting by ROA.
            sorted_top_by_roa = sorted(
                top_mc, key=lambda x: (x.OperationRatios.ROA.Value), reverse=True
            )
            decile = int(len(sorted_top_by_roa) / 10)
            long_top = [x.Symbol for x in sorted_top_by_roa[: decile * 3]]
            short_top = [x.Symbol for x in sorted_top_by_roa[-(decile * 3) :]]

            sorted_bottom_by_roa = sorted(
                bottom_mc, key=lambda x: (x.OperationRatios.ROA.Value), reverse=True
            )
            decile = int(len(sorted_bottom_by_roa) / 10)
            long_bottom = [x.Symbol for x in sorted_bottom_by_roa[: decile * 3]]
            short_bottom = [x.Symbol for x in sorted_bottom_by_roa[-(decile * 3) :]]

            self.long = long_top + long_bottom
            self.short = short_top + short_bottom

        return self.long + self.short

    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False

        # Trade execution.
        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.long + self.short:
                self.Liquidate(symbol)

        long_count = len(self.long)
        short_count = len(self.short)

        for symbol in self.long:
            self.SetHoldings(symbol, 1 / long_count)
        for symbol in self.short:
            self.SetHoldings(symbol, -1 / short_count)

        self.long.clear()
        self.short.clear()

    def Selection(self):
        self.selection_flag = True


# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
