# region imports
from AlgorithmImports import *

# endregion
# Custom fee model
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))


# Quandl "value" data
class QuandlValue(PythonQuandl):
    def __init__(self):
        self.ValueColumnName = "Value"


# Quantpedia data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaFutures(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource(
            "data.quantpedia.com/backtesting_data/futures/{0}.csv".format(
                config.Symbol.Value
            ),
            SubscriptionTransportMedium.RemoteFile,
            FileFormat.Csv,
        )

    def Reader(self, config, line, date, isLiveMode):
        data = QuantpediaFutures()
        data.Symbol = config.Symbol

        if not line[0].isdigit():
            return None
        split = line.split(";")

        data.Time = datetime.strptime(split[0], "%d.%m.%Y") + timedelta(days=1)
        data["back_adjusted"] = float(split[1])
        data["spliced"] = float(split[2])
        data.Value = float(split[1])

        return data


# https://quantpedia.com/strategies/currency-momentum-factor/
#
# Create an investment universe consisting of several currencies (10-20). Go long three currencies with the highest 12-month momentum against USD
# and go short three currencies with the lowest 12-month momentum against USD. Cash not used as margin invest on overnight rates. Rebalance monthly.

import data_tools
from AlgorithmImports import *


class CurrencyMomentumFactor(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.data = {}
        self.period = 12 * 21
        self.SetWarmUp(self.period, Resolution.Daily)

        self.symbols = [
            "CME_AD1",  # Australian Dollar Futures, Continuous Contract #1
            "CME_BP1",  # British Pound Futures, Continuous Contract #1
            "CME_CD1",  # Canadian Dollar Futures, Continuous Contract #1
            "CME_EC1",  # Euro FX Futures, Continuous Contract #1
            "CME_JY1",  # Japanese Yen Futures, Continuous Contract #1
            "CME_MP1",  # Mexican Peso Futures, Continuous Contract #1
            "CME_NE1",  # New Zealand Dollar Futures, Continuous Contract #1
            "CME_SF1",  # Swiss Franc Futures, Continuous Contract #1
        ]

        for symbol in self.symbols:
            data = self.AddData(data_tools.QuantpediaFutures, symbol, Resolution.Daily)
            data.SetFeeModel(data_tools.CustomFeeModel())
            data.SetLeverage(5)
            self.data[symbol] = self.ROC(symbol, self.period, Resolution.Daily)

        self.recent_month = -1

    def OnData(self, data):
        if self.IsWarmingUp:
            return

        # rebalance monthly
        if self.Time.month == self.recent_month:
            return
        self.recent_month = self.Time.month

        perf = {
            x[0]: x[1].Current.Value
            for x in self.data.items()
            if self.data[x[0]].IsReady and x[0] in data and data[x[0]]
        }

        long = []
        short = []
        if len(perf) >= 6:
            sorted_by_performance = sorted(
                perf.items(), key=lambda x: x[1], reverse=True
            )
            long = [x[0] for x in sorted_by_performance[:3]]
            short = [x[0] for x in sorted_by_performance[-3:]]

        # trade execution
        invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
        for symbol in invested:
            if symbol not in long + short:
                self.Liquidate(symbol)

        for symbol in long:
            self.SetHoldings(symbol, 1 / len(long))
        for symbol in short:
            self.SetHoldings(symbol, -1 / len(short))
