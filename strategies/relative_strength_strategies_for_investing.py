# region imports
from AlgorithmImports import *

# endregion

# Use 5 ETFs (SPY - US stocks, EFA - foreign stocks, BND - bonds, VNQ - REITs, GSG - commodities).
# Pick 3 ETFs with strongest 12 month momentum into your portfolio and weight them equally.
# Hold for 1 month and then rebalance.

from datetime import datetime


class AssetClassMomentumAlgorithm(QCAlgorithm):
    def Initialize(self):
        period = 12 * 21
        top = 1
        tickers = ["SPY", "EFA", "BND", "VNQ", "GSG"]
        self.SetStartDate(2000, 1, 1)
        self.SetEndDate(datetime.now())
        self.SetCash(100000)
        self.UniverseSettings.Leverage = 1

        symbols = [
            Symbol.Create(ticker, SecurityType.Equity, Market.USA) for ticker in tickers
        ]
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
        self.SetBrokerageModel(
            BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin
        )
        self.SetWarmUp(period)
        self.UniverseSettings.Resolution = Resolution.Daily

        self.SetAlpha(MomentumAlphaModel(period, top))
        self.SetPortfolioConstruction(
            LeveragedEqualWeightingPCM(self.DateRules.MonthStart("SPY"))
        )
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.2))
        self.SetExecution(ImmediateExecutionModel())

        self.SetBenchmark("SPY")

    def OnData(self, data):
        pass


class MomentumAlphaModel(AlphaModel):
    def __init__(self, period, top):
        self.period = period
        self.top = top
        self.momentum = []
        self.lastRebalance = None

    def OnSecuritiesChanged(self, algorithm, changes):
        for security in changes.AddedSecurities:
            symbol = security.Symbol
            self.momentum.append(
                {
                    "symbol": symbol,
                    "indicator": algorithm.MOM(symbol, self.period, Resolution.Daily),
                }
            )

    def Update(self, algorithm, data):
        if (
            self.lastRebalance is not None
            and self.lastRebalance.month == algorithm.Time.month
        ):
            return []
        self.lastRebalance = algorithm.Time
        ordered = sorted(
            self.momentum, key=lambda kv: kv["indicator"].Current.Value, reverse=True
        )
        selection = ordered[: self.top]
        return Insight.Group(
            [
                Insight.Price(
                    o["symbol"],
                    timedelta(self.period),
                    InsightDirection.Up if o in selection else InsightDirection.Flat,
                )
                for o in ordered
            ]
        )


class LeveragedEqualWeightingPCM(EqualWeightingPortfolioConstructionModel):
    def CreateTargets(self, algorithm, insights):
        targets = super().CreateTargets(algorithm, insights)
        return [
            PortfolioTarget(
                x.Symbol, x.Quantity * algorithm.Securities[x.Symbol].Leverage
            )
            for x in targets
        ]
