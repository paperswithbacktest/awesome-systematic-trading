# https://quantpedia.com/strategies/earnings-quality-factor/
#
# The investment universe consists of all non-financial stocks from NYSE, Amex and Nasdaq. Big stocks are defined as the largest stocks
# that make up 90% of the total market cap within the region, while small stocks make up the remaining 10% of the market cap. Investor defines
# breakpoints by the 30th and 70th percentiles of the multiple “Earnings Quality” ratios between large caps and small caps.
# The first “Earnings Quality” ratio is defined by cash flow relative to reported earnings. The high-quality earnings firms are characterized
# by high cash flows (relative to reported earnings) while the low-quality firms are characterized by high reported earnings (relative to cash flow).
# The second factor is based on return on equity (ROE) to exploit the well-documented “profitability anomaly” by going long high-ROE firms
# (top 30%) and short low-ROE firms (bottom 30%). The third ratio – CF/A (cash flow to assets) factor goes long firms with high cash flow to total assets.
# The fourth ratio – D/A (debt to assets) factor goes long firms with low leverage and short firms with high leverage.
# The investor builds a scored composite quality metric by computing the percentile score of each stock on each of the four quality metrics
# (where “good” quality has a high score, so ideally a stock has low accruals, low leverage, high ROE, and high cash flow) and then add up
# the percentiles to get a score for each stock from 0 to 400. He then forms the composite factor by going long the top 30% of small-cap
# stocks and also large-cap stocks and short the bottom 30% of the small-cap stocks and also large-cap stocks and cap-weighting individual
# stocks within the portfolios. The final factor portfolio is formed at the end of each June and is rebalanced yearly.
#
# QC implementation changes:
#   - Universe consists of top 3000 US non-financial stocks by market cap from NYSE, AMEX and NASDAQ.


