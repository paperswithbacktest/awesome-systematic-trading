#region imports
from AlgorithmImports import *
#endregion
# https://quantpedia.com/strategies/low-volatility-factor-effect-in-stocks-long-only-version/
#
# The investment universe consists of global large-cap stocks (or US large-cap stocks). At the end of each month, the investor constructs 
# equally weighted decile portfolios by ranking the stocks on the past three-year volatility of weekly returns. The investor goes long 
# stocks in the top decile (stocks with the lowest volatility).
#
# QC implementation changes:
#   - Top quartile (stocks with the lowest volatility) is selected instead of decile.

import numpy as np

class LowVolatilityFactorEffectStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)  
        self.SetCash(100000) 

        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.period = 12*21
        
        self.coarse_count = 3000
        self.last_coarse = []
        self.data = {}
        
        self.long = []

        self.selection_flag = True
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(self.DateRules.MonthEnd(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Selection)

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(10)
            
    def CoarseSelectionFunction(self, coarse):
        # Update the rolling window every day.
        for stock in coarse:
            symbol = stock.Symbol

            # Store daily price.
            if symbol in self.data:
                self.data[symbol].update(stock.AdjustedPrice)

        if not self.selection_flag:
            return Universe.Unchanged

        selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa']
        # selected = [x.Symbol
        #     for x in sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa'],
        #         key = lambda x: x.DollarVolume, reverse = True)[:self.coarse_count]]
        
        # Warmup price rolling windows.
        for symbol in selected:
            if symbol in self.data:
                continue
            
            self.data[symbol] = SymbolData(self.period)
            history = self.History(symbol, self.period, Resolution.Daily)
            if history.empty:
                self.Log(f"Not enough data for {symbol} yet.")
                continue
            closes = history.loc[symbol].close
            for time, close in closes.iteritems():
                self.data[symbol].update(close)
        
        return [x for x in selected if self.data[x].is_ready()]

    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0]
        
        # market cap sorting
        if len(fine) > self.coarse_count:
            sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
            fine = sorted_by_market_cap[:self.coarse_count]
        
        weekly_vol = {x.Symbol : self.data[x.Symbol].volatility() for x in fine}
        
        # volatility sorting
        sorted_by_vol = sorted(weekly_vol.items(), key = lambda x: x[1], reverse = True)
        quartile = int(len(sorted_by_vol) / 4)
        self.long = [x[0] for x in sorted_by_vol[-quartile:]]
        
        return self.long
        
    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False

        # Trade execution.
        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.long:
                self.Liquidate(symbol)

        for symbol in self.long:
            if symbol in data and data[symbol]:
                self.SetHoldings(symbol, 1 / len(self.long))

        self.long.clear()
        
    def Selection(self):
        self.selection_flag = True

class SymbolData():
    def __init__(self, period):
        self.price = RollingWindow[float](period)
    
    def update(self, value):
        self.price.Add(value)
    
    def is_ready(self) -> bool:
        return self.price.IsReady
        
    def volatility(self) -> float:
        closes = [x for x in self.price]
        
        # Weekly volatility calc.
        separete_weeks = [closes[x:x+5] for x in range(0, len(closes), 5)]
        weekly_returns = [(x[0] - x[-1]) / x[-1] for x in separete_weeks]
        return np.std(weekly_returns)   

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))