<div align="center">
  <img src="static/images/awesome-systematic-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

[希望阅读中文版？点我](./README_zh.md)

We are collecting a list of resources papers, softwares, books, articles for finding, developing, and running systematic trading (quantitative trading) strategies.

<!-- omit in toc -->
### What will you find here?

- [97 libraries and packages](#libraries-and-packages) for research and live trading
- [696 strategies](#strategies) described by institutionals and academics
- [55 books](#books) for beginners and professionals
- [23 videos](#videos) and interviews
- And also some [blogs](#blogs) and [courses](#courses)

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
  - [Bonds, commodities, currencies, equities](#bonds-commodities-currencies-equities)
  - [Bonds, commodities, equities, REITs](#bonds-commodities-equities-reits)
  - [Bonds, equities](#bonds-equities)
  - [Bonds, equities, REITs](#bonds-equities-reits)
  - [Commodities](#commodities)
  - [Cryptos](#cryptos)
  - [Currencies](#currencies)
  - [Equities](#equities)
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
> [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=A%20free%20and%20comprehensive%20list%20of%20papers%2C%20libraries%2C%20books%2C%20blogs%2C%20tutorials%20for%20quantitative%20traders.&url=https://github.com/edarchimbaud/awesome-systematic-trading)


# Libraries and packages

*List of **97 libraries and packages** implementing trading bots, backtesters, indicators, pricers, etc. Each library is categorized by its programming language and ordered by descending populatrity (number of stars).*


## Backtesting and Live Trading

### General - Event Driven Frameworks


| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [vnpy](https://github.com/vnpy/vnpy) | Python-based open source quantitative trading system development framework, officially released in January 2015, has grown step by step into a full-featured quantitative trading platform | ![GitHub stars](https://badgen.net/github/stars/vnpy/vnpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zipline](https://github.com/quantopian/zipline) | Zipline is a Pythonic algorithmic trading library. It is an event-driven system for backtesting. | ![GitHub stars](https://badgen.net/github/stars/quantopian/zipline) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtrader](https://github.com/mementum/backtrader) | Event driven Python Backtesting library for trading strategies | ![GitHub stars](https://badgen.net/github/stars/mementum/backtrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS) | QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权/港股/虚拟货币 数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案 | ![GitHub stars](https://badgen.net/github/stars/QUANTAXIS/QUANTAXIS) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QuantConnect](https://github.com/QuantConnect/Lean) | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) | ![GitHub stars](https://badgen.net/github/stars/QuantConnect/Lean) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Rqalpha](https://github.com/ricequant/rqalpha) | A extendable, replaceable Python algorithmic backtest && trading framework supporting multiple securities | ![GitHub stars](https://badgen.net/github/stars/ricequant/rqalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finmarketpy](https://github.com/cuemacro/finmarketpy) | Python library for backtesting trading strategies & analyzing financial markets (formerly pythalesians) | ![GitHub stars](https://badgen.net/github/stars/cuemacro/finmarketpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtesting.py](https://github.com/kernc/backtesting.py) | Backtesting.py is a Python framework for inferring viability of trading strategies on historical (past) data. Improved upon the vision of Backtrader, and by all means surpassingly comparable to other accessible alternatives, Backtesting.py is lightweight, fast, user-friendly, intuitive, interactive, intelligent and, hopefully, future-proof. | ![GitHub stars](https://badgen.net/github/stars/kernc/backtesting.py) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zvt](https://github.com/zvtvz/zvt) | Modular quant framework | ![GitHub stars](https://badgen.net/github/stars/zvtvz/zvt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [WonderTrader](https://github.com/wondertrader/wondertrader) | WonderTrader——量化研发交易一站式框架  | ![GitHub stars](https://badgen.net/github/stars/wondertrader/wondertrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester | ![GitHub stars](https://badgen.net/github/stars/nautechsystems/nautilus_trader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PandoraTrader](https://github.com/pegasusTrader/PandoraTrader) | High-frequency quantitative trading platform based on c++ development, supporting multiple trading APIs and cross-platform | ![GitHub stars](https://badgen.net/github/stars/pegasusTrader/PandoraTrader) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [aat](https://github.com/AsyncAlgoTrading/aat) | An asynchronous, event-driven framework for writing algorithmic trading strategies in python with optional acceleration in C++. It is designed to be modular and extensible, with support for a wide variety of instruments and strategies, live trading across (and between) multiple exchanges. | ![GitHub stars](https://badgen.net/github/stars/AsyncAlgoTrading/aat) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) | This project is mainly for newbies into algo trading who are interested in learning to code their own trading algo using python interpreter. | ![GitHub stars](https://badgen.net/github/stars/sreenivasdoosa/sdoosa-algo-trade-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [lumibot](https://github.com/Lumiwealth/lumibot) | A very simple yet useful backtesting and sample based live trading framework (a bit slow to run...) | ![GitHub stars](https://badgen.net/github/stars/Lumiwealth/lumibot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [quanttrader](https://github.com/letianzj/quanttrader) | Backtest and live trading in Python. Event based. Similar to backtesting.py. | ![GitHub stars](https://badgen.net/github/stars/letianzj/quanttrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [gobacktest](https://github.com/gobacktest/gobacktest) | A Go implementation of event-driven backtesting framework | ![GitHub stars](https://badgen.net/github/stars/gobacktest/gobacktest) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [FlashFunk](https://github.com/HFQR/FlashFunk) | High Performance Runtime in Rust | ![GitHub stars](https://badgen.net/github/stars/HFQR/FlashFunk) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |


### General - Vector Based Frameworks

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [vectorbt](https://github.com/polakowo/vectorbt) | vectorbt takes a novel approach to backtesting: it operates entirely on pandas and NumPy objects, and is accelerated by Numba to analyze any data at speed and scale. This allows for testing of many thousands of strategies in seconds. | ![GitHub stars](https://badgen.net/github/stars/polakowo/vectorbt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | Systematic Trading in python from book Systematic Trading by Rob Carver | ![GitHub stars](https://badgen.net/github/stars/robcarver17/pysystemtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [bt](https://github.com/pmorissette/bt) | Flexible backtesting for Python based on Algo and Strategy Tree | ![GitHub stars](https://badgen.net/github/stars/pmorissette/bt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


### Cryptocurrencies

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Freqtrade](https://github.com/freqtrade/freqtrade) | Freqtrade is a free and open source crypto trading bot written in Python. It is designed to support all major exchanges and be controlled via Telegram. It contains backtesting, plotting and money management tools as well as strategy optimization by machine learning. | ![GitHub stars](https://badgen.net/github/stars/freqtrade/freqtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Jesse](https://github.com/jesse-ai/jesse) | Jesse is an advanced crypto trading framework which aims to simplify researching and defining trading strategies. | ![GitHub stars](https://badgen.net/github/stars/jesse-ai/jesse) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OctoBot](https://github.com/Drakkar-Software/OctoBot) | Cryptocurrency trading bot for TA, arbitrage and social trading with an advanced web interface | ![GitHub stars](https://badgen.net/github/stars/Drakkar-Software/OctoBot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Kelp](https://github.com/stellar/kelp) | Kelp is a free and open-source trading bot for the Stellar DEX and 100+ centralized exchanges | ![GitHub stars](https://badgen.net/github/stars/stellar/kelp) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [openlimits](https://github.com/nash-io/openlimits) | A Rust high performance cryptocurrency trading API with support for multiple exchanges and language wrappers. | ![GitHub stars](https://badgen.net/github/stars/nash-io/openlimits) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [bTrader](https://github.com/gabriel-milan/btrader) | Triangle arbitrage trading bot for Binance | ![GitHub stars](https://badgen.net/github/stars/gabriel-milan/btrader) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) | Crawl orderbook and trade messages from crypto exchanges | ![GitHub stars](https://badgen.net/github/stars/crypto-crawler/crypto-crawler-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [Hummingbot](https://github.com/CoinAlpha/hummingbot) | A client for crypto market making | ![GitHub stars](https://badgen.net/github/stars/CoinAlpha/hummingbot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cryptotrader-core](https://github.com/monomadic/cryptotrader-core) | Simple to use Crypto Exchange REST API client in rust. | ![GitHub stars](https://badgen.net/github/stars/monomadic/cryptotrader-core) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

## Trading bots

*Trading bots and alpha models. Some of them are old and not maintained.*

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Blackbird](https://github.com/butor/blackbird) | Blackbird Bitcoin Arbitrage: a long/short market-neutral strategy | ![GitHub stars](https://badgen.net/github/stars/butor/blackbird) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | Bitcoin arbitrage - opportunity detector | ![GitHub stars](https://badgen.net/github/stars/maxme/bitcoin-arbitrage) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ThetaGang](https://github.com/brndnmtthws/thetagang) | ThetaGang is an IBKR bot for collecting money | ![GitHub stars](https://badgen.net/github/stars/brndnmtthws/thetagang) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [czsc](https://github.com/waditu/czsc) | 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 | ![GitHub stars](https://badgen.net/github/stars/waditu/czsc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2) | R2 Bitcoin Arbitrager is an automatic arbitrage trading system powered by Node.js + TypeScript | ![GitHub stars](https://badgen.net/github/stars/bitrinjani/r2) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [analyzingalpha](https://github.com/leosmigel/analyzingalpha) | Implementation of simple strategies | ![GitHub stars](https://badgen.net/github/stars/leosmigel/analyzingalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow) | PyTrendFollow - systematic futures trading using trend following | ![GitHub stars](https://badgen.net/github/stars/chrism2671/PyTrendFollow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Analytics

### Indicators

*Libraries of indicators to predict future price movements.*

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [ta-lib](https://github.com/mrjbq7/ta-lib) | Perform technical analysis of financial market data | ![GitHub stars](https://badgen.net/github/stars/mrjbq7/ta-lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [go-tart](https://github.com/iamjinlei/go-tart) | A Go implementation of the [ta-lib]((https://github.com/mrjbq7/ta-lib) with streaming update support | ![GitHub stars](https://badgen.net/github/stars/iamjinlei/go-tart) | ![made-with-go](https://img.shields.io/badge/Made%20with-go-1f425f.svg) |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | Pandas Technical Analysis (Pandas TA) is an easy to use library that leverages the Pandas package with more than 130 Indicators and Utility functions and more than 60 TA Lib Candlestick Patterns | ![GitHub stars](https://badgen.net/github/stars/twopirllc/pandas-ta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finta](https://github.com/peerchemist/finta) | Common financial technical indicators implemented in Pandas | ![GitHub stars](https://badgen.net/github/stars/peerchemist/finta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ta-rust](https://github.com/greyblake/ta-rs) | Technical analysis library for Rust language | ![GitHub stars](https://badgen.net/github/stars/greyblake/ta-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### Metrics computation

*Librairies of financial metrics.*

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [quantstats](https://github.com/ranaroussi/quantstats) | Portfolio analytics for quants, written in Python | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/quantstats) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ffn](https://github.com/pmorissette/ffn) | A financial function library for Python | ![GitHub stars](https://badgen.net/github/stars/pmorissette/ffn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Optimization

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | Financial portfolio optimizations in python, including classical efficient frontier, Black-Litterman, Hierarchical Risk Parity | ![GitHub stars](https://badgen.net/github/stars/robertmartin8/PyPortfolioOpt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | Portfolio Optimization and Quantitative Strategic Asset Allocation in Python | ![GitHub stars](https://badgen.net/github/stars/dcajasn/Riskfolio-Lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [empyrial](https://github.com/ssantoshp/Empyrial) | Empyrial is a Python-based open-source quantitative investment library dedicated to financial institutions and retail investors, officially released in March 2021 | ![GitHub stars](https://badgen.net/github/stars/ssantoshp/Empyrial) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Deepdow](https://github.com/jankrepl/deepdow) | Python package connecting portfolio optimization and deep learning. Its goal is to facilitate research of networks that perform weight allocation in one forward pass. | ![GitHub stars](https://badgen.net/github/stars/jankrepl/deepdow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
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
| [pyfolio](https://github.com/quantopian/pyfolio) | Portfolio and risk analytics in Python | ![GitHub stars](https://badgen.net/github/stars/quantopian/pyfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |



## Broker APIs

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [ccxt](https://github.com/ccxt/ccxt) | A JavaScript / Python / PHP cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges | ![GitHub stars](https://badgen.net/github/stars/ccxt/ccxt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Ib_insync](https://github.com/erdewit/ib_insync) | Python sync/async framework for Interactive Brokers. | ![GitHub stars](https://badgen.net/github/stars/erdewit/ib_insync) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Coinnect](https://github.com/hugues31/coinnect) | Coinnect is a Rust library aiming to provide a complete access to main crypto currencies exchanges via REST API. | ![GitHub stars](https://badgen.net/github/stars/hugues31/coinnect) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) | Javascript SDK for Trading, Data, and Websockets for FTX, FTXUS, OKX, Bybit, & More. | ![GitHub stars](https://badgen.net/github/stars/CompendiumFi/PENDAX-SDK) | ![made-with-javascript](https://img.shields.io/badge/Made%20with-Javascript-1f425f.svg) |


## Data Sources

### General

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) | Investment Research for Everyone, Anywhere. | ![GitHub stars](https://badgen.net/github/stars/OpenBB-finance/OpenBBTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TuShare](https://github.com/waditu/tushare) | TuShare is a utility for crawling historical data of China stocks | ![GitHub stars](https://badgen.net/github/stars/waditu/tushare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [yfinance](https://github.com/ranaroussi/yfinance) | yfinance offers a threaded and Pythonic way to download market data from Yahoo!Ⓡ finance. | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/yfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AkShare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! | ![GitHub stars](https://badgen.net/github/stars/akfamily/akshare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pandas-datareader](https://github.com/pydata/pandas-datareader) | Up to date remote data access for pandas, works for multiple versions of pandas. | ![GitHub stars](https://badgen.net/github/stars/pydata/pandas-datareader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Quandl](https://github.com/quandl/quandl-python) | Get millions of financial and economic dataset from hundreds of publishers via a single free API. | ![GitHub stars](https://badgen.net/github/stars/quandl/quandl-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [findatapy](https://github.com/cuemacro/findatapy) | findatapy creates an easy to use Python API to download market data from many sources including Quandl, Bloomberg, Yahoo, Google etc. using a unified high level interface. | ![GitHub stars](https://badgen.net/github/stars/cuemacro/findatapy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Investpy](https://github.com/alvarobartt/investpy) | Financial Data Extraction from Investing.com with Python | ![GitHub stars](https://badgen.net/github/stars/alvarobartt/investpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | Fully-fledged Fundamental Analysis package capable of collecting 20 years of Company Profiles, Financial Statements, Ratios and Stock Data of 20.000+ companies. | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FundamentalAnalysis) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Wallstreet](https://github.com/mcdallas/wallstreet) | Wallstreet: Real time Stock and Option tools | ![GitHub stars](https://badgen.net/github/stars/mcdallas/wallstreet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |



### Cryptocurrencies

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Cryptofeed](https://github.com/bmoscon/cryptofeed) | Cryptocurrency Exchange Websocket Data Feed Handler with Asyncio | ![GitHub stars](https://badgen.net/github/stars/bmoscon/cryptofeed) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) | Gekko trading bot dataset dumps. Download and use history files in SQLite format. | ![GitHub stars](https://badgen.net/github/stars/xFFFFF/Gekko-Datasets) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) | A live crypto currency historical trade data blotter. Download live historical trade data from any crypto exchange. | ![GitHub stars](https://badgen.net/github/stars/Optixal/CryptoInscriber) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Data Science

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [TensorFlow](https://github.com/tensorflow/tensorflow) | Fundamental algorithms for scientific computing in Python | ![GitHub stars](https://badgen.net/github/stars/tensorflow/tensorflow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pytorch](https://github.com/pytorch/pytorch) | Tensors and Dynamic neural networks in Python with strong GPU acceleration | ![GitHub stars](https://badgen.net/github/stars/pytorch/pytorch) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Keras](https://github.com/keras-team/keras) | The most user friendly Deep Learning for humans in Python | ![GitHub stars](https://badgen.net/github/stars/keras-team/keras) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | Machine learning in Python | ![GitHub stars](https://badgen.net/github/stars/scikit-learn/scikit-learn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pandas](https://github.com/pandas-dev/pandas) | Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more | ![GitHub stars](https://badgen.net/github/stars/pandas-dev/pandas) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Numpy](https://github.com/numpy/numpy) | The fundamental package for scientific computing with Python | ![GitHub stars](https://badgen.net/github/stars/numpy/numpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scipy](https://github.com/scipy/scipy) | Fundamental algorithms for scientific computing in Python | ![GitHub stars](https://badgen.net/github/stars/scipy/scipy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyMC](https://github.com/pymc-devs/pymc) | Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Aesara | ![GitHub stars](https://badgen.net/github/stars/pymc-devs/pymc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Cvxpy](https://github.com/cvxpy/cvxpy) | A Python-embedded modeling language for convex optimization problems. | ![GitHub stars](https://badgen.net/github/stars/cvxpy/cvxpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Databases

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Marketstore](https://github.com/alpacahq/marketstore) | DataFrame Server for Financial Timeseries Data | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [Tectonicdb](https://github.com/0b01/tectonicdb) | Tectonicdb is a fast, highly compressed standalone database and streaming protocol for order book ticks. | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [ArcticDB (Man Group)](https://github.com/man-group/arcticdb) | High performance datastore for time series and tick data | ![GitHub stars](https://badgen.net/github/stars/man-group/ArcticDB) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Graph Computation

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [Ray](https://github.com/ray-project/ray) | An open source framework that provides a simple, universal API for building distributed applications. | ![GitHub stars](https://badgen.net/github/stars/ray-project/ray) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Dask](https://github.com/dask/dask) | Parallel computing with task scheduling in Python with a Pandas like API | ![GitHub stars](https://badgen.net/github/stars/dask/dask) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | Incremental is a library that gives you a way of building complex computations that can update efficiently in response to their inputs changing, inspired by the work of Umut Acar et. al. on self-adjusting computations. Incremental can be useful in a number of applications | ![GitHub stars](https://badgen.net/github/stars/janestreet/incremental) | ![made-with-ocaml](https://img.shields.io/badge/Made%20with-Ocaml-1f425f.svg) |
| [Man MDF](https://github.com/man-group/mdf) | Data-flow programming toolkit for Python | ![GitHub stars](https://badgen.net/github/stars/man-group/mdf) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [GraphKit](https://github.com/yahoo/graphkit) | A lightweight Python module for creating and running ordered graphs of computations. | ![GitHub stars](https://badgen.net/github/stars/yahoo/graphkit) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Tributary](https://github.com/timkpaine/tributary) | Streaming reactive and dataflow graphs in Python | ![GitHub stars](https://badgen.net/github/stars/timkpaine/tributary) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## Machine Learning

| Repository | Description | Stars | Made with |
|------------|-------------|-------|-----------|
| [QLib (Microsoft)](https://github.com/microsoft/qlib) | Qlib is an AI-oriented quantitative investment platform, which aims to realize the potential, empower the research, and create the value of AI technologies in quantitative investment. With Qlib, you can easily try your ideas to create better Quant investment strategies. An increasing number of SOTA Quant research works/papers are released in Qlib. | ![GitHub stars](https://badgen.net/github/stars/microsoft/qlib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | FinRL is the first open-source framework to demonstrate the great potential of applying deep reinforcement learning in quantitative finance. | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinRL) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [MlFinLab (Hudson & Thames)](https://github.com/hudson-and-thames/mlfinlab) | MlFinLab helps portfolio managers and traders who want to leverage the power of machine learning by providing reproducible, interpretable, and easy to use tools. | ![GitHub stars](https://badgen.net/github/stars/hudson-and-thames/mlfinlab) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradingGym](https://github.com/Yvictor/TradingGym) | Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo. | ![GitHub stars](https://badgen.net/github/stars/Yvictor/TradingGym) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) | Stock Trading Bot using Deep Q-Learning | ![GitHub stars](https://badgen.net/github/stars/pskrunner14/trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


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
| [D-Tale (Man Group)](https://github.com/man-group/dtale) | D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures. | ![GitHub stars](https://badgen.net/github/stars/man-group/dtale) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [mplfinance](https://github.com/matplotlib/mplfinance) | Financial Markets Data Visualization using Matplotlib | ![GitHub stars](https://badgen.net/github/stars/matplotlib/mplfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [btplotting](https://github.com/happydasch/btplotting) | btplotting provides plotting for backtests, optimization results and live data from backtrader. | ![GitHub stars](https://badgen.net/github/stars/happydasch/btplotting) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


# Strategies

*List of **696 academic papers** describing original systematic trading strategies. Each strategy is categorized by its asset class and ordered by descending Sharpe ratio.*

👉 Strategies are now hosted [here](https://edarchimbaud.com):

- [Bonds strategies (7)](https://edarchimbaud.com/bonds)
- [Commodities strategies (50)](https://edarchimbaud.com/commodities)
- [Cryptocurrencies strategies (12)](https://edarchimbaud.com/cryptocurrencies)
- [Currencies strategies (67)](https://edarchimbaud.com/currencies)
- [Equities strategies (471)](https://edarchimbaud.com/equities)
- [Options strategies (8)](https://edarchimbaud.com/options)
- [Bonds / Commodities / Currencies / Equities strategies (22)](https://edarchimbaud.com/bonds-commodities-currencies-equities)
- [Bonds / Commodities / Equities strategies (6)](https://edarchimbaud.com/bonds-commodities-equities)
- [Bonds / Commodities / Equities / REITs strategies (6)](https://edarchimbaud.com/bonds-commodities-equities-reits)
- [Bonds / Equities strategies (13)](https://edarchimbaud.com/bonds-equities)
- [Bonds / Equities / REITs strategies (6)](https://edarchimbaud.com/bonds-equities-reits)
- [Commodities / Equities strategies (3)](https://edarchimbaud.com/commodities-equities)
- [Equities / Options strategies (24)](https://edarchimbaud.com/equities-options)
- [Equities / REITs strategies (1)](https://edarchimbaud.com/equities-reits)

Previous list of strategies:

## Bonds, commodities, currencies, equities

| Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------------|--------------|------------|-------------|----------------|--------|
| Time Series Momentum Effect | `0.576` | `20.5%` | `Monthly` | [QuantConnect](./static/strategies/time-series-momentum-effect.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/TimeSeriesMomentum.pdf) |
| Short Term Reversal with Futures | `-0.05` | `12.3%` | `Weekly` | [QuantConnect](./static/strategies/asset-class-momentum-rotational-system.py) | [Paper](https://ideas.repec.org/a/eee/jbfina/v28y2004i6p1337-1361.html) |

## Bonds, commodities, equities, REITs

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| Asset Class Trend-Following | `0.502` | `10.4%` | `Monthly` | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) |
| Momentum Asset Allocation Strategy | `0.321` | `11%` | `Monthly` | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |

## Bonds, equities

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| Paired Switching | `0.691` | `9.5%` | `Quarterly` | [QuantConnect](./static/strategies/paired-switching.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1917044) |
| FED Model | `0.369` | `14.3%` | `Monthly` | [QuantConnect](./static/strategies/fed-model.py) | [Paper](https://www.researchgate.net/publication/228267011_The_FED_Model_and_Expected_Asset_Returns) |

## Bonds, equities, REITs

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| Value and Momentum Factors across Asset Classes | `0.155` | `9.8%` | `Monthly` | [QuantConnect](./static/strategies/value-and-momentum-factors-across-asset-classes.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1079975) |

## Commodities

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| Skewness Effect in Commodities | `0.482` | `17.7%` | `Monthly` | [QuantConnect](./static/strategies/skewness-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2671165) |
| Return Asymmetry Effect in Commodity Futures | `0.239` | `13.4%` | `Monthly` | [QuantConnect](./static/strategies/return-asymmetry-effect-in-commodity-futures.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3918896) |
| Momentum Effect in Commodities | `0.14` | `20.3%` | `Monthly` | [QuantConnect](./static/strategies/momentum-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=702281) |
| Term Structure Effect in Commodities | `0.128` | `23.1%` | `Monthly` | [QuantConnect](./static/strategies/term-structure-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1127213) |
| Trading WTI/BRENT Spread | `-0.199` | `11.6%` | `Daily` | [QuantConnect](./static/strategies/trading-wti-brent-spread.py) | [Paper](https://link.springer.com/article/10.1057/jdhf.2009.24) |

## Cryptos

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| Overnight Seasonality in Bitcoin | `0.892` | `20.8%` | `Intraday` | [QuantConnect](./static/strategies/intraday-seasonality-in-bitcoin.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4081000) |
| Rebalancing Premium in Cryptocurrencies | `0.698` | `27.5%` | `Daily` | [QuantConnect](./static/strategies/rebalancing-premium-in-cryptocurrencies.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3982120) |

## Currencies

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| FX Carry Trade | `0.254` | `7.8%` | `Monthly` | [QuantConnect](./static/strategies/fx-carry-trade.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| Dollar Carry Trade | `0.113` | `5.8%` | `Monthly` | [QuantConnect](./static/strategies/dollar-carry-trade.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1541230) |
| Currency Momentum Factor | `-0.01` | `6.7%` | `Monthly` | [QuantConnect](./static/strategies/currency-momentum-factor.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| Currency Value Factor – PPP Strategy | `-0.103` | `5%` | `Quarterly` | [QuantConnect](./static/strategies/currency-value-factor-ppp-strategy.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |

## Equities

|  Title       | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
| Asset Growth Effect | `0.835` | `10.2%` | `Yearly` | [QuantConnect](./static/strategies/asset-growth-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1335524) |
| Short Term Reversal Effect in Stocks | `0.816` | `21.4%` | `Weekly` | [QuantConnect](./static/strategies/short-term-reversal-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1605049) |
| Reversal During Earnings-Announcements | `0.785` | `25.7%` | `Daily` | [QuantConnect](./static/strategies/reversal-during-earnings-announcements.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2275982) |
| Size Factor – Small Capitalization Stocks Premium | `0.747` | `11.1%` | `Yearly` | [QuantConnect](./static/strategies/small-capitalization-stocks-premium-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3177539) |
| Low Volatility Factor Effect in Stocks | `0.717` | `11.5%` | `Monthly` | [QuantConnect](./static/strategies/low-volatility-factor-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=980865) |
| How to Use Lexical Density of Company Filings | `0.688` | `10.4%` | `Monthly` | [QuantConnect](./static/strategies/how-to-use-lexical-density-of-company-filings.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3921091) |
| Volatility Risk Premium Effect | `0.637` | `13.2%` | `Monthly` | [QuantConnect](./static/strategies/volatility-risk-premium-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=189840) |
| Pairs Trading with Stocks | `0.634` | `8.5%` | `Daily` | [QuantConnect](./static/strategies/pairs-trading-with-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=141615) |
| Crude Oil Predicts Equity Returns | `0.599` | `11.5%` | `Monthly` | [QuantConnect](./static/strategies/crude-oil-predicts-equity-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=460500) |
| Betting Against Beta Factor in Stocks | `0.594` | `18.9%` | `Monthly` | [QuantConnect](./static/strategies/betting-against-beta-factor-in-stocks.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf) |
| Trend-following Effect in Stocks | `0.569` | `15.2%` | `Daily` | [QuantConnect](./static/strategies/trend-following-effect-in-stocks.py) | [Paper](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf) |
| ESG Factor Momentum Strategy | `0.559` | `21.8%` | `Monthly` | [QuantConnect](./static/strategies/esg-factor-momentum-strategy.py) | [Paper](https://www.semanticscholar.org/paper/Can-ESG-Add-Alpha-An-Analysis-of-ESG-Tilt-and-Nagy-Kassam/64f77da4f8ce5906a73ffe4e9eec7c49c0960acc) |
| Value (Book-to-Market) Factor | `0.526` | `11.9%` | `Monthly` | [QuantConnect](./static/strategies/value-book-to-market-factor.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2595747) |
| Soccer Clubs’ Stocks Arbitrage | `0.515` | `14.2%` | `Daily` | [QuantConnect](./static/strategies/soccer-clubs-stocks-arbitrage.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1343685) |
| Synthetic Lending Rates Predict Subsequent Market Return | `0.494` | `13.7%` | `Daily` | [QuantConnect](./static/strategies/synthetic-lending-rates-predict-subsequent-market-return.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3976307) |
| Option-Expiration Week Effect | `0.452` | `5%` | `Weekly` | [QuantConnect](./static/strategies/option-expiration-week-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1571786) |
| Dispersion Trading | `0.432` | `8.1%` | `Monthly` | [QuantConnect](./static/strategies/dispersion-trading.py) | [Paper](https://www.academia.edu/16327015/EQUILIBRIUM_INDEX_AND_SINGLE_STOCK_VOLATILITY_RISK_PREMIA) |
| Momentum in Mutual Fund Returns | `0.414` | `13.6%` | `Quarterly` | [QuantConnect](./static/strategies/momentum-in-mutual-fund-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1462408) |
| Sector Momentum – Rotational System | `0.401` | `14.1%` | `Monthly` | [QuantConnect](./static/strategies/sector-momentum-rotational-system.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |
| Combining Smart Factors Momentum and Market Portfolio | `0.388` | `8.2%` | `Monthly` | [QuantConnect](./static/strategies/combining-smart-factors-momentum-and-market-portfolio.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3745517) |
| Momentum and Reversal Combined with Volatility Effect in Stocks | `0.375` | `17%` | `Monthly` | [QuantConnect](./static/strategies/momentum-and-reversal-combined-with-volatility-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1679464) |
| Market Sentiment and an Overnight Anomaly | `0.369` | `3.6%` | `Daily` | [QuantConnect](./static/strategies/market-sentiment-and-an-overnight-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3829582) |
| January Barometer | `0.365` | `7.4%` | `Monthly` | [QuantConnect](./static/strategies/january-barometer.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1436516) |
| R&D Expenditures and Stock Returns | `0.354` | `8.1%` | `Yearly` | [QuantConnect](./static/strategies/rd-expenditures-and-stock-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227564) |
| Value Factor – CAPE Effect within Countries | `0.351` | `20.2%` | `Yearly` | [QuantConnect](./static/strategies/value-factor-effect-within-countries.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2129474) |
| 12 Month Cycle in Cross-Section of Stocks Returns | `0.34` | `43.7%` | `Monthly` | [QuantConnect](./static/strategies/12-month-cycle-in-cross-section-of-stocks-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=687022) |
| Turn of the Month in Equity Indexes | `0.305` | `7.2%` | `Daily` | [QuantConnect](./static/strategies/turn-of-the-month-in-equity-indexes.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=917884) |
| Payday Anomaly | `0.269` | `3.8%` | `Daily` | [QuantConnect](./static/strategies/payday-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257064) |
| Pairs Trading with Country ETFs | `0.257` | `5.7%` | `Daily` | [QuantConnect](./static/strategies/pairs-trading-with-country-etfs.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1958546) |
| Residual Momentum Factor | `0.24` | `9.7%` | `Monthly` | [QuantConnect](./static/strategies/residual-momentum-factor.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2319861) |
| Earnings Announcement Premium | `0.192` | `3.7%` | `Monthly` | [QuantConnect](./static/strategies/earnings-announcement-premium.py) | [Paper](https://www.nber.org/system/files/working_papers/w13090/w13090.pdf) |
| ROA Effect within Stocks | `0.155` | `8.7%` | `Monthly` | [QuantConnect](./static/strategies/roa-effect-within-stocks.py) | [Paper](https://static1.squarespace.com/static/5e6033a4ea02d801f37e15bb/t/5f61583e88f43b7d5b7196b5/1600215105801/Chen_Zhang_JF.pdf) |
| 52-Weeks High Effect in Stocks | `0.153` | `19%` | `Monthly` | [QuantConnect](./static/strategies/52-weeks-high-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1787378) |
| Combining Fundamental FSCORE and Equity Short-Term Reversals | `0.153` | `17.6%` | `Monthly` | [QuantConnect](./static/strategies/combining-fundamental-fscore-and-equity-short-term-reversals.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3097420) |
| Betting Against Beta Factor in International Equities | `0.142` | `9.1%` | `Monthly` | [QuantConnect](./static/strategies/betting-against-beta-factor-in-country-equity-indexes.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf) |
| Consistent Momentum Strategy | `0.128` | `28.8%` | `6 Months` | [QuantConnect](./static/strategies/consistent-momentum-strategy.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2652592) |
| Short Interest Effect – Long-Short Version | `0.079` | `6.6%` | `Monthly` | [QuantConnect](./static/strategies/short-interest-effect-long-short-version.py) | [Paper](https://www.semanticscholar.org/paper/Why-Do-Short-Interest-Levels-Predict-Stock-Returns-Boehmer-Erturk/06418ef437dc7156229532a97d0f8392373eb297?p2df) |
| Momentum Factor Combined with Asset Growth Effect | `0.058` | `25.1%` | `Monthly` | [QuantConnect](./static/strategies/momentum-factor-combined-with-asset-growth-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1684767) |
| Momentum Factor Effect in Stocks | `-0.008` | `21.8%` | `Monthly` | [QuantConnect](./static/strategies/momentum-factor-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2435323) |
| Momentum Factor and Style Rotation Effect | `-0.056` | `10%` | `Monthly` | [QuantConnect](./static/strategies/momentum-factor-and-style-rotation-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1276815) |
| Earnings Announcements Combined with Stock Repurchases | `-0.16` | `0.1%` | `Daily` | [QuantConnect](./static/strategies/earnings-announcements-combined-with-stock-repurchases.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2589966) |
| Earnings Quality Factor | `-0.18` | `28.7%` | `Yearly` | [QuantConnect](./static/strategies/earnings-quality-factor.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2179247) |
| Accrual Anomaly | `-0.272` | `13.7%` | `Yearly` | [QuantConnect](./static/strategies/accrual-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=546108) |
| ESG, Price Momentum and Stochastic Optimization | `N/A` | `N/A` | `Monthly` |  | [Paper](https://quantpedia.com/strategies/esg-price-momentum-and-stochastic-optimization/) |
| The Positive Similarity of Company Filings and Stock Returns | `N/A` | `N/A` | `Monthly` |  | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690461) |

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
| [AI & Systematic Trading](https://blog.edarchimbaud.com/)          |
| [Blackarbs blog](http://www.blackarbs.com/blog/)                   |
| [Hardikp, Hardik Patel blog](https://www.hardikp.com/)             |
| [Max Dama on Automated Trading](https://bit.ly/3wVZbh9)            |
| [Medallion.Club on Systematic Trading (FR)](https://medallion.club/trading-algorithmique-quantitatif-systematique/)            |
| [Proof Engineering: The Algorithmic Trading Platform](https://bit.ly/3lX7zYN) |
| [Quantsportal, Jacques Joubert's Blog](http://www.quantsportal.com/blog-page/) |
| [Quantstart - Machine Learning for Trading articles](https://www.quantstart.com/articles) |
| [RobotWealth, Kris Longmore Blog](https://robotwealth.com/blog/) |


# Courses

| Title                                                              |
|--------------------------------------------------------------------|
| [AI in Finance](https://cfte.education/)                           |
| [AI & Systematic Trading](https://edarchimbaud.com/)               |
| [Algorithmic Trading for Cryptocurrencies in Python](https://github.com/tudorelu/tudorials/tree/master/trading) |
| [Coursera, NYU - Guided Tour of Machine Learning in Finance](https://www.coursera.org/learn/guided-tour-machine-learning-finance) |
| [Coursera, NYU - Fundamentals of Machine Learning in Finance](https://www.coursera.org/learn/fundamentals-machine-learning-in-finance) |
| [Coursera, NYU - Reinforcement Learning in Finance](https://www.coursera.org/learn/reinforcement-learning-in-finance) |
| [Coursera, NYU - Overview of Advanced Methods for Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance) |
| [Hudson and Thames Quantitative Research](https://github.com/hudson-and-thames) |
| [NYU: Overview of Advanced Methods of Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance/home/welcome) |
| [Udacity: Artificial Intelligence for Trading](https://www.udacity.com/course/ai-for-trading--nd880) |
| [Udacity, Georgia Tech - Machine Learning for Trading](https://www.udacity.com/course/machine-learning-for-trading--ud501) |
