# https://quantpedia.com/strategies/turn-of-the-month-in-equity-indexes/
#
# Buy SPY ETF 1 day (some papers say 4 days) before the end of the month and sell the 3rd trading day of the new month at the close.

from AlgorithmImports import *

class TurnoftheMonthinEquityIndexes(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(1998, 1, 1)
        self.SetCash(100000)
        
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        
        self.sell_flag = False
        self.days = 0
        
        self.Schedule.On(self.DateRules.MonthStart(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Rebalance)
        self.Schedule.On(self.DateRules.MonthEnd(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Purchase)
    
    def Purchase(self):
        self.SetHoldings(self.symbol, 1)
    
    def Rebalance(self):
        self.sell_flag = True
        
    def OnData(self, data):
        if self.sell_flag:
            self.days += 1
            if self.days == 3:
                self.Liquidate(self.symbol)
                self.sell_flag = False
                self.days = 0