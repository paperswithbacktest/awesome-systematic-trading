#region imports
from AlgorithmImports import *
#endregion
# https://quantpedia.com/strategies/asset-growth-effect/
#
# The investment universe consists of all non-financial U.S. stocks listed on NYSE, AMEX, and NASDAQ. Stocks are then sorted each year at the end 
# of June into ten equal groups based on the percentage change in total assets for the previous year. The investor goes long decile with low asset
# growth firms and short decile with high asset growth firms. The portfolio is weighted equally and rebalanced every year.
#
# QC implementation changes:
#   - Top 3000 stocks by market cap are selected from QC stock universe.

class AssetGrowthEffect(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)
        
        self.symbol:Symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.long:list[Symbol] = []
        self.short:list[Symbol] = []
        
        self.coarse_count:int = 3000
        self.quantile:int = 10
        
        # Latest assets data.
        self.total_assets:dict[Symbol, float] = {}
        
        self.selection_flag:bool = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(self.DateRules.MonthEnd(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Selection)

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(5)
            
    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged
        
        # Select all stocks in universe.
        return [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa']
    
    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.FinancialStatements.BalanceSheet.TotalAssets.TwelveMonths > 0 and
                ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))]
                
        if len(fine) > self.coarse_count:
            sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
            fine = sorted_by_market_cap[:self.coarse_count]
            
        assets_growth:dict[Symbol, float] = {}
        for stock in fine:
            symbol = stock.Symbol
            
            if symbol not in self.total_assets:
                self.total_assets[symbol] = None
                
            current_assets = stock.FinancialStatements.BalanceSheet.TotalAssets.TwelveMonths
            
            # There is not previous assets data.
            if not self.total_assets[symbol]:
                self.total_assets[symbol] = current_assets
                continue
            
            # Assets growth calc.
            assets_growth[symbol] = (current_assets - self.total_assets[symbol]) / self.total_assets[symbol]
            
            # Update data.
            self.total_assets[symbol] = current_assets
        
        # Asset growth sorting.
        if len(assets_growth) >= self.quantile:
            sorted_by_assets_growth = sorted(assets_growth.items(), key = lambda x: x[1], reverse = True)
            decile = int(len(sorted_by_assets_growth) / self.quantile)
            self.long = [x[0] for x in sorted_by_assets_growth[-decile:]]
            self.short = [x[0] for x in sorted_by_assets_growth[:decile]]
        
        return self.long + self.short
        
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

        for symbol in self.short:
            if symbol in data and data[symbol]:
                self.SetHoldings(symbol, -1 / len(self.short))

        self.long.clear()
        self.short.clear()
            
    def Selection(self):
        if self.Time.month == 6:
            self.selection_flag = True
            
# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))