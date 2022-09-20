<div align="center">
  <img src="static/future-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

We are collecting a list of resources papers, softwares, books, articles for finding, developing, and running systematic trading (quantitative trading) strategies.

<!-- omit in toc -->
### What will you find here?

- [96 Libraries and packages](#libraries-and-packages) for research and live trading
- [90 Strategies](#strategies) described by institutionals and academics
- [56 Books](#books) for beginners and professionals
- [Blogs](#blogs)
- [Courses and Tutorials](#courses-and-tutorials)

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
</details>

<!-- omit in toc -->
> ### How can I help?
> You can help by submitting an issue with suggestions and by sharing on Twitter:
>
> [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=A%20free%20and%20comprehensive%20list%20of%20papers%2C%20libraries%2C%20books%2C%20blogs%2C%20tutorials%20for%20quantitative%20traders.&url=https://github.com/edarchimbaud/awesome-systematic-trading)


# Libraries and packages

*List of **96 libraries and packages** implementing trading bots, backtesters, indicators, pricers, etc. Each library is categorized by its programming language and ordered by descending populatrity (number of stars).*


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
| [Arctic (Man Group)](https://github.com/man-group/arctic) | High performance datastore for time series and tick data | ![GitHub stars](https://badgen.net/github/stars/man-group/arctic) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Marketstore](https://github.com/alpacahq/marketstore) | DataFrame Server for Financial Timeseries Data | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [Tectonicdb](https://github.com/0b01/tectonicdb) | Tectonicdb is a fast, highly compressed standalone database and streaming protocol for order book ticks. | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

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

*List of **90 academic papers** describing original systematic trading strategies. Each strategy is categorized by its asset class and ordered by descending Sharpe ratio.*

## ETFs

|  Description | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|--------------|--------------|------------|-------------|----------------|--------|
|  Asset Class Trend-Following | `0.486` | `10.7%` | `monthly` | [QuantConnect](./strategies/relative_strength_strategies_for_investing.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |

## Bonds

| Sharpe Ratio | Volatility | Period of Rebalancing | Implementation | Source | Description |
|--------------|------------|-----------------------|----------------|-------|-------------|
| 0.89         | 7.69%      | Weekly                | []() | [Paper](https://bit.ly/38XmXRR) | Overnight-Intraday Daily Reversal in Commodities |




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




# Books

A comprehensive list of **56 books** for quantitative traders.


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

