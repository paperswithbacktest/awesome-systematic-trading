# https://quantpedia.com/strategies/12-month-cycle-in-cross-section-of-stocks-returns/
#
# The top 30% of firms based on their market cap from NYSE and AMEX are part of the investment universe. Every month, stocks are grouped 
# into ten portfolios (with an equal number of stocks in each portfolio) according to their performance in one month one year ago. Investors
# go long in stocks from the winner decile and shorts stocks from the loser decile. The portfolio is equally weighted and rebalanced every month.
#
# QC implementation changes:
#   - Universe consists of top 3000 US stock by market cap from NYSE, AMEX and NASDAQ.
#   - Portfolio is value weighted.

from AlgorithmImports import *

class Month12CycleinCrossSectionofStocksReturns(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)  
        self.SetCash(100000)

        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.coarse_count = 500
        
        # Monthly close data.
        self.data = {}
        self.period = 13
        
        self.weight = {}

        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        
        self.Schedule.On(self.DateRules.MonthEnd(self.symbol), self.TimeRules.BeforeMarketClose(self.symbol), self.Selection)

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(10)
            
    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged

        # Update the rolling window every month.
        for stock in coarse:
            symbol = stock.Symbol

            # Store monthly price.
            if symbol in self.data:
                self.data[symbol].update(stock.AdjustedPrice)

        # selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa']
        selected = [x.Symbol
            for x in sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa'],
                key = lambda x: x.DollarVolume, reverse = True)[:self.coarse_count]]
        
        # Warmup price rolling windows.
        for symbol in selected:
            if symbol in self.data:
                continue
            
            self.data[symbol] = SymbolData(symbol, self.period)
            history = self.History(symbol, self.period*30, Resolution.Daily)
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
                        self.data[symbol].update(time_close[1])
            
        return [x for x in selected if self.data[x].is_ready()]    
        
    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0 and x.CompanyReference.IsREIT != 1 and  \
                    ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))]
                    
        if len(fine) > self.coarse_count:
            sorted_by_market_cap = sorted(fine, key = lambda x: x.MarketCap, reverse=True)
            top_by_market_cap = sorted_by_market_cap[:self.coarse_count]
        else:
            top_by_market_cap = fine

        # Performance sorting. One month performance, one year ago with market cap data.
        performance_market_cap = { x.Symbol : (self.data[x.Symbol].performance(), x.MarketCap) for x in top_by_market_cap if x.Symbol in self.data and self.data[x.Symbol].is_ready()}
        
        long = []
        short = []
        if len(performance_market_cap) >= 10:
            sorted_by_perf = sorted(performance_market_cap.items(), key = lambda x:x[1][0], reverse = True)
            decile = int(len(sorted_by_perf) / 10)
            long = [x for x in sorted_by_perf[:decile]]
            short = [x for x in sorted_by_perf[-decile:]]
        
        total_market_cap_long = sum([x[1][1] for x in long])
        for symbol, perf_market_cap in long:
            self.weight[symbol] = perf_market_cap[1] / total_market_cap_long

        total_market_cap_short = sum([x[1][1] for x in short])
        for symbol, perf_market_cap in short:
            self.weight[symbol] = perf_market_cap[1] / total_market_cap_short
        
        return [x[0] for x in self.weight.items()]

    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False
        
        # Trade execution.
        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.weight:
                self.Liquidate(symbol)
        
        for symbol, w in self.weight.items():
            self.SetHoldings(symbol, w)

        self.weight.clear()
    
    def Selection(self):
        self.selection_flag = True

class SymbolData():
    def __init__(self, symbol, period):
        self.Symbol = symbol
        self.Window = RollingWindow[float](period)
    
    def update(self, value):
        self.Window.Add(value)
    
    def is_ready(self):
        return self.Window.IsReady
        
    # One month performance, one year ago.
    def performance(self):
        values = [x for x in self.Window]
        return (values[-2] / values[-1] - 1)
        
# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))