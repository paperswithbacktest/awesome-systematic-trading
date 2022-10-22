# https://quantpedia.com/strategies/trend-following-effect-in-stocks/
#
# The investment universe consists of US-listed companies. A minimum stock price filter is used to avoid penny stocks, and a minimum
# daily liquidity filter is used to avoid stocks that are not liquid enough. The entry signal occurs if today’s close is greater than
# or equal to the highest close during the stock’s entire history. A 10-period average true range trailing stop is used as an exit 
# signal. The investor holds all stocks which satisfy entry criterion and are not stopped out. The portfolio is equally weighted and
# rebalanced daily. Transaction costs of 0.5% round-turn are deducted from each trade to account for estimated commission and slippage.
#
# QC implementation:
#   - Universe consists of top 100 liquid US stocks. 

import numpy as np
from AlgorithmImports import *

class TrendFollowingStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2010, 1, 1)
        self.SetCash(100000)

        self.SetSecurityInitializer(lambda x: x.SetMarketPrice(self.GetLastKnownPrice(x)))
        
        self.course_count = 100
        self.long = []
        
        self.max_close = {}
        self.atr = {}
        
        self.sl_order = {}
        self.sl_price = {}
        
        self.selection = []
        self.period = 10*12*21
        
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction)
    
    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            
            symbol = security.Symbol
            if symbol not in self.atr:
                self.atr[symbol] = self.ATR(symbol, 10, Resolution.Daily)
                
            if symbol not in self.max_close:
                hist = self.History([self.Symbol(symbol)], self.period, Resolution.Daily)
                if 'close' in hist.columns:
                    closes = hist['close']
                    self.max_close[symbol] = max(closes)
            
    def CoarseSelectionFunction(self, coarse):
        if self.IsWarmingUp: return
    
        selected = sorted([x for x in coarse if x.HasFundamentalData and x.Price > 5],
            key=lambda x: x.DollarVolume, reverse=True)
        
        self.selection = [x.Symbol for x in selected[:self.course_count]]
        
        return self.selection

    def OnData(self, data):
        if self.IsWarmingUp:
            return

        for symbol in self.selection:
            if symbol in data.Bars:
                price = data[symbol].Value
            
                if symbol not in self.max_close: continue
            
                if price >= self.max_close[symbol]:
                    self.max_close[symbol] = price
                    self.long.append(symbol)

        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        count = len(self.long) + len(stocks_invested)
        if count == 0: return
    
        # Update stoploss orders
        for symbol in stocks_invested:
            if not self.Securities[symbol].IsTradable:
                self.Liquidate(symbol)
                
            if self.atr[symbol].Current.Value == 0: continue
            
            # Move SL
            if symbol not in self.sl_price: continue
            
            self.SetHoldings(symbol, 1 / count)
            
            new_sl = self.Securities[symbol].Price - self.atr[symbol].Current.Value
            if new_sl > self.sl_price[symbol]:
                update_order_fields = UpdateOrderFields()
                update_order_fields.StopPrice = new_sl      # Update SL price
                
                quantity = self.CalculateOrderQuantity(symbol, (1 / count))
                update_order_fields.Quantity = quantity     # Update SL quantity

                self.sl_price[symbol] = new_sl
                self.sl_order[symbol].Update(update_order_fields)
                # self.Log('SL MOVED on ' + str(symbol) + ' to: ' + str(new_sl))

        # Open new trades
        for symbol in self.long:
            if not self.Portfolio[symbol].Invested and self.atr[symbol].Current.Value != 0:
                price = data[symbol].Value
                if self.Securities[symbol].IsTradable:
                    unit_size = self.CalculateOrderQuantity(symbol, (1 / count))
                    
                    self.MarketOrder(symbol, unit_size)
                    
                    sl_price = price - self.atr[symbol].Current.Value
                    self.sl_price[symbol] = sl_price
                    if unit_size != 0:
                        self.sl_order[symbol] = self.StopMarketOrder(symbol, -unit_size, sl_price, 'SL')
                    # self.Log('SL SET on ' + str(symbol) + ' to: ' + str(sl_price))

        self.long.clear()

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))