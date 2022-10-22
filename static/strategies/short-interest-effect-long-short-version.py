# https://quantpedia.com/strategies/short-interest-effect-long-short-version/
#
# All stocks from NYSE, AMEX, and NASDAQ are part of the investment universe. Stocks are then sorted each month into short-interest deciles based on
# the ratio of short interest to shares outstanding. The investor then goes long on the decile with the lowest short ratio and short on the decile
# with the highest short ratio. The portfolio is rebalanced monthly, and stocks in the portfolio are weighted equally.

from AlgorithmImports import *


class ShortInterestEffect(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2010, 1, 1)
        self.SetCash(100000)

        # NOTE: We use only s&p 100 stocks so it's possible to fetch short interest data from quandl.
        self.symbols = [
            "AAPL",
            "MSFT",
            "AMZN",
            "FB",
            "GOOGL",
            "GOOG",
            "JPM",
            "JNJ",
            "V",
            "PG",
            "XOM",
            "UNH",
            "BAC",
            "MA",
            "T",
            "DIS",
            "INTC",
            "HD",
            "VZ",
            "MRK",
            "PFE",
            "CVX",
            "KO",
            "CMCSA",
            "CSCO",
            "PEP",
            "WFC",
            "C",
            "BA",
            "ADBE",
            "WMT",
            "CRM",
            "MCD",
            "MDT",
            "BMY",
            "ABT",
            "NVDA",
            "NFLX",
            "AMGN",
            "PM",
            "PYPL",
            "TMO",
            "COST",
            "ABBV",
            "ACN",
            "HON",
            "NKE",
            "UNP",
            "UTX",
            "NEE",
            "IBM",
            "TXN",
            "AVGO",
            "LLY",
            "ORCL",
            "LIN",
            "SBUX",
            "AMT",
            "LMT",
            "GE",
            "MMM",
            "DHR",
            "QCOM",
            "CVS",
            "MO",
            "LOW",
            "FIS",
            "AXP",
            "BKNG",
            "UPS",
            "GILD",
            "CHTR",
            "CAT",
            "MDLZ",
            "GS",
            "USB",
            "CI",
            "ANTM",
            "BDX",
            "TJX",
            "ADP",
            "TFC",
            "CME",
            "SPGI",
            "COP",
            "INTU",
            "ISRG",
            "CB",
            "SO",
            "D",
            "FISV",
            "PNC",
            "DUK",
            "SYK",
            "ZTS",
            "MS",
            "RTN",
            "AGN",
            "BLK",
        ]

        for symbol in self.symbols:
            data = self.AddEquity(symbol, Resolution.Daily)
            data.SetFeeModel(CustomFeeModel())
            data.SetLeverage(5)

            self.AddData(
                QuandlFINRA_ShortVolume, "FINRA/FNSQ_" + symbol, Resolution.Daily
            )

        self.recent_month = -1

    def OnData(self, data):
        if self.recent_month == self.Time.month:
            return
        self.recent_month = self.Time.month

        short_interest = {}
        for symbol in self.symbols:
            sym = "FINRA/FNSQ_" + symbol
            if sym in data and data[sym] and symbol in data and data[symbol]:
                short_vol = data[sym].GetProperty("SHORTVOLUME")
                total_vol = data[sym].GetProperty("TOTALVOLUME")

                short_interest[symbol] = short_vol / total_vol

        long = []
        short = []
        if len(short_interest) >= 10:
            sorted_by_short_interest = sorted(
                short_interest.items(), key=lambda x: x[1], reverse=True
            )
            decile = int(len(sorted_by_short_interest) / 10)
            long = [x[0] for x in sorted_by_short_interest[-decile:]]
            short = [x[0] for x in sorted_by_short_interest[:decile]]

        # trade execution
        stocks_invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in long + short:
                self.Liquidate(symbol)

        for symbol in long:
            if symbol in data and data[symbol]:
                self.SetHoldings(symbol, 1 / len(long))
        for symbol in short:
            if symbol in data and data[symbol]:
                self.SetHoldings(symbol, -1 / len(short))


class QuandlFINRA_ShortVolume(PythonQuandl):
    def __init__(self):
        self.ValueColumnName = "SHORTVOLUME"  # also 'TOTALVOLUME' is accesible


# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
