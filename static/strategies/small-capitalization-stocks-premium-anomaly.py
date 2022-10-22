# https://quantpedia.com/strategies/small-capitalization-stocks-premium-anomaly/
#
# The investment universe contains all NYSE, AMEX, and NASDAQ stocks. Decile portfolios are formed based on the market capitalization
# of stocks. To capture “size” effect, SMB portfolio goes long small stocks (lowest decile) and short big stocks (highest decile).
#
# QC implementation changes:
#   - Instead of all listed stock, we select top 3000 stocks by market cap from QC stock universe.

from AlgorithmImports import *

class ValueBooktoMarketFactor(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000) 

        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.coarse_count = 3000
        
        self.long = []
        self.short = []
        
        self.month = 12
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        
        self.Schedule.On(self.DateRules.MonthEnd(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Selection)

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(10)

    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged
        
        selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa']
        return selected
    
    def FineSelectionFunction(self, fine):
        sorted_by_market_cap = sorted([x for x in fine if x.MarketCap != 0 and  \
                                ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))],    \
                                key = lambda x:x.MarketCap, reverse=True)
        top_by_market_cap = [x for x in sorted_by_market_cap[:self.coarse_count]]

        quintile = int(len(top_by_market_cap) / 5)
        self.long = [i.Symbol for i in top_by_market_cap[-quintile:]]
        self.short = [i.Symbol for i in top_by_market_cap[:quintile]]
        
        return self.long + self.short
    
    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False
        
        # Trade execution.
        long_count = len(self.long)
        short_count = len(self.short)
        
        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.long + self.short:
                self.Liquidate(symbol)
        
        # Leveraged portfolio - 100% long, 100% short. 
        for symbol in self.long:
            self.SetHoldings(symbol, 1 / long_count)

        for symbol in self.short:
            self.SetHoldings(symbol, -1 / short_count)

        self.long.clear()
        self.short.clear()
    
    def Selection(self):
        if self.month == 12:
            self.selection_flag = True
        
        self.month += 1
        if self.month > 12:
            self.month = 1

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))