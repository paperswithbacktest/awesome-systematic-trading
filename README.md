<div align="center">
  <img src="static/future-trading.jpeg" height=300 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>

We are collecting (an admittedly opinionated) list of resources papers, datasets, blogs, libraries, books and methodologies for finding, developing, and running Systematic Trading (Quantitative Trading).

What will you find here?

- [Academic Papers](#academic-papers) describing systematic trading strategies
- [Libraries and packages](#libraries-and-packages) for research and live trading
- [Books](#books) for beginners and professionals
- [Blogs](#blogs)
- [Courses and Tutorials](#courses-and-tutorials)

How do we pick the resources?

- Fit in Systematic Trading / Quantitative Trading domain
- Covering styles, industries and asset classes from around the world
- Valuable to any financial institution

*We are only at the beginning, and you can help by contributing to this GitHub!*

<!-- omit in toc -->
## How Can I Help?

If you're interested in this area and would like to hear more, join our [mailing list (coming soon)](#)! We'd also appreciate if you could fill out this short [form (coming soon)](#) to help us better understand what your interests might be.

<!-- omit in toc -->
### Feedback

If you have ideas on how we can make this repository better, feel free to submit an issue with suggestions.

<!-- omit in toc -->
### Contributing

We want this resource to grow with contributions from readers and data enthusiasts. If you'd like to make contributions to this Github repository, please read our contributing guidelines.

<!-- omit in toc -->
# Table of Content

- [Academic Papers](#academic-papers)
  - [ETFs](#etfs)
  - [Bonds](#bonds)
  - [Bonds, Commodities, Currencies, Equities](#bonds-commodities-currencies-equities)
  - [Bonds, Currencies, Equities](#bonds-currencies-equities)
  - [Bonds, Equities](#bonds-equities)
  - [Commodities](#commodities)
  - [Commodities, Equities](#commodities-equities)
  - [Cryptos](#cryptos)
  - [Currencies](#currencies)
  - [Equities](#equities)
- [Libraries and packages](#libraries-and-packages)
  - [Alpha Models](#alpha-models)
  - [Analytics](#analytics)
    - [Indicators](#indicators)
    - [Metrics computation](#metrics-computation)
    - [Optimization](#optimization)
    - [Pricing](#pricing)
    - [Risk](#risk)
  - [Backtesting and Live Trading](#backtesting-and-live-trading)
    - [General - Event Driven Frameworks](#general---event-driven-frameworks)
    - [General - Vector Based Frameworks](#general---vector-based-frameworks)
    - [Cryptocurrencies](#cryptocurrencies)
  - [Broker APIs](#broker-apis)
  - [Data Science](#data-science)
  - [Databases](#databases)
    - [Graph Computation](#graph-computation)
    - [Machine Learning](#machine-learning)
    - [TimeSeries Analysis](#timeseries-analysis)
    - [Visualization](#visualization)
  - [Data Sources](#data-sources)
    - [General](#general)
    - [Cryptocurrencies](#cryptocurrencies-1)
- [Books](#books)
  - [Beginner](#beginner)
  - [Biography](#biography)
  - [Coding](#coding)
  - [Crypto](#crypto)
  - [General](#general-1)
  - [High Frequency Trading](#high-frequency-trading)
  - [Machine Learning](#machine-learning-1)
- [Blogs](#blogs)
- [Courses and Tutorials](#courses-and-tutorials)
  - [Interviews](#interviews)
  - [Videos](#videos)

# Academic Papers

List of **89 scientific papers** describing original systematic futures trading strategies. Each strategy is categorized by its asset class (Bonds, Commodities, Cryptos, Currencies, Equities), ordered by descending Sharpe ratio, and described by its Sharpe ratio, volatility and period of rebalancing.

## ETFs

[Relative Strength Strategies for Investing
](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517)

| Sharpe Ratio | Volatility | Period of Rebalancing | Implementation |
|--------------|------------|-----------------------|----------------|
| 0.486         | 10.7%      | Monthly                | [QuantConnect](./strategies/relative_strength_strategies_for_investing.py) |

## Bonds

[Market Closure and Short-Term Reversal](https://bit.ly/38XmXRR)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.89         | 7.69%      | Weekly                |

[Finding Yield in a 2% World](https://bit.ly/3M4ZPi8)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.68         | 8.63%      | Monthly               |

[Profiting from Mean-Reverting Yield Curve Trading Strategies](https://bit.ly/3a1jli2)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.65         | 15%        | Monthly               |

[Profitability of Simple Trading Strategies Exploiting the Forward Premium Bias in Foreign Exchange Markets and the Time Premium in Yield Curves](https://bit.ly/3N0VBt4)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.62         | 10%        | Monthly               |

[Short-Term Momentum (Almost) Everywhere](https://bit.ly/3LYI5oc)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.62         | 9.69%      | Monthly               |

[Cross-Sectional Seasonalities in International Government Bond Returns](https://bit.ly/3t4b4k4)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.56         | 13.85%     | Monthly               |

[Beyond Carry and Momentum in Government Bonds](https://bit.ly/3wUm9Xi)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.13         | 10.1%      | Monthly               |

[Carry investing on the yield curve](https://bit.ly/3PLYlwb)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |

## Bonds, Commodities, Currencies, Equities

[Carry](https://bit.ly/38Wnnbk)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.41         | 4.9%       | Monthly               |

[Time Series Reversal in Trend Following Strategies](https://bit.ly/3lTg5Id)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.17         | 20.9%      | Monthly               |

[Return Signal Momentum](https://bit.ly/3a21R56)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.97         | 12.3%      | Monthly               |

[Carry and time‐series momentum: a match made in Heaven](https://bit.ly/3POC80s)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.92         | 10%        | Monthly               |

[Predicting Out-of-Sample Returns: Using Basis to Beat the Historical Average](https://bit.ly/3wUnxbg)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.49         | 7.67%      | Monthly               |

## Bonds, Currencies, Equities

[Trend-Following and Spillover Effects](https://bit.ly/3sZPmgT)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.67         | 4.8%       | Weekly                |

[Cross-Sectional and Time-Series Tests of Return Predictability: What is the Difference?](https://bit.ly/3N24fr2)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.5          | 12.91%     | 6 Months              |


## Bonds, Equities

[Worth It’s Weight in Gold Offense and Defense in Active Portfolio Management](https://bit.ly/3PHKdnw)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.84         | 11.8%      | Weekly                |

[Return Predictability and Market-Timing: A One-Month Model](https://bit.ly/3M1lurc)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.72         | 11.05%     | Monthly               |

[Cross-Asset Signals and Time Series Momentum](https://bit.ly/3wSLuzD)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.65         | 10%        | Monthly               |

[Opposing Seasonalities in Treasury versus Equity Returns](https://bit.ly/3wO2lmY)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | 6 Months              |

## Commodities

[Pairs Trading the Commodity Futures Curve](https://bit.ly/3wT7iMK)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 3.09         | 2.01%      | Monthly               |

[Timing Commodity Momentum](https://bit.ly/3z5ZRTV)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 2.41         | 11.09%     | Monthly               |

[Short-Term Momentum (Almost) Everywhere](https://bit.ly/3LYI5oc)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.01         | 20.86%     | Monthly               |

[Basis-momentum](https://bit.ly/3PJGXs1)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.92         | 19.98%     | Monthly               |

[Is Gold a Zero-Beta Asset? Analysis of the Investment Potential of Precious Metals](https://bit.ly/3yZQoxs)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.91         | 29.63%     | Monthly               |

[Fear of Hazards in Commodity Futures Markets](https://bit.ly/3MZo9mG)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.89         | 9.26%      | Weekly                |

[Long-Run Reversal in Commodity Returns: Insights from Seven Centuries of Evidence](https://bit.ly/3aioAKg)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.83         | 19.37%     | Yearly                |

[Tactical allocation in commodity futures markets: Combining momentum and term structure signals](https://bit.ly/3PMfJRj)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.79         | 27.6%      | Monthly               |

[Modeling, Forecasting and Trading the Crude Oil Term Structure](https://bit.ly/3t2hm3A)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.76         | 7.1%       | Weekly                |

[Trend Following, Risk Parity and Momentum in Commodity Futures](https://bit.ly/3yZQyoy)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.76         | 19.33%     | Monthly               |

[Commodity Option Implied Volatilities and the Expected Futures Returns](https://bit.ly/3GtLSc2)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.69         | 18.48%     | Monthly               |

[Commodity Strategies Based on Momentum, Term Structure and Idiosyncratic Volatility](https://bit.ly/3LWABCu)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.68         | 10.79%     | Monthly               |

[Idiosyncratic momentum in commodity futures](https://bit.ly/38Xopnh)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.59         | 29.42%     | Monthly               |

[Commodity Strategies Based on Momentum, Term Structure and Idiosyncratic Volatility](https://bit.ly/3LWABCu)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 19.3%      | Weekly                |

[Dynamic Commodity Timing Strategies](https://bit.ly/3wVunhF)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 18%        | Monthly               |

[Long-Short Commodity Investing: Implications for Portfolio Risk and Market Regulation](https://bit.ly/3t2SuZo)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.41         | 18.09%     | Weekly                |

[Multi-Asset Seasonality and Trend-Following Strategies](https://bit.ly/38yM9y8)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.38         | 9.32%      | Monthly               |

[The Case for Long-Short Commodity Investing](https://bit.ly/3GxZfrN)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.25         | 17.17%     | Weekly                |

[Investor Sentiment And Return Predictability in Agricultural Futures Market](https://bit.ly/3wY2Jkr)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Weekly                |

[Political Uncertainty and Commodity Prices](https://bit.ly/3PJIXAx)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Quarterly             |

[The Autumn Effect of Gold](https://bit.ly/3tqRgrt)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |

[What does futures market interest tell us about the macroeconomy and asset prices?](https://bit.ly/3anBHdb)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |

## Commodities, Equities

[How to Time the Commodity Market](https://bit.ly/3MYcEvD)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.24         | 10.3%      | Weekly                |

[When to Own Stocks and When to Own Gold](https://bit.ly/3wVcP4j)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 14%        | Yearly                |

## Cryptos

["Know when to hodl them, know when to fodl them": An Investigation of Factor Based Investing in the Cryptocurrency Space](https://bit.ly/3an1rGx)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.13         | 7.1%       | Weekly                |

[Do Fundamentals Drive Cryptocurrency Prices](https://bit.ly/38sEiSv)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.06         | 9.3%       | Weekly                |

## Currencies

[Combining Mean Reversion and Momentum Trading Strategies in Foreign Exchange Markets](https://bit.ly/3LY7pe7)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 2.43         | 10%        | Monthly               |

[Beyond the Carry Trade: Optimal Currency Portfolios](https://bit.ly/3z5ztt9)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.4          | 23.89%     | Monthly               |

[A Low-Risk Strategy based on Higher Moments in Currency Markets](https://bit.ly/3M1nLTg)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.38         | 8%         | Monthly               |

[Economic Momentum and Currency Returns](https://bit.ly/3PN06t0)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.1          | 5.6%       | Monthly               |

[Are Value Strategies Profitable in the Foreign Exchange Market?](https://bit.ly/3wVcXkj)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.01         | 9.51%      | Monthly               |

[Cross-Asset Return Predictability: Carry Trades, Stocks and Commodities](https://bit.ly/3MXnwdt)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.01         | 9.07%      | Monthly               |

[Optimal and Naive Diversification in Currency Markets](https://bit.ly/3NCfq9Q)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.99         | 6.97%      | Monthly               |

[Basis-momentum](https://bit.ly/3PJGXs1)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.91         | 9.23%      | Monthly               |

[Market Closure and Short-Term Reversal](https://bit.ly/38XmXRR)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.9          | 10.23%     | Weekly                |

[Is There Momentum or Reversal in Weekly Currency Returns?](https://bit.ly/3lRvicM)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.88         | 8.1%       | Weekly                |

[The Revenge of Purchasing Power Parity on Carry Trades during Crises](https://bit.ly/3lRrZlQ)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.87         | 4.97%      | Monthly               |

[Predictability of Currency Carry Trades and Asset Pricing Implications](https://bit.ly/3wYaWDV)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.86         | 10%        | Monthly               |

[Carry On](https://bit.ly/3lPU3pQ)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.82         | 2.47%      | Monthly               |

[The Term Structure of Sovereign CDS and the Cross-Section Exchange Rate Predictability](https://bit.ly/3MSGQZb)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.82         | 5.92%      | Monthly               |

[Forward-Looking Policy Rules and Currency Premia](https://bit.ly/3a25acw)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.81         | 7.61%      | Monthly               |

[U.S. Equity Tail Risk and Currency Risk Premia](https://bit.ly/3POb41l)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.75         | 8.12%      | Monthly               |

[Perceived corruption, carry trades, and the cross section of currency returns](https://bit.ly/3NDQC1e)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.74         | 8.14%      | Yearly                |

[The Equity Differential Factor in Currency Markets](https://bit.ly/3NIODZs)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.61         | 3.1%       | Monthly               |

[Investor sentiment, attention and profitability of currency momentum strategies](https://bit.ly/3PRlNrW)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.56         | 10.36%     | Monthly               |

[The Rise and Fall of the Carry Trade: Links to Exchange Rate Predictability](https://bit.ly/3wUzezU)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.55         | 19.65%     | Monthly               |

[Yield Curve Predictors of Foreign Exchange Returns](https://bit.ly/3z5gfnv)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.52         | 3.67%      | Monthly               |

[A Multi Strategy Approach to Trading Foreign Exchange Futures](https://bit.ly/38sz6y2)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.5          | 13.16%     | Monthly               |

[Carry Trades and Global Foreign Exchange Volatility](https://bit.ly/3lZfvIM)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.48         | 8.68%      | 6 Months              |

[From Carry Trades to Curvy Trades](https://bit.ly/3wXC7ic)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.39         | 6.7%       | Monthly               |

[International Diversification Benefits with Foreign Exchange Investment Styles](https://bit.ly/3N1fW1f)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.33         | 9.56%      | Monthly               |

[Speculation and Hedging in the Currency Futures Markets: Are They Informative to the Spot Exchange Rates](https://bit.ly/3t5FXod)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Weekly                |

## Equities

[The Presidential Term: Is the Third Year the Charm?](https://bit.ly/3z3HsqM)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.29         | 15.34%     | Yearly                |

[Expected Option Returns](https://bit.ly/3a25hos)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.16         | 19%        | Monthly               |

[Stock Returns over the FOMC Cycle](https://bit.ly/3NZymzN)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.83         | 13.92%     | Weekly                |

[Combining equity country selection strategies](https://bit.ly/3a5aHzd)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.82         | 24.53%     | Monthly               |

[Market Timing with Aggregate Accruals](https://bit.ly/3wVv2Qb)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.8          | 37.7%      | Yearly                |

[Short-Term Momentum (Almost) Everywhere](https://bit.ly/3LYI5oc)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.8          | 20.38%     | Monthly               |

[Seven Decades of Long Term Abnormal Return Persistence: The Case of Dividend Initiations and Resumptions](https://bit.ly/3NCfDtE)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.78         | 6.74%      | Monthly               |

[Return Predictability and Market-Timing: A One-Month Model](https://bit.ly/3M1lurc)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.76         | 16.6%      | Monthly               |

[Time-Varying Sharpe Ratios and Market Timing](https://bit.ly/3N0Y86y)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.66         | 15.38%     | Monthly               |

[Exploiting the Informational Content of Hedging Pressure: Timing the Market by "Learning" from Derivatives Traders](https://bit.ly/3wXjbRP)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.52         | 11%        | Weekly                |

[Stock Return Predictability and Seasonality](https://bit.ly/3t3dm2M)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.46         | 17.78%     | 6 Months              |

[Equity premiums in the Presidential cycle: The midterm election resolution of uncertainty](https://bit.ly/3lZfCnG)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.47         | 24.47%     | 6 Months              |

[Market Timing with Aggregate and Idiosyncratic Stock Volatilities](https://bit.ly/3z9zfkS)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 37.8%      | Quarterly             |

[Forecasting the size premium over different time horizons](https://bit.ly/3av9C3R)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.38         | 14.62%     | Monthly               |

[Alpha Momentum and Alpha Reversal in Country and Industry Equity](https://bit.ly/3LX9KWO)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.31         | 20.02%     | Monthly               |

[A Performance Evaluation Model for Global Macro Funds](https://bit.ly/3N27e2I)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.3          | 9.21%      | Monthly               |

[Contrarian Long-Short Futures Arbitrages and Market Efficiency: Evidence in the Index Futures Markets around the Globe](https://bit.ly/3GuurIw)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Weekly                |

[Does Sentiment Matter?](https://bit.ly/3NIOKEm)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |


# Libraries and packages

## Alpha Models

> Note: these bots are old and not maintained. I put them here just to show some logic of crypto arbitrage.

- [analyzingalpha](https://github.com/leosmigel/analyzingalpha)
- [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | `Python` | - Bitcoin arbitrage - opportunity detector 
- [Blackbird](https://github.com/butor/blackbird) | `C++` | - Blackbird Bitcoin Arbitrage: a long/short market-neutral strategy 
- [czsc - 缠中说禅技术分析工具](https://github.com/waditu/czsc) | `Python` | - 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 
- [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow) | `Python` | - PyTrendFollow - systematic futures trading using trend following 
- [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2) | `TypeScript` | - R2 Bitcoin Arbitrager is an automatic arbitrage trading system powered by Node.js + TypeScript.
- [ThetaGang](https://github.com/brndnmtthws/thetagang) - ThetaGang is an IBKR bot for collecting money


## Analytics

### Indicators

- [finta](https://github.com/peerchemist/finta) | `Python` | - Common financial technical indicators implemented in Pandas
- [pandas-ta](https://github.com/twopirllc/pandas-ta) | `Python` | - Pandas Technical Analysis (Pandas TA) is an easy to use library that leverages the Pandas package with more than 130 Indicators and Utility functions and more than 60 TA Lib Candlestick Patterns.
- [TA-Lib](https://ta-lib.org) | `C` | - Perform technical analysis of financial market data
  - [Python Wrapper](https://github.com/mrjbq7/ta-lib) | `Python` |
  - [Go Port](https://github.com/markcheno/go-talib) | `Go` |
  - [Rust Wrapper](https://github.com/CLevasseur/ta-lib-rust) | `Rust` |
- [ta-rust](https://github.com/greyblake/ta-rs) | `Rust` | - Technical analysis library for Rust language

### Metrics computation

- [ffn](https://github.com/pmorissette/ffn) | `Python` | - A financial function library for Python
- [quantstats](https://github.com/ranaroussi/quantstats) | `Python` | - Portfolio analytics for quants, written in Python

### Optimization

- [Deepdow](https://github.com/jankrepl/deepdow) | `Python` | - Python package connecting portfolio optimization and deep learning. Its goal is to facilitate research of networks that perform weight allocation in one forward pass.
- [empyrial](https://github.com/ssantoshp/Empyrial) | `Python` | - Empyrial is a Python-based open-source quantitative investment library dedicated to financial institutions and retail investors, officially released in March 2021.
- [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | `Python` | - Financial portfolio optimizations in python, including classical efficient frontier, Black-Litterman, Hierarchical Risk Parity
- [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | `Python` | - Portfolio Optimization and Quantitative Strategic Asset Allocation in Python
- [spectre](https://github.com/Heerozh/spectre) | `Python` | - spectre is a GPU-accelerated Parallel quantitative trading library, focused on performance.

### Pricing

- [FinancePy](https://github.com/domokane/FinancePy) | `Python` | - A Python Finance Library that focuses on the pricing and risk-management of Financial Derivatives, including fixed-income, equity, FX and credit derivatives.
- [Quantlib](https://www.quantlib.org)
  - [PyQL](https://github.com/enthought/pyql) | `Python`, `Cython` | - Python wrapper of the famous pricing library QuantLib
  - [QuantLib.jl](https://github.com/pazzo83/QuantLib.jl) | `Julia` | - Quantlib implementation in pure Julia.
- [tf-quant-finance](https://github.com/google/tf-quant-finance) - High-performance TensorFlow library for quantitative finance from Google

### Risk

- [pyfolio](https://github.com/quantopian/pyfolio) | `Python` | - Portfolio and risk analytics in Python


## Backtesting and Live Trading

### General - Event Driven Frameworks


Note: the one marked as `Live Trading` has reasonable live trading support for at least 1 broker. Otherwise, backtest function only.


- [aat](https://github.com/AsyncAlgoTrading/aat) | `Python`, `C++`, `Live Trading`| - an asynchronous, event-driven framework for writing algorithmic trading strategies in python with optional acceleration in C++. It is designed to be modular and extensible, with support for a wide variety of instruments and strategies, live trading across (and between) multiple exchanges.
- [backtesting.py](https://github.com/kernc/backtesting.py) | `Python` | - Backtesting.py is a Python framework for inferring viability of trading strategies on historical (past) data. Improved upon the vision of Backtrader, and by all means surpassingly comparable to other accessible alternatives, Backtesting.py is lightweight, fast, user-friendly, intuitive, interactive, intelligent and, hopefully, future-proof.
- :star: [backtrader](https://github.com/mementum/backtrader) | `Python`, `Live Trading` | - Event driven Python Backtesting library for trading strategies
- [barter-rs](https://gitlab.com/open-source-keir/financial-modelling/trading/barter-rs) | `Rust` | - Open-source Rust framework for building event-driven live-trading & backtesting systems. Algorithmic trade with the peace of mind that comes from knowing your strategies have been backtested with a near-identical trading Engine.
- [finmarketpy](https://github.com/cuemacro/finmarketpy) | `Python` | - Python library for backtesting trading strategies & analyzing financial markets (formerly pythalesians)
- [FlashFunk](https://github.com/HFQR/FlashFunk) | `Rust` | -  High Performance Runtime in Rust
- [gobacktest](https://github.com/gobacktest/gobacktest) | `Go` | - A Go implementation of event-driven backtesting framework
- [lumibot](https://github.com/Lumiwealth/lumibot/tree/8da88cadfe9ee35399dd69c94aa5ed3cf995f417) | `Python` | - A very simple yet useful backtesting and sample based live trading framework (a bit slow to run...)
- [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | `Python`, `Cython`, `Rust`, `Live Trading` | - A high-performance algorithmic trading platform and event-driven backtester
- :star: [QuantConnect](https://github.com/QuantConnect/Lean) | `C#`, `.NET`, `Live Trading` | - Lean Algorithmic Trading Engine by QuantConnect (Python, C#)
- [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS) | `Python`, `Rust`, `Live Trading` | - QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权/港股/虚拟货币 数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案
- [quanttrader](https://github.com/letianzj/quanttrader) | `Python` | - Backtest and live trading in Python. Event based. Similar to backtesting.py.
- [Rqalpha](https://github.com/ricequant/rqalpha) | `Python` | - A extendable, replaceable Python algorithmic backtest && trading framework supporting multiple securities
- [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) | `Python` | - This project is mainly for newbies into algo trading who are interested in learning to code their own trading algo using python interpreter.
- [vnpy](https://github.com/vnpy/vnpy) | `Python`, `Stock`, `Futures`, `Crypto`, `Live Trading` | - Python-based open source quantitative trading system development framework, officially released in January 2015, has grown step by step into a full-featured quantitative trading platform
- [WonderTrader](https://github.com/wondertrader/wondertrader) | `C++`, `Python` | - WonderTrader——量化研发交易一站式框架 
- [zipline](https://github.com/quantopian/zipline) | `Python` | - Zipline is a Pythonic algorithmic trading library. It is an event-driven system for backtesting.
- [zvt](https://github.com/zvtvz/zvt) | `Python`, `Stock`, `Backtest` | - Modular quant framework

### General - Vector Based Frameworks

Note: Vector based frameworks are not recommended, more error prone.

- [bt](https://github.com/pmorissette/bt) | `Python` | -  Flexible backtesting for Python based on Algo and Strategy Tree
- [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | `Python`, `Live Trading` | - Systematic Trading in python from book <Systematic Trading> by Rob Carver
- [vectorbt](https://github.com/polakowo/vectorbt) | `Python`, `numba` | - vectorbt takes a novel approach to backtesting: it operates entirely on pandas and NumPy objects, and is accelerated by Numba to analyze any data at speed and scale. This allows for testing of many thousands of strategies in seconds.

### Cryptocurrencies

- [bTrader](https://github.com/gabriel-milan/btrader) | `Rust` | - Triangle arbitrage trading bot for Binance
- [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) | `Rust` | - Crawl orderbook and trade messages from crypto exchanges
- [cryptotrader-core](https://github.com/monomadic/cryptotrader-core) | `Rust` | - Simple to use Crypto Exchange REST API client in rust. 
- [Freqtrade](https://github.com/freqtrade/freqtrade) | `Python` | - Freqtrade is a free and open source crypto trading bot written in Python. It is designed to support all major exchanges and be controlled via Telegram. It contains backtesting, plotting and money management tools as well as strategy optimization by machine learning.
- [Hummingbot](https://github.com/CoinAlpha/hummingbot) | `Python`, `Cython`, `Live Trading` | - A client for crypto market making
- [Kelp](https://github.com/stellar/kelp) | `Go`, `Live Trading` | - Kelp is a free and open-source trading bot for the Stellar DEX and 100+ centralized exchanges
- [Jesse](https://github.com/jesse-ai/jesse) | `Python` | - Jesse is an advanced crypto trading framework which aims to simplify researching and defining trading strategies.
- [OctoBot](https://github.com/Drakkar-Software/OctoBot) | `Python`, `Cython`, `Live Trading`| - Cryptocurrency trading bot for TA, arbitrage and social trading with an advanced web interface
- [openlimits](https://github.com/nash-io/openlimits) | `Rust` | - A Rust high performance cryptocurrency trading API with support for multiple exchanges and language wrappers. 


## Broker APIs

- [ccxt](https://github.com/ccxt/ccxt) | `Python`, `JavaScript` | - A JavaScript / Python / PHP cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges
- [Coinnect](https://github.com/hugues31/coinnect) | `Rust` | - Coinnect is a Rust library aiming to provide a complete access to main crypto currencies exchanges via REST API.
- [Ib_insync](https://github.com/erdewit/ib_insync) | `Python` | - Python sync/async framework for 
- More is coming... (PR welcome)


## Data Science

- [Cvxpy](https://github.com/cvxpy/cvxpy) | `Python`, `C++` | - A Python-embedded modeling language for convex optimization problems.
- [Keras](https://github.com/keras-team/keras) | `Python` | - The most user friendly Deep Learning for humans in Python
- :star: [Numpy](https://github.com/numpy/numpy) | `Python`, `C` | - The fundamental package for scientific computing with Python
- :star: [Pandas](https://github.com/pandas-dev/pandas) | `Python`, `Cython` | - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more
- [Pytorch](https://github.com/pytorch/pytorch) | `Python` | - Tensors and Dynamic neural networks in Python with strong GPU acceleration
- [PyMC](https://github.com/pymc-devs/pymc) | `Python` | - Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Aesara
- :star: [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | `Python`, `Cython` | - Machine learning in Python
- :star: [Scipy](https://github.com/scipy/scipy) | `Python`, `C` | - Fundamental algorithms for scientific computing in Python
- [TensorFlow](https://github.com/tensorflow/tensorflow) | `Python`, `C++` | - More low level Deep Learning framework

## Databases

- [Arctic (Man Group)](https://github.com/man-group/arctic) | `Python` | - High performance datastore for time series and tick data
- [Marketstore](https://github.com/alpacahq/marketstore) | `Go` | - DataFrame Server for Financial Timeseries Data
- [Tectonicdb](https://github.com/0b01/tectonicdb) | `Rust` | - Tectonicdb is a fast, highly compressed standalone database and streaming protocol for order book ticks.

### Graph Computation

- [Dask](https://github.com/dask/dask) | `Python` | - Parallel computing with task scheduling in Python with a Pandas like API
- [GraphKit](https://github.com/yahoo/graphkit) | `Python` | - A lightweight Python module for creating and running ordered graphs of computations.
- [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | `Ocaml` | - Incremental is a library that gives you a way of building complex computations that can update efficiently in response to their inputs changing, inspired by the work of Umut Acar et. al. on self-adjusting computations. Incremental can be useful in a number of applications
- :star: [Man MDF](https://github.com/man-group/mdf) | `Python` | - Data-flow programming toolkit for Python 
- [Ray](https://github.com/ray-project/ray) | `Python`, `C++` | - An open source framework that provides a simple, universal API for building distributed applications.
- [Tributary](https://github.com/timkpaine/tributary) | `Python` | - Streaming reactive and dataflow graphs in Python

### Machine Learning

- [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | `Python` | - FinRL is the first open-source framework to demonstrate the great potential of applying deep reinforcement learning in quantitative finance.
- [MlFinLab (Hudson & Thames)](https://bit.ly/3GxKwNO)  | `Python` | - MlFinLab helps portfolio managers and traders who want to leverage the power of machine learning by providing reproducible, interpretable, and easy to use tools.
- [QLib (Microsoft)](https://github.com/microsoft/qlib) | `Python`, `Cython` | - Qlib is an AI-oriented quantitative investment platform, which aims to realize the potential, empower the research, and create the value of AI technologies in quantitative investment. With Qlib, you can easily try your ideas to create better Quant investment strategies. An increasing number of SOTA Quant research works/papers are released in Qlib.
- [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) | `Python` | - Stock Trading Bot using Deep Q-Learning 
- [TradingGym](https://github.com/Yvictor/TradingGym) | `Python`, `Live Trading` | - Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo.

### TimeSeries Analysis

- [Facebook Prophet](https://github.com/facebook/prophet) - Tool for producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth.
- [pmdarima](https://github.com/alkaline-ml/pmdarima) - A statistical library designed to fill the void in Python's time series analysis capabilities, including the equivalent of R's auto.arima function.
- [statsmodels](http://statsmodels.sourceforge.net) - Python module that allows users to explore data, estimate statistical models, and perform statistical tests.
- [tsfresh](https://github.com/blue-yonder/tsfresh) - Automatic extraction of relevant features from time series.

### Visualization

- [btplotting](https://github.com/happydasch/btplotting) | `Python`, `bokeh` | - btplotting provides plotting for backtests, optimization results and live data from backtrader.
- :star: [D-Tale (Man Group)](https://github.com/man-group/dtale) | `JavaScript`, `Python` | - D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures.
- [mplfinance](https://github.com/matplotlib/mplfinance) | `Python` | - Financial Markets Data Visualization using Matplotlib


## Data Sources

### General

- [AkShare](https://github.com/akfamily/akshare) |`Python`| - AKShare is an elegant and simple financial data interface library for Python, built for human beings!
- [findatapy](https://github.com/cuemacro/findatapy) |`Python`| - findatapy creates an easy to use Python API to download market data from many sources including Quandl, Bloomberg, Yahoo, Google etc. using a unified high level interface.  
- [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | `Python` | - Fully-fledged Fundamental Analysis package capable of collecting 20 years of Company Profiles, Financial Statements, Ratios and Stock Data of 20.000+ companies.
- [Investpy](https://github.com/alvarobartt/investpy) - Financial Data Extraction from Investing.com with Python
- [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) | `Python` | - Investment Research for Everyone, Anywhere.
- [pandas-datareader](https://github.com/pydata/pandas-datareader) |`Python`| - Up to date remote data access for pandas, works for multiple versions of pandas.
- :star: [Quandl](https://www.quandl.com/tools/api) |`Python`| - Get millions of financial and economic dataset from hundreds of publishers via a single free API.
- [TuShare](https://github.com/waditu/tushare) |`Python`| - TuShare is a utility for crawling historical data of China stocks
- [Wallstreet](https://github.com/mcdallas/wallstreet) |`Python`| - Wallstreet: Real time Stock and Option tools
- :star: [yfinance](https://github.com/ranaroussi/yfinance) |`Python`| - yfinance offers a threaded and Pythonic way to download market data from Yahoo!Ⓡ finance.

### Cryptocurrencies

- [Cryptofeed](https://github.com/bmoscon/cryptofeed) |`Python`| - Cryptocurrency Exchange Websocket Data Feed Handler with Asyncio
- [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) |`Python`| - A live crypto currency historical trade data blotter. Download live historical trade data from any crypto exchange.
- [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) |`Python`| - Gekko trading bot dataset dumps. Download and use history files in SQLite format.

# Books

A comprehensive list of **56 books** for quantitative traders.


## Beginner

[A Beginner’s Guide to the Stock Market: Everything You Need to Start Making Money Today - Matthew R. Kratter](https://amzn.to/3QN2VdU)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3QN2VdU">
        <img src="./static/A Beginner’s Guide to the Stock Market.jpeg" style="width:400px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Learn to make money in the stock market, even if you’ve never traded before. The stock market is the greatest opportunity machine ever created. Are you ready to get your piece of it?
        </li>
        <li>
          This book will teach you everything that you need to know to start making money in the stock market today. Don’t gamble with your hard-earned money. If you are going to make a lot of money, you need to know how the stock market really works. You need to avoid the pitfalls and costly mistakes that beginners make. And you need time-tested trading and investing strategies that actually work. This book gives you everything that you will need. It’s a simple road map that anyone can follow.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Algorithmic Trading and DMA: An introduction to direct access trading strategies - Barry Johnson](https://amzn.to/3xYb0UN)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3xYb0UN">
        <img src="./static/Algorithmic Trading and DMA.jpeg" style="width:190px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Algorithmic trading and Direct Market Access (DMA) are important tools for helping both buy and sell-side traders to achieve the best execution.
        </li>
        <li>
          This book starts from the ground up to provide detailed explanations of both these techniques:
        </li>
        <ul>
          <li>
            An introduction to the different types of execution is followed by a review of market microstructure theory. Throughout the book, examples from empirical studies bridge the gap between the theory and practice of trading.
          </li>
          <li>
            Orders are the fundamental building blocks for any strategy. Market, limit, stop, hidden, iceberg, peg, routed, and immediate-or-cancel orders are all described with illustrated examples.
          </li>
        </ul>
      </ul>
    </td>
  </tr>
</table>


[Day Trading QuickStart Guide: The Simplified Beginner’s Guide to Winning Trade Plans, Conquering the Markets, and Becoming a Successful Day Trader - Troy Noonan](https://amzn.to/3HPZijw)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3HPZijw">
        <img src="./static/Day Trading QuickStart Guide.jpeg" style="width:80px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Day Trading QuickStart Guide Is Perfect For:
          <ul>
            <li>
              Complete beginners – even if you’ve never bought a single stock before!
            </li>
            <li>
              People who tried day trading in the past but didn’t find success because of phony gurus and courses
            </li>
            <li>
              Existing traders who want to hone their skills & increase their earning potential
            </li>
            <li>
              Anyone who wants the freedom of making a full-time income with part-time effort!
            </li>
          </ul>
        </li>
        <li>
          Day Trading QuickStart Guide Explains:
          <ul>
            <li>
              The Inner Workings of the Derivatives Market
            </li>
            <li>
              Futures Trading Contracts, How They Work and How to Maximize their Efficiency
            </li>
            <li>
              How to Day Trade Options and Use Options Contracts to Hedge Against Risk
            </li>
            <li>
              The Mechanics of Forex Trading and How to Use Foreign Currency Markets to Your Benefit
            </li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>


[Introduction To Algo Trading: How Retail Traders Can Successfully Compete With Professional Traders - Kevin J Davey](https://amzn.to/39Tf7JC)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/39Tf7JC">
        <img src="./static/Introduction To Algo Trading.jpeg" style="width:480px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Are you interested in algorithmic trading, but unsure how to get started? Join best selling author and champion futures trader Kevin J. Davey as he introduces you to the world of retail algorithmic trading. In this book, you will find out if algo trading is for you while learning the advantages and disadvantages involved. You will also learn how to start algo trading on your own, how to select a trading platform and what is needed to develop simple trading strategies. Finally, you will learn important tips for successful algo trading, along with a roadmap of next steps to take.
          </li>
        </ul>
      </ul>
    </td>
  </tr>
</table>


[Investing QuickStart Guide: The Simplified Beginner’s Guide to Successfully Navigating the Stock Market, Growing Your Wealth & Creating a Secure Financial Future - Ted D. Snow](https://amzn.to/3A5aRkX)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3A5aRkX">
        <img src="./static/Investing QuickStart Guide.jpeg" style="width:130px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Investing QuickStart Guide is Perfect For:
          <ul>
            <li>
              Companion to The Intelligent Investor
            </li>
            <li>
              Stock Market Education for Teen & Kids
            </li>
            <li>
              Beginners with Zero Prior Experience
            </li>
            <li>
              Experienced Investors who Want to Go to the Next Level
            </li>
            <li>
              Discover the Secrets of Successfully Investing In: Stocks (Including Dividend Paying Stocks), Mutual Funds, ETFs, Bonds, Index Funds, REITs, Commodities
            </li>
          </ul>
        </li>
        <li>
          Investing QuickStart Guide Covers:
          <ul>
            <li>
              Everything You Need to Know Before You Make Your First Trade
            </li>
            <li>
              How To Take Advantage Of Opportunities In The Market Without Relying On Guesswork
            </li>
            <li>
              How to Evaluate and Compare Stocks and Other Securities
            </li>
            <li>
              How Disciplined Approaches to Investing Can Lead to Early Retirement and Financial Freedom
            </li>
            <li>
              How National And Global Economic And Geopolitical Factors Can Influence Investment Prospects
            </li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>


[The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns - John C. Bogle](https://amzn.to/3A4mgkR)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3A4mgkR">
        <img src="./static/The Little Book of Common Sense Investing.jpeg" style="width:170px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The Little Book of Common Sense Investing is the classic guide to getting smart about the market. Legendary mutual fund pioneer John C. Bogle reveals his key to getting more out of investing: low-cost index funds.
        </li>
        <li>
          Bogle describes the simplest and most effective investment strategy for building wealth over the long term: buy and hold, at very low cost, a mutual fund that tracks a broad stock market Index such as the S&P 500.
        </li>
      </ul>
    </td>
  </tr>
</table>

[How to Day Trade for a Living: A Beginner’s Guide to Trading Tools and Tactics, Money Management, Discipline and Trading Psychology - Andrew Aziz](https://amzn.to/3bmehFv)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3bmehFv">
        <img src="./static/How to Day Trade for a Living.jpeg" style="width:330px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          In the book, I describe the fundamentals of day trading, explain how day trading is different from other styles of trading and investment, and elaborate on important trading strategies that many traders use every day. I’ve kept the book short, so you can actually finish reading it and not get bored by the middle.
        </li>
        <li>
          For beginner traders, this book gives an understanding of where to start, how to start, what to expect from day trading, and how to develop a strategy. Simply reading this book, however, will not make you a profitable trader. Profit in trading does not come with reading a book or two or browsing online. It comes with practice, the right tools and software and appropriate ongoing education.
        </li>
      </ul>
    </td>
  </tr>
</table>

## Biography


[How I Became a Quant: Insights from 25 of Wall Street’s Elite: - Barry Schachter](https://amzn.to/3Alf8kz)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3Alf8kz">
        <img src="./static/How I Became a Quant.jpeg" style="width:390px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          How I Became a Quant reveals the faces behind the quant revolution, offering you the chance to learn firsthand what it’s like to be a quant today. In this fascinating collection of Wall Street war stories, more than two dozen quants detail their roots, roles, and contributions, explaining what they do and how they do it, as well as outlining the sometimes unexpected paths they have followed from the halls of academia to the front lines of an investment revolution.
        </li>
      </ul>
    </td>
  </tr>
</table>



[My Life as a Quant: Reflections on Physics and Finance - Emanuel Derman](https://amzn.to/3A8KudR)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3A8KudR">
        <img src="./static/My Life as a Quant.jpeg" style="width:410px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          In My Life as a Quant, Emanuel Derman relives his exciting journey as one of the first high-energy particle physicists to migrate to Wall Street. Page by page, Derman details his adventures in this field―analyzing the incompatible personas of traders and quants, and discussing the dissimilar nature of knowledge in physics and finance. Throughout this tale, he also reflects on the appropriate way to apply the refined methods of physics to the hurly-burly world of markets.
        </li>
      </ul>
    </td>
  </tr>
</table>

## Coding

[Algorithmic Trading with Python: Quantitative Methods and Strategy Development - Chris Conlan](https://amzn.to/3u3cxYo)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3u3cxYo">
        <div style="width:200px">
          <img src="./static/Algorithmic Trading with Python.jpeg" style="width:700px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Algorithmic Trading with Python discusses modern quant trading methods in Python with a heavy focus on pandas, numpy, and scikit-learn. After establishing an understanding of technical indicators and performance metrics, readers will walk through the process of developing a trading simulator, strategy optimizer, and financial machine learning pipeline. This book maintains a high standard of reproducibility. All code and data are self-contained in a GitHub repo. The data includes hyper-realistic simulated price data and alternative data based on real securities. Algorithmic Trading with Python (2020) is the spiritual successor to Automated Trading with R (2016). This book covers more content in less time than its predecessor due to advances in open-source technologies for quantitative analysis.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Learn Algorithmic Trading: Build and deploy algorithmic trading systems and strategies using Python and advanced data analysis - Sebastien Donadio](https://amzn.to/3NqNghA)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3NqNghA">
        <div style="width:200px">
          <img src="./static/Learn Algorithmic Trading.jpeg" style="width:660px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          It’s now harder than ever to get a significant edge over competitors in terms of speed and efficiency when it comes to algorithmic trading. Relying on sophisticated trading signals, predictive models and strategies can make all the difference. This book will guide you through these aspects, giving you insights into how modern electronic trading markets and participants operate.
        </li>
        <li>
          You’ll start with an introduction to algorithmic trading, along with setting up the environment required to perform the tasks in the book. You’ll explore the key components of an algorithmic trading business and aspects you’ll need to take into account before starting an automated trading project. Next, you’ll focus on designing, building and operating the components required for developing a practical and profitable algorithmic trading business. Later, you’ll learn how quantitative trading signals and strategies are developed, and also implement and analyze sophisticated trading strategies such as volatility strategies, economic release strategies, and statistical arbitrage. Finally, you’ll create a trading bot from scratch using the algorithms built in the previous sections.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Python for Algorithmic Trading: From Idea to Cloud Deployment - Yves Hilpisch](https://amzn.to/3bpkd0C)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3bpkd0C">
        <div style="width:100px">
          <img src="./static/Python for Algorithmic Trading.jpeg" style="width:340px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Algorithmic trading, once the exclusive domain of institutional players, is now open to small organizations and individual traders using online platforms. The tool of choice for many traders today is Python and its ecosystem of powerful packages. In this practical book, author Yves Hilpisch shows students, academics, and practitioners how to use Python in the fascinating field of algorithmic trading.
        </li>
        <li>
          You’ll learn several ways to apply Python to different aspects of algorithmic trading, such as backtesting trading strategies and interacting with online trading platforms. Some of the biggest buy- and sell-side institutions make heavy use of Python. By exploring options for systematically building and deploying automated algorithmic trading strategies, this book will help you level the playing field.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Python for Finance: Mastering Data-Driven Finance - Yves Hilpisch](https://amzn.to/3NhkTlP)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3NhkTlP">
        <div style="width:100px">
          <img src="./static/Python for Finance.jpeg" style="width:370px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          The financial industry has recently adopted Python at a tremendous rate, with some of the largest investment banks and hedge funds using it to build core trading and risk management systems. Updated for Python 3, the second edition of this hands-on book helps you get started with the language, guiding developers and quantitative analysts through Python libraries and tools for building financial applications and interactive financial analytics.
        </li>
        <li>
          Using practical examples throughout the book, author Yves Hilpisch also shows you how to develop a full-fledged framework for Monte Carlo simulation-based derivatives and risk analytics, based on a large, realistic case study. Much of the book uses interactive IPython Notebooks.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Trading Evolved: Anyone can Build Killer Trading Strategies in Python - Andreas F. Clenow](https://amzn.to/3A0jcGB)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3A0jcGB">
        <div style="width:100px">
          <img src="./static/Trading Evolved.jpeg" style="width:375px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Systematic trading allows you to test and evaluate your trading ideas before risking your money. By formulating trading ideas as concrete rules, you can evaluate past performance and draw conclusions about the viability of your trading plan. Following systematic rules provides a consistent approach where you will have some degree of predictability of returns, and perhaps more importantly, it takes emotions and second-guessing out of the equation.
        </li>
      </ul>
    </td>
  </tr>
</table>


## Crypto

[Bitcoin Billionaires: A True Story of Genius, Betrayal, and Redemption - Ben Mezrich](https://amzn.to/39SkdWt)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/39SkdWt">
        <img src="./static/Bitcoin Billionaires.jpeg" style="width:430px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Planning to start careers as venture capitalists, the brothers quickly discover that no one will take their money after their fight with Zuckerberg. While nursing their wounds in Ibiza, they accidentally run into an eccentric character who tells them about a brand-new idea: cryptocurrency. Immersing themselves in what is then an obscure and sometimes sinister world, they begin to realize “crypto” is, in their own words, “either the next big thing or total bulls–t.” There’s nothing left to do but make a bet.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Mastering Bitcoin: Programming the Open Blockchain - Andreas M. Antonopoulos](https://amzn.to/3NniZ3p)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3NniZ3p">
        <img src="./static/Mastering Bitcoin.jpeg" style="width:350px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Join the technological revolution that’s taking the financial world by storm. Mastering Bitcoin is your guide through the seemingly complex world of bitcoin, providing the knowledge you need to participate in the internet of money. Whether you’re building the next killer app, investing in a startup, or simply curious about the technology, this revised and expanded second edition provides essential detail to get you started.
        </li>
        <li>
          Bitcoin, the first successful decentralized digital currency, is still in its early stages and yet it’s already spawned a multi-billion-dollar global economy open to anyone with the knowledge and passion for participating. Mastering Bitcoin provides knowledge. You simply supply the passion.
        </li>
      </ul>
    </td>
  </tr>
</table>

[The Bitcoin Standard: The Decentralized Alternative to Central Banking - Saifedean Ammous](https://amzn.to/3QMJgec)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3QMJgec">
        <img src="./static/The Bitcoin Standard.jpeg" style="width:480px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          When a pseudonymous programmer introduced “a new electronic cash system that’s fully peer-to-peer, with no trusted third party” to a small online mailing list in 2008, very few paid attention. Ten years later, and against all odds, this upstart autonomous decentralized software offers an unstoppable and globally-accessible hard money alternative to modern central banks. The Bitcoin Standard analyzes the historical context to the rise of Bitcoin, the economic properties that have allowed it to grow quickly, and its likely economic, political, and social implications.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Why Buy Bitcoin: Investing Today in the Money of Tomorrow - Andy Edstrom](https://amzn.to/3OMcKqZ)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3OMcKqZ">
        <img src="./static/Why Buy Bitcoin.jpeg" style="width:750px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Some people still view Bitcoin as a startup. But despite being declared dead many times by the mainstream media, Bitcoin grows stronger every year. What’s going on? It’s not too late to learn about Bitcoin and invest. Bitcoin’s value has grown exponentially over multiple booms and bust cycles spanning a decade. Bitcoin is an Internet-native phenomenon like Alibaba, Amazon, Apple, Facebook, Google, Netflix, Microsoft, and Tencent. It, therefore, benefits from the “network effect” which makes it dramatically more valuable as the network grows. But its potential value is much larger than the giant Internet companies we know so well. If Bitcoin reaches that potential, its value could rise by 50 times its current price in the coming decade. This book will help you understand the role of money in our society, the current state of debt in our economy, and how Bitcoin provides a better solution.
        </li>
      </ul>
    </td>
  </tr>
</table>

## General

[Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk - Richard Grinold, Ronald Kahn](https://amzn.to/3xMKaic)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3xMKaic">
        <img src="./static/Active Portfolio Management.jpeg" style="width:770px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Mathematically rigorous and meticulously organized, Active Portfolio Management broke new ground when it first became available to investment managers in 1994. By outlining an innovative process to uncover raw signals of asset returns, develop them into refined forecasts, then use those forecasts to construct portfolios of exceptional return and minimal risk, i.e., portfolios that consistently beat the market, this hallmark book helped thousands of investment managers. Active Portfolio Management, Second Edition, now sets the bar even higher. Like its predecessor, this volume details how to apply economics, econometrics, and operations research to solving practical investment problems, and uncovering superior profit opportunities. It outlines an active management framework that begins with a benchmark portfolio, then defines exceptional returns as they relate to that benchmark.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Advances in Active Portfolio Management: New Developments in Quantitative Investing - Richard Grinold, Ronald Kahn](https://amzn.to/3xUTK2z)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3xUTK2z">
        <img src="./static/Advances in Active Portfolio Management.jpeg" style="width:470px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Advances in Active Portfolio Management gets you fully up to date on the issues, trends, and challenges in the world of active management―and shows how to apply advances in the Grinold and Kahn’s legendary approach to meet current challenges. Composed of articles published in today’s leading management publications―including several that won Journal of Portfolio Management’s prestigious Bernstein Fabozzi/Jacobs Levy Award―this comprehensive guide is filled with new insights into:
          <ul>
            <li>
              Dynamic Portfolio Management
            </li>
            <li>
              Signal Weighting
            </li>
            <li>
              Implementation Efficiency
            </li>
            <li>
              Holdings-based attribution
            </li>
            <li>
              Expected returns
            </li>
            <li>
              Risk management
            </li>
            <li>
              Portfolio construction
            </li>
            <li>
              Fees
            </li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

[Algorithmic Trading and Quantitative Strategies (Chapman and Hall/CRC Financial Mathematics Series) - Raja Velu, Maxence Hardy, Daniel Nehren](https://amzn.to/3xUTQXZ)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3xUTQXZ">
        <img src="./static/Algorithmic Trading and Quantitative Strategies.jpeg" style="width:690px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Algorithmic Trading and Quantitative Strategies provides an in-depth overview of this growing field with a unique mix of quantitative rigor and practitioner’s hands-on experience. The focus on empirical modelling and practical know-how makes this book a valuable resource for students and professionals.
        </li>
        <li>
          The book starts with the often overlooked context of why and how we trade via a detailed introduction to market structure and quantitative microstructure models. The authors then present the necessary quantitative toolbox, including more advanced machine learning models needed to successfully operate in the field. They next discuss the subject of quantitative trading, alpha generation, active portfolio management and more recent topics like news and sentiment analytics. The last main topic of execution algorithms is covered in detail with emphasis on the state of the field and critical topics, including the elusive concept of market impact. The book concludes with a discussion of the technology infrastructure necessary to implement algorithmic strategies in large-scale production settings.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Algorithmic Trading: Winning Strategies and Their Rationale - Ernest P. Chan](https://amzn.to/3xWi8kd)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3xWi8kd">
        <div style="width:100px">
          <img src="./static/Algorithmic Trading.jpeg" style="width:380px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Engaging and informative, Algorithmic Trading skillfully covers a wide array of strategies. Broadly divided into the mean-reverting and momentum camps, it lays out standard techniques for trading each category of strategies and, equally important, the fundamental reasons why a strategy should work. The emphasis throughout is on simple and linear strategies, as an antidote to the over-fitting and data-snooping biases that often plague complex strategies.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Building Winning Algorithmic Trading Systems: A Trader’s Journey From Data Mining to Monte Carlo Simulation to Live Trading (Wiley Trading) - Kevin J Davey](https://amzn.to/39QnsxA)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/39QnsxA">
        <div style="width:100px">
          <img src="./static/Building Winning Algorithmic Trading Systems.jpeg" style="width:560px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Develop your own trading system with practical guidance and expert advice In Building Algorithmic Trading Systems: A Trader’s Journey From Data Mining to Monte Carlo Simulation to Live Training, award-winning trader Kevin Davey shares his secrets for developing trading systems that generate triple-digit returns. With both explanation and demonstration, Davey guides you step-by-step through the entire process of generating and validating an idea, setting entry and exit points, testing systems, and implementing them in live trading. You’ll find concrete rules for increasing or decreasing allocation to a system, and rules for when to abandon one.
        </li>
      </ul>
    </td>
  </tr>
</table>

[How I Invest My Money: Finance experts reveal how they save, spend, and invest - Joshua Brown, Brian Portnoy](https://amzn.to/3A4rsoU)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3A4rsoU">
        <img src="./static/How I Invest My Money.jpeg" style="width:1100px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The world of investing normally sees experts telling us the “right” way to manage our money. How often do these experts pull back the curtain and tell us how they invest their own money? Never. How I Invest My Money changes that. In this unprecedented collection, 25 financial experts share how they navigate markets with their own capital. In this honest rendering of how they invest, save, spend, give, and borrow, this group of portfolio managers, financial advisors, venture capitalists and other experts detail the “how” and the “why” of their investments. They share stories about their childhood, their families, the struggles they face and the aspirations they hold. Sometimes raw, always revealing, these stories detail the indelible relationship between our money and our values. Taken as a whole, these essays powerfully demonstrate that there is no single “right” way to save, spend, and invest. We see a kaleidoscope of perspectives on stocks, bonds, real assets, funds, charity, and other means of achieving the life one desires. With engaging illustrations throughout by Carl Richards, How I Invest My Money inspires readers to think creatively about their financial decisions and how money figures in the broader quest for a contented life.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Leveraged Trading: A professional approach to trading FX, stocks on margin, CFDs, spread bets and futures for all traders - Robert Carver](https://amzn.to/3Nhl6p7)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3Nhl6p7">
        <img src="./static/Leveraged Trading.jpeg" style="width:245px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          With the right broker, and just a few hundred dollars or pounds, anyone can become a leveraged trader. The products and tools needed are accessible to all: FX, a margin account, CFDs, spread-bets and futures.
        </li>
        <li>
          But this level playing field comes with great risks. Trading with leverage is inherently dangerous. With leverage, losses and costs – the two great killers for traders – are magnified.
        </li>
        <li>
          This does not mean leverage must be avoided altogether, but it does mean that it needs to be used safely. In Leveraged Trading, Robert Carver shows you how to do exactly that, by using a trading system. A trading system can be employed to tackle those twin dangers of serious losses and high costs.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Machine Trading: Deploying Computer Algorithms to Conquer the Markets - Ernest P. Chan](https://amzn.to/3OIBe4o)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3OIBe4o">
        <div style="width:100px">
          <img src="./static/Machine Trading.jpeg" style="width:760px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Machine Trading is a practical guide to building your algorithmic trading business. Written by a recognized trader with major institution expertise, this book provides step-by-step instruction on quantitative trading and the latest technologies available even outside the Wall Street sphere. You’ll discover the latest platforms that are becoming increasingly easy to use, gain access to new markets, and learn new quantitative strategies that are applicable to stocks, options, futures, currencies, and even bitcoins. The companion website provides downloadable software codes, and you’ll learn to design your own proprietary tools using MATLAB. The author’s experiences provide deep insight into both the business and human side of systematic trading and money management, and his evolution from a proprietary trader to fund manager contains valuable lessons for investors at any level.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Naked Forex: High-Probability Techniques for Trading Without Indicators - Alex Nekritin](https://amzn.to/3NkrAUj)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3NkrAUj">
        <img src="./static/Naked Forex.jpeg" style="width:265px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Most forex traders rely on technical analysis books written for stock, futures, and options traders. However, long before computers and calculators, traders were trading naked. Naked trading is the simplest (and oldest) trading method. It’s simply trading without technical indicators, and that is exactly what this book is about.
        </li>
        <li>
          Traders who use standard technical indicators focus on the indicators. Traders using naked trading techniques focus on the price chart. Naked trading is a simple and superior way to trade and is suited to those traders looking to quickly achieve expertise with a trading method.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Option Volatility and Pricing: Advanced Trading Strategies and Techniques, 2nd Edition - Sheldon Natenberg](https://amzn.to/3btOxXL)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3btOxXL">
        <img src="./static/Option Volatility and Pricing.jpeg" style="width:325px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The bestselling Option Volatility & Pricing has made Sheldon Natenberg a widely-recognized authority in the options industry. At firms around the world, the text is often the first book that new professional traders are given to learn the trading strategies and risk management techniques required for success in option markets.
        </li>
        <li>
          Now, in this revised, updated, and expanded second edition, this thirty-year trading professional presents the most comprehensive guide to advanced trading strategies and techniques now in print. Covering a wide range of topics as diverse and exciting as the market itself, this text enables both new and experienced traders to delve in detail into the many aspects of option markets.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Professional Automated Trading: Theory and Practice - Eugene A. Durenard](https://amzn.to/3yhfOpw)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3yhfOpw">
        <div style="width:100px">
          <img src="./static/Professional Automated Trading.jpeg" style="width:465px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          An insider’s view of how to develop and operate an automated proprietary trading network
        </li>
        <li>
          Reflecting author Eugene Durenard’s extensive experience in this field, Professional Automated Trading offers valuable insights you won’t find anywhere else. It reveals how a series of concepts and techniques coming from current research in artificial life and modern control theory can be applied to the design of effective trading systems that outperform the majority of published trading systems. It also skillfully provides you with essential information on the practical coding and implementation of a scalable systematic trading architecture.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Quantitative Equity Portfolio Management: An Active Approach to Portfolio Construction and Management (McGraw-Hill Library of Investment and Finance) - Ludwig B Chincarini, Daehwan Kim](https://amzn.to/3yl9u0c)

<table>
  <tr>
    <td>
      <a href="https://amzn.to/3yl9u0c">
        <img src="./static/Quantitative Equity Portfolio Management.jpeg" style="width:290px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Capitalize on Today’s Most Powerful Quantitative Methods to Construct and Manage a High-Performance Equity Portfolio
        </li>
        <li>
          Quantitative Equity Portfolio Management is a comprehensive guide to the entire process of constructing and managing a high-yield quantitative equity portfolio. This detailed handbook begins with the basic principles of quantitative active management and then clearly outlines how to build an equity portfolio using those powerful concepts.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Quantitative Momentum: A Practitioner’s Guide to Building a Momentum-Based Stock Selection System (Wiley Finance) - Wesley R. Gray, Jack R. Vogel](https://www.amazon.fr/gp/product/111923719X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=111923719X&linkId=b825cb65462a4a9254af3b7dc5328131)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/111923719X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=111923719X&linkId=b825cb65462a4a9254af3b7dc5328131">
        <img src="./static/Quantitative Momentum.jpeg" style="width:790px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Quantitative Momentum brings momentum investing out of Wall Street and into the hands of individual investors. In his last book, Quantitative Value, author Wes Gray brought systematic value strategy from the hedge funds to the masses; in this book, he does the same for momentum investing, the system that has been shown to beat the market and regularly enriches the coffers of Wall Street’s most sophisticated investors. First, you’ll learn what momentum investing is not: it’s not ‘growth’ investing, nor is it an esoteric academic concept. You may have seen it used for asset allocation, but this book details the ways in which momentum stands on its own as a stock selection strategy, and gives you the expert insight you need to make it work for you. You’ll dig into its behavioral psychology roots, and discover the key tactics that are bringing both institutional and individual investors flocking into the momentum fold.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Quantitative Technical Analysis: An integrated approach to trading system development and trading management - Dr Howard B Bandy](https://www.amazon.fr/gp/product/0979183855/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0979183855&linkId=8ef7bda69477bdccf90f5ac02ee495b0)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0979183855/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0979183855&linkId=8ef7bda69477bdccf90f5ac02ee495b0">
        <img src="./static/Quantitative Technical Analysis.jpeg" style="width:68px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          An integrated approach to trading system development and trading management
        </li>
      </ul>
    </td>
  </tr>
</table>

[Quantitative Trading: Algorithms, Analytics, Data, Models, Optimization - Xin Guo, Tze Leung Lai, Howard Shek, Samuel Po-Shing Wong](https://www.amazon.fr/gp/product/0367871815/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0367871815&linkId=3f2ba1cbc0e1fe02e255da740423b2fb)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0367871815/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0367871815&linkId=3f2ba1cbc0e1fe02e255da740423b2fb">
        <img src="./static/Quantitative Trading-2.jpeg" style="width:510px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The first part of this book discusses institutions and mechanisms of algorithmic trading, market microstructure, high-frequency data and stylized facts, time and event aggregation, order book dynamics, trading strategies and algorithms, transaction costs, market impact and execution strategies, risk analysis, and management. The second part covers market impact models, network models, multi-asset trading, machine learning techniques, and nonlinear filtering. The third part discusses electronic market making, liquidity, systemic risk, recent developments and debates on the subject.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Quantitative Trading: How to Build Your Own Algorithmic Trading Business - Ernest P. Chan](https://www.amazon.fr/gp/product/0470284889/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0470284889&linkId=7121da8f65a34315d15f3f8d4e09da15)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0470284889/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0470284889&linkId=7121da8f65a34315d15f3f8d4e09da15">
        <img src="./static/Quantitative Trading.jpeg" style="width:510px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          While institutional traders continue to implement quantitative (or algorithmic) trading, many independent traders have wondered if they can still challenge powerful industry professionals at their own game? The answer is “yes,” and in Quantitative Trading, Dr. Ernest Chan, a respected independent trader and consultant, will show you how. Whether you’re an independent “retail” trader looking to start your own quantitative trading business or an individual who aspires to work as a quantitative trader at a major financial institution, this practical guide contains the information you need to succeed.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Systematic Trading: A unique new method for designing trading and investing systems - Robert Carver](https://www.amazon.fr/gp/product/0857194453/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0857194453&linkId=32d8bffc32c01041cde066bacab76c04)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0857194453/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0857194453&linkId=32d8bffc32c01041cde066bacab76c04">
        <img src="./static/Systematic Trading.jpeg" style="width:370px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          This is not just another book with yet another trading system. This is a complete guide to developing your own systems to help you make and execute trading and investing decisions. It is intended for everyone who wishes to systematize their financial decision making, either completely or to some degree.
        </li>
        <li>
          Author Robert Carver draws on financial theory, his experience managing systematic hedge fund strategies and his own in-depth research to explain why systematic trading makes sense and demonstrates how it can be done safely and profitably. Every aspect, from creating trading rules to position sizing, is thoroughly explained. The framework described here can be used with all assets, including equities, bonds, forex and commodities.
        </li>
      </ul>
    </td>
  </tr>
</table>

[The Art and Science of Technical Analysis: Market Structure, Price Action, and Trading Strategies - Adam Grimes](https://www.amazon.fr/gp/product/1118115120/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118115120&linkId=d5dc1f0e6727b2663d2186a110a31ad0)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1118115120/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118115120&linkId=d5dc1f0e6727b2663d2186a110a31ad0">
        <img src="./static/The Art and Science of Technical Analysis.jpeg" style="width:920px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          A breakthrough trading book that provides powerful insights on profitable technical patterns and strategies The Art and Science of Technical Analysis is a groundbreaking work that bridges the gaps between the academic view of markets, technical analysis, and profitable trading. The book explores why randomness prevails in markets most, but not all, of the time and how technical analysis can be used to capture statistically validated patterns in certain types of market conditions. The belief of the book is that buying and selling pressure causes patterns in prices, but that these technical patterns are only effective in the presence of true buying/selling imbalance. The Art and Science of Technical Analysis is supported by extensive statistical analysis of the markets, which will debunk some tools and patterns such as Fibonacci analysis, and endorse other tools and trade setups. In addition, this reliable resource discusses trader psychology and trader learning curves based on the author’s extensive experience as a trader and trainer of traders.
        </li>
      </ul>
    </td>
  </tr>
</table>

[The Four Pillars of Investing: Lessons for Building a Winning Portfolio - William J. Bernstein](https://www.amazon.fr/gp/product/B0041842TW/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=B0041842TW&linkId=d9bc2fec4f3faa41ca4f24aed3c72122)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/B0041842TW/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=B0041842TW&linkId=d9bc2fec4f3faa41ca4f24aed3c72122">
        <img src="./static/The Four Pillars of Investing.jpeg" style="width:760px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The classic guide to constructing a solid portfolio—without a financial advisor! “With relatively little effort, you can design and assemble an investment portfolio that, because of its wide diversification and minimal expenses, will prove superior to the most professionally managed accounts. Great intelligence and good luck are not required.“ William Bernstein‘s commonsense approach to portfolio construction has served investors well during the past turbulent decade—and it‘s what made The Four Pillars of Investing an instant classic when it was first published nearly a decade ago. This down-to-earth book lays out in easy-to-understand prose the four essential topics that every investor must master: the relationship of risk and reward, the history of the market, the psychology of the investor and the market, and the folly of taking financial advice from investment salespeople.
        </li>
      </ul>
    </td>
  </tr>
</table>

[The Intelligent Investor: The Definitive Book on Value Investing - Benjamin Graham, Jason Zweig](https://www.amazon.fr/gp/product/0060555661/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0060555661&linkId=aba73910e4e3873b6cc8364487662bd6)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0060555661/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0060555661&linkId=aba73910e4e3873b6cc8364487662bd6">
        <img src="./static/The Intelligent Investor.jpeg" style="width:390px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The greatest investment advisor of the twentieth century, Benjamin Graham, taught and inspired people worldwide. Graham’s philosophy of “value investing” which shields investors from substantial error and teaches them to develop long-term strategies has made The Intelligent Investor the stock market bible ever since its original publication in 1949.
        </li>
        <li>
          Over the years, market developments have proven the wisdom of Graham’s strategies. While preserving the integrity of Graham’s original text, this revised edition includes updated commentary by noted financial journalist Jason Zweig. His perspective incorporates the realities of today’s market, draws parallels between Graham’s examples and today’s financial headlines, and gives readers a more thorough understanding of how to apply Graham’s principles.
        </li>
      </ul>
    </td>
  </tr>
</table>

[The New Trading for a Living: Psychology, Discipline, Trading Tools and Systems, Risk Control, Trade Management (Wiley Trading) - Alexander Elder](https://www.amazon.fr/gp/product/1118467450/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118467450&linkId=67ee502653bc52a5240ced9fc88eb76d)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1118467450/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118467450&linkId=67ee502653bc52a5240ced9fc88eb76d">
        <img src="./static/The New Trading for a Living.jpeg" style="width:335px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The New Trading for Living updates a modern classic, popular worldwide among both private and institutional traders. This revised and expanded edition brings time-tested concepts in gear with today’s fast-moving markets, adding new studies and techniques for the modern trader.
        </li>
        <li>
          This classic guide teaches a calm and disciplined approach to the markets. It emphasizes risk management along with self-management and provides clear rules for both. The New Trading for a Living includes templates for rating stock picks, creating trade plans, and rating your own readiness to trade. It provides the knowledge, perspective, and tools for developing your own effective trading system.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Trading and Exchanges: Market Microstructure for Practitioners - Larry Harris](https://www.amazon.fr/gp/product/0195144708/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0195144708&linkId=e47e596fc0696cbd624726cce05b4500)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0195144708/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0195144708&linkId=e47e596fc0696cbd624726cce05b4500">
        <img src="./static/Trading and Exchanges.jpeg" style="width:680px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          This book is about trading, the people who trade securities and contracts, the marketplaces where they trade, and the rules that govern it. Readers will learn about investors, brokers, dealers, arbitrageurs, retail traders, day traders, rogue traders, and gamblers; exchanges, boards of trade, dealer networks, ECNs (electronic communications networks), crossing markets, and pink sheets. Also covered in this text are single price auctions, open outcry auctions, and brokered markets limit orders, market orders, and stop orders. Finally, the author covers the areas of program trades, block trades, and short trades, price priority, time precedence, public order precedence, and display precedence, insider trading, scalping, and bluffing, and investing, speculating, and gambling.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Trading Systems: A New Approach to System Development and Portfolio Optimisation - Emilio Tomasini, Urban Jaekle](https://www.amazon.fr/gp/product/1905641796/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1905641796&linkId=61e6634242c497498338f73641ce0a80)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1905641796/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1905641796&linkId=61e6634242c497498338f73641ce0a80">
        <div style="width:100px">
          <img src="./static/Trading Systems.jpeg" style="width:565px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          The key is how to adapt existing codes to the current market conditions, how to build a portfolio and how to know when the moment has come to a stop one system and start another one’. Every day there are traders who make a fortune. It may seem that it seldom happens, but it does – as William Eckhardt, Ed Seykota, Jim Simons, and many others remind us. You can join them by using systems to manage your trading. This book explains exactly how you can build a winning trading system. It is an insight into what a trader should know and do in order to achieve success in the markets, and it will show you why you don’t need to be a rocket scientist to build a winning trading system.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Trading Systems 2nd edition: A new approach to system development and portfolio optimisation - Emilio Tomasini, Urban Jaekle](https://www.amazon.fr/gp/product/085719755X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=085719755X&linkId=97aa558484a8dc2bf57a5296e7f38cad)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/085719755X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=085719755X&linkId=97aa558484a8dc2bf57a5296e7f38cad">
        <div style="width:100px">
          <img src="./static/Trading Systems 2nd edition.jpeg" style="width:670px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Completely revised and updated second edition, with new AmiBroker codes and new complete portfolio tests. The focus of this book is how to adapt existing codes to the current market conditions, how to build a portfolio, and how to know when the moment has come to a stop one system and use another one. Every day, there are traders who make a fortune. It may seem that it seldom happens, but it does – as William Eckhardt, Ed Seykota, Jim Simons, and many others remind us. You can join them by using systems to manage your trading. This book explains exactly how you can build a winning trading system. It is an insight into what a trader should know and do in order to achieve success in the markets, and it will show you why you don’t need to be a rocket scientist to build a winning trading system.
        </li>
      </ul>
    </td>
  </tr>
</table>

## High Frequency Trading

[Algorithmic and High-Frequency Trading (Mathematics, Finance and Risk) - Álvaro Cartea, Sebastian Jaimungal, José Penalva](https://www.amazon.fr/gp/product/1107091144/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1107091144&linkId=64e3ceb66482d8db6827830964b85613)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1107091144/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1107091144&linkId=64e3ceb66482d8db6827830964b85613">
        <img src="./static/Algorithmic and High-Frequency Trading.jpeg" style="width:870px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          The design of trading algorithms requires sophisticated mathematical models backed up by reliable data. In this textbook, the authors develop models for algorithmic trading in contexts such as executing large orders, market making, targeting VWAP and other schedules, trading pairs or collection of assets, and executing in dark pools. These models are grounded on how the exchanges work, whether the algorithm is trading with better-informed traders (adverse selection), and the type of information available to market participants at both ultra-high and low frequency. Algorithmic and High-Frequency Trading is the first book that combines sophisticated mathematical modelling, empirical facts and financial economics, taking the reader from basic ideas to cutting-edge research and practice. If you need to understand how modern electronic markets operate, what information provides a trading edge, and how other market participants may affect the profitability of the algorithms, then this is the book for you.
        </li>
      </ul>
    </td>
  </tr>
</table>

[An Introduction to High-Frequency Finance - Ramazan Gençay, Michel Dacorogna, Ulrich A. Muller, Olivier Pictet, Richard Olsen](https://www.amazon.fr/gp/product/0122796713/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0122796713&linkId=7e6c098026204f399e45d7fbb803dcca)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0122796713/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0122796713&linkId=7e6c098026204f399e45d7fbb803dcca">
        <img src="./static/An Introduction to High-Frequency Finance.jpeg" style="width:620px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Liquid markets generate hundreds or thousands of ticks (the minimum change in price a security can have, either up or down) every business day. Data vendors such as Reuters transmit more than 275,000 prices per day for foreign exchange spot rates alone. Thus, high-frequency data can be a fundamental object of study, as traders make decisions by observing high-frequency or tick-by-tick data. Yet most studies published in financial literature deal with low frequency, regularly spaced data. For a variety of reasons, high-frequency data are becoming a way of understanding market microstructure. This book discusses the best mathematical models and tools for dealing with such vast amounts of data.
        </li>
      </ul>
    </td>
  </tr>
</table>



[High-Frequency Trading - Maureen O’Hara, David Easley, Marcos M López de Prado](https://www.amazon.fr/gp/product/178272009X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=178272009X&linkId=082f861ff6bbe4cca4ef7ccbe620a2c4)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/178272009X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=178272009X&linkId=082f861ff6bbe4cca4ef7ccbe620a2c4">
        <img src="./static/High-Frequency Trading.jpeg" style="width:160px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          This is the survival guide for trading in a world where high-frequency trading predominates in markets, accounting for upwards of 60% of trading in equities and futures, and 40% in foreign exchange.
        </li>
        <li>
          High-frequency trading is the subject of extensive debate, particularly as to whether it is beneficial for traders and markets or instead allows some traders to benefit at others expense.
        </li>
        <li>
          This book provides you with an important overview and perspective on this area, with a particular focus on how low-frequency traders and asset managers can survive in the high-frequency world.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Inside the Black Box: A Simple Guide to Quantitative and High Frequency Trading - Rishi K. Narang](https://www.amazon.fr/gp/product/1118362411/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118362411&linkId=35e02d4e636350366531a5033597a541)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1118362411/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118362411&linkId=35e02d4e636350366531a5033597a541">
        <img src="./static/Inside the Black Box.jpeg" style="width:470px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          In this updated edition of his bestselling book, Rishi K Narang offers in a straightforward, nontechnical style―supplemented by real-world examples and informative anecdotes―a reliable resource takes you on a detailed tour through the black box. He skillfully sheds light upon the work that quants do, lifting the veil of mystery around quantitative trading and allowing anyone interested in doing so to understand quants and their strategies. This new edition includes information on High-Frequency Trading.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Market Microstructure in Practice - Charles-Albert Lehalle, Sophie Laruelle](https://www.amazon.fr/Market-Microstructure-Practice-Sophie-Laruelle/dp/9813231122)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/Market-Microstructure-Practice-Sophie-Laruelle/dp/9813231122">
        <img src="./static/Market Microstructure in Practice.jpg" style="width:250px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Using a quantitative viewpoint, this book explains how an attrition of liquidity and regulatory changes can impact the whole microstructure of financial markets. A mathematical Appendix details the quantitative tools and indicators used through the book, allowing the reader to go further independently.
        </li>
      </ul>
    </td>
  </tr>
</table>


[The Financial Mathematics of Market Liquidity - Olivier Gueant](https://www.amazon.com/Financial-Mathematics-Market-Liquidity-Execution/dp/1498725473)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.com/Financial-Mathematics-Market-Liquidity-Execution/dp/1498725473">
        <img src="./static/The Financial Mathematics of Market Liquidity.jpg" style="width:380px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          This book is among the first to present the mathematical models most commonly used to solve optimal execution problems and market making problems in finance. The Financial Mathematics of Market Liquidity: From Optimal Execution to Market Making presents a general modeling framework for optimal execution problems–inspired from the Almgren-Chriss approach–and then demonstrates the use of that framework across a wide range of areas.
        </li>
      </ul>
    </td>
  </tr>
</table>


[The Problem of HFT – Collected Writings on High Frequency Trading & Stock Market Structure Reform - Haim Bodek](https://www.amazon.fr/gp/product/1481978357/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1481978357&linkId=2f3acf998de645990b681e2ac9f0217c)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1481978357/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1481978357&linkId=2f3acf998de645990b681e2ac9f0217c">
        <img src="./static/The Problem of HFT.jpeg" style="width:660px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          This book explores the problem of high-frequency trading (HFT) as well as the need for US stock market reform. This collection of previously published and unpublished materials includes the following articles and white papers: The Problem of HFT HFT Scalping Strategies Why HFTs Have an Advantage Electronic Liquidity Strategy HFT – A Systemic Issue Reforming the National Market System NZZ Interview with Haim Bodek TradeTech Interview with Haim Bodek Modern HFT wasn’t a paradigm shift because its innovations brought new efficiencies into the marketplace. HFT was a paradigm shift because its innovations proved that anti-competitive barriers to entry could be erected in the market structure itself to preference one class of market participant above all others.
        </li>
      </ul>
    </td>
  </tr>
</table>

## Machine Learning

[Advances in Financial Machine Learning - Marcos Lopez de Prado](https://www.amazon.fr/gp/product/1119482089/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1119482089&linkId=7eff4d3f3d9f2d00d05032f726386e53)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1119482089/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1119482089&linkId=7eff4d3f3d9f2d00d05032f726386e53">
        <img src="./static/Advances in Financial Machine Learning.jpeg" style="width:365px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Machine learning (ML) is changing virtually every aspect of our lives. Today ML algorithms accomplish tasks that until recently, only expert humans could perform. As it relates to finance, this is the most exciting time to adopt a disruptive technology that will transform how everyone invests for generations.
        </li>
        <li>
          Readers will learn how to structure Big data in a way that is amenable to ML algorithms; how to conduct research with ML algorithms on that data; how to use supercomputing methods; how to backtest your discoveries while avoiding false positives.
        </li>
        <li>
          The book addresses real-life problems faced by practitioners daily and explains scientifically sound solutions using math, supported by code and examples. Readers become active users who can test the proposed solutions in their particular setting. Written by a recognized expert and portfolio manager, this book will equip investment professionals with the groundbreaking tools needed to succeed in modern finance.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Algorithmic Trading Methods: Applications Using Advanced Statistics, Optimization, and Machine Learning Techniques - Robert Kissell](https://www.amazon.fr/gp/product/0128156309/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0128156309&linkId=0a197c0b547a0ee63ccd19389bb42edd)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0128156309/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0128156309&linkId=0a197c0b547a0ee63ccd19389bb42edd">
        <img src="./static/Algorithmic Trading Methods.jpeg" style="width:990px;">
      </a>
    </td>
    <td>
      <ul>
        <li>
          Algorithmic Trading Methods: Applications using Advanced Statistics, Optimization, and Machine Learning Techniques, Second Edition, is a sequel to The Science of Algorithmic Trading and Portfolio Management. This edition includes new chapters on algorithmic trading, advanced trading analytics, regression analysis, optimization, and advanced statistical methods. Increasing its focus on trading strategies and models, this edition includes new insights into the ever-changing financial environment, pre-trade and post-trade analysis, liquidation cost & risk analysis, and compliance and regulatory reporting requirements. Highlighting new investment techniques, this book includes material to assist in the best execution process, model validation, quality and assurance testing, limit order modelling, and smart order routing analysis. Includes advanced modeling techniques using machine learning, predictive analytics, and neural networks. The text provides readers with a suite of transaction cost analysis functions packaged as a TCA library. These programming tools are accessible via numerous software applications and programming languages.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Artificial Intelligence in Finance: A Python-Based Guide - Yves Hilpisch](https://www.amazon.fr/gp/product/1492055433/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1492055433&linkId=7c20249be4d35badb127d6a5423fc495)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1492055433/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1492055433&linkId=7c20249be4d35badb127d6a5423fc495">
        <div style="width:100px">
          <img src="./static/Artificial Intelligence in Finance.jpeg" style="width:410px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          The application of AI to financial trading is still a nascent field, although at the time of writing there are a number of other books available that cover this topic to some extent. Many of these publications, however, fail to show what it means to economically exploit statistical inefficiencies.
        </li>
        <li>
          Some hedge funds already claim to exclusively rely on machine learning to manage their investors’ capital. A prominent example is The Voleon Group, a hedge fund that reported more than six billion dollars (USD) in assets under management at the end of 2019 (see Lee and Karsh 2020). The difficulty of relying on machine learning to outsmart the financial markets is reflected in the fund’s performance of 7% for 2019, a year during which the S&P 500 stock index rose by almost 30%.
        </li>
      </ul>
    </td>
  </tr>
</table>


[Dark Pools: The rise of A.I. trading machines and the looming threat to Wall Street - Scott Patterson](https://www.amazon.fr/gp/product/0307887189/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0307887189&linkId=2572cae24ed7de0b279580312daf0f03)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/0307887189/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0307887189&linkId=2572cae24ed7de0b279580312daf0f03">
        <div style="width:100px">
          <img src="./static/Dark Pools.jpeg" style="width:340px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Dark Pools is pacy, revealing, and profoundly chilling tale of how global markets have been hijacked by trading robots – many so self-directed that humans can’t predict what they’ll do next. It’s the story of the blisteringly intelligent computer programmers behind the rise of these ‘bots’. And it’s a timely warning that as artificial intelligence gradually takes over, we could be on the verge of global meltdown.
        </li>
      </ul>
    </td>
  </tr>
</table>



[Machine Learning for Asset Managers (Elements in Quantitative Finance) - Marcos M López de Prado](https://www.amazon.fr/gp/product/1108792898/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1108792898&linkId=8eb7e3c369d38b36df8dfecf05a622db)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1108792898/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1108792898&linkId=8eb7e3c369d38b36df8dfecf05a622db">
        <div style="width:100px">
          <img src="./static/Machine Learning for Asset Managers.jpeg" style="width:275px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          Successful investment strategies are specific implementations of general theories. An investment strategy that lacks a theoretical justification is likely to be false. Hence, an asset manager should concentrate her efforts on developing a theory rather than on backtesting potential trading rules.
        </li>
        <li>
          The purpose of this Element is to introduce machine learning (ML) tools that can help asset managers discover economical and financial theories. ML is not a black box, and it does not necessarily overfit. ML tools complement rather than replace the classical statistical methods. Some of ML’s strengths include:
          <ol>
            <li>
              a focus on out-of-sample predictability over variance adjudication
            </li>
            <li>
              the use of computational methods to avoid relying on (potentially unrealistic) assumptions
            </li>
            <li>
              the ability to “”learn”” complex specifications, including nonlinear, hierarchical, and noncontinuous interaction effects in a high-dimensional space
            </li>
            <li>
              the ability to disentangle the variable search from the specification search, robust to multicollinearity and other substitution effects.
            </li>
          </ol>
        </li>
      </ul>
    </td>
  </tr>
</table>

[Machine Learning for Algorithmic Trading: Predictive models to extract signals from market and alternative data for systematic trading strategies with Python, 2nd Edition - Stefan Jansen](https://www.amazon.fr/gp/product/1839217715/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1839217715&linkId=80e3e93e1b6027596858ed0f1fbf10c2)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/1839217715/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1839217715&linkId=80e3e93e1b6027596858ed0f1fbf10c2">
        <div style="width:100px">
          <img src="./static/Machine Learning for Algorithmic Trading.jpeg" style="width:265px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          The explosive growth of digital data has boosted the demand for expertise in trading strategies that use machine learning (ML). This revised and expanded second edition enables you to build and evaluate sophisticated supervised, unsupervised, and reinforcement learning models.
        </li>
        <li>
          This book introduces end-to-end machine learning for the trading workflow, from the idea and feature engineering to model optimization, strategy design, and backtesting. It illustrates this by using examples ranging from linear models and tree-based ensembles to deep-learning techniques from cutting edge research.
        </li>
      </ul>
    </td>
  </tr>
</table>

[Machine Learning in Finance: From Theory to Practice - Matthew F. Dixon, Igor Halperin, Paul Bilokon](https://www.amazon.fr/gp/product/3030410676/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=3030410676&linkId=5f5f1df6be62ae96ef7a0c536c3ecdb4)

<table>
  <tr>
    <td>
      <a href="https://www.amazon.fr/gp/product/3030410676/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=3030410676&linkId=5f5f1df6be62ae96ef7a0c536c3ecdb4">
        <div style="width:100px">
          <img src="./static/Machine Learning in Finance.jpeg" style="width:650px;">
        </div>
      </a>
    </td>
    <td>
      <ul>
        <li>
          This book introduces machine learning methods in finance. It presents a unified treatment of machine learning and various statistical and computational disciplines in quantitative finance, such as financial econometrics and discrete-time stochastic control, with an emphasis on how theory and hypothesis tests inform the choice of algorithm for financial data modelling and decision making. With the trend towards increasing computational resources and larger datasets, machine learning has grown into an important skillset for the finance industry. This book is written for advanced graduate students and academics in financial econometrics, mathematical finance and applied statistics, in addition to quants and data scientists in the field of quantitative finance.
        </li>
      </ul>
    </td>
  </tr>
</table>


# Blogs

- [AAA Quants, Tom Starke Blog](http://aaaquants.com/category/blog/)
- [Blackarbs blog](http://www.blackarbs.com/blog/)
- [Hardikp, Hardik Patel blog](https://www.hardikp.com/)
- :star: [Max Dama on Automated Trading](https://bit.ly/3wVZbh9)
- [Proof Engineering: The Algorithmic Trading Platform](https://bit.ly/3lX7zYN)
- [Quantsportal, Jacques Joubert's Blog](http://www.quantsportal.com/blog-page/)
- :star: [Quantstart - Machine Learning for Trading articles](https://www.quantstart.com/articles)
- [RobotWealth, Kris Longmore Blog](https://robotwealth.com/blog/)
- More is coming... (PR welcome)


# Courses and Tutorials

- [AI in Finance](https://cfte.education/) - Learn Fintech Online.
- [Algorithmic Trading for Cryptocurrencies in Python](https://github.com/tudorelu/tudorials/tree/master/trading) - A simple yet practical experiment tutorial for cryto trading.
- Coursera, NYU - Machine Learning and Reinforcement Learning in Finance Specialization (Weakly related to trading)
  - [Coursera, NYU - Guided Tour of Machine Learning in Finance](https://www.coursera.org/learn/guided-tour-machine-learning-finance)
  - [Coursera, NYU - Fundamentals of Machine Learning in Finance](https://www.coursera.org/learn/fundamentals-machine-learning-in-finance)
  - [Coursera, NYU - Reinforcement Learning in Finance](https://www.coursera.org/learn/reinforcement-learning-in-finance)
  - [Coursera, NYU - Overview of Advanced Methods for Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance)- [Hudson and Thames Quantitative Research](https://github.com/hudson-and-thames) - Our mission is to promote the scientific method within investment management by codifying frameworks, algorithms, and best practices.
- [NYU: Overview of Advanced Methods of Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance/home/welcome)
- [Udacity: Artificial Intelligence for Trading](https://www.udacity.com/course/ai-for-trading--nd880)
- [Udacity, Georgia Tech - Machine Learning for Trading](https://www.udacity.com/course/machine-learning-for-trading--ud501)
- More is coming... (PR welcome)

## Interviews

- [Better System Trader EP023 - Portfolio manager Michael Himmel talks AI and machine learning in trading](https://www.youtube.com/watch?v=9tZjeyhfG0g)
- :star: [Better System Trader EP028 - David Aronson shares research into indicators that identify Bull and Bear markets.](https://www.youtube.com/watch?v=Q4rV0Y9NokI)
- :star: [Chat with Traders EP042 - Machine learning for algorithmic trading with Bert Mouler](https://www.youtube.com/watch?v=i8FNO8r7PaE)
- :star: [Better System Trader EP064 - Cryptocurrencies and Machine Learning with Bert Mouler](https://www.youtube.com/watch?v=YgRTd4nLJoU)
- [Better System Trader EP082 - Machine Learning With Kris Longmore](https://www.youtube.com/watch?v=0syNgsd635M)
- [Better System Trader EP090 - This quants’ approach to designing algo strategies with Michael Halls-Moore](https://chatwithtraders.com/ep-090-michael-halls-moore/)* [Chat With Traders EP131 - Trading strategies, powered by machine learning with Morgan Slade](https://www.youtube.com/watch?v=EbWbeYu8zwg)
- :star: [Chat with Traders EP142 - Algo trader using automation to bypass human flaws with Bert Mouler](https://www.youtube.com/watch?v=ofL66mh6Tw0)
- [Chat with Traders EP147 - Detective work leading to viable trading strategies with Tom Starke](https://www.youtube.com/watch?v=JjXw9Mda7eY)
- :star: [Chat with Traders Quantopian 5 - Good Uses of Machine Learning in Finance with Max Margenot](https://www.youtube.com/watch?v=Zj5sXWv9SDM)

## Videos

- [Ernie Chan - Machine Learning for Quantitative Trading Webinar](https://www.youtube.com/watch?v=72aEDjwGMr8&t=1023s)
- [Hitoshi Harada, CTO at Alpaca - Deep Learning in Finance Talk](https://www.youtube.com/watch?v=FoQKCeDuPiY)
- :star: [Howard Bandy - Machine Learning Trading System Development Webinar](https://www.youtube.com/watch?v=v729evhMpYk&t=1s)
- [Krish Naik - Machine learning tutorials and their Application in Stock Prediction](https://www.youtube.com/watch?v=H6du_pfuznE)
- [Master Thesis presentation, Uni of Essex - Analyzing the Limit Order Book, A Deep Learning Approach](https://www.youtube.com/watch?v=qxSh2VFmRGw)
- [Prediction Machines - Deep Learning with Python in Finance Talk](https://www.youtube.com/watch?v=xvm-M-R2fZY)
- [QuantInsti Youtube - webinars about Machine Learning for trading](https://www.youtube.com/user/quantinsti/search?query=machine+learning)
- [QuantNews - Machine Learning for Algorithmic Trading 3 part series](https://www.youtube.com/playlist?list=PLHJACfjILJ-91qkw5YC83S6COKGscctzz)
- :star: [Quantopian - Webinars about Machine Learning for trading](https://www.youtube.com/channel/UC606MUq45P3zFLa4VGKbxsg/search?query=machine+learning)
- [Sentdex - Machine Learning for Forex and Stock analysis and algorithmic trading](https://www.youtube.com/watch?v=v_L9jR8P-54&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO)
- [Sentdex - Python programming for Finance (a few videos including Machine Learning)](https://www.youtube.com/watch?v=Z-5wNWgRJpk&index=9&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ)
- :star: [Siraj Raval - Videos about stock market prediction using Deep Learning](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A/search?query=trading)
- [Tucker Balch - Applying Deep Reinforcement Learning to Trading](https://www.youtube.com/watch?v=Pka0DC_P17k)

