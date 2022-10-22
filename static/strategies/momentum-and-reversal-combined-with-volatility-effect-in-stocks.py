# https://quantpedia.com/strategies/momentum-and-reversal-combined-with-volatility-effect-in-stocks/
#
# The investment universe consists of NYSE, AMEX, and NASDAQ stocks with prices higher than $5 per share. At the beginning of each month, 
# the sample is divided into equal halves, at the size median, and only larger stocks are used. Then each month, realized returns and realized 
# (annualized) volatilities are calculated for each stock for the past six months. One week (seven calendar days) prior to the beginning of 
# each month is skipped to avoid biases due to microstructures. Stocks are then sorted into quintiles based on their realized past returns 
# and past volatility. The investor goes long on stocks from the highest performing quintile from the highest volatility group and short on 
# stocks from the lowest-performing quintile from the highest volatility group. Stocks are equally weighted and held for six months 
# (therefore, 1/6 of the portfolio is rebalanced every month).
#
# QC implementation changes:
#   - Instead of all listed stock, we select 1000 most liquid stocks from QC filtered stock universe (~8000 stocks) due to time complexity issues tied to whole universe filtering.
    
import numpy as np
from AlgorithmImports import *

class MomentumReversalCombinedWithVolatilityEffectinStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2002, 1, 1)
        self.SetCash(100000)

        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        # EW Tranching.
        self.holding_period = 6
        self.managed_queue = []

        # Daily price data.
        self.data = {}
        self.period = 6 * 21
        
        self.coarse_count = 1000
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(self.DateRules.MonthStart(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Selection)

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(10)
            
    def CoarseSelectionFunction(self, coarse):
        # Update the rolling window every day.
        for stock in coarse:
            symbol = stock.Symbol

            # Store monthly price.
            if symbol in self.data:
                self.data[symbol].update(stock.AdjustedPrice)
                self.data[symbol].LastPrice = stock.AdjustedPrice

        if not self.selection_flag:
            return Universe.Unchanged
        
        # selected = [x for x in coarse if x.HasFundamentalData and x.Market == 'usa' and x.Price > 5]
        selected = sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa' and x.Price > 5],    \
                key = lambda x: x.DollarVolume, reverse = True)[:self.coarse_count]
        
        # Warmup price rolling windows.
        for stock in selected:
            symbol = stock.Symbol
            if symbol in self.data:
                continue
            
            self.data[symbol] = SymbolData(symbol, self.period)
            history = self.History(symbol, self.period, Resolution.Daily)
            if history.empty:
                self.Log(f"Not enough data for {symbol} yet.")
                continue
            closes = history.loc[symbol].close
            for time, close in closes.iteritems():
                self.data[symbol].update(close)
                self.data[symbol].LastPrice = close
                
        return [x.Symbol for x in selected if self.data[x.Symbol].is_ready()]

    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0 and \
                    ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))]

        # if len(fine) > self.coarse_count:
        #     sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
        #     top_by_market_cap = sorted_by_market_cap[:self.coarse_count]
        # else:
        #     top_by_market_cap = fine
            
        sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
        half = int(len(sorted_by_market_cap) / 2)
        top_by_market_cap = [x.Symbol for x in sorted_by_market_cap][:half]
        
        # Performance and volatility tuple.
        perf_volatility = {}
        for symbol in top_by_market_cap:
            performance = self.data[symbol].performance()
            annualized_volatility = self.data[symbol].volatility()
            perf_volatility[symbol] = (performance, annualized_volatility)
        
        long = []
        short = []
        if len(perf_volatility) >= 5:
            sorted_by_perf = sorted(perf_volatility.items(), key = lambda x: x[1][0], reverse = True)
            quintile = int(len(sorted_by_perf) / 5)
            top_by_perf = [x[0] for x in sorted_by_perf[:quintile]]
            low_by_perf = [x[0] for x in sorted_by_perf[-quintile:]]
            
            sorted_by_vol = sorted(perf_volatility.items(), key = lambda x: x[1][1], reverse = True)
            quintile = int(len(sorted_by_vol) / 5)
            top_by_vol = [x[0] for x in sorted_by_vol[:quintile]]
            low_by_vol = [x[0] for x in sorted_by_vol[-quintile:]]
            
            long = [x for x in top_by_perf if x in top_by_vol]
            short = [x for x in low_by_perf if x in top_by_vol]

        if len(long) != 0:
            long_w = self.Portfolio.TotalPortfolioValue / self.holding_period / len(long)
            # symbol/quantity collection
            long_symbol_q = [(x, np.ceil(long_w / self.data[x].LastPrice)) for x in long]
        else:
            long_symbol_q = []
    
        if len(short) != 0:
            short_w = self.Portfolio.TotalPortfolioValue / self.holding_period / len(short)
            # symbol/quantity collection
            short_symbol_q = [(x, -np.ceil(short_w / self.data[x].LastPrice)) for x in short]
        else:
            short_symbol_q = []
                
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
                for symbol, quantity in item.symbol_q:
                    if self.Securities[symbol].Price != 0 and self.Securities[symbol].IsTradable:
                        self.MarketOrder(symbol, -quantity)
                
                remove_item = item
            
            # Trade execution    
            if item.holding_period == 0:
                open_symbol_q = []
                
                for symbol, quantity in item.symbol_q:
                    if self.Securities[symbol].Price != 0 and self.Securities[symbol].IsTradable:
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
        self.LastPrice = 0
    
    def update(self, value):
        self.Price.Add(value)
    
    def is_ready(self):
        return self.Price.IsReady
    
    def update(self, close):
        self.Price.Add(close)
        
    def volatility(self):
        closes = np.array([x for x in self.Price][5:]) # Skip last week.
        daily_returns = closes[:-1] / closes[1:] - 1
        return np.std(daily_returns) * np.sqrt(252 / (len(closes)))
        
    def performance(self):
        closes = [x for x in self.Price][5:] # Skip last week.
        return (closes[0] / closes[-1] - 1)

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))