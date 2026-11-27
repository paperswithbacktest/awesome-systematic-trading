<div align="center">
  <img src="static/images/awesome-systematic-trading.jpeg" height=200 alt=""/>
  <h1>令人敬畏的系统化交易</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

[English version here](./README.md)<br>
[日本語版はこちら](./README_ja.md)

我们正在收集一份关于寻找、开发和运行系统性交易（量化交易）策略的资源论文、软件、书籍、文章清单。

<!-- omit in toc -->
### 用 Papers With Backtest 复现第一篇论文

从已发表的策略、对应的 Python 代码和数据开始。将策略克隆到自己的工作区，在浏览器中运行回测。

**[试用价值与规模效应示例 →](https://paperswithbacktest.com/strategies/value-and-size-effect-now-you-see-it-now-you-don-t?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_zh_primary)**

无需信用卡，也无需本地安装。免费账户包含**一次完整策略解锁、一次克隆和 1 美元研究代理额度**。
这些额度每个账户仅提供一次，不会重置；已解锁的策略可持续阅读。

从以下示例中选择一个，使用你的免费解锁额度：

| 研究问题 | 打开示例 |
|---|---|
| 价值和规模如何影响股票收益？ | [价值与规模效应](https://paperswithbacktest.com/strategies/value-and-size-effect-now-you-see-it-now-you-don-t?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_zh_equity) |
| 相关性是否能改善商品动量策略？ | [商品动量](https://paperswithbacktest.com/strategies/how-to-improve-commodity-momentum-using-intra-market-correlation?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_zh_commodity) |
| 趋势与均值回归在比特币市场中表现如何？ | [比特币的季节性、趋势与均值回归](https://paperswithbacktest.com/strategies/seasonality-trend-following-and-mean-reversion-in-bitcoin?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_zh_bitcoin) |

<details>
<summary>完成第一次回测的步骤</summary>

1. 打开一个示例，创建免费账户，解锁该策略的代码和回测结果。
2. 将策略克隆到自己的工作区，回测会在策略聊天窗口中开始运行。
3. 查看结果和代码。使用可用的代理额度，询问回测包含哪些交易成本，以及这些成本如何影响结果。

后续研究会消耗剩余代理额度，也可以充值。
**Backtester** 包含每月 100 次策略解锁、市场数据集、课程、每月 10 美元浏览器代理额度，
以及通过 MCP 从自己的 Claude、Codex 或 Cursor 访问策略目录的权限。
[比较免费与付费权益](https://paperswithbacktest.com/pricing?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_zh_pricing) ·
[连接自己的 AI 助手](https://paperswithbacktest.com/docs/mcp/?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_zh_mcp)

</details>

<!-- omit in toc -->
### 你在这里会发现什么？

- [109 个](#库和包)用于研究和实际交易的[库和包](#库和包)，已失效和停止维护的项目都作了标注
- 来自已发表论文的[策略](#策略)，每一个都附有交易规则和可运行的 Python 代码
- [55本](#书籍)适合初学者和专业人士的[书籍](#书籍)
- [22个视频](#视频)和采访
- 还有一些[博客](#博客)和[课程](#课程)

<!-- omit in toc -->
### 复现结果是什么样的

我们已经把其中 4,843 篇论文编码，并在各自的完整历史上运行。在挑选一个来实现之前，有几个数字值得先知道：

- 复现结果的**夏普比率中位数为 0.37**，**48% 的策略 t 统计量超过 1.96**。
  也就是说，已发表文献中有一半在其自身样本上无法与零区分开。
- 测试窗口中位数为 **34 年**。一个策略大致需要 `(1.96 / 夏普比率)²` 年才能证明自己，
  所以夏普比率 0.4 的策略需要约 24 年。
- 策略对标普 500 的**贝塔中位数为 +0.17**。剔除这部分之后，信息比率中位数降到 **0.21**，
  说明已发表的超额收益中有相当一部分来自指数敞口，而非技巧。
- 在发表日期两侧都有记录的 2,838 篇论文中，控制市场时期之后，我们**没有发现可测量的
  发表后衰减**，误差在每年五分之一个百分点以内。

方法与注意事项写在[维基](https://paperswithbacktest.com/wiki)上。

<details>
<summary>点击这里查看完整的内容表</summary>

- [库和包](#库和包)
  - [回溯测试和真实交易](#回溯测试和真实交易)
    - [一般 - 事件驱动框架](#一般---事件驱动框架)
    - [一般 - 基于矢量的框架](#一般---基于矢量的框架)
    - [加密货币](#加密货币)
  - [交易机器人](#交易机器人)
  - [分析](#分析)
    - [指标](#指标)
    - [度量衡计算](#度量衡计算)
    - [优化](#优化)
    - [定价](#定价)
    - [风险](#风险)
  - [经纪人API](#经纪人api)
  - [数据来源](#数据来源)
    - [一般](#一般)
    - [加密货币](#加密货币-1)
  - [数据科学](#数据科学)
  - [数据库](#数据库)
  - [图形计算](#图形计算)
  - [机器学习](#机器学习)
  - [时间序列分析](#时间序列分析)
  - [视觉化](#视觉化)
- [策略](#策略)
  - [股票](#股票)
  - [债券](#债券)
  - [大宗商品](#大宗商品)
  - [外汇](#外汇)
  - [加密货币](#加密货币-2)
  - [衍生品](#衍生品)
  - [多资产](#多资产)
- [书籍](#书籍)
  - [初学者](#初学者)
  - [传记](#传记)
  - [编码](#编码)
  - [隐蔽性](#隐蔽性)
  - [一般](#一般-1)
  - [高频交易](#高频交易)
  - [机器学习](#机器学习-1)
- [视频](#视频)
- [博客](#博客)
- [课程](#课程)
</details>

<!-- omit in toc -->
> ### 我怎样才能提供帮助？
> 你可以通过提交带有建议的问题和在Twitter上分享来帮助。
>
> [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=A%20free%20and%20comprehensive%20list%20of%20papers%2C%20libraries%2C%20books%2C%20blogs%2C%20tutorials%20for%20quantitative%20traders.&url=https://github.com/paperswithbacktest/awesome-systematic-trading)


# 库和包

*109个实现交易机器人、回溯测试器、指标、定价器等的库和包列表。每个库都按其编程语言分类，并按人口降序排列（星星的数量）。*


## 回溯测试和真实交易

### 一般 - 事件驱动框架


| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [vnpy](https://github.com/vnpy/vnpy) | 基于Python的开源量化交易系统开发框架，于2015年1月正式发布，已经一步步成长为一个全功能的量化交易平台。 | ![GitHub stars](https://badgen.net/github/stars/vnpy/vnpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zipline](https://github.com/quantopian/zipline) | Zipline是一个Pythonic算法交易库。它是一个事件驱动的系统，用于回溯测试。 | ![GitHub stars](https://badgen.net/github/stars/quantopian/zipline) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtrader](https://github.com/mementum/backtrader) | 事件驱动的Python交易策略回测库 | ![GitHub stars](https://badgen.net/github/stars/mementum/backtrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS) | QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权/港股/虚拟货币 数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案 | ![GitHub stars](https://badgen.net/github/stars/QUANTAXIS/QUANTAXIS) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QuantConnect](https://github.com/QuantConnect/Lean) | QuantConnect的精益算法交易引擎（Python，C#）。 | ![GitHub stars](https://badgen.net/github/stars/QuantConnect/Lean) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Rqalpha](https://github.com/ricequant/rqalpha) | 一个可扩展、可替换的Python算法回测和交易框架，支持多种证券 | ![GitHub stars](https://badgen.net/github/stars/ricequant/rqalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finmarketpy](https://github.com/cuemacro/finmarketpy) | 用于回测交易策略和分析金融市场的Python库（前身为pythalesians）。 | ![GitHub stars](https://badgen.net/github/stars/cuemacro/finmarketpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtesting.py](https://github.com/kernc/backtesting.py) | Backtesting.py是一个Python框架，用于根据历史（过去）数据推断交易策略的可行性。Backtesting.py在Backtrader的基础上进行了改进，并以各种方式超越了其他可获得的替代方案，Backtesting.py是轻量级的、快速的、用户友好的、直观的、互动的、智能的，并希望是面向未来的。 | ![GitHub stars](https://badgen.net/github/stars/kernc/backtesting.py) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zvt](https://github.com/zvtvz/zvt) | 模块化的量化框架 | ![GitHub stars](https://badgen.net/github/stars/zvtvz/zvt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [WonderTrader](https://github.com/wondertrader/wondertrader) | WonderTrader——量化研发交易一站式框架  | ![GitHub stars](https://badgen.net/github/stars/wondertrader/wondertrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 一个高性能的算法交易平台和事件驱动的回测器 | ![GitHub stars](https://badgen.net/github/stars/nautechsystems/nautilus_trader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PandoraTrader](https://github.com/pegasusTrader/PandoraTrader) | 基于c++开发，支持多种交易API，跨平台的高频量化交易平台 | ![GitHub stars](https://badgen.net/github/stars/pegasusTrader/PandoraTrader) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
[HFTBacktest](https://github.com/nkaz001/hftbacktest) | Python+Numba 对高频交易数据进行高精度回测 | ![GitHub stars](https://badgen.net/github/stars/nkaz001/hftbacktest) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [aat](https://github.com/AsyncAlgoTrading/aat) | 一个异步的、事件驱动的框架，用于用python编写算法交易策略，并可选择用C++进行加速。它的设计是模块化和可扩展的，支持各种工具和策略，在多个交易所之间进行实时交易。 | ![GitHub stars](https://badgen.net/github/stars/AsyncAlgoTrading/aat) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) | 这个项目主要是为那些有兴趣学习使用python解释器编写自己的交易算法的algo交易新手准备的。 | ![GitHub stars](https://badgen.net/github/stars/sreenivasdoosa/sdoosa-algo-trade-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [lumibot](https://github.com/Lumiwealth/lumibot) | 一个非常简单而有用的回溯测试和基于样本的实时交易框架（运行速度有点慢......）。 | ![GitHub stars](https://badgen.net/github/stars/Lumiwealth/lumibot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [quanttrader](https://github.com/letianzj/quanttrader) | 在Python中进行回测和实时交易。基于事件。类似于backtesting.py。 | ![GitHub stars](https://badgen.net/github/stars/letianzj/quanttrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [gobacktest](https://github.com/gobacktest/gobacktest) | 事件驱动的回溯测试框架的Go实现 | ![GitHub stars](https://badgen.net/github/stars/gobacktest/gobacktest) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [PineForge](https://github.com/pineforge-4pass/pineforge-engine) | 将 PineScript v6 策略转译为 C++，并使用用户提供的 OHLCV 数据运行确定性的离线回测。 | ![GitHub stars](https://badgen.net/github/stars/pineforge-4pass/pineforge-engine) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [FlashFunk](https://github.com/HFQR/FlashFunk) | Rust中的高性能运行时 | ![GitHub stars](https://badgen.net/github/stars/HFQR/FlashFunk) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |


### 一般 - 基于矢量的框架

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [QTradeX](https://github.com/squidKid-deluxe/QTradeX-Algo-Trading-SDK) | 功能强大且灵活的 Python 框架，用于设计、回测、优化和部署算法交易机器人 | ![GitHub stars](https://badgen.net/github/stars/squidKid-deluxe/QTradeX-Algo-Trading-SDK) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [vectorbt](https://github.com/polakowo/vectorbt) | vectorbt采取了一种新颖的回测方法：它完全在pandas和NumPy对象上运行，并由Numba加速，以速度和规模分析任何数据。这允许在几秒钟内对成千上万的策略进行测试。 | ![GitHub stars](https://badgen.net/github/stars/polakowo/vectorbt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | 罗布-卡弗的《系统交易》一书中的python系统交易 | ![GitHub stars](https://badgen.net/github/stars/robcarver17/pysystemtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [bt](https://github.com/pmorissette/bt) | 基于Algo和策略树的Python的灵活回测 | ![GitHub stars](https://badgen.net/github/stars/pmorissette/bt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ml-quant-trading](https://github.com/initial-d/ml-quant-trading) | 面向机器学习多因子交易的 PyTorch 研究栈：213 个因子、偏差修正、组合优化、向量化回测，并附公开的验证报告 | ![GitHub stars](https://badgen.net/github/stars/initial-d/ml-quant-trading) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [manifoldbt](https://github.com/manifoldbt/manifoldbt) | 基于 Rust 引擎的 Python 回测库：向量化信号表达式、参数扫描、滚动前向优化与蒙特卡洛，按K线、逐笔成交或订单簿模拟成交。 | ![GitHub stars](https://badgen.net/github/stars/manifoldbt/manifoldbt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |


### 加密货币

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [Freqtrade](https://github.com/freqtrade/freqtrade) | Freqtrade是一个用Python编写的免费和开源的加密货币交易机器人。它被设计为支持所有主要交易所，并通过Telegram进行控制。它包含回测、绘图和资金管理工具，以及通过机器学习进行策略优化。 | ![GitHub stars](https://badgen.net/github/stars/freqtrade/freqtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Jesse](https://github.com/jesse-ai/jesse) | Jesse是一个先进的加密货币交易框架，旨在简化研究和定义交易策略。 | ![GitHub stars](https://badgen.net/github/stars/jesse-ai/jesse) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OctoBot](https://github.com/Drakkar-Software/OctoBot) | 用于TA、套利和社会交易的加密货币交易机器人，具有先进的网络界面 | ![GitHub stars](https://badgen.net/github/stars/Drakkar-Software/OctoBot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Kelp](https://github.com/stellar/kelp) | Kelp是一个免费和开源的交易机器人，适用于Stellar DEX和100多个集中式交易所 | ![GitHub stars](https://badgen.net/github/stars/stellar/kelp) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [openlimits](https://github.com/nash-io/openlimits) | 一个Rust高性能的加密货币交易API，支持多个交易所和语言封装器。 | ![GitHub stars](https://badgen.net/github/stars/nash-io/openlimits) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [bTrader](https://github.com/gabriel-milan/btrader) | Binance的三角套利交易机器人 | ![GitHub stars](https://badgen.net/github/stars/gabriel-milan/btrader) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) | 抓取加密货币交易所的订单簿和交易信息 | ![GitHub stars](https://badgen.net/github/stars/crypto-crawler/crypto-crawler-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [Hummingbot](https://github.com/CoinAlpha/hummingbot) | 一个用于加密货币做市的客户 | ![GitHub stars](https://badgen.net/github/stars/CoinAlpha/hummingbot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cryptotrader-core](https://github.com/monomadic/cryptotrader-core) | 简单的使用Rust中的加密货币交易所REST API客户端。 | ![GitHub stars](https://badgen.net/github/stars/monomadic/cryptotrader-core) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

## 交易机器人

*交易机器人和阿尔法模型。其中一些是旧的，没有维护。*

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [Blackbird](https://github.com/butor/blackbird) | 黑鸟比特币套利：市场中立的多/空策略 | ![GitHub stars](https://badgen.net/github/stars/butor/blackbird) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | 比特币套利 - 机会检测器 | ![GitHub stars](https://badgen.net/github/stars/maxme/bitcoin-arbitrage) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ThetaGang](https://github.com/brndnmtthws/thetagang) | ThetaGang是一个用于收集资金的IBKR机器人 | ![GitHub stars](https://badgen.net/github/stars/brndnmtthws/thetagang) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [czsc](https://github.com/waditu/czsc) | 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 | ![GitHub stars](https://badgen.net/github/stars/waditu/czsc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2) | R2 Bitcoin Arbitrager是一个由Node.js + TypeScript驱动的自动套利交易系统。 | ![GitHub stars](https://badgen.net/github/stars/bitrinjani/r2) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [Intelligent Trading Bot](https://github.com/asavinov/intelligent-trading-bot) | 智能交易机器人：基于机器学习和特征工程自动生成信号并执行交易 | ![GitHub stars](https://badgen.net/github/stars/asavinov/intelligent-trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [analyzingalpha](https://github.com/leosmigel/analyzingalpha) | 实施简单的策略 | ![GitHub stars](https://badgen.net/github/stars/leosmigel/analyzingalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow) | PyTrendFollow - 使用趋势跟踪的系统性期货交易 | ![GitHub stars](https://badgen.net/github/stars/chrism2671/PyTrendFollow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradeSight](https://github.com/rmbell09-lang/tradesight) | AI 驱动的算法交易平台：RSI/MACD 信号、隔夜策略锦标赛、通过 Alpaca 进行模拟交易、多股票扫描和网页看板 | ![GitHub stars](https://badgen.net/github/stars/rmbell09-lang/tradesight) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PRISM-INSIGHT](https://github.com/dragon1086/prism-insight) | AI 驱动的股票分析，由 13 个专业智能体协作，并通过 KIS API 自动交易（韩国和美国市场） | ![GitHub stars](https://badgen.net/github/stars/dragon1086/prism-insight) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## 分析

### 指标

*预测未来价格走势的指标库。*

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [ta-lib](https://github.com/mrjbq7/ta-lib) | 对金融市场数据进行技术分析 | ![GitHub stars](https://badgen.net/github/stars/mrjbq7/ta-lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [go-tart](https://github.com/iamjinlei/go-tart) | 用Go实现的[ta-lib]((https://github.com/mrjbq7/ta-lib)，支持增量更新 | ![GitHub stars](https://badgen.net/github/stars/iamjinlei/go-tart) | ![made-with-go](https://img.shields.io/badge/Made%20with-go-1f425f.svg) |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | 潘达斯技术分析（Pandas TA）是一个易于使用的库，它利用潘达斯软件包的130多个指标和实用功能以及60多个TA Lib蜡烛图。 | ![GitHub stars](https://badgen.net/github/stars/twopirllc/pandas-ta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finta](https://github.com/peerchemist/finta) | 在Pandas中实施的共同财务技术指标 | ![GitHub stars](https://badgen.net/github/stars/peerchemist/finta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ta-rust](https://github.com/greyblake/ta-rs) | Rust语言的技术分析库 | ![GitHub stars](https://badgen.net/github/stars/greyblake/ta-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [wickra](https://github.com/wickra-lib/wickra) | 以流式处理为先的技术分析库，Rust 内核，提供 Python/Node/WASM 原生绑定和 C ABI（C、C++、C#/.NET、Go、Java、R）；涵盖 24 个类别的 514 个每次 tick 为 O(1) 的指标，批处理与流式结果按位一致 | ![GitHub stars](https://badgen.net/github/stars/wickra-lib/wickra) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### 度量衡计算

*财务衡量标准。*

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [quantstats](https://github.com/ranaroussi/quantstats) | 用Python编写的面向量化投资人的投资组合分析方法 | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/quantstats) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ffn](https://github.com/pmorissette/ffn) | 一个用于Python的金融函数库 | ![GitHub stars](https://badgen.net/github/stars/pmorissette/ffn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### 优化

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [skfolio](https://github.com/skfolio/skfolio) | 基于scikit-learn构建的投资组合优化。它提供了统一的接口和与sklearn兼容的工具，用于构建、调优和交叉验证投资组合模型。| ![GitHub stars](https://badgen.net/github/stars/skfolio/skfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | 在python中进行金融投资组合优化，包括经典的有效边界、Black-Litterman、分级风险平价等。 | ![GitHub stars](https://badgen.net/github/stars/robertmartin8/PyPortfolioOpt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | Python中的投资组合优化和定量战略资产配置 | ![GitHub stars](https://badgen.net/github/stars/dcajasn/Riskfolio-Lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [empyrial](https://github.com/ssantoshp/Empyrial) | Empyrial是一个基于Python的开源量化投资库，专门为金融机构和零售投资者服务，于2021年3月正式发布。 | ![GitHub stars](https://badgen.net/github/stars/ssantoshp/Empyrial) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Deepdow](https://github.com/jankrepl/deepdow) | 连接组合优化和深度学习的Python包。它的目标是促进研究在一次前进过程中进行权重分配的网络。 | ![GitHub stars](https://badgen.net/github/stars/jankrepl/deepdow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [spectre](https://github.com/Heerozh/spectre) | Python中的投资组合优化和定量战略资产配置 | ![GitHub stars](https://badgen.net/github/stars/Heerozh/spectre) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### 定价

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [tf-quant-finance](https://github.com/google/tf-quant-finance) | 谷歌为量化金融提供的高性能TensorFlow库 | ![GitHub stars](https://badgen.net/github/stars/google/tf-quant-finance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinancePy](https://github.com/domokane/FinancePy) | 一个Python金融库，专注于金融衍生品的定价和风险管理，包括固定收益、股票、外汇和信用衍生品。 | ![GitHub stars](https://badgen.net/github/stars/domokane/FinancePy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyQL](https://github.com/enthought/pyql) | 著名定价库QuantLib的Python封装器 | ![GitHub stars](https://badgen.net/github/stars/enthought/pyql) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### 风险

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [pyfolio](https://github.com/quantopian/pyfolio) | Python中的投资组合和风险分析 | ![GitHub stars](https://badgen.net/github/stars/quantopian/pyfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |



## 经纪人API

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [ccxt](https://github.com/ccxt/ccxt) | 一个JavaScript / Python / PHP加密货币交易API，支持100多个比特币/altcoin交易所 | ![GitHub stars](https://badgen.net/github/stars/ccxt/ccxt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Ib_insync](https://github.com/erdewit/ib_insync) | 用于交互式经纪人的Python同步/async框架。 | ![GitHub stars](https://badgen.net/github/stars/erdewit/ib_insync) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Coinnect](https://github.com/hugues31/coinnect) | Coinnect是一个Rust库，旨在通过REST API提供对主要加密货币交易所的完整访问。 | ![GitHub stars](https://badgen.net/github/stars/hugues31/coinnect) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |


## 数据来源

### 一般

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) | 为每个人、在任何地方进行投资研究。 | ![GitHub stars](https://badgen.net/github/stars/OpenBB-finance/OpenBBTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TuShare](https://github.com/waditu/tushare) | TuShare是一个用于抓取中国股票历史数据的工具。 | ![GitHub stars](https://badgen.net/github/stars/waditu/tushare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [yfinance](https://github.com/ranaroussi/yfinance) | yfinance提供了一个线程和Pythonic方式，从雅虎金融下载市场数据。 | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/yfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AkShare](https://github.com/akfamily/akshare) | AKShare是一个优雅而简单的Python金融数据接口库，它是为人类而建的！它是为人类服务的。 | ![GitHub stars](https://badgen.net/github/stars/akfamily/akshare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pandas-datareader](https://github.com/pydata/pandas-datareader) | 为pandas提供最新的远程数据访问，适用于多个版本的pandas。 | ![GitHub stars](https://badgen.net/github/stars/pydata/pandas-datareader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Quandl](https://github.com/quandl/quandl-python) | 通过一个免费的API，从数百个出版商那里获得数以百万计的金融和经济数据集。 | ![GitHub stars](https://badgen.net/github/stars/quandl/quandl-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [findatapy](https://github.com/cuemacro/findatapy) | findatapy创建了一个易于使用的Python API，使用统一的高级接口从许多来源下载市场数据，包括Quandl、彭博、雅虎、谷歌等。 | ![GitHub stars](https://badgen.net/github/stars/cuemacro/findatapy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Investpy](https://github.com/alvarobartt/investpy) | 用Python从Investing.com提取金融数据 | ![GitHub stars](https://badgen.net/github/stars/alvarobartt/investpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | 完整的基本面分析软件包能够收集20年的公司简介、财务报表、比率和20,000多家公司的股票数据。 | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FundamentalAnalysis) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Wallstreet](https://github.com/mcdallas/wallstreet) | 华尔街。实时股票和期权工具 | ![GitHub stars](https://badgen.net/github/stars/mcdallas/wallstreet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pwb-toolbox](https://github.com/paperswithbacktest/pwb-toolbox) | Hugging Face 上 32 个 Papers With Backtest 数据集的加载器：股票、ETF、指数、外汇和大宗商品自 1962 年起的日频价格，主权收益率曲线，季度财务报表，FRED-MD 宏观序列，以及 57 亿行美股分钟级数据。数据卡和字段说明公开可读，下载需要授权。 | ![GitHub stars](https://badgen.net/github/stars/paperswithbacktest/pwb-toolbox) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |



### 加密货币

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [Cryptofeed](https://github.com/bmoscon/cryptofeed) | 使用Asyncio的加密货币交易所Websocket数据源处理程序 | ![GitHub stars](https://badgen.net/github/stars/bmoscon/cryptofeed) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) | Gekko交易机器人数据集转储。下载和使用SQLite格式的历史文件。 | ![GitHub stars](https://badgen.net/github/stars/xFFFFF/Gekko-Datasets) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) | 一个实时的加密货币历史交易数据图谱。从任何加密货币交易所下载实时历史交易数据。 | ![GitHub stars](https://badgen.net/github/stars/Optixal/CryptoInscriber) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
[Crypto Lake](https://github.com/crypto-lake/lake-api) | 加密货币的高频订单簿和交易数据
 | ![GitHub stars](https://badgen.net/github/stars/crypto-lake/lake-api) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## 数据科学

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [TensorFlow](https://github.com/tensorflow/tensorflow) | Python中科学计算的基本算法 | ![GitHub stars](https://badgen.net/github/stars/tensorflow/tensorflow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pytorch](https://github.com/pytorch/pytorch) | Python中的张量和动态神经网络具有强大的GPU加速功能 | ![GitHub stars](https://badgen.net/github/stars/pytorch/pytorch) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Keras](https://github.com/keras-team/keras) | 最具用户友好性的Python中的人类深度学习 | ![GitHub stars](https://badgen.net/github/stars/keras-team/keras) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | Python中的机器学习 | ![GitHub stars](https://badgen.net/github/stars/scikit-learn/scikit-learn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pandas](https://github.com/pandas-dev/pandas) | 灵活而强大的Python数据分析/操作库，提供类似于R data.frame对象的标记数据结构、统计函数以及更多。 | ![GitHub stars](https://badgen.net/github/stars/pandas-dev/pandas) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Numpy](https://github.com/numpy/numpy) | 用Python进行科学计算的基本包 | ![GitHub stars](https://badgen.net/github/stars/numpy/numpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scipy](https://github.com/scipy/scipy) | Python中科学计算的基本算法 | ![GitHub stars](https://badgen.net/github/stars/scipy/scipy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyMC](https://github.com/pymc-devs/pymc) | Python中的概率编程。用Aesara进行贝叶斯建模和概率机器学习 | ![GitHub stars](https://badgen.net/github/stars/pymc-devs/pymc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Cvxpy](https://github.com/cvxpy/cvxpy) | 一种用于凸优化问题的Python嵌入式建模语言。 | ![GitHub stars](https://badgen.net/github/stars/cvxpy/cvxpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## 数据库

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [Marketstore](https://github.com/alpacahq/marketstore) | 金融时序数据的DataFrame服务器 | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [Tectonicdb](https://github.com/0b01/tectonicdb) | Tectonicdb是一个快速、高度压缩的独立数据库和流媒体协议，用于订单簿上的点子。 | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [ArcticDB (Man Group)](https://github.com/man-group/arcticdb) | 用于时间序列和tick数据的高性能数据存储 | ![GitHub stars](https://badgen.net/github/stars/man-group/ArcticDB) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## 图形计算

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [Ray](https://github.com/ray-project/ray) | 一个开源框架，为构建分布式应用提供了一个简单、通用的API。 | ![GitHub stars](https://badgen.net/github/stars/ray-project/ray) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Dask](https://github.com/dask/dask) | 在Python中使用类似Pandas的API进行任务调度的并行计算 | ![GitHub stars](https://badgen.net/github/stars/dask/dask) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | Incremental是一个库，它为你提供了一种建立复杂计算的方法，可以根据输入的变化进行有效的更新，其灵感来自Umut Acar等人关于自我调整计算的工作。Incremental在许多应用中都很有用 | ![GitHub stars](https://badgen.net/github/stars/janestreet/incremental) | ![made-with-ocaml](https://img.shields.io/badge/Made%20with-Ocaml-1f425f.svg) |
| [Man MDF](https://github.com/man-group/mdf) | 用于Python的数据流编程工具包 | ![GitHub stars](https://badgen.net/github/stars/man-group/mdf) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [GraphKit](https://github.com/yahoo/graphkit) | 一个轻量级的Python模块，用于创建和运行计算的有序图。 | ![GitHub stars](https://badgen.net/github/stars/yahoo/graphkit) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Tributary](https://github.com/timkpaine/tributary) | 在Python中流化反应式和数据流图 | ![GitHub stars](https://badgen.net/github/stars/timkpaine/tributary) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## 机器学习

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [QLib (Microsoft)](https://github.com/microsoft/qlib) | Qlib是一个以人工智能为导向的量化投资平台，旨在实现人工智能技术在量化投资中的潜力，授权研究，并创造价值。通过Qlib，你可以轻松尝试你的想法，创造更好的量化投资策略。越来越多的SOTA量化研究作品/论文在Qlib中发布。 | ![GitHub stars](https://badgen.net/github/stars/microsoft/qlib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | FinRL是第一个开源框架，展示了在量化金融中应用深度强化学习的巨大潜力。 | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinRL) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [MlFinLab (Hudson & Thames)](https://github.com/hudson-and-thames/mlfinlab) | MlFinLab通过提供可重复的、可解释的和易于使用的工具，帮助那些希望利用机器学习的力量的投资组合经理和交易者。 | ![GitHub stars](https://badgen.net/github/stars/hudson-and-thames/mlfinlab) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradingGym](https://github.com/Yvictor/TradingGym) | 交易和回测环境，用于训练强化学习代理或简单的规则基础算法。 | ![GitHub stars](https://badgen.net/github/stars/Yvictor/TradingGym) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) | 使用深度Q-学习的股票交易机器人 | ![GitHub stars](https://badgen.net/github/stars/pskrunner14/trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## 时间序列分析

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [Facebook Prophet](https://github.com/facebook/prophet) | 对具有线性或非线性增长的多季节性的时间序列数据产生高质量的预测的工具。 | ![GitHub stars](https://badgen.net/github/stars/facebook/prophet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [statsmodels](https://github.com/statsmodels/statsmodels) | Python模块，允许用户探索数据，估计统计模型，并进行统计测试。 | ![GitHub stars](https://badgen.net/github/stars/statsmodels/statsmodels) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [tsfresh](https://github.com/blue-yonder/tsfresh) | 从时间序列中自动提取相关特征。 | ![GitHub stars](https://badgen.net/github/stars/blue-yonder/tsfresh) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pmdarima](https://github.com/alkaline-ml/pmdarima) | 一个统计库，旨在填补Python时间序列分析能力的空白，包括相当于R的auto.arima函数。 | ![GitHub stars](https://badgen.net/github/stars/alkaline-ml/pmdarima) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


## 视觉化

| 存储库 | 描述 | 明星 | 使用方法 |
|------------|-------------|-------|-----------|
| [D-Tale (Man Group)](https://github.com/man-group/dtale) | D-Tale是Flask后端和React前端的结合，为你带来查看和分析Pandas数据结构的简单方法。 | ![GitHub stars](https://badgen.net/github/stars/man-group/dtale) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [mplfinance](https://github.com/matplotlib/mplfinance) | 使用Matplotlib实现金融市场数据可视化 | ![GitHub stars](https://badgen.net/github/stars/matplotlib/mplfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [btplotting](https://github.com/happydasch/btplotting) | btplotting为回测、优化结果和backtrader的实时数据提供绘图。 | ![GitHub stars](https://badgen.net/github/stars/happydasch/btplotting) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |


# 策略

*下表中的每一条都是一篇已发表的论文，经过编码并在其完整历史上运行。表格由 [`scripts/build_strategies_table.py`](./scripts/build_strategies_table.py) 从公开目录自动生成，目录变化时列表随之更新。*

<!-- STRATEGIES:START - generated by scripts/build_strategies_table.py -->

*共 84 个已发布的策略，每类资产最多 12 个，按字母顺序排列。每个链接都会在 Papers With Backtest 上打开论文、其交易规则和 Python 代码。*

## 股票

| 策略 | 代码与回测 |
|---|---|
| 1/N | [打开](https://paperswithbacktest.com/strategies/n) |
| 130/30 investing: just another hype or here to stay? | [打开](https://paperswithbacktest.com/strategies/investing-just-another-hype-or-here-to-stay) |
| 25 years of Dutch IPOs | [打开](https://paperswithbacktest.com/strategies/years-of-dutch-ipos) |
| 4-Factor Model for Overnight Returns | [打开](https://paperswithbacktest.com/strategies/4-factor-model-for-overnight-returns) |
| 50 Years in PEAD Research | [打开](https://paperswithbacktest.com/strategies/years-in-pead-research) |
| A Backtesting Protocol in the Era of Machine Learning | [打开](https://paperswithbacktest.com/strategies/a-backtesting-protocol-in-the-era-of-machine-learning) |
| A Behavioral Factor Model for China A-share Market | [打开](https://paperswithbacktest.com/strategies/a-behavioral-factor-model-for-china-a-share-market) |
| A Better Three-Factor Model That Explains More Anomalies | [打开](https://paperswithbacktest.com/strategies/a-better-three-factor-model-that-explains-more-anomalies) |
| A Case Study in Multiperiod Portfolio Optimization: A Classic Problem Revisited | [打开](https://paperswithbacktest.com/strategies/a-case-study-in-multiperiod-portfolio-optimization-a-classic-problem-revisited) |
| A closed-form solution for optimal mean-reverting trading strategies | [打开](https://paperswithbacktest.com/strategies/a-closed-form-solution-for-optimal-mean-reverting-trading-strategies) |
| A Combined Signal Approach to Technical Analysis On | [打开](https://paperswithbacktest.com/strategies/a-combined-signal-approach-to-technical-analysis-on) |
| A comparative analysis of ability of mimicking portfolios in representing the background factors | [打开](https://paperswithbacktest.com/strategies/a-comparative-analysis-of-ability-of-mimicking-portfolios-in-representing-the-background-factors) |

## 债券

| 策略 | 代码与回测 |
|---|---|
| A comparison of the historical performance of rolling bond ladders and bond index funds | [打开](https://paperswithbacktest.com/strategies/a-comparison-of-the-historical-performance-of-rolling-bond-ladders-and-bond-index-funds) |
| A Credit-Based Theory of the Currency Risk Premium | [打开](https://paperswithbacktest.com/strategies/a-credit-based-theory-of-the-currency-risk-premium) |
| A Frequency-Specific Factorization to Identify Commonalities with an Application to the European Bond Markets | [打开](https://paperswithbacktest.com/strategies/a-frequency-specific-factorization-to-identify-commonalities-with-an-application-to-the-european-bond-markets) |
| A Key Rate Approach to Replicating Annuities with U.S. Treasury Funds | [打开](https://paperswithbacktest.com/strategies/a-key-rate-approach-to-replicating-annuities-with-u-s-treasury-funds) |
| A research-based approach to fixed income factor portfolio implementation | [打开](https://paperswithbacktest.com/strategies/a-research-based-approach-to-fixed-income-factor-portfolio-implementation) |
| A Sharper Angle on Optimization | [打开](https://paperswithbacktest.com/strategies/a-sharper-angle-on-optimization) |
| A Study on the Effectiveness of China Bond Market ESG Investment Practice | [打开](https://paperswithbacktest.com/strategies/a-study-on-the-effectiveness-of-china-bond-market-esg-investment-practice) |
| An agent-based model of dynamics in corporate bond trading | [打开](https://paperswithbacktest.com/strategies/an-agent-based-model-of-dynamics-in-corporate-bond-trading) |
| Are Bond Returns Predictable with Real-Time Macro Data? | [打开](https://paperswithbacktest.com/strategies/are-bond-returns-predictable-with-real-time-macro-data) |
| Are there pricing spillovers within ETFs? Evidence from Emerging Market Corporate Bonds | [打开](https://paperswithbacktest.com/strategies/are-there-pricing-spillovers-within-etfs-evidence-from-emerging-market-corporate-bonds) |
| Asymmetric Violations of the Spanning Hypothesis | [打开](https://paperswithbacktest.com/strategies/asymmetric-violations-of-the-spanning-hypothesis) |
| Banks’ exposure to interest rate risk, their earnings from term transformation, and the dynamics of the term structure | [打开](https://paperswithbacktest.com/strategies/banks-exposure-to-interest-rate-risk-their-earnings-from-term-transformation-and-the-dynamics-of-the-term-structure) |

## 大宗商品

| 策略 | 代码与回测 |
|---|---|
| A Trend Factor in Commodity Futures Markets: Any Economic Gains from Using Information over Investment Horizons? | [打开](https://paperswithbacktest.com/strategies/a-trend-factor-in-commodity-futures-markets-any-economic-gains-from-using-information) |
| Alternative Beta Strategies in Commodities | [打开](https://paperswithbacktest.com/strategies/alternative-beta-strategies-in-commodities) |
| Decomposing Alpha in a Machine-Learning Gold Timing System: Trend Following, Forecast Quality, and the Cost of Look-Ahead Bias | [打开](https://paperswithbacktest.com/strategies/decomposing-alpha-in-a-machine-learning-gold-timing-system-trend-following-forecast) |
| Diversification Return, Portfolio Rebalancing, and the Commodity Return Puzzle | [打开](https://paperswithbacktest.com/strategies/diversification-return-portfolio-rebalancing-and-the-commodity-return-puzzle) |
| Dynamic Regime Strategy for Stress Testing and Optimizing Institutional Investor Portfolios | [打开](https://paperswithbacktest.com/strategies/dynamic-regime-strategy-for-stress-testing-and-optimizing-institutional-investor-port) |
| Ensembling ARIMAX Model in Algorithmic Investment Strategies on Commodities Market | [打开](https://paperswithbacktest.com/strategies/ensembling-arimax-model-in-algorithmic-investment-strategies-on-commodities-market) |
| Financialization and Commodity Markets Serial Dependence | [打开](https://paperswithbacktest.com/strategies/financialization-and-commodity-markets-serial-dependence) |
| Forecasting Crude Oil Prices: Does Global Financial Uncertainty Matter? | [打开](https://paperswithbacktest.com/strategies/forecasting-crude-oil-prices-does-global-financial-uncertainty-matter) |
| Forecasting Real Oil Returns Using a Deep Forest Ensemble Approach | [打开](https://paperswithbacktest.com/strategies/forecasting-real-oil-returns-using-a-deep-forest-ensemble-approach) |
| Gold and Oil Prices: Abnormal Returns, Momentum and Contrarian Effects | [打开](https://paperswithbacktest.com/strategies/gold-and-oil-prices-abnormal-returns-momentum-and-contrarian-effects) |
| How Do Portfolio Weighting Schemes Affect Commodity Futures Risk Premia? | [打开](https://paperswithbacktest.com/strategies/miffre-faff-how-do-portfolio-weighting-schemes-affect-commodity-futures-risk-premia) |
| How to Improve Commodity Momentum Using Intra-Market Correlation | [打开](https://paperswithbacktest.com/strategies/how-to-improve-commodity-momentum-using-intra-market-correlation) |

## 外汇

| 策略 | 代码与回测 |
|---|---|
| A Habit-Based Explanation of the Exchange Rate Risk Premium | [打开](https://paperswithbacktest.com/strategies/a-habit-based-explanation-of-the-exchange-rate-risk-premium) |
| A Hamiltonian Phase-Space Approach to Foreign Exchange: Physics-Based Predictive Distributions without Curve Fitting | [打开](https://paperswithbacktest.com/strategies/a-hamiltonian-phase-space-approach-to-foreign-exchange-physics-based-predictive-distributions-without-curve-fitting) |
| A Liquidity-Based Resolution of the Uncovered Interest Parity Puzzle | [打开](https://paperswithbacktest.com/strategies/a-liquidity-based-resolution-of-the-uncovered-interest-parity-puzzle) |
| A Low-Risk Strategy based on Higher Moments in Currency Markets | [打开](https://paperswithbacktest.com/strategies/a-low-risk-strategy-based-on-higher-moments-in-currency-markets) |
| A Multi-Strategy Approach to Trading Foreign Exchange Futures | [打开](https://paperswithbacktest.com/strategies/a-multi-strategy-approach-to-trading-foreign-exchange-futures) |
| A Test of Momentum Trading Strategies in Foreign Exchange Markets | [打开](https://paperswithbacktest.com/strategies/a-test-of-momentum-trading-strategies-in-foreign-exchange-markets-evidence-from-the-g) |
| Algorithmic Trading Model for Manifold Learning in FX | [打开](https://paperswithbacktest.com/strategies/algorithmic-trading-model-for-manifold-learning-in-fx) |
| Alpha Asymmetry in Foreign Exchange Markets An Investigation of Exploitability | [打开](https://paperswithbacktest.com/strategies/alpha-asymmetry-in-foreign-exchange-markets-an-investigation-of-exploitability) |
| An Interpretation of Carry Trade Profitability | [打开](https://paperswithbacktest.com/strategies/an-interpretation-of-carry-trade-profitability) |
| Analyst Forecasts and Currency Markets | [打开](https://paperswithbacktest.com/strategies/analyst-forecasts-and-currency-markets) |
| ANANTA: A Systematic Quantitative FX Trading Strategy | [打开](https://paperswithbacktest.com/strategies/a-systematic-quantitative-fx-trading-strategy) |
| Anatomy of Alpha Illusion in Daily FX Markets | [打开](https://paperswithbacktest.com/strategies/anatomy-of-alpha-illusion-in-daily-fx-markets) |

## 加密货币

| 策略 | 代码与回测 |
|---|---|
| A Filtered-Label Calibrated XGBoost Framework with Walk-Forward Validation for Robust Bitcoin Direction Prediction | [打开](https://paperswithbacktest.com/strategies/a-filtered-label-calibrated-xgboost-framework-with-walk-forward-validation-for-robust) |
| A Prospect Theory Model for Predicting Cryptocurrency Returns | [打开](https://paperswithbacktest.com/strategies/a-prospect-theory-model-for-predicting-cryptocurrency-returns) |
| Algorithmic Predatory Equilibrium: Multi-Agent Reinforcement Learning and Market Manipulation in Decentralized Finance | [打开](https://paperswithbacktest.com/strategies/algorithmic-predatory-equilibrium-multi-agent-reinforcement-learning-and-market-manipulation-in-decentralized-finance) |
| Analysis of an Algo Trading Strategy Based on the Kaufman Adaptive Moving Average (KAMA) and Statistical Validation Using Bootstrap and Bayesian Optimization | [打开](https://paperswithbacktest.com/strategies/analysis-of-an-algo-trading-strategy-based-on-the-kaufman-adaptive-moving-average-kama-and-statistical-validation-using-bootstrap-and-bayesian-optimization) |
| Backtesting of Algorithmic Cryptocurrency Trading Strategies | [打开](https://paperswithbacktest.com/strategies/backtesting-of-algorithmic-cryptocurrency-trading-strategies) |
| Behavioral Anomalies in Cryptocurrency Markets | [打开](https://paperswithbacktest.com/strategies/behavioral-anomalies-in-cryptocurrency-markets) |
| Bitcoin Price Dynamics: The Stark Contrast between P2P and Exchange Trading | [打开](https://paperswithbacktest.com/strategies/bitcoin-price-dynamics-the-stark-contrast-between-p-p-and-exchange-trading) |
| Bitcoin: Speculative Asset or Innovative Technology? | [打开](https://paperswithbacktest.com/strategies/bitcoin-speculative-asset-or-innovative-technology) |
| Bitcoin: Systematic Force of Cryptocurrency Portfolio | [打开](https://paperswithbacktest.com/strategies/bitcoin-systematic-force-of-cryptocurrency-portfolio) |
| Common risk factors in the returns on cryptocurrencies | [打开](https://paperswithbacktest.com/strategies/common-risk-factors-in-the-returns-on-cryptocurrencies) |
| Constant Harmonic Market Maker A Way to Address Impermanent Loss | [打开](https://paperswithbacktest.com/strategies/constant-harmonic-market-maker-a-way-to-address-impermanent-loss) |
| Constructing Cointegrated Cryptocurrency Portfolios for Statistical Arbitrage | [打开](https://paperswithbacktest.com/strategies/constructing-cointegrated-cryptocurrency-portfolios-for-statistical-arbitrage) |

## 衍生品

| 策略 | 代码与回测 |
|---|---|
| A Derivatives Trading Recommendation System: the Mid-Curve Calendar Spread Case | [打开](https://paperswithbacktest.com/strategies/a-derivatives-trading-recommendation-system-the-mid-curve-calendar-spread-case) |
| A Leveraged Portfolio Management Approach Applying The CBOE Russell 2000 PutWrite Index | [打开](https://paperswithbacktest.com/strategies/a-leveraged-portfolio-management-approach-applying-the-cboe-russell-putwrite-index) |
| A semiparametric factor model for CDO surfaces dynamics | [打开](https://paperswithbacktest.com/strategies/a-semiparametric-factor-model-for-cdo-surfaces-dynamics) |
| A Spectral Decomposition of the Credit Default Swap Indices | [打开](https://paperswithbacktest.com/strategies/a-spectral-decomposition-of-the-credit-default-swap-indices) |
| A Theory of Model Sophistication and Operational Risk | [打开](https://paperswithbacktest.com/strategies/a-theory-of-model-sophistication-and-operational-risk) |
| A transaction data study of the forward bias puzzle | [打开](https://paperswithbacktest.com/strategies/a-transaction-data-study-of-the-forward-bias-puzzle) |
| A “Bad Beta, Good Beta” Anatomy of Currency Risk Premiums and Trading Strategies | [打开](https://paperswithbacktest.com/strategies/a-bad-beta-good-beta-anatomy-of-currency-risk-premiums-and-trading-strategies) |
| An Integrated Approach to Currency Factor Investing | [打开](https://paperswithbacktest.com/strategies/an-integrated-approach-to-currency-factor-investing) |
| An intraday trend-following trading strategy on equity derivatives in India | [打开](https://paperswithbacktest.com/strategies/an-intraday-trend-following-trading-strategy-on-equity-derivatives-in-india) |
| Analise do Desempenho de Regras da Analise Tecnica Aplicada ao Mercado Intradiario do Contrato Futuro do Indice Ibovespa | [打开](https://paperswithbacktest.com/strategies/analise-do-desempenho-de-regras-da-analise-tecnica-aplicada-ao-mercado-intradiario-do-contrato-futuro-do-indice-ibovespa) |
| Anchoring Credit Default Swap Spreads to Firm Fundamentals | [打开](https://paperswithbacktest.com/strategies/anchoring-credit-default-swap-spreads-to-firm-fundamentals) |
| Approximate Hedging of Contingent Claims under Transaction Costs for General Pay-offs | [打开](https://paperswithbacktest.com/strategies/approximate-hedging-of-contingent-claims-under-transaction-costs-for-general-pay-offs) |

## 多资产

| 策略 | 代码与回测 |
|---|---|
| 0DTE Asset Pricing | [打开](https://paperswithbacktest.com/strategies/dte-asset-pricing) |
| 0DTE option pricing | [打开](https://paperswithbacktest.com/strategies/dte-option-pricing) |
| 0DTE Trading Rules | [打开](https://paperswithbacktest.com/strategies/dte-trading-rules) |
| 0DTEs: Trading, Gamma Risk and Volatility Propagation | [打开](https://paperswithbacktest.com/strategies/dtes-trading-gamma-risk-and-volatility-propagation) |
| 1/N and Long Run Optimal Portfolios: Results for Mixed Asset Menus | [打开](https://paperswithbacktest.com/strategies/n-and-long-run-optimal-portfolios-results-for-mixed-asset-menus) |
| 150 Years of Return Predictability Around the World: A Holistic View Across Assets | [打开](https://paperswithbacktest.com/strategies/years-of-return-predictability-around-the-world-a-holistic-view-across-assets) |
| 151 Trading Strategies | [打开](https://paperswithbacktest.com/strategies/trading-strategies) |
| 1998 Pricing Performance of Market Advisory Services for Corn and Soybeans | [打开](https://paperswithbacktest.com/strategies/pricing-performance-of-market-advisory-services-for-corn-and-soybeans) |
| 1999 Pricing Performance of Market Advisory Services for Corn and Soybeans | [打开](https://paperswithbacktest.com/strategies/pricing-performance-of-market-advisory-services-for-corn-and-soybeans-1) |
| 20 Myths About Long-Short | [打开](https://paperswithbacktest.com/strategies/myths-about-long-short) |
| A Bayesian Approach to Detecting Nonlinear Risk Exposures in Hedge | [打开](https://paperswithbacktest.com/strategies/a-bayesian-approach-to-detecting-nonlinear-risk-exposures-in-hedge) |
| A Bayesian Stochastic Discount Factor for the Cross-Section of Individual Equity Options | [打开](https://paperswithbacktest.com/strategies/a-bayesian-stochastic-discount-factor-for-the-cross-section-of-individual-equity-options) |

<!-- STRATEGIES:END -->

部分论文的旧版 QuantConnect 实现保存在 [`static/strategies`](./static/strategies)。

# 书籍

为量化交易者提供的55本书的综合清单。


## 初学者

|  标题   | 评论 | 评价 |
|----------|---------|--------|
| [A Beginner’s Guide to the Stock Market: Everything You Need to Start Making Money Today - Matthew R. Kratter](https://amzn.to/3QN2VdU) | ![](https://badgen.net/badge/reviews/14%20161/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [How to Day Trade for a Living: A Beginner’s Guide to Trading Tools and Tactics, Money Management, Discipline and Trading Psychology - Andrew Aziz](https://amzn.to/3bmehFv) | ![](https://badgen.net/badge/reviews/12%20278/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns - John C. Bogle](https://amzn.to/3A4mgkR) | ![](https://badgen.net/badge/reviews/6%20969/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Investing QuickStart Guide: The Simplified Beginner’s Guide to Successfully Navigating the Stock Market, Growing Your Wealth & Creating a Secure Financial Future - Ted D. Snow](https://amzn.to/3A5aRkX) | ![](https://badgen.net/badge/reviews/2%20537/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Day Trading QuickStart Guide: The Simplified Beginner’s Guide to Winning Trade Plans, Conquering the Markets, and Becoming a Successful Day Trader - Troy Noonan](https://amzn.to/3HPZijw) | ![](https://badgen.net/badge/reviews/1%20229/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Introduction To Algo Trading: How Retail Traders Can Successfully Compete With Professional Traders - Kevin J Davey](https://amzn.to/39Tf7JC) | ![](https://badgen.net/badge/reviews/131/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [Algorithmic Trading and DMA: An introduction to direct access trading strategies - Barry Johnson](https://amzn.to/3xYb0UN) | ![](https://badgen.net/badge/reviews/69/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |


## 传记

|  标题   | 评论 | 评价 |
|----------|---------|--------|
| [My Life as a Quant: Reflections on Physics and Finance - Emanuel Derman](https://amzn.to/3A8KudR) | ![](https://badgen.net/badge/reviews/192/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [How I Became a Quant: Insights from 25 of Wall Street’s Elite: - Barry Schachter](https://amzn.to/3Alf8kz) | ![](https://badgen.net/badge/reviews/27/blue) | ![](https://badgen.net/badge/rating/3.7/blue) |



## 编码

|  标题   | 评论 | 评价 |
|----------|---------|--------|
| [Python for Finance: Mastering Data-Driven Finance - Yves Hilpisch](https://amzn.to/3NhkTlP) | ![](https://badgen.net/badge/reviews/249/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Trading Evolved: Anyone can Build Killer Trading Strategies in Python - Andreas F. Clenow](https://amzn.to/3A0jcGB) | ![](https://badgen.net/badge/reviews/173/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Python for Algorithmic Trading: From Idea to Cloud Deployment - Yves Hilpisch](https://amzn.to/3bpkd0C) | ![](https://badgen.net/badge/reviews/90/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Algorithmic Trading with Python: Quantitative Methods and Strategy Development - Chris Conlan](https://amzn.to/3u3cxYo) | ![](https://badgen.net/badge/reviews/48/blue) | ![](https://badgen.net/badge/rating/4.2/blue) |
| [Learn Algorithmic Trading: Build and deploy algorithmic trading systems and strategies using Python and advanced data analysis - Sebastien Donadio](https://amzn.to/3NqNghA) | ![](https://badgen.net/badge/reviews/46/blue) | ![](https://badgen.net/badge/rating/4.1/blue) |


## 隐蔽性

|  标题   | 评论 | 评价 |
|----------|---------|--------|
| [The Bitcoin Standard: The Decentralized Alternative to Central Banking - Saifedean Ammous](https://amzn.to/3QMJgec) | ![](https://badgen.net/badge/reviews/5%20136/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Bitcoin Billionaires: A True Story of Genius, Betrayal, and Redemption - Ben Mezrich](https://amzn.to/39SkdWt) | ![](https://badgen.net/badge/reviews/1%20787/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Mastering Bitcoin: Programming the Open Blockchain - Andreas M. Antonopoulos](https://amzn.to/3NniZ3p) | ![](https://badgen.net/badge/reviews/955/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [Why Buy Bitcoin: Investing Today in the Money of Tomorrow - Andy Edstrom](https://amzn.to/3OMcKqZ) | ![](https://badgen.net/badge/reviews/192/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |


## 一般

|  标题   | 评论 | 评价 |
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


## 高频交易

|  标题   | 评论 | 评价 |
|----------|---------|--------|
| [Inside the Black Box: A Simple Guide to Quantitative and High Frequency Trading - Rishi K. Narang](https://www.amazon.fr/gp/product/1118362411/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118362411&linkId=35e02d4e636350366531a5033597a541) | ![](https://badgen.net/badge/reviews/76/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Algorithmic and High-Frequency Trading (Mathematics, Finance and Risk) - Álvaro Cartea, Sebastian Jaimungal, José Penalva](https://www.amazon.fr/gp/product/1107091144/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1107091144&linkId=64e3ceb66482d8db6827830964b85613) | ![](https://badgen.net/badge/reviews/52/blue) | ![](https://badgen.net/badge/rating/4.1/blue) |
| [The Problem of HFT – Collected Writings on High Frequency Trading & Stock Market Structure Reform - Haim Bodek](https://www.amazon.fr/gp/product/1481978357/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1481978357&linkId=2f3acf998de645990b681e2ac9f0217c) | ![](https://badgen.net/badge/reviews/38/blue) | ![](https://badgen.net/badge/rating/4/blue) |
| [An Introduction to High-Frequency Finance - Ramazan Gençay, Michel Dacorogna, Ulrich A. Muller, Olivier Pictet, Richard Olsen](https://www.amazon.fr/gp/product/0122796713/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0122796713&linkId=7e6c098026204f399e45d7fbb803dcca) | ![](https://badgen.net/badge/reviews/11/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Market Microstructure in Practice - Charles-Albert Lehalle, Sophie Laruelle](https://www.amazon.fr/Market-Microstructure-Practice-Sophie-Laruelle/dp/9813231122) | ![](https://badgen.net/badge/reviews/8/blue) | ![](https://badgen.net/badge/rating/3.9/blue) |
| [The Financial Mathematics of Market Liquidity - Olivier Gueant](https://www.amazon.com/Financial-Mathematics-Market-Liquidity-Execution/dp/1498725473) | ![](https://badgen.net/badge/reviews/6/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [High-Frequency Trading - Maureen O’Hara, David Easley, Marcos M López de Prado](https://www.amazon.fr/gp/product/178272009X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=178272009X&linkId=082f861ff6bbe4cca4ef7ccbe620a2c4) | ![](https://badgen.net/badge/reviews/1/blue) | ![](https://badgen.net/badge/rating/3/blue) |


## 机器学习

|  标题   | 评论 | 评价 |
|----------|---------|--------|
| [Dark Pools: The rise of A.I. trading machines and the looming threat to Wall Street - Scott Patterson](https://www.amazon.fr/gp/product/0307887189/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0307887189&linkId=2572cae24ed7de0b279580312daf0f03) | ![](https://badgen.net/badge/reviews/532/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Advances in Financial Machine Learning - Marcos Lopez de Prado](https://www.amazon.fr/gp/product/1119482089/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1119482089&linkId=7eff4d3f3d9f2d00d05032f726386e53) | ![](https://badgen.net/badge/reviews/446/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Machine Learning for Algorithmic Trading: Predictive models to extract signals from market and alternative data for systematic trading strategies with Python, 2nd Edition - Stefan Jansen](https://www.amazon.fr/gp/product/1839217715/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1839217715&linkId=80e3e93e1b6027596858ed0f1fbf10c2) | ![](https://badgen.net/badge/reviews/229/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Machine Learning for Asset Managers (Elements in Quantitative Finance) - Marcos M López de Prado](https://www.amazon.fr/gp/product/1108792898/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1108792898&linkId=8eb7e3c369d38b36df8dfecf05a622db) | ![](https://badgen.net/badge/reviews/96/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Machine Learning in Finance: From Theory to Practice - Matthew F. Dixon, Igor Halperin, Paul Bilokon](https://www.amazon.fr/gp/product/3030410676/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=3030410676&linkId=5f5f1df6be62ae96ef7a0c536c3ecdb4) | ![](https://badgen.net/badge/reviews/76/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Artificial Intelligence in Finance: A Python-Based Guide - Yves Hilpisch](https://www.amazon.fr/gp/product/1492055433/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1492055433&linkId=7c20249be4d35badb127d6a5423fc495) | ![](https://badgen.net/badge/reviews/38/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Algorithmic Trading Methods: Applications Using Advanced Statistics, Optimization, and Machine Learning Techniques - Robert Kissell](https://www.amazon.fr/gp/product/0128156309/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0128156309&linkId=0a197c0b547a0ee63ccd19389bb42edd) | ![](https://badgen.net/badge/reviews/15/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |


# 视频

| 标题                                                              | 喜欢 |
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



# 博客

| 标题                                                              |
|--------------------------------------------------------------------|
| [AAA Quants, Tom Starke Blog](http://aaaquants.com/category/blog/) |
| [AI & Systematic Trading](https://blog.paperswithbacktest.com/)          |
| [Blackarbs blog](http://www.blackarbs.com/blog/)                   |
| [Hardikp, Hardik Patel blog](https://www.hardikp.com/)             |
| [Max Dama on Automated Trading](https://bit.ly/3wVZbh9)            |
| [Medallion.Club on Systematic Trading (FR)](https://medallion.club/trading-algorithmique-quantitatif-systematique/)            |
| [Proof Engineering: The Algorithmic Trading Platform](https://bit.ly/3lX7zYN) |
| [Quantsportal, Jacques Joubert's Blog](http://www.quantsportal.com/blog-page/) |
| [Quantstart - Machine Learning for Trading articles](https://www.quantstart.com/articles) |
| [RobotWealth, Kris Longmore Blog](https://robotwealth.com/blog/) |


# 课程

| 标题                                                              |
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
