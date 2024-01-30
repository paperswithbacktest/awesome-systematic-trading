# region imports
from AlgorithmImports import *

# endregion
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


# Custom fee model.
class CustomFeeModel:
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))


# region imports
from AlgorithmImports import *

# endregion
# https://quantpedia.com/strategies/fx-carry-trade/
#
# Create an investment universe consisting of several currencies (10-20). Go long three currencies with the highest central bank prime rates and
# go short three currencies with the lowest central bank prime rates. The cash not used as the margin is invested in overnight rates. The strategy
# is rebalanced monthly.

import data_tools


class ForexCarryTrade(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        # Source: https://www.quandl.com/data/OECD-Organisation-for-Economic-Co-operation-and-Development
        self.symbols = {
            "CME_AD1": "OECD/KEI_IR3TIB01_AUS_ST_M",  # Australian Dollar Futures, Continuous Contract #1
            "CME_BP1": "OECD/KEI_IR3TIB01_GBR_ST_M",  # British Pound Futures, Continuous Contract #1
            "CME_CD1": "OECD/KEI_IR3TIB01_CAN_ST_M",  # Canadian Dollar Futures, Continuous Contract #1
            "CME_EC1": "OECD/KEI_IR3TIB01_EA19_ST_M",  # Euro FX Futures, Continuous Contract #1
            "CME_JY1": "OECD/KEI_IR3TIB01_JPN_ST_M",  # Japanese Yen Futures, Continuous Contract #1
            "CME_MP1": "OECD/KEI_IR3TIB01_MEX_ST_M",  # Mexican Peso Futures, Continuous Contract #1
            "CME_NE1": "OECD/KEI_IR3TIB01_NZL_ST_M",  # New Zealand Dollar Futures, Continuous Contract #1
            "CME_SF1": "SNB/ZIMOMA",  # Swiss Franc Futures, Continuous Contract #1
        }

        for symbol, rate_symbol in self.symbols.items():
            self.AddData(Quandl, rate_symbol, Resolution.Daily)

            data = self.AddData(data_tools.QuantpediaFutures, symbol, Resolution.Daily)
            data.SetFeeModel(data_tools.CustomFeeModel())
            data.SetLeverage(5)

        self.recent_month = -1

    def OnData(self, data):
        rebalance_flag: bool = False
        rate: dict[str, float] = {}

        for symbol, int_rate in self.symbols.items():
            # futures data is present in the algorithm
            if symbol in data and data[symbol]:
                if self.recent_month != self.Time.month:
                    rebalance_flag = True
                    self.recent_month = self.Time.month

                # IR data is still coming in
                if (
                    self.Securities[int_rate].GetLastData()
                    and (
                        self.Time.date()
                        - self.Securities[int_rate].GetLastData().Time.date()
                    ).days
                    <= 31
                ):
                    rate[symbol] = self.Securities[int_rate].Price

        if rebalance_flag:
            long = []
            short = []
            if len(rate) >= 3:
                # interbank rate sorting
                sorted_by_rate = sorted(rate.items(), key=lambda x: x[1], reverse=True)
                traded_count = 3
                long = [x[0] for x in sorted_by_rate[:traded_count]]
                short = [x[0] for x in sorted_by_rate[-traded_count:]]

            # trade execution
            invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
            for symbol in invested:
                if symbol not in long + short:
                    self.Liquidate(symbol)

            for symbol in long:
                self.SetHoldings(symbol, 1 / len(long))
            for symbol in short:
                self.SetHoldings(symbol, -1 / len(short))