class EarningsQualityFactor(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2000, 1, 1)
        self.SetCash(100000)

        self.coarse_count = 3000

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.accruals_data = {}

        self.long = []
        self.short = []

        self.data = {}

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
            security.SetFeeModel(CustomFeeModel(self))

    def CoarseSelectionFunction(self, coarse):
        if not self.selection_flag:
            return Universe.Unchanged

        selected = [
            x.Symbol for x in coarse if x.HasFundamentalData and x.Market == "usa"
        ]

        return selected

    def FineSelectionFunction(self, fine):
        fine = [
            x
            for x in fine
            if x.MarketCap != 0
            and x.CompanyReference.IndustryTemplateCode != "B"
            and (
                (x.SecurityReference.ExchangeId == "NYS")
                or (x.SecurityReference.ExchangeId == "NAS")
                or (x.SecurityReference.ExchangeId == "ASE")
            )
            and x.FinancialStatements.BalanceSheet.CurrentAssets.Value != 0
            and x.FinancialStatements.BalanceSheet.CashAndCashEquivalents.Value != 0
            and x.FinancialStatements.BalanceSheet.CurrentLiabilities.Value != 0
            and x.FinancialStatements.BalanceSheet.CurrentDebt.Value != 0
            and x.FinancialStatements.IncomeStatement.DepreciationAndAmortization.Value
            != 0
            and x.FinancialStatements.BalanceSheet.GrossPPE.Value != 0
            and x.FinancialStatements.IncomeStatement.TotalRevenueAsReported.Value != 0
            and x.FinancialStatements.CashFlowStatement.OperatingCashFlow.Value != 0
            and x.EarningReports.BasicEPS.Value != 0
            and x.EarningReports.BasicAverageShares.Value != 0
            and x.OperationRatios.DebttoAssets.Value != 0
            and x.OperationRatios.ROE.Value != 0
        ]

        if len(fine) > self.coarse_count:
            sorted_by_market_cap = sorted(fine, key=lambda x: x.MarketCap, reverse=True)
            top_by_market_cap = [x for x in sorted_by_market_cap[: self.coarse_count]]
        else:
            top_by_market_cap = fine

        for stock in top_by_market_cap:
            symbol = stock.Symbol

            if symbol not in self.accruals_data:
                # Data for previous year.
                self.accruals_data[symbol] = None

            # Accrual calc.
            current_accruals_data = AcrrualsData(
                stock.FinancialStatements.BalanceSheet.CurrentAssets.Value,
                stock.FinancialStatements.BalanceSheet.CashAndCashEquivalents.Value,
                stock.FinancialStatements.BalanceSheet.CurrentLiabilities.Value,
                stock.FinancialStatements.BalanceSheet.CurrentDebt.Value,
                stock.FinancialStatements.BalanceSheet.IncomeTaxPayable.Value,
                stock.FinancialStatements.IncomeStatement.DepreciationAndAmortization.Value,
                stock.FinancialStatements.BalanceSheet.TotalAssets.Value,
                stock.FinancialStatements.IncomeStatement.TotalRevenueAsReported.Value,
            )

            # There is not previous accruals data.
            if not self.accruals_data[symbol]:
                self.accruals_data[symbol] = current_accruals_data
                continue

            current_accruals = self.CalculateAccruals(
                current_accruals_data, self.accruals_data[symbol]
            )

            # cash flow to assets
            CFA = (
                stock.FinancialStatements.CashFlowStatement.OperatingCashFlow.Value
                / (
                    stock.EarningReports.BasicEPS.Value
                    * stock.EarningReports.BasicAverageShares.Value
                )
            )
            # debt to assets
            DA = stock.OperationRatios.DebttoAssets.Value
            # return on equity
            ROE = stock.OperationRatios.ROE.Value

            if symbol not in self.data:
                self.data[symbol] = None

            self.data[symbol] = StockData(current_accruals, CFA, DA, ROE)
            self.accruals_data[symbol] = current_accruals_data

        # Remove not updated symbols.
        updated_symbols = [x.Symbol for x in top_by_market_cap]
        not_updated = [x for x in self.data if x not in updated_symbols]
        for symbol in not_updated:
            del self.data[symbol]
            del self.accruals_data[symbol]

        return [x[0] for x in self.data.items()]

    def OnData(self, data):
        if not self.selection_flag:
            return
        self.selection_flag = False

        # Sort stocks by four factors respectively.
        sorted_by_accruals = sorted(
            self.data.items(), key=lambda x: x[1].Accruals, reverse=True
        )  # high score with low accrual
        sorted_by_CFA = sorted(
            self.data.items(), key=lambda x: x[1].CFA
        )  # high score with high CFA
        sorted_by_DA = sorted(
            self.data.items(), key=lambda x: x[1].DA, reverse=True
        )  # high score with low leverage
        sorted_by_ROE = sorted(
            self.data.items(), key=lambda x: x[1].ROE
        )  # high score with high ROE

        score = {}

        # Assign a score to each stock according to their rank with different factors.
        for i, obj in enumerate(sorted_by_accruals):
            score_accruals = i
            score_CFA = sorted_by_CFA.index(obj)
            score_DA = sorted_by_DA.index(obj)
            score_ROE = sorted_by_ROE.index(obj)
            score[obj[0]] = score_accruals + score_CFA + score_DA + score_ROE

        sorted_by_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
        tercile = int(len(sorted_by_score) / 3)
        long = [x[0] for x in sorted_by_score[:tercile]]
        short = [x[0] for x in sorted_by_score[-tercile:]]

        # Trade execution.
        # NOTE: Skip year 2007 due to data error.
        if self.Time.year == 2007:
            self.Liquidate()
            return

        stocks_invested = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in long + short:
                self.Liquidate(symbol)

        for symbol in long:
            if (
                self.Securities[symbol].Price != 0
                and self.Securities[symbol].IsTradable
            ):  # Prevent error message.
                self.SetHoldings(symbol, 1 / len(long))
        for symbol in short:
            if (
                self.Securities[symbol].Price != 0
                and self.Securities[symbol].IsTradable
            ):  # Prevent error message.
                self.SetHoldings(symbol, -1 / len(short))

    # Source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3188172
    def CalculateAccruals(self, current_accrual_data, prev_accrual_data):
        delta_assets = (
            current_accrual_data.CurrentAssets - prev_accrual_data.CurrentAssets
        )
        delta_cash = (
            current_accrual_data.CashAndCashEquivalents
            - prev_accrual_data.CashAndCashEquivalents
        )
        delta_liabilities = (
            current_accrual_data.CurrentLiabilities
            - prev_accrual_data.CurrentLiabilities
        )
        delta_debt = current_accrual_data.CurrentDebt - prev_accrual_data.CurrentDebt
        dep = current_accrual_data.DepreciationAndAmortization
        total_assets_prev_year = prev_accrual_data.TotalAssets

        acc = (
            delta_assets - delta_liabilities - delta_cash + delta_debt - dep
        ) / total_assets_prev_year
        return acc

    def Selection(self):
        if self.Time.month == 7:
            self.selection_flag = True


class AcrrualsData:
    def __init__(
        self,
        current_assets,
        cash_and_cash_equivalents,
        current_liabilities,
        current_debt,
        income_tax_payable,
        depreciation_and_amortization,
        total_assets,
        sales,
    ):
        self.CurrentAssets = current_assets
        self.CashAndCashEquivalents = cash_and_cash_equivalents
        self.CurrentLiabilities = current_liabilities
        self.CurrentDebt = current_debt
        self.IncomeTaxPayable = income_tax_payable
        self.DepreciationAndAmortization = depreciation_and_amortization
        self.TotalAssets = total_assets

        self.Sales = sales


class StockData:
    def __init__(self, accruals, cfa, da, roe):
        self.Accruals = accruals
        self.CFA = cfa
        self.DA = da
        self.ROE = roe


def MultipleLinearRegression(x, y):
    x = np.array(x).T
    x = sm.add_constant(x)
    result = sm.OLS(endog=y, exog=x).fit()
    return result


# Custom fee model
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))
