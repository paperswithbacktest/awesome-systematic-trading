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
- [Datasets (coming soon)](#datasets-coming-soon)
- [Modeling Methodology](#modeling-methodology)
- [Books](#books)
- [Blogs](#blogs)
- [Basic Libraries](#basic-libraries)

# Strategy Papers

List of **[89 scientific papers](strategy-papers.md)** describing original systematic futures trading strategies. Each strategy is categorized by its asset class (Bonds, Commodities, Cryptos, Currencies, Equities), ordered by descending Sharpe ratio, and described by its Sharpe ratio, volatility and period of rebalancing.

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

👉 [**The rest of the list is here**](strategy-papers.md)


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

👉 [**The rest of the list is here**](datasets.md)


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

👉 [**The rest of the methodology is here**](modeling-methodology.md)

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

👉 [**The rest of the list is here**](books.md)

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