# https://quantpedia.com/strategies/payday-anomaly/
#
# The investment universe consists of the S&P500 index. Simply, buy and hold the index during the 16th day in the month during each month of the year.

from dateutil.relativedelta import relativedelta
from AlgorithmImports import *

class PayDayAnomaly(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)
        
        self.symbol = self.AddEquity('SPY', Resolution.Minute).Symbol
        self.liquidate_next_day = False
        
        self.Schedule.On(self.DateRules.EveryDay(self.symbol), self.TimeRules.BeforeMarketClose(self.symbol, 1), self.Purchase)
    
    def Purchase(self):
        alg_time = self.Time
        paydate = self.PaydayDate(alg_time)

        if alg_time.date() == paydate:
            self.SetHoldings(self.symbol, 1)
            self.liquidate_next_day = True
            # self.algorithm.EmitInsights(Insight.Price(self.symbol, timedelta(days=1), InsightDirection.Up, None, None, None, self.weight))

        if self.liquidate_next_day:
            self.liquidate_next_day = False
            return
        
        if self.Portfolio[self.symbol].IsLong:
            self.Liquidate(self.symbol)

    def PaydayDate(self, date_time):
        payday = date(date_time.year, date_time.month, 1) + relativedelta(day=15)
        
        if payday.weekday() == 5: # Is saturday.
            payday = payday - timedelta(days=1)
        elif payday.weekday() == 6: # Is sunday.
            payday = payday - timedelta(days=2)
        
        return payday