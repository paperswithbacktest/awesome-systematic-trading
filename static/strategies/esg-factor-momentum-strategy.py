#region imports
from AlgorithmImports import *
#endregion
# https://quantpedia.com/strategies/esg-factor-momentum-strategy/
#
# The investment universe consists of stocks in the MSCI World Index. Paper uses MSCI ESG Ratings as the ESG database.
# The ESG Momentum strategy is built by overweighting, relative to the MSCI World Index, companies that increased their
# ESG ratings most during the recent past and underweight those with decreased ESG ratings, where the increases and decreases
# are based on a 12-month ESG momentum. The paper uses the Barra Global Equity Model (GEM3) for portfolio construction with 
# constraints that can be found in Appendix 2. Therefore, this strategy is very specific, but we aim to present the idea, not 
# the portfolio construction. The strategy is rebalanced monthly.
#
# QC implementation:
#   - Universe consists of ~700 stocks with ESG score data.

from numpy import floor

class ESGFactorMomentumStrategy(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2009, 6, 1)
        self.SetEndDate(2019, 12, 31)
        self.SetCash(100000)
        
        # Decile weighting.
        # True - Value weighted
        # False - Equally weighted
        self.value_weighting = True
        
        self.symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.esg_data = self.AddData(ESGData, 'ESG', Resolution.Daily)
        self.tickers = []
        
        self.holding_period = 3
        self.managed_queue = []

        # Monthly ESG decile data.
        self.esg = {}
        self.period = 14
        
        self.latest_price = {}
        
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
    
    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel(self))
            security.SetLeverage(10)
    
    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged
        
        self.latest_price.clear()
        
        selected = [x for x in coarse if (x.Symbol.Value).lower() in self.tickers]
        
        for stock in selected:
            symbol = stock.Symbol
            self.latest_price[symbol] = stock.AdjustedPrice

        return [x.Symbol for x in selected]
    
    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0]

        momentum = {}
        
        # Momentum calc.
        for stock in fine:
            symbol = stock.Symbol
            ticker = symbol.Value
            # ESG data for 14 months is ready.
            if ticker in self.esg and self.esg[ticker].IsReady:
                esg_data = [x for x in self.esg[ticker]]
                
                esg_decile_2_months_ago = esg_data[1]
                esg_decile_14_months_ago = esg_data[13]
                
                if esg_decile_14_months_ago != 0 and esg_decile_2_months_ago != 0:
                    # Momentum as difference.
                    # momentum_ = esg_decile_2_months_ago - esg_decile_14_months_ago
                    
                    # Momentum as ratio.
                    momentum_ = (esg_decile_2_months_ago / esg_decile_14_months_ago) - 1
                    
                    # Store momentum/market cap pair.
                    momentum[stock] = momentum_
                
        # Momentum sorting.
        sorted_by_momentum = sorted(momentum.items(), key = lambda x: x[1], reverse = True)
        decile = int(len(sorted_by_momentum) / 10)
        long = [x[0] for x in sorted_by_momentum[:decile]]
        short = [x[0] for x in sorted_by_momentum[-decile:]]
        
        long_symbol_q = []
        short_symbol_q = []
        
        # ew
        if not self.value_weighting:
            if len(long) != 0:
                long_w = self.Portfolio.TotalPortfolioValue / self.holding_period / len(long)
                long_symbol_q = [(x.Symbol, floor(long_w / self.latest_price[x.Symbol])) for x in long]
            
            if len(short) != 0:
                short_w = self.Portfolio.TotalPortfolioValue / self.holding_period / len(short)
                short_symbol_q = [(x.Symbol, -floor(short_w / self.latest_price[x.Symbol])) for x in short]
        # vw
        else:
            if len(long) != 0:
                total_market_cap_long = sum([x.MarketCap for x in long])
                long_w = self.Portfolio.TotalPortfolioValue / self.holding_period
                long_symbol_q = [(x.Symbol, floor((long_w * (x.MarketCap / total_market_cap_long))) / self.latest_price[x.Symbol]) for x in long]
            
            short_symbol_q = []
            if len(short) != 0:
                total_market_cap_short = sum([x.MarketCap for x in short])
                short_w = self.Portfolio.TotalPortfolioValue / self.holding_period
                short_symbol_q = [(x.Symbol, -floor((short_w * (x.MarketCap / total_market_cap_short))) / self.latest_price[x.Symbol]) for x in short]
        
        self.managed_queue.append(RebalanceQueueItem(long_symbol_q + short_symbol_q))
        
        return [x.Symbol for x in long + short]
    
    def OnData(self, data):
        new_data_arrived = False
        
        if 'ESG' in data and data['ESG']:
            # Store universe tickers.
            if len(self.tickers) == 0:
                # TODO '_typename' in storage dictionary?
                self.tickers = [x.Key for x in self.esg_data.GetLastData().GetStorageDictionary()][:-1]
        
            # Store history for every ticker.
            for ticker in self.tickers:
                ticker_u = ticker.upper()
                if ticker_u not in self.esg:
                    self.esg[ticker_u] = RollingWindow[float](self.period)
                
                decile = self.esg_data.GetLastData()[ticker]
                self.esg[ticker_u].Add(decile)
                
                # trigger selection after new esg data arrived.
                if not self.selection_flag:
                    new_data_arrived = True
        
        if new_data_arrived:
            self.selection_flag = True
            return
        
        if not self.selection_flag:
            return
        self.selection_flag = False

        # Trade execution
        remove_item = None
        
        # Rebalance portfolio
        for item in self.managed_queue:
            if item.holding_period == self.holding_period:
                for symbol, quantity in item.symbol_q:
                    if quantity >= 1:
                        self.MarketOrder(symbol, -quantity)
                            
                remove_item = item
                
            elif item.holding_period == 0:
                open_symbol_q = []
                
                for symbol, quantity in item.symbol_q:
                    if quantity >= 1:
                        if self.Securities[symbol].Price != 0 and self.Securities[symbol].IsTradable:
                            self.MarketOrder(symbol, quantity)
                            open_symbol_q.append((symbol, quantity))
                            
                # Only opened orders will be closed        
                item.symbol_q = open_symbol_q
                
            item.holding_period += 1
            
        if remove_item:
            self.managed_queue.remove(remove_item)

class RebalanceQueueItem():
    def __init__(self, symbol_q):
        # symbol/quantity collections
        self.symbol_q = symbol_q  
        self.holding_period = 0

# ESG data.
class ESGData(PythonData):
    def __init__(self):
        self.tickers = []
    
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/economic/esg_deciles_data.csv", SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)
    
    def Reader(self, config, line, date, isLiveMode):
        data = ESGData()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit():
            self.tickers = [x for x in line.split(';')][1:]
            return None
            
        split = line.split(';')
        
        data.Time = datetime.strptime(split[0], "%Y-%m-%d") + timedelta(days=1)

        index = 1
        for ticker in self.tickers:
            data[ticker] = float(split[index])
            index += 1
            
        data.Value = float(split[1])
        return data
        
# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))