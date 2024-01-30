from AlgorithmImports import *

import numpy as np
from scipy.optimize import minimize
import statsmodels.api as sm

sp100_stocks = ['AAPL','MSFT','AMZN','FB','BRKB','GOOGL','GOOG','JPM','JNJ','V','PG','XOM','UNH','BAC','MA','T','DIS','INTC','HD','VZ','MRK','PFE','CVX','KO','CMCSA','CSCO','PEP','WFC','C','BA','ADBE','WMT','CRM','MCD','MDT','BMY','ABT','NVDA','NFLX','AMGN','PM','PYPL','TMO','COST','ABBV','ACN','HON','NKE','UNP','UTX','NEE','IBM','TXN','AVGO','LLY','ORCL','LIN','SBUX','AMT','LMT','GE','MMM','DHR','QCOM','CVS','MO','LOW','FIS','AXP','BKNG','UPS','GILD','CHTR','CAT','MDLZ','GS','USB','CI','ANTM','BDX','TJX','ADP','TFC','CME','SPGI','COP','INTU','ISRG','CB','SO','D','FISV','PNC','DUK','SYK','ZTS','MS','RTN','AGN','BLK']

def MonthDiff(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def Return(values):
    return (values[-1] - values[0]) / values[0]
    
def Volatility(values):
    values = np.array(values)
    returns = (values[1:] - values[:-1]) / values[:-1]
    return np.std(returns)  

def MultipleLinearRegression(x, y):
    x = np.array(x).T
    x = sm.add_constant(x)
    result = sm.OLS(endog=y, exog=x).fit()
    return result
    
# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))

# Quandl free data
class QuandlFutures(PythonQuandl):
    def __init__(self):
        self.ValueColumnName = "settle"

# Quandl "value" data
class QuandlValue(PythonQuandl):
    def __init__(self):
        self.ValueColumnName = 'Value'

# Quandl short interest data.
class QuandlFINRA_ShortVolume(PythonQuandl):
    def __init__(self):
        self.ValueColumnName = 'SHORTVOLUME'    # also 'TOTALVOLUME' is accesible

# Commitments of Traders data.
# NOTE: IMPORTANT: Data order must be ascending (datewise).
# Data source: https://commitmentsoftraders.org/cot-data/
# Data description: https://commitmentsoftraders.org/wp-content/uploads/Static/CoTData/file_key.html
class CommitmentsOfTraders(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/futures/cot/{0}.PRN".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    # File example.
    # DATE   OPEN     HIGH        LOW       CLOSE     VOLUME   OI
    # ----   ----     ----        ---       -----     ------   --
    # DATE   LARGE    SPECULATOR  COMMERCIAL HEDGER   SMALL TRADER
    #        LONG     SHORT       LONG      SHORT     LONG     SHORT
    def Reader(self, config, line, date, isLiveMode):
        data = CommitmentsOfTraders()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(',')
        
        # Prevent lookahead bias.
        data.Time = datetime.strptime(split[0], "%Y%m%d") + timedelta(days=1)
        
        data['LARGE_SPECULATOR_LONG'] = int(split[1])
        data['LARGE_SPECULATOR_SHORT'] = int(split[2])
        data['COMMERCIAL_HEDGER_LONG'] = int(split[3])
        data['COMMERCIAL_HEDGER_SHORT'] = int(split[4])
        data['SMALL_TRADER_LONG'] = int(split[5])
        data['SMALL_TRADER_SHORT'] = int(split[6])
        data['open_interest'] = int(split[1]) + int(split[2]) + int(split[3]) + int(split[4]) + int(split[5]) + int(split[6])
        data.Value = int(split[1])

        return data

# Quantpedia bond yield data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaIndices(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/index/{0}.csv".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    def Reader(self, config, line, date, isLiveMode):
        data = QuantpediaIndices()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(',')
        
        data.Time = datetime.strptime(split[0], "%Y-%m-%d") + timedelta(days=1)
        data['close'] = float(split[1])
        data.Value = float(split[1])

        return data

# Quantpedia bond yield data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaBondYield(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/bond_yield/{0}.csv".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    def Reader(self, config, line, date, isLiveMode):
        data = QuantpediaBondYield()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(',')
        
        data.Time = datetime.strptime(split[0], "%Y-%m-%d") + timedelta(days=1)
        data['yield'] = float(split[1])
        data.Value = float(split[1])

        return data

# Quantpedia data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaFutures(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/futures/{0}.csv".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    def Reader(self, config, line, date, isLiveMode):
        data = QuantpediaFutures()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(';')
        
        data.Time = datetime.strptime(split[0], "%d.%m.%Y") + timedelta(days=1)
        data['back_adjusted'] = float(split[1])
        data['spliced'] = float(split[2])
        data.Value = float(split[1])

        return data

# Commitments of Traders data.
# NOTE: IMPORTANT: Data order must be ascending (datewise).
# Data source: https://commitmentsoftraders.org/cot-data/
# Data description: https://commitmentsoftraders.org/wp-content/uploads/Static/CoTData/file_key.html
class CommitmentsOfTraders(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/futures/cot/{0}.PRN".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    # File example.
    # DATE   OPEN     HIGH        LOW       CLOSE     VOLUME   OI
    # ----   ----     ----        ---       -----     ------   --
    # DATE   LARGE    SPECULATOR  COMMERCIAL HEDGER   SMALL TRADER
    #        LONG     SHORT       LONG      SHORT     LONG     SHORT
    def Reader(self, config, line, date, isLiveMode):
        data = CommitmentsOfTraders()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(',')
        
        # Prevent lookahead bias.
        data.Time = datetime.strptime(split[0], "%Y%m%d") + timedelta(days=1)
        
        data['LARGE_SPECULATOR_LONG'] = int(split[1])
        data['LARGE_SPECULATOR_SHORT'] = int(split[2])
        data['COMMERCIAL_HEDGER_LONG'] = int(split[3])
        data['COMMERCIAL_HEDGER_SHORT'] = int(split[4])
        data['SMALL_TRADER_LONG'] = int(split[5])
        data['SMALL_TRADER_SHORT'] = int(split[6])

        data.Value = int(split[1])

        return data
        
# NOTE: Manager for new trades. It's represented by certain count of equally weighted brackets for long and short positions.
# If there's a place for new trade, it will be managed for time of holding period.
class TradeManager():
    def __init__(self, algorithm, long_size, short_size, holding_period):
        self.algorithm = algorithm  # algorithm to execute orders in.
        
        self.long_size = long_size
        self.short_size = short_size
        
        self.long_len = 0
        self.short_len = 0
    
        # Arrays of ManagedSymbols
        self.symbols = []
        
        self.holding_period = holding_period    # Days of holding.
    
    # Add stock symbol object
    def Add(self, symbol, long_flag):
        # Open new long trade.
        managed_symbol = ManagedSymbol(symbol, self.holding_period, long_flag)
        
        if long_flag:
            # If there's a place for it.
            if self.long_len < self.long_size:
                self.symbols.append(managed_symbol)
                self.algorithm.SetHoldings(symbol, 1 / self.long_size)
                self.long_len += 1
            else:
                self.algorithm.Log("There's not place for additional trade.")

        # Open new short trade.
        else:
            # If there's a place for it.
            if self.short_len < self.short_size:
                self.symbols.append(managed_symbol)
                self.algorithm.SetHoldings(symbol, - 1 / self.short_size)
                self.short_len += 1
            else:
                self.algorithm.Log("There's not place for additional trade.")
   
    # Decrement holding period and liquidate symbols.
    def TryLiquidate(self):
        symbols_to_delete = []
        for managed_symbol in self.symbols:
            managed_symbol.days_to_liquidate -= 1
            
            # Liquidate.
            if managed_symbol.days_to_liquidate == 0:
                symbols_to_delete.append(managed_symbol)
                self.algorithm.Liquidate(managed_symbol.symbol)
                
                if managed_symbol.long_flag: self.long_len -= 1
                else: self.short_len -= 1

        # Remove symbols from management.
        for managed_symbol in symbols_to_delete:
            self.symbols.remove(managed_symbol)
    
    def LiquidateTicker(self, ticker):
        symbol_to_delete = None
        for managed_symbol in self.symbols:
            if managed_symbol.symbol.Value == ticker:
                self.algorithm.Liquidate(managed_symbol.symbol)
                symbol_to_delete = managed_symbol
                if managed_symbol.long_flag: self.long_len -= 1
                else: self.short_len -= 1
                
                break
        
        if symbol_to_delete: self.symbols.remove(symbol_to_delete)
        else: self.algorithm.Debug("Ticker is not held in portfolio!")
    
class ManagedSymbol():
    def __init__(self, symbol, days_to_liquidate, long_flag):
        self.symbol = symbol
        self.days_to_liquidate = days_to_liquidate
        self.long_flag = long_flag
        
class PortfolioOptimization(object):
    def __init__(self, df_return, risk_free_rate, num_assets):
        self.daily_return = df_return
        self.risk_free_rate = risk_free_rate
        self.n = num_assets # numbers of risk assets in portfolio
        self.target_vol = 0.05

    def annual_port_return(self, weights):
        # calculate the annual return of portfolio
        return np.sum(self.daily_return.mean() * weights) * 252

    def annual_port_vol(self, weights):
        # calculate the annual volatility of portfolio
        return np.sqrt(np.dot(weights.T, np.dot(self.daily_return.cov() * 252, weights)))

    def min_func(self, weights):
        # method 1: maximize sharp ratio
        return - self.annual_port_return(weights) / self.annual_port_vol(weights)
        
        # method 2: maximize the return with target volatility
        #return - self.annual_port_return(weights) / self.target_vol

    def opt_portfolio(self):
        # maximize the sharpe ratio to find the optimal weights
        cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bnds = tuple((0, 1) for x in range(2)) + tuple((0, 0.25) for x in range(self.n - 2))
        opt = minimize(self.min_func,                               # object function
                       np.array(self.n * [1. / self.n]),            # initial value
                       method='SLSQP',                              # optimization method
                       bounds=bnds,                                 # bounds for variables 
                       constraints=cons)                            # constraint conditions
                      
        opt_weights = opt['x']
 
        return opt_weights


# https://quantpedia.com/strategies/crude-oil-predicts-equity-returns/
#
# Several types of oil can be used (Brent, WTI, Dubai etc.) without big differences in results. The source paper for
# this anomaly uses Arab Light crude oil. Monthly oil returns are used in the regression equation as an independent
# variable and equity returns are used as a dependent variable. The model is re-estimated every month and
# observations of the last month are added. The investor determines whether the expected stock market return in 
# a specific month (based on regression results and conditional on the oil price change in the previous month) is higher
# or lower than the risk-free rate. The investor is fully invested in the market portfolio if the expected
# return is higher (bull market); he invests in cash if the expected return is lower (bear market).

from data_tools import QuantpediaFutures, QuandlValue, CustomFeeModel
from AlgorithmImports import *
import numpy as np
from collections import deque
from scipy import stats

class CrudeOilPredictsEquityReturns(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.data = {}

        self.symbols = [
            "CME_ES1",  # E-mini S&P 500 Futures, Continuous Contract #1
            "CME_CL1"   # Crude Oil Futures, Continuous Contract #1
        ]
        
        self.cash = self.AddEquity('SHY', Resolution.Daily).Symbol
        
        self.risk_free_rate = self.AddData(QuandlValue, 'FRED/DGS3MO', Resolution.Daily).Symbol
        
        # Monhtly price data.
        self.data = {}
        
        for symbol in self.symbols:
            data = self.AddData(QuantpediaFutures, symbol, Resolution.Daily)
            data.SetLeverage(5)
            data.SetFeeModel(CustomFeeModel())
            self.data[symbol] = deque()
        
        self.recent_month = -1

    def OnData(self, data):
        rebalance_flag = False
        
        for symbol in self.symbols:
            if symbol in data:
                if self.recent_month != self.Time.month:
                    rebalance_flag = True
                    
                if data[symbol]:
                    price = data[symbol].Value
                    self.data[symbol].append(price)

        if rebalance_flag:
            self.recent_month = self.Time.month
        
        rf_rate = 0
        if self.Securities[self.risk_free_rate].GetLastData() and (self.Time.date() - self.Securities[self.risk_free_rate].GetLastData().Time.date()).days < 5:
            rf_rate = self.Securities[self.risk_free_rate].Price
        else:
            return
            
        if self.Securities[self.cash].GetLastData() and (self.Time.date() - self.Securities[self.cash].GetLastData().Time.date()).days >= 5:
            return
            
        market_prices = np.array(self.data[self.symbols[0]])
        oil_prices = np.array(self.data[self.symbols[1]])
        
        # At least one year of data is ready.
        if len(market_prices) < 13 or len(oil_prices) < 13:
            return
        
        # Trim price series lengths.
        min_size = min(len(market_prices), len(oil_prices))
        market_prices = market_prices[-min_size:]
        oil_prices = oil_prices[-min_size:]
        
        market_returns = (market_prices[1:] - market_prices[:-1]) / market_prices[:-1]
        oil_returns = (oil_prices[1:] - oil_prices[:-1]) / oil_prices[:-1]
        
        # Simple Linear Regression
        # Y = C + (M * X)
        # Y = α + (β ∗ X)

        # Y = Dependent variable (output/outcome/prediction/estimation)
        # C/α = Constant (Y-Intercept)
        # M/β = Slope of the regression line (the effect that X has on Y)
        # X = Independent variable (input variable used in the prediction of Y)

        slope, intercept, r_value, p_value, std_err = stats.linregress(oil_returns[:-1], market_returns[1:])
        X = oil_returns[-1]
        expected_market_return = intercept + (slope * X)
        
        if expected_market_return > rf_rate:
            self.SetHoldings(self.symbols[0], 1)
        else:
            if self.Securities[self.cash].Price != 0:
                self.SetHoldings(self.cash, 1)