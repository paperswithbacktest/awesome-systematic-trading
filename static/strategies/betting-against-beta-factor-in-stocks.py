# https://quantpedia.com/strategies/betting-against-beta-factor-in-stocks/
# 
# The investment universe consists of all stocks from the CRSP database. The beta for each stock is calculated with respect to the MSCI US Equity Index using a 1-year 
# rolling window. Stocks are then ranked in ascending order on the basis of their estimated beta. The ranked stocks are assigned to one of two portfolios: low beta and
# high beta. Securities are weighted by the ranked betas, and portfolios are rebalanced every calendar month. Both portfolios are rescaled to have a beta of one at portfolio
# formation. The “Betting-Against-Beta” is the zero-cost zero-beta portfolio that is long on the low-beta portfolio and short on the high-beta portfolio. There are a lot of 
# simple modifications (like going long on the bottom beta decile and short on the top beta decile), which could probably improve the strategy’s performance.
#
# QC implementation changes:
#   - The investment universe consists of 1000 most liquid US stocks with price > 5$.

from scipy import stats
from AlgorithmImports import *
import numpy as np

class  BettingAgainstBetaFactorinStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        # Daily price data.
        self.data = {}
        self.period = 12 * 21

        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        self.data[self.symbol] = RollingWindow[float](self.period)
        
        self.weight = {}
        self.long = []
        self.short = []
        self.long_lvg = 1   # leverage for long portfolio calculated from average beta
        self.short_lvg = 1  # leverage for short portfolio calculated from average beta
        self.leverage_cap = 2
        
        self.coarse_count = 1000
        
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(self.DateRules.MonthStart(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Selection)
        
    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(self.leverage_cap*3)
            
    def CoarseSelectionFunction(self, coarse):
        # Update the rolling window every day.
        for stock in coarse:
            symbol = stock.Symbol

            if symbol in self.data:
                # Store daily price.
                self.data[symbol].Add(stock.AdjustedPrice)
        
        # Selection once a month.
        if not self.selection_flag:
            return Universe.Unchanged
        
        # selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa' and x.Price > 5]
        selected = [x.Symbol
            for x in sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa' and x.Price > 5],
                key = lambda x: x.DollarVolume, reverse = True)[:self.coarse_count]]
                
        # Warmup price rolling windows.
        for symbol in selected:
            if symbol in self.data:
                continue
            
            self.data[symbol] = RollingWindow[float](self.period)
            history = self.History(symbol, self.period, Resolution.Daily)
            if history.empty:
                self.Log(f"Not enough data for {symbol} yet")
                continue
            closes = history.loc[symbol].close
            for time, close in closes.iteritems():
                self.data[symbol].Add(close)
                
        return [x for x in selected if self.data[x].IsReady]
    
    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0]
                    
        # if len(fine) > self.coarse_count:
        #     sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
        #     top_by_market_cap = sorted_by_market_cap[:self.coarse_count]
        # else:
        #     top_by_market_cap = fine
            
        beta = {}
        
        if not self.data[self.symbol].IsReady: return []
        
        for stock in fine:
            symbol = stock.Symbol
            market_closes = np.array([x for x in self.data[self.symbol]])
            stock_closes = np.array([x for x in self.data[symbol]])
              
            market_returns = (market_closes[:-1] - market_closes[1:]) / market_closes[1:]
            stock_returns = (stock_closes[:-1] - stock_closes[1:]) / stock_closes[1:]
            
            cov = np.cov(stock_returns[::-1], market_returns[::-1])[0][1]
            market_variance = np.var(market_returns)
            beta[symbol] = cov / market_variance
            
            # beta_, intercept, r_value, p_value, std_err = stats.linregress(market_returns[::-1], stock_returns[::-1])
            # beta[symbol] = beta_
        
        if len(beta) >= 10:
            # sort by beta
            sorted_by_beta = sorted(beta.items(), key = lambda x:x[1], reverse=True)
            decile = int(len(sorted_by_beta) / 10)
            self.long = [x for x in sorted_by_beta[-decile:]]
            self.short = [x for x in sorted_by_beta[:decile]]
            
            # create zero-beta portfolio
            long_mean_beta = np.mean([x[1] for x in self.long])
            short_mean_beta = np.mean([x[1] for x in self.short])
            
            self.long = [x[0] for x in self.long]
            self.short = [x[0] for x in self.short]
            
            self.long_lvg = 1/long_mean_beta
            self.short_lvg = 1/short_mean_beta
            
            # cap leverage
            if self.long_lvg <= 0:
                self.long_lvg = self.leverage_cap
            else:
                self.long_lvg = min(self.leverage_cap, self.long_lvg)
                
            if self.short_lvg <= 0:
                self.short_lvg = self.leverage_cap
            else:
                self.short_lvg = min(self.leverage_cap, self.short_lvg)
        
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
        
        long_len = len(self.long)
        short_len = len(self.short)
        
        for symbol in self.long:
            self.SetHoldings(symbol, (1/long_len)*self.long_lvg)
        for symbol in self.short:
            self.SetHoldings(symbol, -(1/short_len)*self.short_lvg)
        
        self.long.clear()
        self.short.clear()
        self.long_lvg = 1
        self.short_lvg = 1
        
    def Selection(self):
        self.selection_flag = True
            
# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))