# https://quantpedia.com/strategies/residual-momentum-factor/
#
# The investment universe consists of all domestic, primary stocks listed on the New York (NYSE), American (AMEX), and NASDAQ 
# stock markets with a price higher than $1. Closed-end funds, REITs, unit trusts, ADRs, and foreign stocks are removed. The 
# 10% largest stocks in terms of market capitalization are then selected for trading.
# The residual momentum strategy is defined as a zero-investment top-minus-bottom decile portfolio based on ranking stocks 
# every month on their past 12-month residual returns, excluding the most recent month, standardized by the standard deviation
# of the residual returns over the same period. Residual returns are estimated each month for all stocks over the past 36 months
# using a regression model. The regression model is calculated every month for all eligible stocks using the Fama and French 
# three factors as independent variables. The portfolio is equally weighted and rebalanced monthly.
#
# QC implementation changes:
#   - Universe consists of top 3000 US stock by market cap from NYSE, AMEX and NASDAQ.

import numpy as np
from AlgorithmImports import *
import statsmodels.api as sm

class ResidualMomentumFactor(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.coarse_count = 500

        # Monthly price data.
        self.data = {}
        self.period = 37

        # Warmup market monthly data.
        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        self.data[self.symbol] = RollingWindow[float](self.period)
        
        history = self.History(self.symbol, self.period * 21, Resolution.Daily)
        if history.empty:
            self.Log(f"Not enough data for {self.symbol} yet.")
        else:    
            closes = history.loc[self.symbol].close
            closes_len = len(closes.keys())
            # Find monthly closes.
            for index, time_close in enumerate(closes.iteritems()):
                # index out of bounds check.
                if index + 1 < closes_len:
                    date_month = time_close[0].date().month
                    next_date_month = closes.keys()[index + 1].month
                
                    # Found last day of month.
                    if date_month != next_date_month:
                        self.data[self.symbol].Add(time_close[1])        
        
        # Factors.
        self.size_factor_symbols = []                                   # Symbol,long_flag tuple.
        self.size_factor_vector = RollingWindow[float](self.period - 1) # Monthly performance.

        self.value_factor_symbols = []
        self.value_factor_vector = RollingWindow[float](self.period - 1)
        
        # Monthly residual returns for each stock.
        self.residual_return = {}
        self.residual_momentum_period = 12
        
        self.long = []
        self.short = []
        
        self.last_month = -1
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        
    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetLeverage(10)
            security.SetFeeModel(CustomFeeModel())
    
    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged

        # Update the rolling window every month.
        for stock in coarse:
            symbol = stock.Symbol
            
            # Store monthly market price.
            if symbol == self.symbol:
                self.data[self.symbol].Add(stock.AdjustedPrice)
            else:
                # Store monthly stock price.
                if symbol in self.data:
                    self.data[symbol].Add(stock.AdjustedPrice)

        selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa']
        # selected = [x.Symbol
        #     for x in sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa'],
        #         key = lambda x: x.DollarVolume, reverse = True)[:self.coarse_count]]
        
        # Warmup price rolling windows.
        for symbol in selected:
            if symbol in self.data:
                continue
            
            self.data[symbol] = RollingWindow[float](self.period)
            history = self.History(symbol, self.period * 21, Resolution.Daily)
            if history.empty:
                self.Log(f"Not enough data for {symbol} yet.")
                continue
            closes = history.loc[symbol].close
            
            closes_len = len(closes.keys())
            # Find monthly closes.
            for index, time_close in enumerate(closes.iteritems()):
                # index out of bounds check.
                if index + 1 < closes_len:
                    date_month = time_close[0].date().month
                    next_date_month = closes.keys()[index + 1].month
                
                    # Found last day of month.
                    if date_month != next_date_month:
                        self.data[symbol].Add(time_close[1])
            
        return [x for x in selected if self.data[x].IsReady]        

    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0 and x.CompanyReference.IsREIT == 0 and      \
                ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))]
                
        if len(fine) > self.coarse_count:
            sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
            top_by_market_cap = sorted_by_market_cap[:self.coarse_count]
        else:
            top_by_market_cap = fine

        # Size factor.
        # sorted_by_market_cap = sorted(top_by_market_cap, key = lambda x:(x.MarketCap), reverse=False)
        quintile = int(len(top_by_market_cap) / 5)
        size_factor_long = [ (i.Symbol,True) for i in top_by_market_cap[-quintile:]]
        size_factor_short = [(i.Symbol,False) for i in top_by_market_cap[:quintile]]
        # Calculate last month's performance.
        if len(self.size_factor_symbols) != 0:
            monthly_return = self.CalculateFactorPerformance(self.data, self.size_factor_symbols)
            if monthly_return != 0:
                self.size_factor_vector.Add(monthly_return)
        # Store new factor symbols.
        self.size_factor_symbols = size_factor_long + size_factor_short
                
        # Value factor.
        sorted_by_pb = sorted(top_by_market_cap, key = lambda x:(x.ValuationRatios.PBRatio), reverse=False)
        quintile = int(len(sorted_by_pb) / 5)
        value_factor_long = [(i.Symbol,True) for i in sorted_by_pb[:quintile]]
        value_factor_short = [(i.Symbol,False) for i in sorted_by_pb[-quintile:]]
        # Calculate last month's performance.
        if len(self.value_factor_symbols) != 0:
            monthly_return = self.CalculateFactorPerformance(self.data, self.value_factor_symbols)
            if monthly_return != 0:
                self.value_factor_vector.Add(monthly_return)
        # Store new factor symbols.
        self.value_factor_symbols = value_factor_long + value_factor_short
            
        # Every factor vector is ready.
        if self.size_factor_vector.IsReady and self.value_factor_vector.IsReady:
            
            # Market factor.
            market_factor = []
            if self.symbol in self.data and self.data[self.symbol].IsReady:
                market_factor_prices = np.array([x for x in self.data[self.symbol]])
                market_factor = (market_factor_prices[:-1] - market_factor_prices[1:]) / market_factor_prices[1:]
            
                if len(market_factor) == (self.period - 1): 
                    # Residual return calc.
                    x = [
                        [x for x in market_factor], 
                        [x for x in self.size_factor_vector], 
                        [x for x in self.value_factor_vector]
                    ]
                    
                    standardized_residual_momentum = {}
                    for stock in top_by_market_cap:
                        symbol = stock.Symbol
                        if symbol in self.data and self.data[symbol].IsReady:
                            monthly_prices = np.array([x for x in self.data[symbol]])
                            monthly_returns = (monthly_prices[:-1] - monthly_prices[1:]) / monthly_prices[1:]
                            
                            regression_model = self.MultipleLinearRegression(x, monthly_returns)
                            alpha = regression_model.params[0]
                            
                            if symbol not in self.residual_return:
                                self.residual_return[symbol] = RollingWindow[float](self.residual_momentum_period)
                            self.residual_return[symbol].Add(alpha)
                            
                            # Residual data for 12 months is ready.
                            if self.residual_return[symbol].IsReady:
                                residual_returns = [x for x in self.residual_return[symbol]]
                                standardized_residual_momentum[symbol] = sum(residual_returns) / np.std(residual_returns)
        
                    sorted_by_resid_momentum = sorted(standardized_residual_momentum.items(), key = lambda x: x[1], reverse=True)
                    decile = int(len(sorted_by_resid_momentum) / 10)
                    self.long = [x[0] for x in sorted_by_resid_momentum[:decile]]
                    self.short = [x[0] for x in sorted_by_resid_momentum[-decile:]]
 
        return self.long + self.short
    
    def OnData(self, data):
        if self.Time.month != self.last_month:
            self.last_month = self.Time.month
            self.selection_flag = True
            return
        
        if not self.selection_flag:
            return
        self.selection_flag = False
        
        # Trade execution.
        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.long + self.short:
                self.Liquidate(symbol)

        for symbol in self.long:
            self.SetHoldings(symbol, 1 / len(self.long))
        for symbol in self.short:
            self.SetHoldings(symbol, -1 / len(self.short))
        
        self.long.clear()
        self.short.clear()

    def CalculateFactorPerformance(self, data, factor_symbols):
        monthly_return = 0
        if len(factor_symbols) != 0:
            for symbol, long_flag in factor_symbols:
                if symbol in data and data[symbol].Count >= 2:
                    closes = [x for x in data[symbol]]
                    if long_flag:
                        monthly_return += ((closes[0] / closes[1] - 1) / len(factor_symbols))
                    else:
                        monthly_return -= ((closes[0] / closes[1] - 1) / len(factor_symbols))

        return monthly_return

    def MultipleLinearRegression(self, x, y):
        x = np.array(x).T
        x = sm.add_constant(x)
        result = sm.OLS(endog=y, exog=x).fit()
        return result

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))