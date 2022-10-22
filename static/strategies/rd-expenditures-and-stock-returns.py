# https://quantpedia.com/strategies/rd-expenditures-and-stock-returns/
#
# The investment universe consists of stocks that are listed on NYSE NASDAQ or AMEX. At the end of April, for each stock in the universe, calculate a measure of total R&D expenditures in the past 5 years scaled by the firm’s Market cap (defined on page 7, eq. 1).
# Go long (short) on the quintile of firms with the highest (lowest) R&D expenditures relative to their Market Cap. Weight the portfolio equally and rebalance next year. The backtested performance of the paper is substituted by our more recent backtest in Quantconnect.

# region imports
from AlgorithmImports import *
from numpy import log, average
from scipy import stats
import numpy as np

# endregion


class RDExpendituresandStockReturns(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(1998, 1, 1)
        self.SetCash(100000)

        self.weight = {}
        self.coarse_count = 3000

        # R&D history.
        self.RD = {}
        self.rd_period = 5

        self.long = []
        self.short = []

        data = self.AddEquity("XLK", Resolution.Daily)
        data.SetLeverage(10)
        self.technology_sector = data.Symbol

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.selection_flag = True
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(
            self.DateRules.MonthEnd(self.symbol),
            self.TimeRules.AfterMarketOpen(self.symbol),
            self.Selection,
        )

    def OnSecuritiesChanged(self, changes):
        for security in changes.AddedSecurities:
            security.SetLeverage(10)
            security.SetFeeModel(CustomFeeModel())

    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged

        selected = [x.Symbol for x in coarse if x.HasFundamentalData and x.Price > 5]

        return selected

    def FineSelectionFunction(self, fine):
        fine = [
            x
            for x in fine
            if (
                x.FinancialStatements.IncomeStatement.ResearchAndDevelopment.TwelveMonths
            )
            and (x.MarketCap != 0)
            and (
                (x.SecurityReference.ExchangeId == "NYS")
                or (x.SecurityReference.ExchangeId == "NAS")
                or (x.SecurityReference.ExchangeId == "ASE")
            )
        ]
        # and x.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.Technology]

        top_by_market_cap = None
        if len(fine) > self.coarse_count:
            sorted_by_market_cap = sorted(fine, key=lambda x: x.MarketCap, reverse=True)
            top_by_market_cap = sorted_by_market_cap[: self.coarse_count]
        else:
            top_by_market_cap = fine

        fine_symbols = [x.Symbol for x in top_by_market_cap]
        ability = {}

        updated_flag = []  # updated this year already

        for stock in top_by_market_cap:
            symbol = stock.Symbol

            # prevent storing duplicated value for the same stock in one year
            if symbol not in updated_flag:

                # Update RD.
                if symbol not in self.RD:
                    self.RD[symbol] = RollingWindow[float](self.rd_period)
                # rd = stock.FinancialStatements.IncomeStatement.ResearchAndDevelopment.TwelveMonths
                # self.RD[symbol].Add(rd)

                if self.RD[symbol].IsReady:
                    coefs = np.array([1, 0.8, 0.6, 0.4, 0.2])
                    rds = np.array([x for x in self.RD[symbol]])

                    rdc = sum(coefs * rds)
                    ability[stock] = rdc / stock.MarketCap

                rd = (
                    stock.FinancialStatements.IncomeStatement.ResearchAndDevelopment.TwelveMonths
                )
                self.RD[symbol].Add(rd)

            # prevent storing duplicated value for the same stock in one year
            if fine_symbols.count(symbol) > 1:
                updated_flag.append(symbol)

        # Ability market cap weighting.
        # total_market_cap = sum([x.MarketCap for x in ability])
        # for stock, rdc in ability.items():
        # ability[stock] = rdc * (stock.MarketCap / total_market_cap)

        # Remove not updated symbols
        symbols_to_delete = []
        for symbol in self.RD.keys():
            if symbol not in fine_symbols:
                symbols_to_delete.append(symbol)
        for symbol in symbols_to_delete:
            if symbol in self.RD:
                del self.RD[symbol]

        # starts trading after data storing period
        if len(ability) != 0:
            # Ability sorting.
            sorted_by_ability = sorted(
                ability.items(), key=lambda x: x[1], reverse=True
            )
            decile = int(len(sorted_by_ability) / 5)
            high_by_ability = [x[0].Symbol for x in sorted_by_ability[:decile]]
            low_by_ability = [x[0].Symbol for x in sorted_by_ability[-decile:]]

            self.long = high_by_ability
            self.short = low_by_ability
            # self.short = [self.technology_sector]

        return self.long + self.short

    def Selection(self):
        if self.Time.month == 4:
            self.selection_flag = True

    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False

        # Trade execution.
        long_count = len(self.long)
        short_count = len(self.short)

        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.long + self.short:
                self.Liquidate(symbol)

        for symbol in self.long:
            if (
                self.Securities[symbol].Price != 0
                and self.Securities[symbol].IsTradable
            ):
                self.SetHoldings(symbol, 1 / long_count)

        for symbol in self.short:
            if (
                self.Securities[symbol].Price != 0
                and self.Securities[symbol].IsTradable
            ):
                self.SetHoldings(symbol, -1 / short_count)

        self.long.clear()
        self.short.clear()


class SymbolData:
    def __init__(self, tested_growth, period):
        self.TestedGrowth = tested_growth
        self.RD = RollingWindow[float](period)

    def update(self, window_value):
        self.RD.Add(window_value)

    def is_ready(self):
        return self.RD.IsReady


class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
