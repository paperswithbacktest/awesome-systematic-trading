# https://quantpedia.com/strategies/january-barometer/
#
# Invest in the equity market in each January. Stay invested in equity markets (via ETF, fund, or futures) only if January return is positive; otherwise, switch investments to T-Bills.

from AlgorithmImports import *


class JanuaryBarometer(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        data = self.AddEquity("SPY", Resolution.Daily)
        data.SetLeverage(10)
        self.market = data.Symbol

        data = self.AddEquity("BIL", Resolution.Daily)
        data.SetLeverage(10)
        self.t_bills = data.Symbol

        self.start_price = None
        self.recent_month = -1

    def OnData(self, data):
        if self.recent_month == self.Time.month:
            return
        self.recent_month = self.Time.month

        if (
            self.Securities[self.market].GetLastData()
            and self.Securities[self.t_bills].GetLastData()
        ):
            if (
                self.Time.date()
                - self.Securities[self.market].GetLastData().Time.date()
            ).days < 5 and (
                self.Time.date()
                - self.Securities[self.t_bills].GetLastData().Time.date()
            ).days < 5:
                if self.Time.month == 1:
                    self.Liquidate(self.t_bills)
                    self.SetHoldings(self.market, 1)

                    self.start_price = self.Securities[self.market].Price

                if self.Time.month == 2 and self.start_price:
                    returns = (
                        self.Securities[self.market].Price - self.start_price
                    ) / self.start_price
                    if returns > 0:
                        self.SetHoldings(self.market, 1)
                    else:
                        self.start_price = None
                        self.Liquidate(self.market)
                        self.SetHoldings(self.t_bills, 1)
            else:
                self.Liquidate()
        else:
            self.Liquidate()
