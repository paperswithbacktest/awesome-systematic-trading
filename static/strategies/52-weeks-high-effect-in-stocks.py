# https://quantpedia.com/strategies/52-weeks-high-effect-in-stocks/
#
# The investment universe consists of all stocks from NYSE, AMEX and NASDAQ (the research paper used the CRSP 
# database for backtesting). The ratio between the current price and 52-week high is calculated for each stock 
# at the end of each month (PRILAG i,t = Price i,t / 52-Week High i,t). Every month, the investor then calculates
# the weighted average of ratios (PRILAG i,t) from all firms in each industry (20 industries are used), where the
# weight is the market capitalization of the stock at the end of month t. The winners (losers) are stocks in the
# six industries with the highest (lowest) weighted averages of PRILAGi,t. The investor buys stocks in the winner
# portfolio and shorts stocks in the loser portfolio and holds them for three months. Stocks are weighted equally
# and the portfolio is rebalanced monthly (which means that 1/3 of the portfolio is rebalanced each month).
#
# QC implementation changes:
#   - Universe consists of 500 most liquid stocks traded on NYSE, AMEX, or NASDAQ.

from numpy import floor
from AlgorithmImports import *

class Weeks52HighEffectinStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.SetSecurityInitializer(lambda x: x.SetMarketPrice(self.GetLastKnownPrice(x)))
        
        self.period = 12 * 21

        # Tranching.
        self.holding_period = 3
        self.managed_queue = []

        # Daily 'high' data.
        self.data = {}
        
        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.coarse_count = 500
        self.selection_flag = False
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

            if symbol in self.data:
                # Store daily price.
                self.data[symbol].update(stock.AdjustedPrice)
            
        if not self.selection_flag:
            return Universe.Unchanged
        
        selected = [x.Symbol
            for x in sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa'],
                key = lambda x: x.DollarVolume, reverse = True)[:self.coarse_count]]
        
        # Warmup price rolling windows.
        for symbol in selected:
            if symbol in self.data:
                continue
            
            self.data[symbol] = SymbolData(symbol, self.period)
            history = self.History(symbol, self.period, Resolution.Daily)
            if history.empty:
                self.Log(f"Not enough data for {symbol} yet")
                continue
            closes = history.loc[symbol].close
            for time, close in closes.iteritems():
                self.data[symbol].update(close)
                
        return [x for x in selected if self.data[x].is_ready()]

    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0 and \
                ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))]
        
        group = {}
        for stock in fine:
            symbol = stock.Symbol
            
            industry_group_code = stock.AssetClassification.MorningstarIndustryGroupCode
            if industry_group_code == 0: continue
            
            # Adding stocks in groups.
            if not industry_group_code in group:
                group[industry_group_code] = []
            
            max_high = self.data[symbol].maximum()
            price = self.data[symbol].get_latest_price()
            
            stock_prilag = (stock, price / max_high)
            group[industry_group_code].append(stock_prilag)
        
        top_industries = []
        low_industries = []
        
        if len(group) != 0: 
            # Weighted average of ratios calc.
            industry_prilag_weighted_avg = {}
            for industry_code in group:
                total_market_cap = sum([stock_prilag_data[0].MarketCap for stock_prilag_data in group[industry_code]])
                if total_market_cap == 0: continue
                industry_prilag_weighted_avg[industry_code] = sum([stock_prilag_data[1] * (stock_prilag_data[0].MarketCap / total_market_cap) for stock_prilag_data in group[industry_code]])
            
            if len(industry_prilag_weighted_avg) != 0:
                # Weighted average industry sorting.
                sorted_by_weighted_avg = sorted(industry_prilag_weighted_avg.items(), key=lambda x: x[1], reverse = True)
                top_industries = [x[0] for x in sorted_by_weighted_avg[:6]]
                low_industries = [x[0] for x in sorted_by_weighted_avg[-6:]]
        
        long = []
        short = []
        for industry_code in top_industries:
            for stock_prilag_data in group[industry_code]:
                symbol = stock_prilag_data[0].Symbol
                long.append(symbol)
        
        for industry_code in low_industries:
            for stock_prilag_data in group[industry_code]:
                symbol = stock_prilag_data[0].Symbol
                short.append(symbol)
                
        long_w = self.Portfolio.TotalPortfolioValue / self.holding_period / len(long)
        short_w = self.Portfolio.TotalPortfolioValue / self.holding_period / len(short)
        
        # symbol/quantity collection
        long_symbol_q = [(x, floor(long_w / self.data[x].get_latest_price())) for x in long]
        short_symbol_q = [(x, -floor(short_w / self.data[x].get_latest_price())) for x in short]
        
        self.managed_queue.append(RebalanceQueueItem(long_symbol_q + short_symbol_q))
        
        return long + short

    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False

        remove_item = None
        
        # Rebalance portfolio
        for item in self.managed_queue:
            if item.holding_period == self.holding_period:
                # Liquidate
                for symbol, quantity in item.symbol_q:
                    self.MarketOrder(symbol, -quantity)
                remove_item = item
            
            # Trade execution    
            if item.holding_period == 0:
                open_symbol_q = []
                
                for symbol, quantity in item.symbol_q:
                    if self.Securities.ContainsKey(symbol) and self.Securities[symbol].IsTradable:
                        self.MarketOrder(symbol, quantity)
                        open_symbol_q.append((symbol, quantity))
                            
                # Only opened orders will be closed        
                item.symbol_q = open_symbol_q
                
            item.holding_period += 1
            
        # We need to remove closed part of portfolio after loop. Otherwise it will miss one item in self.managed_queue.
        if remove_item:
            self.managed_queue.remove(remove_item)

    def Selection(self):
        self.selection_flag = True

class RebalanceQueueItem():
    def __init__(self, symbol_q):
        # symbol/quantity collections
        self.symbol_q = symbol_q  
        self.holding_period = 0

class SymbolData():
    def __init__(self, symbol, period):
        self.Symbol = symbol
        self.Price = RollingWindow[float](period)
    
    def update(self, value):
        self.Price.Add(value)
    
    def is_ready(self):
        return self.Price.IsReady
     
    def maximum(self):
        return max([x for x in self.Price])
        
    def get_latest_price(self):
        return [x for x in self.Price][0]

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))