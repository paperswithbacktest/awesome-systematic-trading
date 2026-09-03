<div align="center">
  <img src="static/images/awesome-systematic-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

[希望阅读中文版？点我](./README_zh.md)<br>
[日本語版はこちら](./README_ja.md)

We are collecting a list of resources papers, softwares, books, articles for finding, developing, and running systematic trading (quantitative trading) strategies.

<!-- omit in toc -->
### What will you find here?

- [136 libraries and packages](#libraries-and-packages) for research and live trading, with dead and dormant projects flagged
- [Strategies](#strategies) from published papers, with the Sharpe ratio each one produced when it was coded and run
- [55 books](#books) for beginners and professionals
- [22 videos](#videos) and interviews
- And also some [blogs](#blogs) and [courses](#courses)

<!-- omit in toc -->
### What the replication record looks like

We have coded and run 4,843 of these papers over their own full history. Some numbers worth
knowing before you pick one to implement:

- The median replication returns a **Sharpe ratio of 0.37**, and **48% clear a t-statistic of 1.96**.
  Half the published record cannot be distinguished from zero on its own sample.
- Median test window: **34 years**. A strategy needs roughly `(1.96 / Sharpe)²` years to prove
  itself, so a Sharpe of 0.4 needs about 24 of them.
- The median strategy carries a **beta of +0.17** to the S&P 500. Removing it takes the median
  information ratio down to **0.21**, so a meaningful slice of the published edge is index
  exposure rather than skill.
- Across 2,838 papers with a record on both sides of their publication date, we could find **no
  measurable decay after publication** once the market period is controlled for, to within a fifth
  of a percentage point a year.

Method and caveats are written up on [the wiki](https://paperswithbacktest.com/wiki).

<div align="center" style="margin-bottom: 50px; margin-top: 50px;">
  <div style="border: 2px solid #007bff; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
    <h2>📈 Interested in trading strategies implemented in Python?</h2>
    <p>Visit our comprehensive collection at <a href="https://paperswithbacktest.com" target="_blank">paperswithbacktest.com</a> for exclusive content!</p>
  </div>
</div>


<details>
<summary>Click here to see the full table of content</summary>

- [Libraries and packages](#libraries-and-packages)
  - [Backtesting and Live Trading](#backtesting-and-live-trading)
    - [General - Event Driven Frameworks](#general---event-driven-frameworks)
    - [General - Vector Based Frameworks](#general---vector-based-frameworks)
    - [Cryptocurrencies](#cryptocurrencies)
  - [Trading bots](#trading-bots)
  - [Analytics](#analytics)
    - [Indicators](#indicators)
    - [Metrics computation](#metrics-computation)
    - [Optimization](#optimization)
    - [Pricing](#pricing)
    - [Risk](#risk)
  - [Broker APIs](#broker-apis)
  - [Data Sources](#data-sources)
    - [General](#general)
    - [Cryptocurrencies](#cryptocurrencies-1)
  - [Data Science](#data-science)
  - [Databases](#databases)
  - [Graph Computation](#graph-computation)
  - [Machine Learning](#machine-learning)
  - [TimeSeries Analysis](#timeseries-analysis)
  - [Visualization](#visualization)
- [Strategies](#strategies)
  - [Equities](#equities)
  - [Bonds](#bonds)
  - [Commodities](#commodities)
  - [Currencies](#currencies)
  - [Cryptocurrencies](#cryptocurrencies-2)
  - [Derivatives](#derivatives)
  - [Multi-asset](#multi-asset)
- [Books](#books)
  - [Beginner](#beginner)
  - [Biography](#biography)
  - [Coding](#coding)
  - [Crypto](#crypto)
  - [General](#general-1)
  - [High Frequency Trading](#high-frequency-trading)
  - [Machine Learning](#machine-learning-1)
- [Videos](#videos)
- [Blogs](#blogs)
- [Courses](#courses)
</details>

<!-- omit in toc -->
> ### How can I help?
> You can help by submitting an issue with suggestions and by sharing on Twitter:
>
> [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=A%20free%20and%20comprehensive%20list%20of%20papers%2C%20libraries%2C%20books%2C%20blogs%2C%20tutorials%20for%20quantitative%20traders.&url=https://github.com/paperswithbacktest/awesome-systematic-trading)


# Libraries and packages

*List of **136 libraries and packages** implementing trading bots, backtesters, indicators, pricers, etc. Each library is categorized by its programming language and ordered by descending populatrity (number of stars).*


## Backtesting and Live Trading

### General - Event Driven Frameworks


| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [vnpy](https://github.com/vnpy/vnpy) | Python-based open source quantitative trading system development framework, officially released in January 2015, has grown step by step into a full-featured quantitative trading platform | ![GitHub stars](https://badgen.net/github/stars/vnpy/vnpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zipline](https://github.com/quantopian/zipline) `dormant since 2024-02` | Zipline is a Pythonic algorithmic trading library. It is an event-driven system for backtesting. | ![GitHub stars](https://badgen.net/github/stars/quantopian/zipline) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtrader](https://github.com/mementum/backtrader) `dormant since 2024-08` | Event driven Python Backtesting library for trading strategies | ![GitHub stars](https://badgen.net/github/stars/mementum/backtrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS) | QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权/港股/虚拟货币 数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案 | ![GitHub stars](https://badgen.net/github/stars/QUANTAXIS/QUANTAXIS) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QuantConnect](https://github.com/QuantConnect/Lean) | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) | ![GitHub stars](https://badgen.net/github/stars/QuantConnect/Lean) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Rqalpha](https://github.com/ricequant/rqalpha) | A extendable, replaceable Python algorithmic backtest && trading framework supporting multiple securities | ![GitHub stars](https://badgen.net/github/stars/ricequant/rqalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finmarketpy](https://github.com/cuemacro/finmarketpy) | Python library for backtesting trading strategies & analyzing financial markets (formerly pythalesians) | ![GitHub stars](https://badgen.net/github/stars/cuemacro/finmarketpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtesting.py](https://github.com/kernc/backtesting.py) | Backtesting.py is a Python framework for inferring viability of trading strategies on historical (past) data. Improved upon the vision of Backtrader, and by all means surpassingly comparable to other accessible alternatives, Backtesting.py is lightweight, fast, user-friendly, intuitive, interactive, intelligent and, hopefully, future-proof. | ![GitHub stars](https://badgen.net/github/stars/kernc/backtesting.py) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zvt](https://github.com/zvtvz/zvt) | Modular quant framework | ![GitHub stars](https://badgen.net/github/stars/zvtvz/zvt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [WonderTrader](https://github.com/wondertrader/wondertrader) | WonderTrader——量化研发交易一站式框架  | ![GitHub stars](https://badgen.net/github/stars/wondertrader/wondertrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester | ![GitHub stars](https://badgen.net/github/stars/nautechsystems/nautilus_trader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PandoraTrader](https://github.com/pegasusTrader/PandoraTrader) | High-frequency quantitative trading platform based on c++ development, supporting multiple trading APIs and cross-platform | ![GitHub stars](https://badgen.net/github/stars/pegasusTrader/PandoraTrader) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [HFTBacktest](https://github.com/nkaz001/hftbacktest) | Highly precise backtest on HFT data in Python+Numba | ![GitHub stars](https://badgen.net/github/stars/nkaz001/hftbacktest) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyBroker](https://github.com/edtechre/pybroker) | Algorithmic trading in Python with machine learning: rule based and model driven strategies, walkforward analysis and bootstrapped significance tests on the results | ![GitHub stars](https://badgen.net/github/stars/edtechre/pybroker) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Hikyuu](https://github.com/fasiondog/hikyuu) | C++/Python quantitative research framework built around reusable strategy components, with its own bar and indicator engine | ![GitHub stars](https://badgen.net/github/stars/fasiondog/hikyuu) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [barter-rs](https://github.com/barter-rs/barter-rs) | Open source Rust framework for building event driven live trading and backtesting systems, running strategies on a near identical engine on both sides | ![GitHub stars](https://badgen.net/github/stars/barter-rs/barter-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [Investing Algorithm Framework](https://github.com/coding-kitties/investing-algorithm-framework) | Framework for developing, backtesting and deploying automated trading algorithms and trading bots | ![GitHub stars](https://badgen.net/github/stars/coding-kitties/investing-algorithm-framework) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [qf-lib](https://github.com/quarkfin/qf-lib) | Modular event driven backtester with data vendor and broker integrations, portfolio construction tools and automated PDF reporting | ![GitHub stars](https://badgen.net/github/stars/quarkfin/qf-lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [trade-frame](https://github.com/rburkholder/trade-frame) | C++17 library and sample applications for automated trading of equities, futures, currencies, ETFs and options on IQFeed and Interactive Brokers data | ![GitHub stars](https://badgen.net/github/stars/rburkholder/trade-frame) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [QuantFabric](https://github.com/QuantFabric/QuantFabric) | Linux/C++ mid and high frequency trading system for the Chinese futures, stock and bond exchanges | ![GitHub stars](https://badgen.net/github/stars/QuantFabric/QuantFabric) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [aat](https://github.com/AsyncAlgoTrading/aat) | An asynchronous, event-driven framework for writing algorithmic trading strategies in python with optional acceleration in C++. It is designed to be modular and extensible, with support for a wide variety of instruments and strategies, live trading across (and between) multiple exchanges. | ![GitHub stars](https://badgen.net/github/stars/AsyncAlgoTrading/aat) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) `dormant since 2023-09` | This project is mainly for newbies into algo trading who are interested in learning to code their own trading algo using python interpreter. | ![GitHub stars](https://badgen.net/github/stars/sreenivasdoosa/sdoosa-algo-trade-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [lumibot](https://github.com/Lumiwealth/lumibot) | A very simple yet useful backtesting and sample based live trading framework (a bit slow to run...) | ![GitHub stars](https://badgen.net/github/stars/Lumiwealth/lumibot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [quanttrader](https://github.com/letianzj/quanttrader) `dormant since 2024-06` | Backtest and live trading in Python. Event based. Similar to backtesting.py. | ![GitHub stars](https://badgen.net/github/stars/letianzj/quanttrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [gobacktest](https://github.com/gobacktest/gobacktest) `archived` | A Go implementation of event-driven backtesting framework | ![GitHub stars](https://badgen.net/github/stars/gobacktest/gobacktest) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [PineForge](https://github.com/pineforge-4pass/pineforge-engine) | Transpiles PineScript v6 strategies to C++ and runs deterministic offline backtests on user-provided OHLCV data. | ![GitHub stars](https://badgen.net/github/stars/pineforge-4pass/pineforge-engine) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [FlashFunk](https://github.com/HFQR/FlashFunk) | High Performance Runtime in Rust | ![GitHub stars](https://badgen.net/github/stars/HFQR/FlashFunk) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |


### General - Vector Based Frameworks

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [QTradeX](https://github.com/squidKid-deluxe/QTradeX-Algo-Trading-SDK) | A powerful and flexible Python framework for designing, backtesting, optimizing, and deploying algotrading bots | ![GitHub stars](https://badgen.net/github/stars/squidKid-deluxe/QTradeX-Algo-Trading-SDK) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [vectorbt](https://github.com/polakowo/vectorbt) | vectorbt takes a novel approach to backtesting: it operates entirely on pandas and NumPy objects, and is accelerated by Numba to analyze any data at speed and scale. This allows for testing of many thousands of strategies in seconds. | ![GitHub stars](https://badgen.net/github/stars/polakowo/vectorbt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | Systematic Trading in python from book Systematic Trading by Rob Carver | ![GitHub stars](https://badgen.net/github/stars/robcarver17/pysystemtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [bt](https://github.com/pmorissette/bt) | Flexible backtesting for Python based on Algo and Strategy Tree | ![GitHub stars](https://badgen.net/github/stars/pmorissette/bt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ml-quant-trading](https://github.com/initial-d/ml-quant-trading) | PyTorch research stack for ML multi-factor trading with 213 factors, bias correction, portfolio optimization, vectorized backtesting, and public validation reports | ![GitHub stars](https://badgen.net/github/stars/initial-d/ml-quant-trading) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


### Cryptocurrencies

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Freqtrade](https://github.com/freqtrade/freqtrade) | Freqtrade is a free and open source crypto trading bot written in Python. It is designed to support all major exchanges and be controlled via Telegram. It contains backtesting, plotting and money management tools as well as strategy optimization by machine learning. | ![GitHub stars](https://badgen.net/github/stars/freqtrade/freqtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Jesse](https://github.com/jesse-ai/jesse) | Jesse is an advanced crypto trading framework which aims to simplify researching and defining trading strategies. | ![GitHub stars](https://badgen.net/github/stars/jesse-ai/jesse) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OctoBot](https://github.com/Drakkar-Software/OctoBot) | Cryptocurrency trading bot for TA, arbitrage and social trading with an advanced web interface | ![GitHub stars](https://badgen.net/github/stars/Drakkar-Software/OctoBot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Kelp](https://github.com/stellar/kelp) `archived` | Kelp is a free and open-source trading bot for the Stellar DEX and 100+ centralized exchanges | ![GitHub stars](https://badgen.net/github/stars/stellar/kelp) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [basana](https://github.com/gbeced/basana) | Python async and event driven framework for algorithmic trading, with a focus on crypto currencies | ![GitHub stars](https://badgen.net/github/stars/gbeced/basana) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [openlimits](https://github.com/nash-io/openlimits) `dormant since 2022-07` | A Rust high performance cryptocurrency trading API with support for multiple exchanges and language wrappers. | ![GitHub stars](https://badgen.net/github/stars/nash-io/openlimits) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [bTrader](https://github.com/gabriel-milan/btrader) `archived` | Triangle arbitrage trading bot for Binance | ![GitHub stars](https://badgen.net/github/stars/gabriel-milan/btrader) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) `dormant since 2023-03` | Crawl orderbook and trade messages from crypto exchanges | ![GitHub stars](https://badgen.net/github/stars/crypto-crawler/crypto-crawler-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [Hummingbot](https://github.com/CoinAlpha/hummingbot) | A client for crypto market making | ![GitHub stars](https://badgen.net/github/stars/CoinAlpha/hummingbot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cryptotrader-core](https://github.com/monomadic/cryptotrader-core) `dormant since 2019-06` | Simple to use Crypto Exchange REST API client in rust. | ![GitHub stars](https://badgen.net/github/stars/monomadic/cryptotrader-core) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

## Trading bots

*Trading bots and alpha models. Some of them are old and not maintained.*

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Blackbird](https://github.com/butor/blackbird) `no longer available` | Blackbird Bitcoin Arbitrage: a long/short market-neutral strategy | ![GitHub stars](https://badgen.net/github/stars/butor/blackbird) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | Bitcoin arbitrage - opportunity detector | ![GitHub stars](https://badgen.net/github/stars/maxme/bitcoin-arbitrage) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ThetaGang](https://github.com/brndnmtthws/thetagang) | ThetaGang is an IBKR bot for collecting money | ![GitHub stars](https://badgen.net/github/stars/brndnmtthws/thetagang) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [czsc](https://github.com/waditu/czsc) | 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 | ![GitHub stars](https://badgen.net/github/stars/waditu/czsc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2) `dormant since 2023-04` | R2 Bitcoin Arbitrager is an automatic arbitrage trading system powered by Node.js + TypeScript | ![GitHub stars](https://badgen.net/github/stars/bitrinjani/r2) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [Intelligent Trading Bot](https://github.com/asavinov/intelligent-trading-bot) | Intelligent Trading Bot: Automatically generating signals and trading based on machine learning and feature engineering | ![GitHub stars](https://badgen.net/github/stars/asavinov/intelligent-trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [analyzingalpha](https://github.com/leosmigel/analyzingalpha) `dormant since 2023-08` | Implementation of simple strategies | ![GitHub stars](https://badgen.net/github/stars/leosmigel/analyzingalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow) `dormant since 2018-04` | PyTrendFollow - systematic futures trading using trend following | ![GitHub stars](https://badgen.net/github/stars/chrism2671/PyTrendFollow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradeSight](https://github.com/rmbell09-lang/tradesight) | AI-powered algorithmic trading platform with RSI/MACD signals, overnight strategy tournaments, paper trading via Alpaca, multi-stock scanning, and web dashboard | ![GitHub stars](https://badgen.net/github/stars/rmbell09-lang/tradesight) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PRISM-INSIGHT](https://github.com/dragon1086/prism-insight) | AI-powered stock analysis with 13 specialized agents, automated trading via KIS API (Korean & US markets) | ![GitHub stars](https://badgen.net/github/stars/dragon1086/prism-insight) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Analytics

### Indicators

*Libraries of indicators to predict future price movements.*

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [ta-lib](https://github.com/mrjbq7/ta-lib) | Perform technical analysis of financial market data | ![GitHub stars](https://badgen.net/github/stars/mrjbq7/ta-lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [go-tart](https://github.com/iamjinlei/go-tart) `dormant since 2021-06` | A Go implementation of the [ta-lib]((https://github.com/mrjbq7/ta-lib) with streaming update support | ![GitHub stars](https://badgen.net/github/stars/iamjinlei/go-tart) | ![made-with-go](https://img.shields.io/badge/Made%20with-go-1f425f.svg) |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) `no longer available` | Pandas Technical Analysis (Pandas TA) is an easy to use library that leverages the Pandas package with more than 130 Indicators and Utility functions and more than 60 TA Lib Candlestick Patterns | ![GitHub stars](https://badgen.net/github/stars/twopirllc/pandas-ta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finta](https://github.com/peerchemist/finta) `archived` | Common financial technical indicators implemented in Pandas | ![GitHub stars](https://badgen.net/github/stars/peerchemist/finta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ta-rust](https://github.com/greyblake/ta-rs) `dormant since 2024-07` | Technical analysis library for Rust language | ![GitHub stars](https://badgen.net/github/stars/greyblake/ta-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [kand](https://github.com/kand-ta/kand) | Technical analysis library written in Rust with Python and WASM bindings, exposing both batch and incremental streaming updates | ![GitHub stars](https://badgen.net/github/stars/kand-ta/kand) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [wickra](https://github.com/wickra-lib/wickra) | Streaming-first technical-analysis library with a Rust core and native Python/Node/WASM bindings plus a C ABI (C, C++, C#/.NET, Go, Java, R); 514 O(1)-per-tick indicators across 24 families, bit-exact batch and streaming | ![GitHub stars](https://badgen.net/github/stars/wickra-lib/wickra) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### Metrics computation

*Librairies of financial metrics.*

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [quantstats](https://github.com/ranaroussi/quantstats) | Portfolio analytics for quants, written in Python | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/quantstats) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ffn](https://github.com/pmorissette/ffn) | A financial function library for Python | ![GitHub stars](https://badgen.net/github/stars/pmorissette/ffn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Optimization

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [skfolio](https://github.com/skfolio/skfolio) | Portfolio optimization built on top of scikit-learn. It provides a unified interface and sklearn compatible tools to build, tune and cross-validate portfolio models.  | ![GitHub stars](https://badgen.net/github/stars/skfolio/skfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | Financial portfolio optimizations in python, including classical efficient frontier, Black-Litterman, Hierarchical Risk Parity | ![GitHub stars](https://badgen.net/github/stars/robertmartin8/PyPortfolioOpt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | Portfolio Optimization and Quantitative Strategic Asset Allocation in Python | ![GitHub stars](https://badgen.net/github/stars/dcajasn/Riskfolio-Lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [empyrial](https://github.com/ssantoshp/Empyrial) | Empyrial is a Python-based open-source quantitative investment library dedicated to financial institutions and retail investors, officially released in March 2021 | ![GitHub stars](https://badgen.net/github/stars/ssantoshp/Empyrial) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cvxportfolio](https://github.com/cvxgrp/cvxportfolio) | Portfolio optimization and back-testing from the Stanford convex optimization group, implementing the multi-period framework of Boyd et al. | ![GitHub stars](https://badgen.net/github/stars/cvxgrp/cvxportfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Deepdow](https://github.com/jankrepl/deepdow) `dormant since 2024-01` | Python package connecting portfolio optimization and deep learning. Its goal is to facilitate research of networks that perform weight allocation in one forward pass. | ![GitHub stars](https://badgen.net/github/stars/jankrepl/deepdow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [spectre](https://github.com/Heerozh/spectre) | Portfolio Optimization and Quantitative Strategic Asset Allocation in Python | ![GitHub stars](https://badgen.net/github/stars/Heerozh/spectre) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Pricing

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [tf-quant-finance](https://github.com/google/tf-quant-finance) | High-performance TensorFlow library for quantitative finance from Google | ![GitHub stars](https://badgen.net/github/stars/google/tf-quant-finance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinancePy](https://github.com/domokane/FinancePy) | A Python Finance Library that focuses on the pricing and risk-management of Financial Derivatives, including fixed-income, equity, FX and credit derivatives | ![GitHub stars](https://badgen.net/github/stars/domokane/FinancePy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyQL](https://github.com/enthought/pyql) | Python wrapper of the famous pricing library QuantLib | ![GitHub stars](https://badgen.net/github/stars/enthought/pyql) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Risk

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [pyfolio](https://github.com/quantopian/pyfolio) `dormant since 2023-12` | Portfolio and risk analytics in Python | ![GitHub stars](https://badgen.net/github/stars/quantopian/pyfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |



## Broker APIs

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [ccxt](https://github.com/ccxt/ccxt) | A JavaScript / Python / PHP cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges | ![GitHub stars](https://badgen.net/github/stars/ccxt/ccxt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Ib_insync](https://github.com/erdewit/ib_insync) `archived` | Python sync/async framework for Interactive Brokers. | ![GitHub stars](https://badgen.net/github/stars/erdewit/ib_insync) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pmxt](https://github.com/pmxt-dev/pmxt) | Unified prediction market trading API across Polymarket, Kalshi and other venues, in the spirit of ccxt | ![GitHub stars](https://badgen.net/github/stars/pmxt-dev/pmxt) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [Coinnect](https://github.com/hugues31/coinnect) `dormant since 2021-11` | Coinnect is a Rust library aiming to provide a complete access to main crypto currencies exchanges via REST API. | ![GitHub stars](https://badgen.net/github/stars/hugues31/coinnect) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) `dormant since 2024-05` | Javascript SDK for Trading, Data, and Websockets for FTX, FTXUS, OKX, Bybit, & More. | ![GitHub stars](https://badgen.net/github/stars/CompendiumFi/PENDAX-SDK) | ![made-with-javascript](https://img.shields.io/badge/Made%20with-Javascript-1f425f.svg) |


## Data Sources

### General

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Fincept Terminal](https://github.com/Fincept-Corporation/FinceptTerminal) | Fincept Terminal is a comprehensive CLI tool that provides financial insights, market analysis, and a host of other financial services such as technical analysis, fundamental analysis, sentiment analysis, quantitative analysis, and economic data services. | ![GitHub stars](https://badgen.net/github/stars/Fincept-Corporation/FinceptTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) | Investment Research for Everyone, Anywhere. | ![GitHub stars](https://badgen.net/github/stars/OpenBB-finance/OpenBBTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TuShare](https://github.com/waditu/tushare) `dormant since 2024-03` | TuShare is a utility for crawling historical data of China stocks | ![GitHub stars](https://badgen.net/github/stars/waditu/tushare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [yfinance](https://github.com/ranaroussi/yfinance) | yfinance offers a threaded and Pythonic way to download market data from Yahoo!Ⓡ finance. | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/yfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AkShare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! | ![GitHub stars](https://badgen.net/github/stars/akfamily/akshare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) | Database of 300,000+ symbols covering equities, ETFs, funds, indices, currencies, cryptocurrencies and money markets | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FinanceDatabase) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinanceToolkit](https://github.com/JerBouma/FinanceToolkit) | 200+ financial metrics, ratios, technical indicators and risk measures computed from Financial Modeling Prep and Yahoo Finance data | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FinanceToolkit) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pandas-datareader](https://github.com/pydata/pandas-datareader) | Up to date remote data access for pandas, works for multiple versions of pandas. | ![GitHub stars](https://badgen.net/github/stars/pydata/pandas-datareader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [edgartools](https://github.com/dgunning/edgartools) | SEC EDGAR filings in Python: XBRL fundamentals, 13F institutional holdings, insider transactions (Forms 3/4/5) and 8-K events | ![GitHub stars](https://badgen.net/github/stars/dgunning/edgartools) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Quandl](https://github.com/quandl/quandl-python) `archived` | Get millions of financial and economic dataset from hundreds of publishers via a single free API. | ![GitHub stars](https://badgen.net/github/stars/quandl/quandl-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [findatapy](https://github.com/cuemacro/findatapy) | findatapy creates an easy to use Python API to download market data from many sources including Quandl, Bloomberg, Yahoo, Google etc. using a unified high level interface. | ![GitHub stars](https://badgen.net/github/stars/cuemacro/findatapy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Investpy](https://github.com/alvarobartt/investpy) | Financial Data Extraction from Investing.com with Python | ![GitHub stars](https://badgen.net/github/stars/alvarobartt/investpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | Fully-fledged Fundamental Analysis package capable of collecting 20 years of Company Profiles, Financial Statements, Ratios and Stock Data of 20.000+ companies. | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FundamentalAnalysis) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Wallstreet](https://github.com/mcdallas/wallstreet) `dormant since 2024-07` | Wallstreet: Real time Stock and Option tools | ![GitHub stars](https://badgen.net/github/stars/mcdallas/wallstreet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pwb-toolbox](https://github.com/paperswithbacktest/pwb-toolbox) | Loader for the 32 Papers With Backtest datasets on Hugging Face: daily prices back to 1962 for stocks, ETFs, indices, currencies and commodities, sovereign yield curves, quarterly fundamentals, FRED-MD macro series, and 5.7 billion rows of 1-minute US equity bars. Cards and schemas are open to read, downloads are gated. | ![GitHub stars](https://badgen.net/github/stars/paperswithbacktest/pwb-toolbox) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


### Cryptocurrencies

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Cryptofeed](https://github.com/bmoscon/cryptofeed) | Cryptocurrency Exchange Websocket Data Feed Handler with Asyncio | ![GitHub stars](https://badgen.net/github/stars/bmoscon/cryptofeed) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) `dormant since 2018-05` | Gekko trading bot dataset dumps. Download and use history files in SQLite format. | ![GitHub stars](https://badgen.net/github/stars/xFFFFF/Gekko-Datasets) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) `dormant since 2018-03` | A live crypto currency historical trade data blotter. Download live historical trade data from any crypto exchange. | ![GitHub stars](https://badgen.net/github/stars/Optixal/CryptoInscriber) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Crypto Lake](https://github.com/crypto-lake/lake-api) | High frequency order book & trade data for crypto | ![GitHub stars](https://badgen.net/github/stars/crypto-lake/lake-api) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Data Science

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [TensorFlow](https://github.com/tensorflow/tensorflow) | Fundamental algorithms for scientific computing in Python | ![GitHub stars](https://badgen.net/github/stars/tensorflow/tensorflow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pytorch](https://github.com/pytorch/pytorch) | Tensors and Dynamic neural networks in Python with strong GPU acceleration | ![GitHub stars](https://badgen.net/github/stars/pytorch/pytorch) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Keras](https://github.com/keras-team/keras) | The most user friendly Deep Learning for humans in Python | ![GitHub stars](https://badgen.net/github/stars/keras-team/keras) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | Machine learning in Python | ![GitHub stars](https://badgen.net/github/stars/scikit-learn/scikit-learn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pandas](https://github.com/pandas-dev/pandas) | Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more | ![GitHub stars](https://badgen.net/github/stars/pandas-dev/pandas) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [JAX](https://github.com/jax-ml/jax) | Composable transformations of Python+NumPy programs: automatic differentiation, vectorization and JIT compilation to GPU/TPU | ![GitHub stars](https://badgen.net/github/stars/jax-ml/jax) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Numpy](https://github.com/numpy/numpy) | The fundamental package for scientific computing with Python | ![GitHub stars](https://badgen.net/github/stars/numpy/numpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scipy](https://github.com/scipy/scipy) | Fundamental algorithms for scientific computing in Python | ![GitHub stars](https://badgen.net/github/stars/scipy/scipy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyMC](https://github.com/pymc-devs/pymc) | Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Aesara | ![GitHub stars](https://badgen.net/github/stars/pymc-devs/pymc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Cvxpy](https://github.com/cvxpy/cvxpy) | A Python-embedded modeling language for convex optimization problems. | ![GitHub stars](https://badgen.net/github/stars/cvxpy/cvxpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Databases

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [DuckDB](https://github.com/duckdb/duckdb) | In-process analytical SQL database that queries Parquet and Arrow files directly, a common backend for research datasets | ![GitHub stars](https://badgen.net/github/stars/duckdb/duckdb) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [Marketstore](https://github.com/alpacahq/marketstore) `no longer available` | DataFrame Server for Financial Timeseries Data | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [Tectonicdb](https://github.com/0b01/tectonicdb) `dormant since 2024-01` | Tectonicdb is a fast, highly compressed standalone database and streaming protocol for order book ticks. | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [ArcticDB (Man Group)](https://github.com/man-group/arcticdb) | High performance datastore for time series and tick data | ![GitHub stars](https://badgen.net/github/stars/man-group/ArcticDB) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyStore](https://github.com/ranaroussi/pystore) | Fast datastore for Pandas time series data, built on Dask and Parquet | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/pystore) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Graph Computation

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Ray](https://github.com/ray-project/ray) | An open source framework that provides a simple, universal API for building distributed applications. | ![GitHub stars](https://badgen.net/github/stars/ray-project/ray) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Dask](https://github.com/dask/dask) | Parallel computing with task scheduling in Python with a Pandas like API | ![GitHub stars](https://badgen.net/github/stars/dask/dask) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | Incremental is a library that gives you a way of building complex computations that can update efficiently in response to their inputs changing, inspired by the work of Umut Acar et. al. on self-adjusting computations. Incremental can be useful in a number of applications | ![GitHub stars](https://badgen.net/github/stars/janestreet/incremental) | ![made-with-ocaml](https://img.shields.io/badge/Made%20with-Ocaml-1f425f.svg) |
| [csp (Point72)](https://github.com/Point72/csp) | High performance reactive stream processing library written in C++ and Python, where the same graph runs in backtest and in real time | ![GitHub stars](https://badgen.net/github/stars/Point72/csp) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Man MDF](https://github.com/man-group/mdf) `dormant since 2016-12` | Data-flow programming toolkit for Python | ![GitHub stars](https://badgen.net/github/stars/man-group/mdf) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [GraphKit](https://github.com/yahoo/graphkit) `dormant since 2023-03` | A lightweight Python module for creating and running ordered graphs of computations. | ![GitHub stars](https://badgen.net/github/stars/yahoo/graphkit) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Tributary](https://github.com/timkpaine/tributary) | Streaming reactive and dataflow graphs in Python | ![GitHub stars](https://badgen.net/github/stars/timkpaine/tributary) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Machine Learning

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) | Educational hedge fund simulator where a team of LLM agents modelled on well known investors debates and takes positions | ![GitHub stars](https://badgen.net/github/stars/virattt/ai-hedge-fund) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QLib (Microsoft)](https://github.com/microsoft/qlib) | Qlib is an AI-oriented quantitative investment platform, which aims to realize the potential, empower the research, and create the value of AI technologies in quantitative investment. With Qlib, you can easily try your ideas to create better Quant investment strategies. An increasing number of SOTA Quant research works/papers are released in Qlib. | ![GitHub stars](https://badgen.net/github/stars/microsoft/qlib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | Open source financial large language models, with the fine-tuned weights released on HuggingFace | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinGPT) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Machine Learning for Trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Code for Machine Learning for Trading (3rd edition), from data sourcing and alpha factor research to live execution | ![GitHub stars](https://badgen.net/github/stars/stefan-jansen/machine-learning-for-trading) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Qbot](https://github.com/UFund-Me/Qbot) | AI powered quantitative investment platform covering data collection, strategy research, backtesting and live trading | ![GitHub stars](https://badgen.net/github/stars/UFund-Me/Qbot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | FinRL is the first open-source framework to demonstrate the great potential of applying deep reinforcement learning in quantitative finance. | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinRL) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [MlFinLab (Hudson & Thames)](https://github.com/hudson-and-thames/mlfinlab) `dormant since 2023-10` | MlFinLab helps portfolio managers and traders who want to leverage the power of machine learning by providing reproducible, interpretable, and easy to use tools. | ![GitHub stars](https://badgen.net/github/stars/hudson-and-thames/mlfinlab) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradingGym](https://github.com/Yvictor/TradingGym) `dormant since 2024-02` | Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo. | ![GitHub stars](https://badgen.net/github/stars/Yvictor/TradingGym) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AlphaGen](https://github.com/ICT-FinD-Lab/alphagen) | Generating sets of formulaic alpha factors with reinforcement learning | ![GitHub stars](https://badgen.net/github/stars/ICT-FinD-Lab/alphagen) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) `dormant since 2023-12` | Stock Trading Bot using Deep Q-Learning | ![GitHub stars](https://badgen.net/github/stars/pskrunner14/trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## TimeSeries Analysis

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Facebook Prophet](https://github.com/facebook/prophet) | Tool for producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth. | ![GitHub stars](https://badgen.net/github/stars/facebook/prophet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [statsmodels](https://github.com/statsmodels/statsmodels) | Python module that allows users to explore data, estimate statistical models, and perform statistical tests. | ![GitHub stars](https://badgen.net/github/stars/statsmodels/statsmodels) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [tsfresh](https://github.com/blue-yonder/tsfresh) | Automatic extraction of relevant features from time series. | ![GitHub stars](https://badgen.net/github/stars/blue-yonder/tsfresh) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pmdarima](https://github.com/alkaline-ml/pmdarima) | A statistical library designed to fill the void in Python's time series analysis capabilities, including the equivalent of R's auto.arima function. | ![GitHub stars](https://badgen.net/github/stars/alkaline-ml/pmdarima) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Visualization

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Perspective](https://github.com/perspective-dev/perspective) | Data visualization and analytics component built for large and streaming datasets, originally open sourced by J.P. Morgan | ![GitHub stars](https://badgen.net/github/stars/perspective-dev/perspective) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [D-Tale (Man Group)](https://github.com/man-group/dtale) | D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures. | ![GitHub stars](https://badgen.net/github/stars/man-group/dtale) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [mplfinance](https://github.com/matplotlib/mplfinance) `dormant since 2024-08` | Financial Markets Data Visualization using Matplotlib | ![GitHub stars](https://badgen.net/github/stars/matplotlib/mplfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [btplotting](https://github.com/happydasch/btplotting) | btplotting provides plotting for backtests, optimization results and live data from backtrader. | ![GitHub stars](https://badgen.net/github/stars/happydasch/btplotting) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


# Strategies

*Every strategy below is a published paper that has been coded and run over its own full history. The table is regenerated from the replication catalogue by [`scripts/build_strategies_table.py`](./scripts/build_strategies_table.py), so the numbers move when the catalogue does.*

<!-- STRATEGIES:START - generated by scripts/build_strategies_table.py -->

*Showing the 61 strongest of 1,687 replications that clear a t-statistic of 1.96 over at least 10 years, up to 12 per asset class. Sharpe ratios are measured on each strategy's own active window, not on a common calendar, and are gross of trading costs. Series with an annualised volatility outside 1% to 100% are treated as degenerate and dropped. The t-statistic is shown because a Sharpe ratio without one says very little: half the catalogue does not clear it.*

## Equities

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [A Study Of Differences In Returns Between Large And Small Companies In Europe](https://paperswithbacktest.com/strategies/a-study-of-differences-in-returns-between-large-and-small-companies-in-europe) | `1.89` | `11.4` | `6.4%` | `37` |
| [The Investment CAPM](https://paperswithbacktest.com/strategies/the-investment-capm-1) | `1.80` | `11.0` | `2.9%` | `37` |
| [Important Characteristics, Weaknesses and Errors in German Equity Data from Thomson](https://paperswithbacktest.com/strategies/important-characteristics-weaknesses-and-errors-in-german-equity-data-from-thomson) | `1.68` | `10.2` | `6.4%` | `37` |
| [The Role of Beta and Size in the Cross-Section of European Stock Returns](https://paperswithbacktest.com/strategies/the-role-of-beta-and-size-in-the-cross-section-of-european-stock-returns) | `1.63` | `9.6` | `5.3%` | `34` |
| [Systematic Abnormal Return Variation and Global Market Inefficiencies](https://paperswithbacktest.com/strategies/systematic-abnormal-return-variation-and-global-market-inefficiencies) | `1.57` | `8.2` | `9.5%` | `27` |
| [Value and Size Effect: Now You See It, Now You Don’t](https://paperswithbacktest.com/strategies/value-and-size-effect-now-you-see-it-now-you-don-t) | `1.52` | `9.3` | `5.9%` | `37` |
| [Properties of the Most Diversified Portfolio](https://paperswithbacktest.com/strategies/properties-of-the-most-diversified-portfolio) | `1.50` | `9.0` | `14.3%` | `37` |
| [Understanding Momentum and Reversal?](https://paperswithbacktest.com/strategies/understanding-momentum-and-reversal) | `1.36` | `8.2` | `5.1%` | `36` |
| [Fact, Fiction, and the Size Effect](https://paperswithbacktest.com/strategies/fact-fiction-and-the-size-effect) | `1.33` | `8.1` | `2.6%` | `37` |
| [The cross-section of returns in frontier equity markets: Integrated or segmented pricing?](https://paperswithbacktest.com/strategies/the-cross-section-of-returns-in-frontier-equity-markets-integrated-or-segmented-pricing) | `1.32` | `8.0` | `3.9%` | `36` |
| [Analytical Solution for Kelly’s Criterion for Multiple Outcomes](https://paperswithbacktest.com/strategies/analytical-solution-for-kelly-s-criterion-for-multiple-outcomes) | `1.31` | `7.9` | `13.3%` | `37` |
| [End-To-End Large Portfolio Optimization For Variance Minimization With Neural Networks Through Covariance Cleaning](https://paperswithbacktest.com/strategies/end-to-end-large-portfolio-optimization-for-variance-minimization-with-neural-networks-through-covariance-cleaning) | `1.28` | `7.3` | `15.4%` | `33` |

## Bonds

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [Statistical and Economic Benefits of Whitening Residuals in Bond Yields](https://paperswithbacktest.com/strategies/statistical-and-economic-benefits-of-whitening-residuals-in-bond-yields) | `0.90` | `5.0` | `18.6%` | `30` |
| [Dynamic Risk-Aware Yield Search: A Useful Tool for Fixed Income Investors](https://paperswithbacktest.com/strategies/dynamic-risk-aware-yield-search-a-useful-tool-for-fixed-income-investors) | `0.89` | `4.4` | `2.9%` | `25` |
| [Out-performing corporate bonds indices with factor investing](https://paperswithbacktest.com/strategies/out-performing-corporate-bonds-indices-with-factor-investing) | `0.85` | `5.1` | `12.3%` | `36` |
| [Priced risk in corporate bonds](https://paperswithbacktest.com/strategies/priced-risk-in-corporate-bonds) | `0.72` | `3.0` | `6.0%` | `17` |
| [Sitting Bucks: Stale Pricing in Fixed Income Funds](https://paperswithbacktest.com/strategies/sitting-bucks-stale-pricing-in-fixed-income-funds) | `0.64` | `3.9` | `5.7%` | `37` |
| [Frontier and Emerging Government Bond Markets](https://paperswithbacktest.com/strategies/frontier-and-emerging-government-bond-markets) | `0.62` | `3.7` | `13.7%` | `36` |
| [Regime-based portfolio optimisation:  A Hidden Markov Model approach for fixed  income portfolios](https://paperswithbacktest.com/strategies/regime-based-portfolio-optimisation-a-hidden-markov-model-approach-for-fixed-income-portfolios) | `0.62` | `3.6` | `6.0%` | `33` |
| [Price Effects of Sovereign Debt Auctions in the Euro-zone: The Role of the Crisis](https://paperswithbacktest.com/strategies/price-effects-of-sovereign-debt-auctions-in-the-euro-zone-the-role-of-the-crisis) | `0.51` | `3.1` | `13.4%` | `37` |
| [Are Bond Returns Predictable with Real-Time Macro Data?](https://paperswithbacktest.com/strategies/are-bond-returns-predictable-with-real-time-macro-data) | `0.49` | `2.5` | `5.9%` | `26` |
| [Trading the Term Premium](https://paperswithbacktest.com/strategies/trading-the-term-premium) | `0.45` | `2.8` | `5.0%` | `37` |
| [Banks’ exposure to interest rate risk, their earnings from term transformation, and the dynamics of the term structure](https://paperswithbacktest.com/strategies/banks-exposure-to-interest-rate-risk-their-earnings-from-term-transformation-and-the-dynamics-of-the-term-structure) | `0.44` | `2.7` | `7.9%` | `38` |
| [Predictable End-of-Month Treasury Returns](https://paperswithbacktest.com/strategies/predictable-end-of-month-treasury-returns) | `0.43` | `2.6` | `3.8%` | `37` |

## Commodities

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [How to Improve Commodity Momentum Using Intra-Market Correlation](https://paperswithbacktest.com/strategies/how-to-improve-commodity-momentum-using-intra-market-correlation) | `0.65` | `2.8` | `8.7%` | `19` |
| [Long-Run Reversal in Commodity Returns: Insights from Seven Centuries of Evidence](https://paperswithbacktest.com/strategies/long-run-reversal-in-commodity-returns-insights-from-seven-centuries-of-evidence) | `0.63` | `3.8` | `20.7%` | `37` |
| [Rolling vs. Expanding Windows in Mean-Reversion Strategies: Evidence from Gold-Silver and Cross-Asset Validation](https://paperswithbacktest.com/strategies/rolling-vs-expanding-windows-in-mean-reversion-strategies-evidence-from-gold-silver-and-cross-asset-validation) | `0.36` | `2.2` | `98.5%` | `37` |

## Currencies

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [Good Carry, Bad Carry](https://paperswithbacktest.com/strategies/good-carry-bad-carry) | `1.74` | `10.6` | `4.6%` | `37` |
| [The Time-Varying Systematic Risk of](https://paperswithbacktest.com/strategies/the-time-varying-systematic-risk-of) | `1.53` | `9.3` | `4.1%` | `36` |
| [Lessons from the Evolution of Foreign Exchange Trading Strategies](https://paperswithbacktest.com/strategies/lessons-from-the-evolution-of-foreign-exchange-trading-strategies) | `1.24` | `7.4` | `12.4%` | `36` |
| [Optimal Currency Shares In International Reserves The Impact Of The Euro And The Prospects For The Dollar](https://paperswithbacktest.com/strategies/optimal-currency-shares-in-international-reserves-the-impact-of-the-euro-and-the-prospects-for-the-dollar) | `0.68` | `2.9` | `55.3%` | `19` |

## Cryptocurrencies

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [How to Design a Simple Multi-Timeframe Trend Strategy on Bitcoin](https://paperswithbacktest.com/strategies/how-to-design-a-simple-multi-timeframe-trend-strategy-on-bitcoin) | `3.39` | `16.2` | `46.3%` | `23` |
| [‘Know When to Hodl ‘Em, Know When to Fodl ‘Em’: An Investigation of Factor Based Investing in the Cryptocurrency Space](https://paperswithbacktest.com/strategies/know-when-to-hodl-em-know-when-to-fodl-em-an-investigation-of-factor-based-investing-in-the-cryptocurrency-space) | `1.53` | `6.2` | `9.6%` | `16` |
| [Seasonality, Trend-following, and Mean reversion in Bitcoin](https://paperswithbacktest.com/strategies/seasonality-trend-following-and-mean-reversion-in-bitcoin) | `1.11` | `4.5` | `49.5%` | `16` |
| [Do Risk Preferences Drive Momentum in Cryptocurrencies?](https://paperswithbacktest.com/strategies/do-risk-preferences-drive-momentum-in-cryptocurrencies) | `0.68` | `4.0` | `54.9%` | `34` |
| [The Blockchain Risk Parity Line: Moving From The Efficient Frontier To The Final Frontier Of Investments](https://paperswithbacktest.com/strategies/the-blockchain-risk-parity-line-moving-from-the-efficient-frontier-to-the-final-frontier-of-investments) | `0.58` | `3.4` | `54.1%` | `34` |
| [Price Overreactions in the Cryptocurrency Market](https://paperswithbacktest.com/strategies/price-overreactions-in-the-cryptocurrency-market) | `0.53` | `3.1` | `32.3%` | `35` |
| [Proof-of-What? Detecting original consensus algorithms in cryptocurrencies with a four-factor model](https://paperswithbacktest.com/strategies/proof-of-what-detecting-original-consensus-algorithms-in-cryptocurrencies-with-a-four-factor-model) | `0.52` | `2.4` | `85.9%` | `22` |
| [Cryptocurrency as money: A trading strategy solution](https://paperswithbacktest.com/strategies/cryptocurrency-as-money-a-trading-strategy-solution) | `0.47` | `2.8` | `15.4%` | `35` |

## Derivatives

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [Media Tone Goes Viral: Global Evidence from the Currency Market](https://paperswithbacktest.com/strategies/media-tone-goes-viral-global-evidence-from-the-currency-market) | `1.06` | `6.5` | `1.3%` | `38` |
| [Robust Portfolio Optimization with Value-At-Risk Adjusted Sharpe Ratios](https://paperswithbacktest.com/strategies/robust-portfolio-optimization-with-value-at-risk-adjusted-sharpe-ratios) | `0.92` | `5.6` | `17.1%` | `37` |
| [When Factor Timing Makes Sense](https://paperswithbacktest.com/strategies/when-factor-timing-makes-sense) | `0.74` | `4.5` | `10.4%` | `37` |
| [Rational Decision-Making Under Uncertainty: Observed Betting Patterns on a Biased Coin](https://paperswithbacktest.com/strategies/rational-decision-making-under-uncertainty-observed-betting-patterns-on-a-biased-coin) | `0.60` | `3.7` | `3.6%` | `38` |
| [Can Financial Innovation Succeed by Catering to Behavioral Preferences? Evidence from a Callable Options Market](https://paperswithbacktest.com/strategies/can-financial-innovation-succeed-by-catering-to-behavioral-preferences-evidence-from-a-callable-options-market) | `0.55` | `3.4` | `17.7%` | `37` |
| [A Theory of Model Sophistication and Operational Risk](https://paperswithbacktest.com/strategies/a-theory-of-model-sophistication-and-operational-risk) | `0.50` | `3.1` | `9.4%` | `37` |
| [Tail-Risk Protection Trading Strategies](https://paperswithbacktest.com/strategies/tail-risk-protection-trading-strategies) | `0.49` | `3.0` | `13.6%` | `37` |
| [Is Media Tone just a Tone? Time-Series and Cross-Sectional Evidence from the Currency Market](https://paperswithbacktest.com/strategies/is-media-tone-just-a-tone-time-series-and-cross-sectional-evidence-from-the-currency-market) | `0.35` | `2.1` | `3.1%` | `36` |
| [The Temporal Pattern of Trading Rule Returns and Central Bank Intervention: Intervention Does Not Generate Technical Trading Rule Profits](https://paperswithbacktest.com/strategies/the-temporal-pattern-of-trading-rule-returns-and-central-bank-intervention-intervention-does-not-generate-technical-trading-rule-profits) | `0.33` | `2.0` | `9.3%` | `37` |
| [Arbitrage in the Foreign Exchange Market: Turning on the Microscope](https://paperswithbacktest.com/strategies/arbitrage-in-the-foreign-exchange-market-turning-on-the-microscope) | `0.32` | `2.0` | `8.4%` | `37` |

## Multi-asset

| Strategy | Sharpe | t-stat | Volatility | Years tested |
|---|---|---|---|---|
| [Optimal Annuity Risk Management](https://paperswithbacktest.com/strategies/optimal-annuity-risk-management) | `1.62` | `9.9` | `5.4%` | `38` |
| [Explaining low annuity demand: an optimal portfolio application to Japan](https://paperswithbacktest.com/strategies/explaining-low-annuity-demand-an-optimal-portfolio-application-to-japan) | `1.60` | `9.8` | `4.8%` | `38` |
| [Diverging roads: Theory-based vs. machine learning-implied stock risk premia](https://paperswithbacktest.com/strategies/diverging-roads-theory-based-vs-machine-learning-implied-stock-risk-premia) | `1.57` | `9.5` | `8.3%` | `37` |
| [The Anomalous Behavior of the S&P Covered Call Closed End Fund](https://paperswithbacktest.com/strategies/the-anomalous-behavior-of-the-s-p-covered-call-closed-end-fund) | `1.36` | `8.3` | `18.6%` | `37` |
| [Any role for mean reversion in short term asset](https://paperswithbacktest.com/strategies/any-role-for-mean-reversion-in-short-term-asset) | `1.30` | `7.4` | `8.6%` | `32` |
| [Inconsistent investment and consumption problems](https://paperswithbacktest.com/strategies/inconsistent-investment-and-consumption-problems) | `1.26` | `7.7` | `2.6%` | `38` |
| [Heuristic Portfolio Rules with Labor Income](https://paperswithbacktest.com/strategies/heuristic-portfolio-rules-with-labor-income) | `1.21` | `7.4` | `10.5%` | `38` |
| [Investing for the Long-Run in European Real Estate](https://paperswithbacktest.com/strategies/investing-for-the-long-run-in-european-real-estate) | `1.11` | `4.5` | `5.5%` | `16` |
| [Regime-Aware Risk Management in Concentrated Equity Portfolios: Evidence from the Magnificent Seven](https://paperswithbacktest.com/strategies/regime-aware-risk-management-in-concentrated-equity-portfolios-evidence-from-the-magnificent-seven) | `1.11` | `6.4` | `1.4%` | `33` |
| [Are Heuristics Better than Theory if Market Crashes Are](https://paperswithbacktest.com/strategies/are-heuristics-better-than-theory-if-market-crashes-are) | `1.10` | `6.7` | `8.4%` | `37` |
| [Risk Parity Portfolios with Risk Factors](https://paperswithbacktest.com/strategies/risk-parity-portfolios-with-risk-factors) | `1.08` | `6.3` | `17.3%` | `34` |
| [A Risk Based Approach to Tactical Asset Allocation](https://paperswithbacktest.com/strategies/a-risk-based-approach-to-tactical-asset-allocation) | `1.06` | `6.4` | `5.0%` | `37` |

<!-- STRATEGIES:END -->

Older QuantConnect implementations of some of these papers are kept in [`static/strategies`](./static/strategies).


# Books

A comprehensive list of **55 books** for quantitative traders.


## Beginner

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [A Beginner’s Guide to the Stock Market: Everything You Need to Start Making Money Today - Matthew R. Kratter](https://amzn.to/3QN2VdU) | ![](https://badgen.net/badge/reviews/14%20161/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [How to Day Trade for a Living: A Beginner’s Guide to Trading Tools and Tactics, Money Management, Discipline and Trading Psychology - Andrew Aziz](https://amzn.to/3bmehFv) | ![](https://badgen.net/badge/reviews/12%20278/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns - John C. Bogle](https://amzn.to/3A4mgkR) | ![](https://badgen.net/badge/reviews/6%20969/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Investing QuickStart Guide: The Simplified Beginner’s Guide to Successfully Navigating the Stock Market, Growing Your Wealth & Creating a Secure Financial Future - Ted D. Snow](https://amzn.to/3A5aRkX) | ![](https://badgen.net/badge/reviews/2%20537/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Day Trading QuickStart Guide: The Simplified Beginner’s Guide to Winning Trade Plans, Conquering the Markets, and Becoming a Successful Day Trader - Troy Noonan](https://amzn.to/3HPZijw) | ![](https://badgen.net/badge/reviews/1%20229/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Introduction To Algo Trading: How Retail Traders Can Successfully Compete With Professional Traders - Kevin J Davey](https://amzn.to/39Tf7JC) | ![](https://badgen.net/badge/reviews/131/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [Algorithmic Trading and DMA: An introduction to direct access trading strategies - Barry Johnson](https://amzn.to/3xYb0UN) | ![](https://badgen.net/badge/reviews/69/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |


## Biography

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [My Life as a Quant: Reflections on Physics and Finance - Emanuel Derman](https://amzn.to/3A8KudR) | ![](https://badgen.net/badge/reviews/192/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [How I Became a Quant: Insights from 25 of Wall Street’s Elite: - Barry Schachter](https://amzn.to/3Alf8kz) | ![](https://badgen.net/badge/reviews/27/blue) | ![](https://badgen.net/badge/rating/3.7/blue) |



## Coding

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [Python for Finance: Mastering Data-Driven Finance - Yves Hilpisch](https://amzn.to/3NhkTlP) | ![](https://badgen.net/badge/reviews/249/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Trading Evolved: Anyone can Build Killer Trading Strategies in Python - Andreas F. Clenow](https://amzn.to/3A0jcGB) | ![](https://badgen.net/badge/reviews/173/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Python for Algorithmic Trading: From Idea to Cloud Deployment - Yves Hilpisch](https://amzn.to/3bpkd0C) | ![](https://badgen.net/badge/reviews/90/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Algorithmic Trading with Python: Quantitative Methods and Strategy Development - Chris Conlan](https://amzn.to/3u3cxYo) | ![](https://badgen.net/badge/reviews/48/blue) | ![](https://badgen.net/badge/rating/4.2/blue) |
| [Learn Algorithmic Trading: Build and deploy algorithmic trading systems and strategies using Python and advanced data analysis - Sebastien Donadio](https://amzn.to/3NqNghA) | ![](https://badgen.net/badge/reviews/46/blue) | ![](https://badgen.net/badge/rating/4.1/blue) |


## Crypto

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [The Bitcoin Standard: The Decentralized Alternative to Central Banking - Saifedean Ammous](https://amzn.to/3QMJgec) | ![](https://badgen.net/badge/reviews/5%20136/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Bitcoin Billionaires: A True Story of Genius, Betrayal, and Redemption - Ben Mezrich](https://amzn.to/39SkdWt) | ![](https://badgen.net/badge/reviews/1%20787/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Mastering Bitcoin: Programming the Open Blockchain - Andreas M. Antonopoulos](https://amzn.to/3NniZ3p) | ![](https://badgen.net/badge/reviews/955/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Why Buy Bitcoin: Investing Today in the Money of Tomorrow - Andy Edstrom](https://amzn.to/3OMcKqZ) | ![](https://badgen.net/badge/reviews/192/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |


## General

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [The Intelligent Investor: The Definitive Book on Value Investing - Benjamin Graham, Jason Zweig](https://www.amazon.fr/gp/product/0060555661/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0060555661&linkId=aba73910e4e3873b6cc8364487662bd6) | ![](https://badgen.net/badge/reviews/38%20087/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [How I Invest My Money: Finance experts reveal how they save, spend, and invest - Joshua Brown, Brian Portnoy](https://amzn.to/3A4rsoU) | ![](https://badgen.net/badge/reviews/892/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Naked Forex: High-Probability Techniques for Trading Without Indicators - Alex Nekritin](https://amzn.to/3NkrAUj) | ![](https://badgen.net/badge/reviews/720/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [The Four Pillars of Investing: Lessons for Building a Winning Portfolio - William J. Bernstein](https://www.amazon.fr/gp/product/B0041842TW/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=B0041842TW&linkId=d9bc2fec4f3faa41ca4f24aed3c72122) | ![](https://badgen.net/badge/reviews/441/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Option Volatility and Pricing: Advanced Trading Strategies and Techniques, 2nd Edition - Sheldon Natenberg](https://amzn.to/3btOxXL) | ![](https://badgen.net/badge/reviews/388/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [The Art and Science of Technical Analysis: Market Structure, Price Action, and Trading Strategies - Adam Grimes](https://www.amazon.fr/gp/product/1118115120/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118115120&linkId=d5dc1f0e6727b2663d2186a110a31ad0) | ![](https://badgen.net/badge/reviews/305/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [The New Trading for a Living: Psychology, Discipline, Trading Tools and Systems, Risk Control, Trade Management (Wiley Trading) - Alexander Elder](https://www.amazon.fr/gp/product/1118467450/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118467450&linkId=67ee502653bc52a5240ced9fc88eb76d) | ![](https://badgen.net/badge/reviews/242/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Building Winning Algorithmic Trading Systems: A Trader’s Journey From Data Mining to Monte Carlo Simulation to Live Trading (Wiley Trading) - Kevin J Davey](https://amzn.to/39QnsxA) | ![](https://badgen.net/badge/reviews/163/blue) | ![](https://badgen.net/badge/rating/4.2/blue) |
| [Systematic Trading: A unique new method for designing trading and investing systems - Robert Carver](https://www.amazon.fr/gp/product/0857194453/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0857194453&linkId=32d8bffc32c01041cde066bacab76c04) | ![](https://badgen.net/badge/reviews/123/blue) | ![](https://badgen.net/badge/rating/4.2/blue) |
| [Quantitative Momentum: A Practitioner’s Guide to Building a Momentum-Based Stock Selection System (Wiley Finance) - Wesley R. Gray, Jack R. Vogel](https://www.amazon.fr/gp/product/111923719X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=111923719X&linkId=b825cb65462a4a9254af3b7dc5328131) | ![](https://badgen.net/badge/reviews/105/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Algorithmic Trading: Winning Strategies and Their Rationale - Ernest P. Chan](https://amzn.to/3xWi8kd) | ![](https://badgen.net/badge/reviews/100/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Leveraged Trading: A professional approach to trading FX, stocks on margin, CFDs, spread bets and futures for all traders - Robert Carver](https://amzn.to/3Nhl6p7) | ![](https://badgen.net/badge/reviews/98/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Trading Systems: A New Approach to System Development and Portfolio Optimisation - Emilio Tomasini, Urban Jaekle](https://www.amazon.fr/gp/product/1905641796/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1905641796&linkId=61e6634242c497498338f73641ce0a80) | ![](https://badgen.net/badge/reviews/67/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Trading and Exchanges: Market Microstructure for Practitioners - Larry Harris](https://www.amazon.fr/gp/product/0195144708/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0195144708&linkId=e47e596fc0696cbd624726cce05b4500) | ![](https://badgen.net/badge/reviews/61/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Trading Systems 2nd edition: A new approach to system development and portfolio optimisation - Emilio Tomasini, Urban Jaekle](https://www.amazon.fr/gp/product/085719755X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=085719755X&linkId=97aa558484a8dc2bf57a5296e7f38cad) | ![](https://badgen.net/badge/reviews/42/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [Machine Trading: Deploying Computer Algorithms to Conquer the Markets - Ernest P. Chan](https://amzn.to/3OIBe4o) | ![](https://badgen.net/badge/reviews/53/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [Quantitative Equity Portfolio Management: An Active Approach to Portfolio Construction and Management (McGraw-Hill Library of Investment and Finance) - Ludwig B Chincarini, Daehwan Kim](https://amzn.to/3yl9u0c) | ![](https://badgen.net/badge/reviews/51/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk - Richard Grinold, Ronald Kahn](https://amzn.to/3xMKaic) | ![](https://badgen.net/badge/reviews/46/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [Quantitative Technical Analysis: An integrated approach to trading system development and trading management - Dr Howard B Bandy](https://www.amazon.fr/gp/product/0979183855/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0979183855&linkId=8ef7bda69477bdccf90f5ac02ee495b0) | ![](https://badgen.net/badge/reviews/37/blue) | ![](https://badgen.net/badge/rating/3.8/blue) |
| [Advances in Active Portfolio Management: New Developments in Quantitative Investing - Richard Grinold, Ronald Kahn](https://amzn.to/3xUTK2z) | ![](https://badgen.net/badge/reviews/19/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Professional Automated Trading: Theory and Practice - Eugene A. Durenard](https://amzn.to/3yhfOpw) | ![](https://badgen.net/badge/reviews/15/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Algorithmic Trading and Quantitative Strategies (Chapman and Hall/CRC Financial Mathematics Series) - Raja Velu, Maxence Hardy, Daniel Nehren](https://amzn.to/3xUTQXZ) | ![](https://badgen.net/badge/reviews/11/blue) | ![](https://badgen.net/badge/rating/4.2/blue) |
| [Quantitative Trading: Algorithms, Analytics, Data, Models, Optimization - Xin Guo, Tze Leung Lai, Howard Shek, Samuel Po-Shing Wong](https://www.amazon.fr/gp/product/0367871815/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0367871815&linkId=3f2ba1cbc0e1fe02e255da740423b2fb) | ![](https://badgen.net/badge/reviews/2/blue) | ![](https://badgen.net/badge/rating/3/blue) |


## High Frequency Trading

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [Inside the Black Box: A Simple Guide to Quantitative and High Frequency Trading - Rishi K. Narang](https://www.amazon.fr/gp/product/1118362411/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118362411&linkId=35e02d4e636350366531a5033597a541) | ![](https://badgen.net/badge/reviews/76/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Algorithmic and High-Frequency Trading (Mathematics, Finance and Risk) - Álvaro Cartea, Sebastian Jaimungal, José Penalva](https://www.amazon.fr/gp/product/1107091144/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1107091144&linkId=64e3ceb66482d8db6827830964b85613) | ![](https://badgen.net/badge/reviews/52/blue) | ![](https://badgen.net/badge/rating/4.1/blue) |
| [The Problem of HFT – Collected Writings on High Frequency Trading & Stock Market Structure Reform - Haim Bodek](https://www.amazon.fr/gp/product/1481978357/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1481978357&linkId=2f3acf998de645990b681e2ac9f0217c) | ![](https://badgen.net/badge/reviews/38/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [An Introduction to High-Frequency Finance - Ramazan Gençay, Michel Dacorogna, Ulrich A. Muller, Olivier Pictet, Richard Olsen](https://www.amazon.fr/gp/product/0122796713/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0122796713&linkId=7e6c098026204f399e45d7fbb803dcca) | ![](https://badgen.net/badge/reviews/11/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Market Microstructure in Practice - Charles-Albert Lehalle, Sophie Laruelle](https://www.amazon.fr/Market-Microstructure-Practice-Sophie-Laruelle/dp/9813231122) | ![](https://badgen.net/badge/reviews/8/blue) | ![](https://badgen.net/badge/rating/3.9/blue) |
| [The Financial Mathematics of Market Liquidity - Olivier Gueant](https://www.amazon.com/Financial-Mathematics-Market-Liquidity-Execution/dp/1498725473) | ![](https://badgen.net/badge/reviews/6/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [High-Frequency Trading - Maureen O’Hara, David Easley, Marcos M López de Prado](https://www.amazon.fr/gp/product/178272009X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=178272009X&linkId=082f861ff6bbe4cca4ef7ccbe620a2c4) | ![](https://badgen.net/badge/reviews/1/blue) | ![](https://badgen.net/badge/rating/3/blue) |


## Machine Learning

|  Title   | Reviews | Rating |
|----------|---------|--------|
| [Dark Pools: The rise of A.I. trading machines and the looming threat to Wall Street - Scott Patterson](https://www.amazon.fr/gp/product/0307887189/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0307887189&linkId=2572cae24ed7de0b279580312daf0f03) | ![](https://badgen.net/badge/reviews/532/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Advances in Financial Machine Learning - Marcos Lopez de Prado](https://www.amazon.fr/gp/product/1119482089/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1119482089&linkId=7eff4d3f3d9f2d00d05032f726386e53) | ![](https://badgen.net/badge/reviews/446/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Machine Learning for Algorithmic Trading: Predictive models to extract signals from market and alternative data for systematic trading strategies with Python, 2nd Edition - Stefan Jansen](https://www.amazon.fr/gp/product/1839217715/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1839217715&linkId=80e3e93e1b6027596858ed0f1fbf10c2) | ![](https://badgen.net/badge/reviews/229/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Machine Learning for Asset Managers (Elements in Quantitative Finance) - Marcos M López de Prado](https://www.amazon.fr/gp/product/1108792898/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1108792898&linkId=8eb7e3c369d38b36df8dfecf05a622db) | ![](https://badgen.net/badge/reviews/96/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Machine Learning in Finance: From Theory to Practice - Matthew F. Dixon, Igor Halperin, Paul Bilokon](https://www.amazon.fr/gp/product/3030410676/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=3030410676&linkId=5f5f1df6be62ae96ef7a0c536c3ecdb4) | ![](https://badgen.net/badge/reviews/76/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Artificial Intelligence in Finance: A Python-Based Guide - Yves Hilpisch](https://www.amazon.fr/gp/product/1492055433/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1492055433&linkId=7c20249be4d35badb127d6a5423fc495) | ![](https://badgen.net/badge/reviews/38/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Algorithmic Trading Methods: Applications Using Advanced Statistics, Optimization, and Machine Learning Techniques - Robert Kissell](https://www.amazon.fr/gp/product/0128156309/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0128156309&linkId=0a197c0b547a0ee63ccd19389bb42edd) | ![](https://badgen.net/badge/reviews/15/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |


# Videos

| Title                                                              | Likes |
|--------------------------------------------------------------------|-------|
| [Krish Naik - Machine learning tutorials and their Application in Stock Prediction](https://www.youtube.com/watch?v=H6du_pfuznE) | ![](https://badgen.net/badge/likes/6.3k/blue) |
| [QuantInsti Youtube - webinars about Machine Learning for trading](https://www.youtube.com/user/quantinsti/search?query=machine+learning) | ![](https://badgen.net/badge/likes/6.1k/blue) |
| [Siraj Raval - Videos about stock market prediction using Deep Learning](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A/search?query=trading) | ![](https://badgen.net/badge/likes/1.7k/blue) |
| [Quantopian - Webinars about Machine Learning for trading](https://www.youtube.com/channel/UC606MUq45P3zFLa4VGKbxsg/search?query=machine+learning) | ![](https://badgen.net/badge/likes/1.5k/blue) |
| [Sentdex - Machine Learning for Forex and Stock analysis and algorithmic trading](https://www.youtube.com/watch?v=v_L9jR8P-54&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO) | ![](https://badgen.net/badge/likes/1.5k/blue) |
| [QuantNews - Machine Learning for Algorithmic Trading 3 part series](https://www.youtube.com/playlist?list=PLHJACfjILJ-91qkw5YC83S6COKGscctzz) | ![](https://badgen.net/badge/likes/806/blue) |
| [Sentdex - Python programming for Finance (a few videos including Machine Learning)](https://www.youtube.com/watch?v=Z-5wNWgRJpk&index=9&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ) | ![](https://badgen.net/badge/likes/735/blue) |
| [Chat with Traders EP042 - Machine learning for algorithmic trading with Bert Mouler](https://www.youtube.com/watch?v=i8FNO8r7PaE) | ![](https://badgen.net/badge/likes/687/blue) |
| [Tucker Balch - Applying Deep Reinforcement Learning to Trading](https://www.youtube.com/watch?v=Pka0DC_P17k) | ![](https://badgen.net/badge/likes/487/blue) |
| [Ernie Chan - Machine Learning for Quantitative Trading Webinar](https://www.youtube.com/watch?v=72aEDjwGMr8&t=1023s) | ![](https://badgen.net/badge/likes/436/blue) |
| [Chat with Traders EP147 - Detective work leading to viable trading strategies with Tom Starke](https://www.youtube.com/watch?v=JjXw9Mda7eY) | ![](https://badgen.net/badge/likes/407/blue) |
| [Chat with Traders EP142 - Algo trader using automation to bypass human flaws with Bert Mouler](https://www.youtube.com/watch?v=ofL66mh6Tw0) | ![](https://badgen.net/badge/likes/316/blue) |
| [Master Thesis presentation, Uni of Essex - Analyzing the Limit Order Book, A Deep Learning Approach](https://www.youtube.com/watch?v=qxSh2VFmRGw) | ![](https://badgen.net/badge/likes/264/blue) |
| [Howard Bandy - Machine Learning Trading System Development Webinar](https://www.youtube.com/watch?v=v729evhMpYk&t=1s) | ![](https://badgen.net/badge/likes/253/blue) |
| [Chat With Traders EP131 - Trading strategies, powered by machine learning with Morgan Slade](https://www.youtube.com/watch?v=EbWbeYu8zwg) | ![](https://badgen.net/badge/likes/229/blue) |
| [Chat with Traders Quantopian 5 - Good Uses of Machine Learning in Finance with Max Margenot](https://www.youtube.com/watch?v=Zj5sXWv9SDM) | ![](https://badgen.net/badge/likes/198/blue) |
| [Hitoshi Harada, CTO at Alpaca - Deep Learning in Finance Talk](https://www.youtube.com/watch?v=FoQKCeDuPiY) | ![](https://badgen.net/badge/likes/147/blue) |
| [Better System Trader EP028 - David Aronson shares research into indicators that identify Bull and Bear markets.](https://www.youtube.com/watch?v=Q4rV0Y9NokI) | ![](https://badgen.net/badge/likes/97/blue) |
| [Prediction Machines - Deep Learning with Python in Finance Talk](https://www.youtube.com/watch?v=xvm-M-R2fZY) | ![](https://badgen.net/badge/likes/87/blue) |
| [Better System Trader EP064 - Cryptocurrencies and Machine Learning with Bert Mouler](https://www.youtube.com/watch?v=YgRTd4nLJoU) | ![](https://badgen.net/badge/likes/35/blue) |
| [Better System Trader EP023 - Portfolio manager Michael Himmel talks AI and machine learning in trading](https://www.youtube.com/watch?v=9tZjeyhfG0g) | ![](https://badgen.net/badge/likes/29/blue) |
| [Better System Trader EP082 - Machine Learning With Kris Longmore](https://www.youtube.com/watch?v=0syNgsd635M) | ![](https://badgen.net/badge/likes/18/blue) |



# Blogs

| Title                                                              |
|--------------------------------------------------------------------|
| [AAA Quants, Tom Starke Blog](http://aaaquants.com/category/blog/) |
| [AI & Systematic Trading](https://blog.paperswithbacktest.com/)          |
| [Blackarbs blog](http://www.blackarbs.com/blog/)                   |
| [Hardikp, Hardik Patel blog](https://www.hardikp.com/)             |
| [Hudson River Trading - HRTBeat Engineering](https://www.hudsonrivertrading.com/hrtbeat/category/engineering/) |
| [Jane Street Tech Blog](https://blog.janestreet.com/) |
| [Man Group Tech Articles](https://www.man.com/tech-articles-all) |
| [Max Dama on Automated Trading](https://bit.ly/3wVZbh9)            |
| [Medallion.Club on Systematic Trading (FR)](https://medallion.club/trading-algorithmique-quantitatif-systematique/)            |
| [NeuPortal - AI agents forecasting crypto and prediction markets](https://neuportal.ai/blog) |
| [Proof Engineering: The Algorithmic Trading Platform](https://bit.ly/3lX7zYN) |
| [Quantsportal, Jacques Joubert's Blog](http://www.quantsportal.com/blog-page/) |
| [Quantstart - Machine Learning for Trading articles](https://www.quantstart.com/articles) |
| [RobotWealth, Kris Longmore Blog](https://robotwealth.com/blog/) |
| [Two Sigma Engineering](https://www.twosigma.com/topic/engineering/) |


# Courses

| Title                                                              |
|--------------------------------------------------------------------|
| [AI in Finance](https://cfte.education/)                           |
| [AI & Systematic Trading](https://paperswithbacktest.com/course)               |
| [Algorithmic Trading for Cryptocurrencies in Python](https://github.com/tudorelu/tudorials/tree/master/trading) |
| [Coursera, NYU - Guided Tour of Machine Learning in Finance](https://www.coursera.org/learn/guided-tour-machine-learning-finance) |
| [Coursera, NYU - Fundamentals of Machine Learning in Finance](https://www.coursera.org/learn/fundamentals-machine-learning-in-finance) |
| [Coursera, NYU - Reinforcement Learning in Finance](https://www.coursera.org/learn/reinforcement-learning-in-finance) |
| [Coursera, NYU - Overview of Advanced Methods for Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance) |
| [Hudson and Thames Quantitative Research](https://github.com/hudson-and-thames) |
| [NYU: Overview of Advanced Methods of Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance/home/welcome) |
| [Udacity: Artificial Intelligence for Trading](https://www.udacity.com/course/ai-for-trading--nd880) |
| [Udacity, Georgia Tech - Machine Learning for Trading](https://www.udacity.com/course/machine-learning-for-trading--ud501) |
