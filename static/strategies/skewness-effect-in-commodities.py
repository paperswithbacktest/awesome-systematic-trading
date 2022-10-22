# https://quantpedia.com/strategies/skewness-effect-in-commodities/
#
# The investment universe consists of 27 futures contracts on commodities. Each month, investor calculates skewness (3rd moment of returns)
# from daily returns from data going 12 months into the past for all futures. Commodities are then sorted into quintiles and investor goes
# long quintile containing the commodities with the 20% lowest total skewness and short quintile containing the commodities with the 20% highest
# total skewness (over a ranking period of 12 months). The resultant portfolio is equally weighted and rebalanced each month.

import numpy as np
from AlgorithmImports import *
from scipy.stats import skew


class SkewnessEffect(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.symbols = [
            "CME_S1",  # Soybean Futures, Continuous Contract
            "CME_W1",  # Wheat Futures, Continuous Contract
            "CME_SM1",  # Soybean Meal Futures, Continuous Contract
            "CME_BO1",  # Soybean Oil Futures, Continuous Contract
            "CME_C1",  # Corn Futures, Continuous Contract
            "CME_O1",  # Oats Futures, Continuous Contract
            "CME_LC1",  # Live Cattle Futures, Continuous Contract
            "CME_FC1",  # Feeder Cattle Futures, Continuous Contract
            "CME_LN1",  # Lean Hog Futures, Continuous Contract
            "CME_GC1",  # Gold Futures, Continuous Contract
            "CME_SI1",  # Silver Futures, Continuous Contract
            "CME_PL1",  # Platinum Futures, Continuous Contract
            "CME_CL1",  # Crude Oil Futures, Continuous Contract
            "CME_HG1",  # Copper Futures, Continuous Contract
            "CME_LB1",  # Random Length Lumber Futures, Continuous Contract
            # "CME_NG1",  # Natural Gas (Henry Hub) Physical Futures, Continuous Contract
            "CME_PA1",  # Palladium Futures, Continuous Contract
            "CME_RR1",  # Rough Rice Futures, Continuous Contract
            "CME_DA1",  # Class III Milk Futures
            "ICE_RS1",  # Canola Futures, Continuous Contract
            "ICE_GO1",  # Gas Oil Futures, Continuous Contract
            "CME_RB2",  # Gasoline Futures, Continuous Contract
            "CME_KW2",  # Wheat Kansas, Continuous Contract
            "ICE_WT1",  # WTI Crude Futures, Continuous Contract
            "ICE_CC1",  # Cocoa Futures, Continuous Contract
            "ICE_CT1",  # Cotton No. 2 Futures, Continuous Contract
            "ICE_KC1",  # Coffee C Futures, Continuous Contract
            "ICE_O1",  # Heating Oil Futures, Continuous Contract
            "ICE_OJ1",  # Orange Juice Futures, Continuous Contract
            "ICE_SB1",  # Sugar No. 11 Futures, Continuous Contract
        ]

        self.period = 12 * 21
        self.quantile = 5
        self.SetWarmup(self.period)
        self.data = {}

        for symbol in self.symbols:
            data = self.AddData(QuantpediaFutures, symbol, Resolution.Daily)
            data.SetFeeModel(CustomFeeModel())
            data.SetLeverage(5)

            self.data[symbol] = RollingWindow[float](self.period)

        self.Schedule.On(
            self.DateRules.MonthStart(self.symbols[0]),
            self.TimeRules.At(0, 0),
            self.Rebalance,
        )

    def OnData(self, data):
        for symbol in self.symbols:
            symbol_obj = self.Symbol(symbol)
            if symbol_obj in data.Keys:
                price = data[symbol_obj].Value
                if price != 0:
                    self.data[symbol].Add(price)

    def Rebalance(self):
        if self.IsWarmingUp:
            return

        # Skewness calculation
        skewness_data = {}
        for symbol in self.symbols:
            if self.data[symbol].IsReady:
                if (
                    self.Securities[symbol].GetLastData()
                    and (
                        self.Time.date()
                        - self.Securities[symbol].GetLastData().Time.date()
                    ).days
                    < 5
                ):
                    prices = np.array([x for x in self.data[symbol]])
                    returns = (prices[:-1] / prices[1:]) - 1
                    if len(returns) == self.period - 1:
                        # NOTE: Manual skewness calculation example
                        # avg = np.average(returns)
                        # std = np.std(returns)
                        # skewness = (sum(np.power((x - avg), 3) for x in returns)) / ((self.return_history[symbol].maxlen-1) * np.power(std, 3))
                        skewness_data[symbol] = skew(returns)

        long = []
        short = []
        if len(skewness_data) >= self.quantile:
            # Skewness sorting
            sorted_by_skewness = sorted(
                skewness_data.items(), key=lambda x: x[1], reverse=True
            )
            quintile = int(len(sorted_by_skewness) / self.quantile)
            long = [x[0] for x in sorted_by_skewness[-quintile:]]
            short = [x[0] for x in sorted_by_skewness[:quintile]]

        # Trade execution
        invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
        for symbol in invested:
            if symbol not in long + short:
                self.Liquidate(symbol)

        for symbol in long:
            self.SetHoldings(symbol, 1 / len(long))
        for symbol in short:
            self.SetHoldings(symbol, -1 / len(short))


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
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
