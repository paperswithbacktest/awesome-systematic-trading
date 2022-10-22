# https://quantpedia.com/strategies/soccer-clubs-stocks-arbitrage/
#
# The investment universe consists of liquid soccer clubs’ stocks that are publicly traded.
# The investor then sells short stocks of clubs that play UEFA Championship matches (or other important matches)
# at the end of the business day before the match. Stocks are held for one day,
# and the portfolio of stocks is equally weighted (if there are multiple clubs with matches that day).
#
# QC Implementation:

#region imports
from AlgorithmImports import *
#endregion

class SoccerClubsStocksArbitrage(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)
        
        self.tickers = [
            'FCPP',  # Futebol Clube Do Porto
            'SPSO',  # Sporting Clube De Portugal
            'SLBEN', # Benfica
            'LAZI',  # Lazio
            'ASR',   # AS Rome
            'AJAX',  # AJAX
            'JUVE',  # Juventus
            'MANU',  # Manchester United
            'BVB',   # Dortmund
            'CCP',   # Celtic
            # 'BOLA' # Bali Bintang Sejahtera Tbk PT
        ]
        
        self.match_dates = {}
        
        for ticker in self.tickers:
            security = self.AddData(QuantpediaSoccer, ticker, Resolution.Daily)
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(5)
            
        csv_string_file = self.Download('data.quantpedia.com/backtesting_data/equity/soccer/soccer_matches.csv')
        lines = csv_string_file.split('\r\n')
        for line in lines:
            line_split = line.split(';')
            date = datetime.strptime(line_split[0], "%d.%m.%Y").date()
            
            self.match_dates[date] = []
            for i in range(1, len(line_split)):
                ticker = line_split[i]
                self.match_dates[date].append(ticker)
        
    def OnData(self, data):
        self.Liquidate()
        
        short = []
        
        # Looking for todays date, because only daily closes are traded.
        today = (self.Time - timedelta(days=1)).date()
        
        if today in self.match_dates:
            for ticker in self.tickers:
                if ticker in self.match_dates[today] and ticker in data:
                    short.append(ticker)
                    
        for ticker in short:
            self.SetHoldings(ticker, -1 / len(short))

# Quantpedia data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaSoccer(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/equity/soccer/{0}.csv".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    def Reader(self, config, line, date, isLiveMode):
        data = QuantpediaSoccer()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(';')
        
        data.Time = datetime.strptime(split[0], "%d.%m.%Y") + timedelta(days=1)
        data['price'] = float(split[1])
        data.Value = float(split[1])

        return data

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))