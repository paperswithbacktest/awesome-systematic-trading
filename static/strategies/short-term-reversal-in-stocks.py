# region imports
from AlgorithmImports import *

# endregion
# https://quantpedia.com/strategies/short-term-reversal-in-stocks/
#
# The investment universe consists of the 100 biggest companies by market capitalization.
# The investor goes long on the ten stocks with the lowest performance in the previous week and
# goes short on the ten stocks with the greatest performance of the prior month. The portfolio is rebalanced weekly.
#
# QC implementation changes:
#   - Instead of all listed stocks, we first select 500 most liquid stock from QC as a first filter due to time complexity issues tied to whole universe filtering.
#   - Then top 100 market cap stocks are used in momentum sorting.


class ShortTermReversalEffectinStocks(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.coarse_count = 500
        self.stock_selection = 10
        self.top_by_market_cap_count = 100

        self.period = 21

        self.long = []
        self.short = []

        # Daily close data
        self.data = {}

        self.day = 1
        self.selection_flag = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(
            self.DateRules.EveryDay(self.symbol),
            self.TimeRules.AfterMarketOpen(self.symbol),
            self.Selection,
        )

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(5)

    def CoarseSelectionFunction(self, coarse):
        # Update the rolling window every day.
        for stock in coarse:
            symbol = stock.Symbol

            # Store monthly price.
            if symbol in self.data:
                self.data[symbol].update(stock.AdjustedPrice)

        if not self.selection_flag:
            return Universe.Unchanged

        selected = sorted(
            [
                x
                for x in coarse
                if x.HasFundamentalData and x.Market == "usa" and x.Price > 1
            ],
            key=lambda x: x.DollarVolume,
            reverse=True,
        )
        selected = [x.Symbol for x in selected][: self.coarse_count]

        # Warmup price rolling windows.
        for symbol in selected:
            if symbol in self.data:
                continue

            self.data[symbol] = SymbolData(self.period)
            history = self.History(symbol, self.period, Resolution.Daily)
            if history.empty:
                self.Log(f"Not enough data for {symbol} yet")
                continue
            closes = history.loc[symbol].close
            for time, close in closes.iteritems():
                self.data[symbol].update(close)

        return [x for x in selected if self.data[x].is_ready()]

    def FineSelectionFunction(self, fine):
        fine = [x for x in fine if x.MarketCap != 0]

        sorted_by_market_cap = sorted(fine, key=lambda x: x.MarketCap, reverse=True)
        top_by_market_cap = [
            x.Symbol for x in sorted_by_market_cap[: self.top_by_market_cap_count]
        ]

        month_performances = {
            symbol: self.data[symbol].monthly_return() for symbol in top_by_market_cap
        }
        week_performances = {
            symbol: self.data[symbol].weekly_return() for symbol in top_by_market_cap
        }

        sorted_by_month_perf = [
            x[0]
            for x in sorted(
                month_performances.items(), key=lambda item: item[1], reverse=True
            )
        ]
        sorted_by_week_perf = [
            x[0] for x in sorted(week_performances.items(), key=lambda item: item[1])
        ]

        self.long = sorted_by_week_perf[: self.stock_selection]

        for symbol in sorted_by_month_perf:  # Month performances are sorted descending
            if symbol not in self.long:
                self.short.append(symbol)

            if len(self.short) == 10:
                break

        return self.long + self.short

    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False

        invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in invested:
            if symbol not in self.long + self.short:
                self.Liquidate(symbol)

        # Leveraged portfolio - 100% long, 100% short.
        for symbol in self.long:
            if (
                self.Securities[symbol].Price != 0
                and self.Securities[symbol].IsTradable
            ):
                self.SetHoldings(symbol, 1 / len(self.long))

        for symbol in self.short:
            if (
                self.Securities[symbol].Price != 0
                and self.Securities[symbol].IsTradable
            ):
                self.SetHoldings(symbol, -1 / len(self.short))

        self.long.clear()
        self.short.clear()

    def Selection(self):
        if self.day == 5:
            self.selection_flag = True

        self.day += 1
        if self.day > 5:
            self.day = 1


class SymbolData:
    def __init__(self, period):
        self.closes = RollingWindow[float](period)
        self.period = period

    def update(self, close):
        self.closes.Add(close)

    def is_ready(self) -> bool:
        return self.closes.IsReady

    def weekly_return(self) -> float:
        return self.closes[0] / self.closes[5] - 1

    def monthly_return(self) -> float:
        return self.closes[0] / self.closes[self.period - 1] - 1


# Custom fee model
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
