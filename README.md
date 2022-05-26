<div align="center">
  <img src="static/future-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic (Futures) Trading</h1>
</div>

We're collecting (an admittedly opinionated) list of resources papers, datasets, blogs, libraries, books and methodologies for finding, developing, and running Systematic Trading (Quantitative Trading) on Futures.

What will you find here?

- 89 scientific papers describing systematic trading strategies
- 82 futures datasets
- 56 books for quantitative traders
- A unique quantitative modeling methodology
- A more

How do we pick the resources?

- Fit in systematic futures trading domain
- Focus on mid/low frequency strategies for tradability
- Rational giving reasonable probability to bring above market performances

*We're only at the beginning, and you can help by contributing to this GitHub!*

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

- [Strategy Papers](#strategy-papers)
  - [Bonds](#bonds)
  - [Bonds, Commodities, Currencies, Equities](#bonds-commodities-currencies-equities)
  - [Bonds, Currencies, Equities](#bonds-currencies-equities)
  - [Bonds, Equities](#bonds-equities)
  - [Commodities](#commodities)
  - [Commodities, Equities](#commodities-equities)
  - [Cryptos](#cryptos)
  - [Currencies](#currencies)
  - [Equities](#equities)
- [Datasets (coming soon)](#datasets-coming-soon)
- [Modeling Methodology](#modeling-methodology)
- [Books](#books)
- [Blogs](#blogs)
- [Basic Libraries](#basic-libraries)

# Strategy Papers

List of **89 scientific papers** describing original systematic futures trading strategies. Each strategy is categorized by its asset class (Bonds, Commodities, Cryptos, Currencies, Equities), ordered by descending Sharpe ratio, and described by its Sharpe ratio, volatility and period of rebalancing.

## Bonds

[Market Closure and Short-Term Reversal](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2730304)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.89         | 7.69%      | Weekly                |

[Finding Yield in a 2% World](https://mebfaber.com/wp-content/uploads/2016/05/SSRN-id2724737.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.68         | 8.63%      | Monthly               |

[Profiting from Mean-Reverting Yield Curve Trading Strategies](https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=3488&context=lkcsb_research)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.65         | 15%        | Monthly               |

[Profitability of Simple Trading Strategies Exploiting the Forward Premium Bias in Foreign Exchange Markets and the Time Premium in Yield Curves](https://haldus.eestipank.ee/sites/default/files/publication/en/WorkingPapers/2006/_wp_406.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.62         | 10%        | Monthly               |

[Short-Term Momentum (Almost) Everywhere](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3340085)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.62         | 9.69%      | Monthly               |

[Cross-Sectional Seasonalities in International Government Bond Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3212995)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.56         | 13.85%     | Monthly               |

[Beyond Carry and Momentum in Government Bonds](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3446653)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.13         | 10.1%      | Monthly               |

[Carry investing on the yield curve](https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2017-Athens/papers/EFMA2017_0407_fullpaper.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |

## Bonds, Commodities, Currencies, Equities

[Carry](https://pages.stern.nyu.edu/~lpederse/papers/Carry.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.41         | 4.9%       | Monthly               |

[Time Series Reversal in Trend Following Strategies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2971875)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.17         | 20.9%      | Monthly               |

[Return Signal Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2971444)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.97         | 12.3%      | Monthly               |

[Carry and time‐series momentum: a match made in Heaven](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3470864)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.92         | 10%        | Monthly               |

[Predicting Out-of-Sample Returns: Using Basis to Beat the Historical Average](https://www.researchgate.net/publication/324670834_Predicting_Out-of-Sample_Returns_Using_Basis_to_Beat_the_Historical_Average)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.49         | 7.67%      | Monthly               |

## Bonds, Currencies, Equities

[Trend-Following and Spillover Effects](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3473657)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.67         | 4.8%       | Weekly                |

[Cross-Sectional and Time-Series Tests of Return Predictability: What is the Difference?](http://www.smallake.kr/wp-content/uploads/2016/03/581.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.5          | 12.91%     | 6 Months              |


## Bonds, Equities

[Worth It’s Weight in Gold Offense and Defense in Active Portfolio Management](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2604248)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.84         | 11.8%      | Weekly                |

[Return Predictability and Market-Timing: A One-Month Model](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3050254)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.72         | 11.05%     | Monthly               |

[Cross-Asset Signals and Time Series Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2891434)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.65         | 10%        | Monthly               |

[Opposing Seasonalities in Treasury versus Equity Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=891215)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | 6 Months              |

## Commodities

[Pairs Trading the Commodity Futures Curve](http://jultika.oulu.fi/files/nbnfioulu-201211141056.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 3.09         | 2.01%      | Monthly               |

[Timing Commodity Momentum](https://risk.edhec.edu/sites/risk/files/EDHEC_Working_Paper_Timing_Commodity_Momentum.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 2.41         | 11.09%     | Monthly               |

[Short-Term Momentum (Almost) Everywhere](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3340085)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.01         | 20.86%     | Monthly               |

[Basis-momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2587784)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.92         | 19.98%     | Monthly               |

[Is Gold a Zero-Beta Asset? Analysis of the Investment Potential of Precious Metals](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=920496)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.91         | 29.63%     | Monthly               |

[Fear of Hazards in Commodity Futures Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3411117)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.89         | 9.26%      | Weekly                |

[Long-Run Reversal in Commodity Returns: Insights from Seven Centuries of Evidence](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3314834)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.83         | 19.37%     | Yearly                |

[Tactical allocation in commodity futures markets: Combining momentum and term structure signals](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1127213)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.79         | 27.6%      | Monthly               |

[Modeling, Forecasting and Trading the Crude Oil Term Structure](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2874869)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.76         | 7.1%       | Weekly                |

[Trend Following, Risk Parity and Momentum in Commodity Futures](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2126813)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.76         | 19.33%     | Monthly               |

[Commodity Option Implied Volatilities and the Expected Futures Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2939649)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.69         | 18.48%     | Monthly               |

[Commodity Strategies Based on Momentum, Term Structure and Idiosyncratic Volatility](https://risk.edhec.edu/sites/risk/files/edhec-working-paper-commodity-strategies-based-on-momentum_1368521019664_0.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.68         | 10.79%     | Monthly               |

[Idiosyncratic momentum in commodity futures](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3035397)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.59         | 29.42%     | Monthly               |

[Commodity Strategies Based on Momentum, Term Structure and Idiosyncratic Volatility](https://risk.edhec.edu/sites/risk/files/edhec-working-paper-commodity-strategies-based-on-momentum_1368521019664_0.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 19.3%      | Weekly                |

[Dynamic Commodity Timing Strategies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=581423)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 18%        | Monthly               |

[Long-Short Commodity Investing: Implications for Portfolio Risk and Market Regulation](https://risk.edhec.edu/sites/risk/files/edhec_working_paper_long-short_commodity_investing.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.41         | 18.09%     | Weekly                |

[Multi-Asset Seasonality and Trend-Following Strategies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2710334)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.38         | 9.32%      | Monthly               |

[The Case for Long-Short Commodity Investing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1920454)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.25         | 17.17%     | Weekly                |

[Investor Sentiment And Return Predictability in Agricultural Futures Market](https://mpra.ub.uni-muenchen.de/36425/1/MPRA_paper_36425.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Weekly                |

[Political Uncertainty and Commodity Prices](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3064295)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Quarterly             |

[The Autumn Effect of Gold](https://ideas.repec.org/a/eee/riibaf/v27y2013i1p1-11.html)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |

[What does futures market interest tell us about the macroeconomy and asset prices?](https://www.nber.org/system/files/working_papers/w16712/w16712.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |

## Commodities, Equities

[How to Time the Commodity Market](https://www.edhec.edu/sites/www.edhec-portail.pprod.net/files/publications/pdf/com.univ.collaboratif.utils.LectureFichiergw%3FID_FICHIER%3D1328885972050jpg)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.24         | 10.3%      | Weekly                |

[When to Own Stocks and When to Own Gold](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3535152)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 14%        | Yearly                |

## Cryptos

["Know when to hodl them, know when to fodl them": An Investigation of Factor Based Investing in the Cryptocurrency Space](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3055498)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.13         | 7.1%       | Weekly                |

[Do Fundamentals Drive Cryptocurrency Prices](https://wpcarey.asu.edu/sites/default/files/2021-11/george_korniotis_seminar_paper_november_8_2019.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.06         | 9.3%       | Weekly                |

## Currencies

[Combining Mean Reversion and Momentum Trading Strategies in Foreign Exchange Markets](http://www.forexmentoronline.com/wp-content/uploads/2015/11/09-14.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 2.43         | 10%        | Monthly               |

[Beyond the Carry Trade: Optimal Currency Portfolios](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2041460)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.4          | 23.89%     | Monthly               |

[A Low-Risk Strategy based on Higher Moments in Currency Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2666223)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.38         | 8%         | Monthly               |

[Economic Momentum and Currency Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2579666)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.1          | 5.6%       | Monthly               |

[Are Value Strategies Profitable in the Foreign Exchange Market?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2559375)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.01         | 9.51%      | Monthly               |

[Cross-Asset Return Predictability: Carry Trades, Stocks and Commodities](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2399282)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.01         | 9.07%      | Monthly               |

[Optimal and Naive Diversification in Currency Markets](https://www.researchgate.net/publication/306128512_Optimal_and_Naive_Diversification_in_Currency_Markets)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.99         | 6.97%      | Monthly               |

[Basis-momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2587784)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.91         | 9.23%      | Monthly               |

[Market Closure and Short-Term Reversal](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2730304)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.9          | 10.23%     | Weekly                |

[Is There Momentum or Reversal in Weekly Currency Returns?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2258253)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.88         | 8.1%       | Weekly                |

[The Revenge of Purchasing Power Parity on Carry Trades during Crises](https://ideas.repec.org/p/sol/wpaper/09-013.html)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.87         | 4.97%      | Monthly               |

[Predictability of Currency Carry Trades and Asset Pricing Implications](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1977642)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.86         | 10%        | Monthly               |

[Carry On](https://jai.pm-research.com/content/22/2/100.short)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.82         | 2.47%      | Monthly               |

[The Term Structure of Sovereign CDS and the Cross-Section Exchange Rate Predictability](http://wp.lancs.ac.uk/fofi2018/files/2018/03/FoFI-2018-0071-Giovanni-Calice.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.82         | 5.92%      | Monthly               |

[Forward-Looking Policy Rules and Currency Premia](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3412612)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.81         | 7.61%      | Monthly               |

[U.S. Equity Tail Risk and Currency Risk Premia](https://www.federalreserve.gov/econres/ifdp/files/ifdp1253.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.75         | 8.12%      | Monthly               |

[Perceived corruption, carry trades, and the cross section of currency returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2961743)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.74         | 8.14%      | Yearly                |

[The Equity Differential Factor in Currency Markets](https://www.tandfonline.com/doi/epub/10.1080/0015198X.2020.1712924?needAccess=true)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.61         | 3.1%       | Monthly               |

[Investor sentiment, attention and profitability of currency momentum strategies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2862161)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.56         | 10.36%     | Monthly               |

[The Rise and Fall of the Carry Trade: Links to Exchange Rate Predictability](https://www.researchgate.net/publication/336206761_The_Rise_and_Fall_of_the_Carry_Trade_Links_to_Exchange_Rate_Predictability)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.55         | 19.65%     | Monthly               |

[Yield Curve Predictors of Foreign Exchange Returns](https://www0.gsb.columbia.edu/faculty/aang/papers/FXrets.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.52         | 3.67%      | Monthly               |

[A Multi Strategy Approach to Trading Foreign Exchange Futures](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3322717)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.5          | 13.16%     | Monthly               |

[Carry Trades and Global Foreign Exchange Volatility](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1342968)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.48         | 8.68%      | 6 Months              |

[From Carry Trades to Curvy Trades](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2149.en.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.39         | 6.7%       | Monthly               |

[International Diversification Benefits with Foreign Exchange Investment Styles](https://academic.oup.com/rof/article/18/5/1847/1575295)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.33         | 9.56%      | Monthly               |

[Speculation and Hedging in the Currency Futures Markets: Are They Informative to the Spot Exchange Rates](https://economics.umbc.edu/files/2014/09/wp_09_116.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Weekly                |

## Equities

[The Presidential Term: Is the Third Year the Charm?](http://www.uwosh.edu/faculty_staff/beyers/workingpapers/Presidential%20Cycle%20JPM%20forthcoming.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.29         | 15.34%     | Yearly                |

[Expected Option Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=189840)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 1.16         | 19%        | Monthly               |

[Stock Returns over the FOMC Cycle](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2687614)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.83         | 13.92%     | Weekly                |

[Combining equity country selection strategies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2616056)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.82         | 24.53%     | Monthly               |

[Market Timing with Aggregate Accruals](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.383.7502&rep=rep1&type=pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.8          | 37.7%      | Yearly                |

[Short-Term Momentum (Almost) Everywhere](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3340085)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.8          | 20.38%     | Monthly               |

[Seven Decades of Long Term Abnormal Return Persistence: The Case of Dividend Initiations and Resumptions](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=204437)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.78         | 6.74%      | Monthly               |

[Return Predictability and Market-Timing: A One-Month Model](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3050254)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.76         | 16.6%      | Monthly               |

[Time-Varying Sharpe Ratios and Market Timing](https://pages.stern.nyu.edu/~rwhitela/papers/tvsharpe.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.66         | 15.38%     | Monthly               |

[Exploiting the Informational Content of Hedging Pressure: Timing the Market by "Learning" from Derivatives Traders](https://www.edhec.edu/sites/www.edhec-portail.pprod.net/files/publications/pdf/com.univ.collaboratif.utils.LectureFichiergw%3FID_FICHIER%3D1328885972665jpg)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.52         | 11%        | Weekly                |

[Stock Return Predictability and Seasonality](http://www.apjfs.org/resource/global/cafm/2018-5-1.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.46         | 17.78%     | 6 Months              |

[Equity premiums in the Presidential cycle: The midterm election resolution of uncertainty](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2903067)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.47         | 24.47%     | 6 Months              |

[Market Timing with Aggregate and Idiosyncratic Stock Volatilities](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=869447)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.43         | 37.8%      | Quarterly             |

[Forecasting the size premium over different time horizons](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1951931)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.38         | 14.62%     | Monthly               |

[Alpha Momentum and Alpha Reversal in Country and Industry Equity](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3235350)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.31         | 20.02%     | Monthly               |

[A Performance Evaluation Model for Global Macro Funds](https://www.researchgate.net/publication/334653500_A_Performance_Evaluation_Model_for_Global_Macro_Funds)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| 0.3          | 9.21%      | Monthly               |

[Contrarian Long-Short Futures Arbitrages and Market Efficiency: Evidence in the Index Futures Markets around the Globe](http://centerforpbbefr.rutgers.edu/2006/Paper%202006/12AS01-046-INT_Index_Futures.pdf)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Weekly                |

[Does Sentiment Matter?](https://www.researchgate.net/publication/228760482_Does_sentiment_matter)

| Sharpe Ratio | Volatility | Period of Rebalancing |
|--------------|------------|-----------------------|
| N/A          | N/A        | Monthly               |



# Datasets (coming soon)

List of **[82 futures datasets](datasets.md)** covering prices, volumes, COT, and much more.

| Ticker | Name                    | Exchange | Link          |
|--------|-------------------------|----------|---------------|
| BO     | Soybean Oil             | CME      | [Download](#) |
| C      | Corn                    | CME      | [Download](#) |
| CC     | Cocoa                   | NYBOT    | [Download](#) |
| CT     | Cotton #2               | NYCE     | [Download](#) |
| FC     | Feeder Cattle           | CME      | [Download](#) |
| JRB    | Azuki Beans-Red         | TGE      | [Download](#) |
| KC     | Coffee                  | CSCE     | [Download](#) |
| LB     | Random Length Lumber    | CME      | [Download](#) |
| LC     | Live Cattle             | CME      | [Download](#) |
| LH     | Lean Hogs               | CME      | [Download](#) |
| O      | Oats                    | CME      | [Download](#) |
| OJ     | Orange Juice A          | NYCE     | [Download](#) |
| RR     | Rough Rice              | CME      | [Download](#) |
| RS     | Rapeseed (Canola)       | WCE      | [Download](#) |
| S      | Soybean                 | CME      | [Download](#) |
| SB     | Sugar No. 11            | CSCE     | [Download](#) |
| SM     | Soybean Meal            | CME      | [Download](#) |
| SRS    | Rubber RSS1             | TCE      | [Download](#) |
| W      | Wheat                   | CME      | [Download](#) |

👉 [**The rest of the list is on its dedicated page.**](datasets.md)


# Modeling Methodology

[Modeling Methodology Area Page](modeling-methodology.md)

This section outlines a **[quantitative methodology](modeling-methodology.md)** for identifying systematic training signals.

To start, when you develop a systematic trading strategy, you need to make a distinction between two main types of variables in your dataset:

- **the variables to be explained** (which correspond to market characteristics that can be exploited in terms of trading)
- and **the potentially explanatory variables**.

> A multi-scale view of the variables must always be maintained. The more independent scales the multiscale analysis will reveal, the more easily they will be recombined.

A first step is to label the data. You need to pre-compute a multi-scale target signal, which is the one you will then try to predict. A very important point is that you are allowed to use future information for this.

Then you need to decompose the explanatory variables on multiple scales and make them independent.
In this step, you will have to see the results of the pre-treatments as estimators, and retain the uncertainty that they owe to the estimation processes that allowed them to be estimated.

You will systematically use descriptive statistics to qualify a variable before including it in any further analysis.

👉 [**The rest of the methodology is on its dedicated page.**](modeling-methodology.md)

# Books

A comprehensive list of **[56 books](books.md)** for quantitative traders.

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

👉 [**The rest of the list is on its dedicated page.**](books.md)

# Blogs

- [Proof Engineering: The Algorithmic Trading Platform](https://medium.com/prooftrading/proof-engineering-the-algorithmic-trading-platform-b9c2f195433d)
- [Max Dama on Automated Trading](http://isomorphisms.sdf.org/maxdama.pdf)


# Basic Libraries

Machine learning:

- [MlFinLab (Hudson & Thames)](https://github.com/edarchimbaud/mlfinlab) - MlFinLab helps portfolio managers and traders who want to leverage the power of machine learning by providing reproducible, interpretable, and easy to use tools.
- [QLib (Microsoft)](https://github.com/microsoft/qlib) - Qlib is an AI-oriented quantitative investment platform, which aims to realize the potential, empower the research, and create the value of AI technologies in quantitative investment. With Qlib, you can easily try your ideas to create better Quant investment strategies. An increasing number of SOTA Quant research works/papers are released in Qlib.


Metrics computation:

- [quantstats](https://github.com/ranaroussi/quantstats) - Portfolio analytics for quants, written in Python

Visualization:

- [D-Tale (Man Group)](https://github.com/man-group/dtale) - D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures.