# https://quantpedia.com/strategies/momentum-factor-effect-in-stocks/
#
# The investment universe consists of NYSE, AMEX, and NASDAQ stocks. We define momentum as the past 12-month return, skipping the most 
# recent month’s return (to avoid microstructure and liquidity biases). To capture “momentum”, UMD portfolio goes long stocks that have 
# high relative past one-year returns and short stocks that have low relative past one-year returns.
#
# QC implementation changes:
#   - Instead of all listed stock, we select top 500 stocks by market cap from QC stock universe.
    
from AlgorithmImports import *

class MomentumFactorEffectinStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.weight = {}
        self.data = {}
        self.period = 12 * 21
        self.quantile = 5
        
        self.coarse_count = 500
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(self.DateRules.MonthStart(symbol), self.TimeRules.AfterMarketOpen(symbol), self.Selection)

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
                self.data[symbol].Add(stock.AdjustedPrice)

        if not self.selection_flag:
            return Universe.Unchanged
        
        # selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa' and x.Price > 5]
        selected = [x.Symbol
            for x in sorted([x for x in coarse if x.HasFundamentalData and x.Market == 'usa'],
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
        fine = [x for x in fine if x.MarketCap != 0 and \
                    ((x.SecurityReference.ExchangeId == "NYS") or (x.SecurityReference.ExchangeId == "NAS") or (x.SecurityReference.ExchangeId == "ASE"))]
                    
        # if len(fine) > self.coarse_count:
        #     sorted_by_market_cap = sorted(fine, key = lambda x:x.MarketCap, reverse=True)
        #     top_by_market_cap = [x for x in sorted_by_market_cap[:self.coarse_count]]
        # else:
        #     top_by_market_cap = fine

        perf = {x.Symbol : self.data[x.Symbol][0] / self.data[x.Symbol][self.period-1] - 1 for x in fine}

        if len(perf) >= self.quantile:
            sorted_by_perf = sorted(perf.items(), key = lambda x:x[1], reverse=True)
            quantile = int(len(sorted_by_perf) / self.quantile)
            long = [x[0] for x in sorted_by_perf[:quantile]]
            short = [x[0] for x in sorted_by_perf[-quantile:]]

            long_count = len(long)
            short_count = len(short)

            for symbol in long:
                self.weight[symbol] = 1 / long_count
            for symbol in short:
                self.weight[symbol] = -1 / short_count
        
        return list(self.weight.keys())
        
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
            if symbol in data and data[symbol]:
                self.SetHoldings(symbol, w)

        self.weight.clear()
        
    def Selection(self):
        self.selection_flag = True

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))