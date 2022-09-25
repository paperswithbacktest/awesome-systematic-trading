# https://quantpedia.com/strategies/paired-switching/
#
# This strategy is very flexible. Investors could use stocks, funds, or ETFs as an investment vehicle. We show simple trading rules for a sample strategy
# from the source research paper. The investor uses two Vanguard funds as his investment vehicles – one equity fund (VFINX) and one government bond
from AlgorithmImports import *

# fund (VUSTX). These two funds have a negative correlation as they are proxies for two negatively correlated asset classes. The investor looks at the
# performance of the two funds over the prior quarter and buys the fund that has a higher return during the ranking period. The position is held for one
# quarter (the investment period). At the end of the investment period, the cycle is repeated.


class PairedSwitching(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2004, 1, 1)
        self.SetCash(100000)

        self.first_symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.second_symbol = self.AddEquity("AGG", Resolution.Daily).Symbol
        self.recent_month = -1

    def OnData(self, data):
        if self.Time.month == self.recent_month:
            return
        self.recent_month = self.Time.month

        if self.recent_month % 3 == 0:
            if self.first_symbol in data and self.second_symbol in data:
                history_call = self.History(
                    [self.first_symbol, self.second_symbol], timedelta(days=90)
                )
                if not history_call.empty:
                    first_bars = history_call.loc[self.first_symbol.Value]
                    last_p1 = first_bars["close"].iloc[0]

                    second_bars = history_call.loc[self.second_symbol.Value]
                    last_p2 = second_bars["close"].iloc[0]

                    # Calculates performance of funds over the prior quarter.
                    first_performance = (
                        float(self.Securities[self.first_symbol].Price) - float(last_p1)
                    ) / (float(self.Securities[self.first_symbol].Price))
                    second_performance = (
                        float(self.Securities[self.second_symbol].Price)
                        - float(last_p2)
                    ) / (float(self.Securities[self.second_symbol].Price))

                    # Buys the fund that has the higher return during the period.
                    if first_performance > second_performance:
                        if self.Securities[self.second_symbol].Invested:
                            self.Liquidate(self.second_symbol)
                        self.SetHoldings(self.first_symbol, 1)
                    else:
                        if self.Securities[self.first_symbol].Invested:
                            self.Liquidate(self.first_symbol)
                        self.SetHoldings(self.second_symbol, 1)
