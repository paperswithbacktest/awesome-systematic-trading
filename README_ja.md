<div align="center">
  <img src="static/images/awesome-systematic-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

[中文版はこちら](./README_zh.md)<br>
[English version here](./README.md)

システマティックトレーディング（クオンタティブ・トレーディング）戦略の発見・開発・運用に役立つ論文、ソフトウェア、書籍、記事のリストを収集しています。

<!-- omit in toc -->

### ここで見つかるもの

- リサーチとライブトレーディング向けの [97のライブラリ・パッケージ](#ライブラリとパッケージ)
- 機関投資家や学術研究者が紹介する [40以上の戦略](#戦略)
- 初心者からプロ向けの [55冊の書籍](#書籍)
- [23本の動画](#動画) とインタビュー
- また [ブログ](#ブログ) や [コース](#コース) も掲載

<div align="center" style="margin-bottom: 50px; margin-top: 50px;">
  <div style="border: 2px solid #007bff; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
    <h2>📈 Pythonで実装されたトレーディング戦略に興味がありますか？</h2>
    <p>限定コンテンツは <a href="https://paperswithbacktest.com" target="_blank">paperswithbacktest.com</a> にてご覧いただけます！</p>
  </div>
</div>

<details>
<summary>目次全体を表示するにはここをクリック</summary>

- [ライブラリとパッケージ](#ライブラリとパッケージ)
  - [バックテスト・ライブトレーディング](#バックテストとライブトレーディング)
    - [汎用 - イベント駆動型フレームワーク](#汎用---イベント駆動型フレームワーク)
    - [汎用 - ベクトルベースフレームワーク](#汎用---ベクトルベースフレームワーク)
    - [暗号通貨](#暗号通貨)
  - [トレーディングボット](#トレーディングボット)
  - [アナリティクス](#アナリティクス)
    - [インジケーター](#インジケーター)
    - [メトリクス計算](#メトリクス計算)
    - [最適化](#最適化)
    - [プライシング](#プライシング)
    - [リスク](#リスク)
  - [ブローカーAPI](#ブローカーapi)
  - [データソース](#データソース)
    - [汎用](#汎用)
    - [暗号通貨](#暗号通貨-1)
  - [データサイエンス](#データサイエンス)
  - [データベース](#データベース)
  - [グラフ計算](#グラフ計算)
  - [機械学習](#機械学習)
  - [時系列分析](#時系列分析)
  - [可視化](#可視化)
- [戦略](#戦略)
  - [債券・コモディティ・通貨・株式](#債券コモディティ通貨株式)
  - [債券・コモディティ・株式・REIT](#債券コモディティ株式reit)
  - [債券・株式](#債券株式)
  - [債券・株式・REIT](#債券株式reit)
  - [コモディティ](#コモディティ)
  - [暗号資産](#暗号資産)
  - [通貨](#通貨)
  - [株式](#株式)
- [書籍](#書籍)
  - [入門](#入門)
  - [伝記](#伝記)
  - [コーディング](#コーディング)
  - [暗号資産](#暗号資産-1)
  - [一般](#一般)
  - [高頻度取引](#高頻度取引)
  - [機械学習](#機械学習-1)
- [動画](#動画)
- [ブログ](#ブログ)
- [コース](#コース)
</details>

<!-- omit in toc -->

> ### 協力するには？
>
> Issueで提案を送ったり、Twitterでシェアすることで協力できます:
>
> [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=A%20free%20and%20comprehensive%20list%20of%20papers%2C%20libraries%2C%20books%2C%20blogs%2C%20tutorials%20for%20quantitative%20traders.&url=https://github.com/paperswithbacktest/awesome-systematic-trading)

# ライブラリとパッケージ

_トレーディングボット、バックテスター、インジケーター、プライサーなどを実装した **97のライブラリ・パッケージ** のリストです。各ライブラリはプログラミング言語ごとに分類され、人気順（スター数の降順）に並んでいます。_

## バックテストとライブトレーディング

### 汎用 - イベント駆動型フレームワーク

| リポジトリ                                                                             | 説明                                                                                                                                                                                            | スター                                                                                   | 使用技術                                                                        |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [vnpy](https://github.com/vnpy/vnpy)                                                   | Pythonベースのオープンソース量子取引システム開発フレームワーク。2015年1月に正式リリースされ、フル機能の量子取引プラットフォームに成長。                                                         | ![GitHub stars](https://badgen.net/github/stars/vnpy/vnpy)                               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zipline](https://github.com/quantopian/zipline)                                       | Pythonicなアルゴリズムトレーディングライブラリでイベントドリブンなバックテストシステム。                                                                                                        | ![GitHub stars](https://badgen.net/github/stars/quantopian/zipline)                      | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtrader](https://github.com/mementum/backtrader)                                   | トレーディング戦略向けのイベント駆動型Pythonバックテストライブラリ。                                                                                                                            | ![GitHub stars](https://badgen.net/github/stars/mementum/backtrader)                     | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS)                                    | タスクスケジューリングと分散デプロイメントをサポートする株式/先物/オプション/香港株/仮想通貨のデータ/バックテスト/シミュレーション/取引/可視化/マルチアカウントのローカル量子化ソリューション。 | ![GitHub stars](https://badgen.net/github/stars/QUANTAXIS/QUANTAXIS)                     | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QuantConnect](https://github.com/QuantConnect/Lean)                                   | QuantConnectによるLeanアルゴリズムトレーディングエンジン（Python、C#）。                                                                                                                        | ![GitHub stars](https://badgen.net/github/stars/QuantConnect/Lean)                       | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Rqalpha](https://github.com/ricequant/rqalpha)                                        | 複数の有価証券に対応した拡張・置換可能なPythonアルゴリズムバックテスト＆トレーディングフレームワーク。                                                                                          | ![GitHub stars](https://badgen.net/github/stars/ricequant/rqalpha)                       | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finmarketpy](https://github.com/cuemacro/finmarketpy)                                 | トレーディング戦略のバックテストと金融市場分析のためのPythonライブラリ（旧pythalesians）。                                                                                                      | ![GitHub stars](https://badgen.net/github/stars/cuemacro/finmarketpy)                    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtesting.py](https://github.com/kernc/backtesting.py)                              | 過去データでトレーディング戦略の実行可能性を検証するPythonフレームワーク。軽量・高速・ユーザーフレンドリーで直感的・インタラクティブ。                                                          | ![GitHub stars](https://badgen.net/github/stars/kernc/backtesting.py)                    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zvt](https://github.com/zvtvz/zvt)                                                    | モジュール型量子フレームワーク。                                                                                                                                                                | ![GitHub stars](https://badgen.net/github/stars/zvtvz/zvt)                               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [WonderTrader](https://github.com/wondertrader/wondertrader)                           | WonderTrader——量子研究・開発・取引のオールインワンフレームワーク。                                                                                                                              | ![GitHub stars](https://badgen.net/github/stars/wondertrader/wondertrader)               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [nautilus_trader](https://github.com/nautechsystems/nautilus_trader)                   | 高性能アルゴリズムトレーディングプラットフォームとイベント駆動型バックテスター。                                                                                                                | ![GitHub stars](https://badgen.net/github/stars/nautechsystems/nautilus_trader)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PandoraTrader](https://github.com/pegasusTrader/PandoraTrader)                        | C++で開発された高頻度量子取引プラットフォーム。複数の取引APIとクロスプラットフォームに対応。                                                                                                    | ![GitHub stars](https://badgen.net/github/stars/pegasusTrader/PandoraTrader)             | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg)       |
| [HFTBacktest](https://github.com/nkaz001/hftbacktest)                                  | Python+NumbaでHFTデータの高精度バックテスト。                                                                                                                                                   | ![GitHub stars](https://badgen.net/github/stars/nkaz001/hftbacktest)                     | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [aat](https://github.com/AsyncAlgoTrading/aat)                                         | Pythonでアルゴリズムトレーディング戦略を記述するための非同期イベント駆動フレームワーク。C++による任意加速に対応。モジュール型・拡張可能で多様な銘柄・戦略・複数取引所のライブ取引をサポート。   | ![GitHub stars](https://badgen.net/github/stars/AsyncAlgoTrading/aat)                    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) | Pythonインタープリターで自作トレーディングアルゴの開発に興味があるアルゴ取引初心者向けのプロジェクト。                                                                                          | ![GitHub stars](https://badgen.net/github/stars/sreenivasdoosa/sdoosa-algo-trade-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [lumibot](https://github.com/Lumiwealth/lumibot)                                       | シンプルながら実用的なバックテスト・サンプルベースのライブトレーディングフレームワーク（実行はやや遅め）。                                                                                      | ![GitHub stars](https://badgen.net/github/stars/Lumiwealth/lumibot)                      | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [quanttrader](https://github.com/letianzj/quanttrader)                                 | Pythonでのバックテストとライブトレーディング。イベントベースでbacktesting.pyに類似。                                                                                                            | ![GitHub stars](https://badgen.net/github/stars/letianzj/quanttrader)                    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [gobacktest](https://github.com/gobacktest/gobacktest)                                 | イベント駆動型バックテストフレームワークのGo実装。                                                                                                                                              | ![GitHub stars](https://badgen.net/github/stars/gobacktest/gobacktest)                   | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg)         |
| [FlashFunk](https://github.com/HFQR/FlashFunk)                                         | Rustによる高性能ランタイム。                                                                                                                                                                    | ![GitHub stars](https://badgen.net/github/stars/HFQR/FlashFunk)                          | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |

### 汎用 - ベクトルベースフレームワーク

| リポジトリ                                                    | 説明                                                                                                                     | スター                                                                     | 使用技術                                                                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [vectorbt](https://github.com/polakowo/vectorbt)              | バックテストへの新しいアプローチ。pandasとNumPyオブジェクト上で動作し、Numbaにより高速化。数千の戦略を数秒でテスト可能。 | ![GitHub stars](https://badgen.net/github/stars/polakowo/vectorbt)         | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | Rob Carverの著書「Systematic Trading」に基づくPythonでのシステマティックトレーディング。                                 | ![GitHub stars](https://badgen.net/github/stars/robcarver17/pysystemtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [bt](https://github.com/pmorissette/bt)                       | AlgoとStrategy Treeに基づくPython向け柔軟なバックテストフレームワーク。                                                  | ![GitHub stars](https://badgen.net/github/stars/pmorissette/bt)            | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### 暗号通貨

| リポジトリ                                                               | 説明                                                                                                                                                                     | スター                                                                            | 使用技術                                                                        |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Freqtrade](https://github.com/freqtrade/freqtrade)                      | Pythonで書かれた無料オープンソースの暗号通貨取引ボット。主要取引所とTelegram経由での操作に対応。バックテスト・プロット・資金管理ツールと機械学習による戦略最適化を含む。 | ![GitHub stars](https://badgen.net/github/stars/freqtrade/freqtrade)              | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Jesse](https://github.com/jesse-ai/jesse)                               | トレーディング戦略のリサーチと定義を簡素化することを目的とした高度な暗号取引フレームワーク。                                                                             | ![GitHub stars](https://badgen.net/github/stars/jesse-ai/jesse)                   | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OctoBot](https://github.com/Drakkar-Software/OctoBot)                   | テクニカル分析・アービトラージ・ソーシャルトレーディングに対応した高度なWebインターフェイス付き暗号通貨取引ボット。                                                      | ![GitHub stars](https://badgen.net/github/stars/Drakkar-Software/OctoBot)         | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Kelp](https://github.com/stellar/kelp)                                  | Stellar DEXと100以上の中央集権型取引所向けの無料オープンソース取引ボット。                                                                                               | ![GitHub stars](https://badgen.net/github/stars/stellar/kelp)                     | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg)         |
| [openlimits](https://github.com/nash-io/openlimits)                      | 複数取引所と言語ラッパーに対応したRust製の高性能暗号通貨取引API。                                                                                                        | ![GitHub stars](https://badgen.net/github/stars/nash-io/openlimits)               | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |
| [bTrader](https://github.com/gabriel-milan/btrader)                      | Binance向けの三角アービトラージ取引ボット。                                                                                                                              | ![GitHub stars](https://badgen.net/github/stars/gabriel-milan/btrader)            | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |
| [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) | 暗号通貨取引所からオーダーブックと取引メッセージを収集。                                                                                                                 | ![GitHub stars](https://badgen.net/github/stars/crypto-crawler/crypto-crawler-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |
| [Hummingbot](https://github.com/CoinAlpha/hummingbot)                    | 暗号通貨マーケットメイキング向けクライアント。                                                                                                                           | ![GitHub stars](https://badgen.net/github/stars/CoinAlpha/hummingbot)             | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cryptotrader-core](https://github.com/monomadic/cryptotrader-core)      | Rustで書かれた使いやすい暗号取引所REST APIクライアント。                                                                                                                 | ![GitHub stars](https://badgen.net/github/stars/monomadic/cryptotrader-core)      | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |

## トレーディングボット

_トレーディングボットとアルファモデル。古くメンテナンスが停止しているものもあります。_

| リポジトリ                                                      | 説明                                                                           | スター                                                                    | 使用技術                                                                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [Blackbird](https://github.com/butor/blackbird)                 | Blackbird Bitcoinアービトラージ：ロング/ショートのマーケットニュートラル戦略。 | ![GitHub stars](https://badgen.net/github/stars/butor/blackbird)          | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg)               |
| [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | Bitcoinアービトラージ - 機会検出器。                                           | ![GitHub stars](https://badgen.net/github/stars/maxme/bitcoin-arbitrage)  | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)         |
| [ThetaGang](https://github.com/brndnmtthws/thetagang)           | ThetaGangはお金を集めるためのIBKRボット。                                      | ![GitHub stars](https://badgen.net/github/stars/brndnmtthws/thetagang)    | ![made-with-typescript](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)     |
| [czsc](https://github.com/waditu/czsc)                          | 缠中说禅テクニカル分析ツール；缠論；株式；先物；クオント；量子化取引。         | ![GitHub stars](https://badgen.net/github/stars/waditu/czsc)              | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)         |
| [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2)       | Node.js + TypeScript製の自動アービトラージ取引システム。                       | ![GitHub stars](https://badgen.net/github/stars/bitrinjani/r2)            | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [analyzingalpha](https://github.com/leosmigel/analyzingalpha)   | シンプルな戦略の実装集。                                                       | ![GitHub stars](https://badgen.net/github/stars/leosmigel/analyzingalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)         |
| [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow)    | PyTrendFollow - トレンドフォローを使ったシステマティック先物取引。             | ![GitHub stars](https://badgen.net/github/stars/chrism2671/PyTrendFollow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)         |

## アナリティクス

### インジケーター

_将来の価格動向を予測するためのインジケーターライブラリ。_

| リポジトリ                                          | 説明                                                                                                                                  | スター                                                               | 使用技術                                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [ta-lib](https://github.com/mrjbq7/ta-lib)          | 金融市場データのテクニカル分析を実行。                                                                                                | ![GitHub stars](https://badgen.net/github/stars/mrjbq7/ta-lib)       | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [go-tart](https://github.com/iamjinlei/go-tart)     | ストリーミング更新対応の [ta-lib](https://github.com/mrjbq7/ta-lib) Go実装。                                                          | ![GitHub stars](https://badgen.net/github/stars/iamjinlei/go-tart)   | ![made-with-go](https://img.shields.io/badge/Made%20with-go-1f425f.svg)         |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | Pandasを活用した使いやすいテクニカル分析ライブラリ。130以上のインジケーターとユーティリティ、60以上のTA Libローソク足パターンを搭載。 | ![GitHub stars](https://badgen.net/github/stars/twopirllc/pandas-ta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finta](https://github.com/peerchemist/finta)       | Pandasで実装された一般的な金融テクニカル指標。                                                                                        | ![GitHub stars](https://badgen.net/github/stars/peerchemist/finta)   | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ta-rust](https://github.com/greyblake/ta-rs)       | Rust言語向けテクニカル分析ライブラリ。                                                                                                | ![GitHub stars](https://badgen.net/github/stars/greyblake/ta-rs)     | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |

### メトリクス計算

_金融メトリクスのライブラリ。_

| リポジトリ                                             | 説明                                                   | スター                                                                 | 使用技術                                                                        |
| ------------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [quantstats](https://github.com/ranaroussi/quantstats) | Pythonで書かれたクオンツ向けポートフォリオ分析ツール。 | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/quantstats) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ffn](https://github.com/pmorissette/ffn)              | Python向け金融関数ライブラリ。                         | ![GitHub stars](https://badgen.net/github/stars/pmorissette/ffn)       | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### 最適化

| リポジトリ                                                        | 説明                                                                                                                                | スター                                                                        | 使用技術                                                                        |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | Pythonによる金融ポートフォリオ最適化。古典的効率的フロンティア、Black-Litterman、階層的リスクパリティなどを含む。                   | ![GitHub stars](https://badgen.net/github/stars/robertmartin8/PyPortfolioOpt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib)         | Pythonによるポートフォリオ最適化とクオンタティブ戦略的資産配分。                                                                    | ![GitHub stars](https://badgen.net/github/stars/dcajasn/Riskfolio-Lib)        | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [empyrial](https://github.com/ssantoshp/Empyrial)                 | 金融機関と個人投資家向けのPythonベースオープンソース量子投資ライブラリ。2021年3月正式リリース。                                     | ![GitHub stars](https://badgen.net/github/stars/ssantoshp/Empyrial)           | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Deepdow](https://github.com/jankrepl/deepdow)                    | ポートフォリオ最適化とディープラーニングを結びつけるPythonパッケージ。1回のフォワードパスで重み配分を行うネットワークの研究を促進。 | ![GitHub stars](https://badgen.net/github/stars/jankrepl/deepdow)             | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [spectre](https://github.com/Heerozh/spectre)                     | Pythonによるポートフォリオ最適化とクオンタティブ戦略的資産配分。                                                                    | ![GitHub stars](https://badgen.net/github/stars/Heerozh/spectre)              | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### プライシング

| リポジトリ                                                     | 説明                                                                                                                       | スター                                                                   | 使用技術                                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| [tf-quant-finance](https://github.com/google/tf-quant-finance) | Googleによる量子金融向け高性能TensorFlowライブラリ。                                                                       | ![GitHub stars](https://badgen.net/github/stars/google/tf-quant-finance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinancePy](https://github.com/domokane/FinancePy)             | 固定収益・株式・FX・クレジットデリバティブを含む金融デリバティブのプライシングとリスク管理に特化したPython金融ライブラリ。 | ![GitHub stars](https://badgen.net/github/stars/domokane/FinancePy)      | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyQL](https://github.com/enthought/pyql)                      | 著名なプライシングライブラリQuantLibのPythonラッパー。                                                                     | ![GitHub stars](https://badgen.net/github/stars/enthought/pyql)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### リスク

| リポジトリ                                       | 説明                                     | スター                                                              | 使用技術                                                                        |
| ------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [pyfolio](https://github.com/quantopian/pyfolio) | Pythonによるポートフォリオとリスク分析。 | ![GitHub stars](https://badgen.net/github/stars/quantopian/pyfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## ブローカーAPI

| リポジトリ                                           | 説明                                                                                     | スター                                                                   | 使用技術                                                                                |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| [ccxt](https://github.com/ccxt/ccxt)                 | 100以上のビットコイン/アルトコイン取引所に対応したJavaScript/Python/PHP暗号通貨取引API。 | ![GitHub stars](https://badgen.net/github/stars/ccxt/ccxt)               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)         |
| [Ib_insync](https://github.com/erdewit/ib_insync)    | Interactive Brokers向けのPython同期/非同期フレームワーク。                               | ![GitHub stars](https://badgen.net/github/stars/erdewit/ib_insync)       | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)         |
| [Coinnect](https://github.com/hugues31/coinnect)     | REST APIで主要な暗号通貨取引所へのフルアクセスを提供することを目的としたRustライブラリ。 | ![GitHub stars](https://badgen.net/github/stars/hugues31/coinnect)       | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)             |
| [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) | FTX、FTXUS、OKX、Bybitなど向けの取引・データ・WebSocket JavaScript SDK。                 | ![GitHub stars](https://badgen.net/github/stars/CompendiumFi/PENDAX-SDK) | ![made-with-javascript](https://img.shields.io/badge/Made%20with-Javascript-1f425f.svg) |

## データソース

### 汎用

| リポジトリ                                                                   | 説明                                                                                                                           | スター                                                                         | 使用技術                                                                        |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal)          | 誰でも、どこでも使える投資リサーチツール。                                                                                     | ![GitHub stars](https://badgen.net/github/stars/OpenBB-finance/OpenBBTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TuShare](https://github.com/waditu/tushare)                                 | 中国株式の過去データをクロールするユーティリティ。                                                                             | ![GitHub stars](https://badgen.net/github/stars/waditu/tushare)                | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [yfinance](https://github.com/ranaroussi/yfinance)                           | Yahoo!ファイナンスから市場データをスレッド化されたPythonicな方法でダウンロード。                                               | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/yfinance)           | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AkShare](https://github.com/akfamily/akshare)                               | 人に優しいエレガントでシンプルなPython向け金融データインターフェースライブラリ。                                               | ![GitHub stars](https://badgen.net/github/stars/akfamily/akshare)              | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pandas-datareader](https://github.com/pydata/pandas-datareader)             | 複数バージョンのpandasに対応した最新のリモートデータアクセス。                                                                 | ![GitHub stars](https://badgen.net/github/stars/pydata/pandas-datareader)      | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Quandl](https://github.com/quandl/quandl-python)                            | 単一の無料APIで数百のプロバイダーから数百万の金融・経済データセットを取得。                                                    | ![GitHub stars](https://badgen.net/github/stars/quandl/quandl-python)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [findatapy](https://github.com/cuemacro/findatapy)                           | Quandl、Bloomberg、Yahoo、Googleなど多数のソースから統一した高レベルインターフェースで市場データをダウンロードするPython API。 | ![GitHub stars](https://badgen.net/github/stars/cuemacro/findatapy)            | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Investpy](https://github.com/alvarobartt/investpy)                          | PythonでInvesting.comから金融データを抽出。                                                                                    | ![GitHub stars](https://badgen.net/github/stars/alvarobartt/investpy)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | 2万社以上の企業プロフィール・財務諸表・財務比率・株価データを20年分収集できるファンダメンタル分析パッケージ。                  | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FundamentalAnalysis)  | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Wallstreet](https://github.com/mcdallas/wallstreet)                         | Wallstreet：リアルタイム株式・オプションツール。                                                                               | ![GitHub stars](https://badgen.net/github/stars/mcdallas/wallstreet)           | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### 暗号通貨

| リポジトリ                                                    | 説明                                                                                             | スター                                                                   | 使用技術                                                                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| [Cryptofeed](https://github.com/bmoscon/cryptofeed)           | Asyncio対応の暗号通貨取引所WebSocketデータフィードハンドラー。                                   | ![GitHub stars](https://badgen.net/github/stars/bmoscon/cryptofeed)      | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets)    | Gekko取引ボットのデータセットダンプ。SQLite形式の過去データをダウンロード可能。                  | ![GitHub stars](https://badgen.net/github/stars/xFFFFF/Gekko-Datasets)   | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) | ライブ暗号通貨過去取引データブロッター。任意の暗号取引所からライブ過去取引データをダウンロード。 | ![GitHub stars](https://badgen.net/github/stars/Optixal/CryptoInscriber) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Crypto Lake](https://github.com/crypto-lake/lake-api)        | 暗号通貨向けの高頻度オーダーブック・取引データ。                                                 | ![GitHub stars](https://badgen.net/github/stars/crypto-lake/lake-api)    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## データサイエンス

| リポジトリ                                                   | 説明                                                                                                            | スター                                                                     | 使用技術                                                                        |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [TensorFlow](https://github.com/tensorflow/tensorflow)       | Pythonによる科学計算の基本アルゴリズム。                                                                        | ![GitHub stars](https://badgen.net/github/stars/tensorflow/tensorflow)     | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pytorch](https://github.com/pytorch/pytorch)                | 強力なGPUアクセラレーションによるPythonのテンソルと動的ニューラルネットワーク。                                 | ![GitHub stars](https://badgen.net/github/stars/pytorch/pytorch)           | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Keras](https://github.com/keras-team/keras)                 | Pythonで最もユーザーフレンドリーな人間向けディープラーニング。                                                  | ![GitHub stars](https://badgen.net/github/stars/keras-team/keras)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | Pythonによる機械学習。                                                                                          | ![GitHub stars](https://badgen.net/github/stars/scikit-learn/scikit-learn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pandas](https://github.com/pandas-dev/pandas)               | Rのdata.frameに類似したラベル付きデータ構造、統計関数などを提供するPython向け柔軟なデータ分析・操作ライブラリ。 | ![GitHub stars](https://badgen.net/github/stars/pandas-dev/pandas)         | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Numpy](https://github.com/numpy/numpy)                      | Pythonによる科学計算の基本パッケージ。                                                                          | ![GitHub stars](https://badgen.net/github/stars/numpy/numpy)               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scipy](https://github.com/scipy/scipy)                      | Pythonによる科学計算の基本アルゴリズム。                                                                        | ![GitHub stars](https://badgen.net/github/stars/scipy/scipy)               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyMC](https://github.com/pymc-devs/pymc)                    | PythonによるProbabilistic Programming：AesaraによるベイズモデリングとProbabilistic Machine Learning。           | ![GitHub stars](https://badgen.net/github/stars/pymc-devs/pymc)            | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Cvxpy](https://github.com/cvxpy/cvxpy)                      | 凸最適化問題向けのPython埋め込みモデリング言語。                                                                | ![GitHub stars](https://badgen.net/github/stars/cvxpy/cvxpy)               | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## データベース

| リポジトリ                                                    | 説明                                                                                               | スター                                                                | 使用技術                                                                        |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Marketstore](https://github.com/alpacahq/marketstore)        | 金融時系列データ向けDataFrameサーバー。                                                            | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg)         |
| [Tectonicdb](https://github.com/0b01/tectonicdb)              | オーダーブックのティック向け高速・高圧縮スタンドアロンデータベースおよびストリーミングプロトコル。 | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb)      | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg)     |
| [ArcticDB (Man Group)](https://github.com/man-group/arcticdb) | 時系列・ティックデータ向け高性能データストア。                                                     | ![GitHub stars](https://badgen.net/github/stars/man-group/ArcticDB)   | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## グラフ計算

| リポジトリ                                                            | 説明                                                                                                                                       | スター                                                                  | 使用技術                                                                        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Ray](https://github.com/ray-project/ray)                             | 分散アプリケーション構築のためのシンプルかつ汎用的なAPIを提供するオープンソースフレームワーク。                                            | ![GitHub stars](https://badgen.net/github/stars/ray-project/ray)        | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Dask](https://github.com/dask/dask)                                  | Pandas風APIによるPythonのタスクスケジューリング並列計算。                                                                                  | ![GitHub stars](https://badgen.net/github/stars/dask/dask)              | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | 入力変化に対して効率的に更新できる複雑な計算を構築する方法を提供するライブラリ。Umut Acarらのself-adjusting computationsに着想を得たもの。 | ![GitHub stars](https://badgen.net/github/stars/janestreet/incremental) | ![made-with-ocaml](https://img.shields.io/badge/Made%20with-Ocaml-1f425f.svg)   |
| [Man MDF](https://github.com/man-group/mdf)                           | Python向けデータフロープログラミングツールキット。                                                                                         | ![GitHub stars](https://badgen.net/github/stars/man-group/mdf)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [GraphKit](https://github.com/yahoo/graphkit)                         | 順序付き計算グラフの作成・実行向け軽量Pythonモジュール。                                                                                   | ![GitHub stars](https://badgen.net/github/stars/yahoo/graphkit)         | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Tributary](https://github.com/timkpaine/tributary)                   | Pythonによるストリーミングリアクティブおよびデータフローグラフ。                                                                           | ![GitHub stars](https://badgen.net/github/stars/timkpaine/tributary)    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## 機械学習

| リポジトリ                                                                            | 説明                                                                                                                                                                 | スター                                                                       | 使用技術                                                                        |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [QLib (Microsoft)](https://github.com/microsoft/qlib)                                 | AI指向の量子投資プラットフォーム。量子投資におけるAI技術の潜在能力を引き出し、研究を支援し価値を創造することを目指す。多数のSOTAクオンタティブ研究論文をリリース中。 | ![GitHub stars](https://badgen.net/github/stars/microsoft/qlib)              | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL)                               | 量子金融に深層強化学習を適用する可能性を示した初のオープンソースフレームワーク。                                                                                     | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinRL) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [MlFinLab (Hudson & Thames)](https://github.com/hudson-and-thames/mlfinlab)           | 機械学習の力を活用したいポートフォリオマネージャーやトレーダー向けに、再現可能・解釈可能・使いやすいツールを提供。                                                   | ![GitHub stars](https://badgen.net/github/stars/hudson-and-thames/mlfinlab)  | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradingGym](https://github.com/Yvictor/TradingGym)                                   | 強化学習エージェントやシンプルなルールベースアルゴの訓練向けトレーディング・バックテスト環境。                                                                       | ![GitHub stars](https://badgen.net/github/stars/Yvictor/TradingGym)          | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) | Deep Q-Learningを使った株式取引ボット。                                                                                                                              | ![GitHub stars](https://badgen.net/github/stars/pskrunner14/trading-bot)     | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## 時系列分析

| リポジトリ                                                | 説明                                                               | スター                                                                   | 使用技術                                                                        |
| --------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| [Facebook Prophet](https://github.com/facebook/prophet)   | 線形・非線形成長を持つ多重季節性時系列データの高品質予測ツール。   | ![GitHub stars](https://badgen.net/github/stars/facebook/prophet)        | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [statsmodels](https://github.com/statsmodels/statsmodels) | データ探索・統計モデル推定・統計検定を可能にするPythonモジュール。 | ![GitHub stars](https://badgen.net/github/stars/statsmodels/statsmodels) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [tsfresh](https://github.com/blue-yonder/tsfresh)         | 時系列から関連特徴量を自動抽出。                                   | ![GitHub stars](https://badgen.net/github/stars/blue-yonder/tsfresh)     | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pmdarima](https://github.com/alkaline-ml/pmdarima)       | PythonのR言語auto.arima相当の機能を含む時系列分析ライブラリ。      | ![GitHub stars](https://badgen.net/github/stars/alkaline-ml/pmdarima)    | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## 可視化

| リポジトリ                                               | 説明                                                                                     | スター                                                                 | 使用技術                                                                        |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [D-Tale (Man Group)](https://github.com/man-group/dtale) | FlaskバックエンドとReactフロントエンドの組み合わせでPandasデータ構造を簡単に表示・分析。 | ![GitHub stars](https://badgen.net/github/stars/man-group/dtale)       | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [mplfinance](https://github.com/matplotlib/mplfinance)   | Matplotlibを使った金融市場データの可視化。                                               | ![GitHub stars](https://badgen.net/github/stars/matplotlib/mplfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [btplotting](https://github.com/happydasch/btplotting)   | backtraderのバックテスト・最適化結果・ライブデータのプロット提供。                       | ![GitHub stars](https://badgen.net/github/stars/happydasch/btplotting) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

# 戦略

_オリジナルのシステマティックトレーディング戦略を説明する **40以上の学術論文** のリストです。各戦略はアセットクラスごとに分類され、シャープレシオの降順に並んでいます。_

👉 戦略は[こちら](https://paperswithbacktest.com)にホストされています。

過去の戦略リスト：

## 債券・コモディティ・通貨・株式

| タイトル                       | シャープレシオ | ボラティリティ | リバランス | 実装                                                                          | ソース                                                                      |
| ------------------------------ | -------------- | -------------- | ---------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| タイムシリーズ・モメンタム効果 | `0.576`        | `20.5%`        | `月次`     | [QuantConnect](./static/strategies/time-series-momentum-effect.py)            | [論文](https://pages.stern.nyu.edu/~lpederse/papers/TimeSeriesMomentum.pdf) |
| 先物による短期リバーサル       | `-0.05`        | `12.3%`        | `週次`     | [QuantConnect](./static/strategies/asset-class-momentum-rotational-system.py) | [論文](https://ideas.repec.org/a/eee/jbfina/v28y2004i6p1337-1361.html)      |

## 債券・コモディティ・株式・REIT

| タイトル                         | シャープレシオ | ボラティリティ | リバランス | 実装                                                               | ソース                                                              |
| -------------------------------- | -------------- | -------------- | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| アセットクラス・トレンドフォロー | `0.502`        | `10.4%`        | `月次`     | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461)  |
| モメンタム資産配分戦略           | `0.321`        | `11%`          | `月次`     | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |

## 債券・株式

| タイトル             | シャープレシオ | ボラティリティ | リバランス | 実装                                                    | ソース                                                                                              |
| -------------------- | -------------- | -------------- | ---------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| ペアードスイッチング | `0.691`        | `9.5%`         | `四半期`   | [QuantConnect](./static/strategies/paired-switching.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1917044)                                 |
| FEDモデル            | `0.369`        | `14.3%`        | `月次`     | [QuantConnect](./static/strategies/fed-model.py)        | [論文](https://www.researchgate.net/publication/228267011_The_FED_Model_and_Expected_Asset_Returns) |

## 債券・株式・REIT

| タイトル                                         | シャープレシオ | ボラティリティ | リバランス | 実装                                                                                   | ソース                                                              |
| ------------------------------------------------ | -------------- | -------------- | ---------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| アセットクラス横断バリュー・モメンタムファクター | `0.155`        | `9.8%`         | `月次`     | [QuantConnect](./static/strategies/value-and-momentum-factors-across-asset-classes.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1079975) |

## コモディティ

| タイトル                                       | シャープレシオ | ボラティリティ | リバランス | 実装                                                                                | ソース                                                              |
| ---------------------------------------------- | -------------- | -------------- | ---------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| コモディティにおけるスキューネス効果           | `0.482`        | `17.7%`        | `月次`     | [QuantConnect](./static/strategies/skewness-effect-in-commodities.py)               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2671165) |
| コモディティ先物のリターン非対称性効果         | `0.239`        | `13.4%`        | `月次`     | [QuantConnect](./static/strategies/return-asymmetry-effect-in-commodity-futures.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3918896) |
| コモディティにおけるモメンタム効果             | `0.14`         | `20.3%`        | `月次`     | [QuantConnect](./static/strategies/momentum-effect-in-commodities.py)               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=702281)  |
| コモディティにおけるターム・ストラクチャー効果 | `0.128`        | `23.1%`        | `月次`     | [QuantConnect](./static/strategies/term-structure-effect-in-commodities.py)         | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1127213) |
| WTI/BRENTスプレッド取引                        | `-0.199`       | `11.6%`        | `日次`     | [QuantConnect](./static/strategies/trading-wti-brent-spread.py)                     | [論文](https://link.springer.com/article/10.1057/jdhf.2009.24)      |

## 暗号資産

| タイトル                       | シャープレシオ | ボラティリティ | リバランス     | 実装                                                                           | ソース                                                              |
| ------------------------------ | -------------- | -------------- | -------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Bitcoinの夜間季節性            | `0.892`        | `20.8%`        | `イントラデイ` | [QuantConnect](./static/strategies/intraday-seasonality-in-bitcoin.py)         | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4081000) |
| 暗号通貨のリバランスプレミアム | `0.698`        | `27.5%`        | `日次`         | [QuantConnect](./static/strategies/rebalancing-premium-in-cryptocurrencies.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3982120) |

## 通貨

| タイトル                         | シャープレシオ | ボラティリティ | リバランス | 実装                                                                      | ソース                                                                       |
| -------------------------------- | -------------- | -------------- | ---------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| FXキャリートレード               | `0.254`        | `7.8%`         | `月次`     | [QuantConnect](./static/strategies/fx-carry-trade.py)                     | [論文](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| ドルキャリートレード             | `0.113`        | `5.8%`         | `月次`     | [QuantConnect](./static/strategies/dollar-carry-trade.py)                 | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1541230)          |
| 通貨モメンタムファクター         | `-0.01`        | `6.7%`         | `月次`     | [QuantConnect](./static/strategies/currency-momentum-factor.py)           | [論文](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| 通貨バリューファクター – PPP戦略 | `-0.103`       | `5%`           | `四半期`   | [QuantConnect](./static/strategies/currency-value-factor-ppp-strategy.py) | [論文](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |

## 株式

| タイトル                                                     | シャープレシオ | ボラティリティ | リバランス | 実装                                                                                                   | ソース                                                                                                                                                        |
| ------------------------------------------------------------ | -------------- | -------------- | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 資産成長効果                                                 | `0.835`        | `10.2%`        | `年次`     | [QuantConnect](./static/strategies/asset-growth-effect.py)                                             | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1335524)                                                                                           |
| 株式の短期リバーサル効果                                     | `0.816`        | `21.4%`        | `週次`     | [QuantConnect](./static/strategies/short-term-reversal-in-stocks.py)                                   | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1605049)                                                                                           |
| 決算発表時のリバーサル                                       | `0.785`        | `25.7%`        | `日次`     | [QuantConnect](./static/strategies/reversal-during-earnings-announcements.py)                          | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2275982)                                                                                           |
| サイズファクター – 小型株プレミアム                          | `0.747`        | `11.1%`        | `年次`     | [QuantConnect](./static/strategies/small-capitalization-stocks-premium-anomaly.py)                     | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3177539)                                                                                           |
| 株式の低ボラティリティファクター効果                         | `0.717`        | `11.5%`        | `月次`     | [QuantConnect](./static/strategies/low-volatility-factor-effect-in-stocks.py)                          | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=980865)                                                                                            |
| 企業開示の語彙密度の活用方法                                 | `0.688`        | `10.4%`        | `月次`     | [QuantConnect](./static/strategies/how-to-use-lexical-density-of-company-filings.py)                   | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3921091)                                                                                           |
| ボラティリティリスクプレミアム効果                           | `0.637`        | `13.2%`        | `月次`     | [QuantConnect](./static/strategies/volatility-risk-premium-effect.py)                                  | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=189840)                                                                                            |
| 株式のペアズトレーディング                                   | `0.634`        | `8.5%`         | `日次`     | [QuantConnect](./static/strategies/pairs-trading-with-stocks.py)                                       | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=141615)                                                                                            |
| 原油による株式リターンの予測                                 | `0.599`        | `11.5%`        | `月次`     | [QuantConnect](./static/strategies/crude-oil-predicts-equity-returns.py)                               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=460500)                                                                                            |
| 株式のBetting Against Betaファクター                         | `0.594`        | `18.9%`        | `月次`     | [QuantConnect](./static/strategies/betting-against-beta-factor-in-stocks.py)                           | [論文](https://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf)                                                                                   |
| 株式のトレンドフォロー効果                                   | `0.569`        | `15.2%`        | `日次`     | [QuantConnect](./static/strategies/trend-following-effect-in-stocks.py)                                | [論文](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf)                                                                                                  |
| ESGファクター・モメンタム戦略                                | `0.559`        | `21.8%`        | `月次`     | [QuantConnect](./static/strategies/esg-factor-momentum-strategy.py)                                    | [論文](https://www.semanticscholar.org/paper/Can-ESG-Add-Alpha-An-Analysis-of-ESG-Tilt-and-Nagy-Kassam/64f77da4f8ce5906a73ffe4e9eec7c49c0960acc)              |
| バリュー（簿価時価比率）ファクター                           | `0.526`        | `11.9%`        | `月次`     | [QuantConnect](./static/strategies/value-book-to-market-factor.py)                                     | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2595747)                                                                                           |
| サッカークラブ株式のアービトラージ                           | `0.515`        | `14.2%`        | `日次`     | [QuantConnect](./static/strategies/soccer-clubs-stocks-arbitrage.py)                                   | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1343685)                                                                                           |
| 合成レンディングレートによる翌市場リターン予測               | `0.494`        | `13.7%`        | `日次`     | [QuantConnect](./static/strategies/synthetic-lending-rates-predict-subsequent-market-return.py)        | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3976307)                                                                                           |
| オプション満期週効果                                         | `0.452`        | `5%`           | `週次`     | [QuantConnect](./static/strategies/option-expiration-week-effect.py)                                   | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1571786)                                                                                           |
| ディスパーション・トレーディング                             | `0.432`        | `8.1%`         | `月次`     | [QuantConnect](./static/strategies/dispersion-trading.py)                                              | [論文](https://www.academia.edu/16327015/EQUILIBRIUM_INDEX_AND_SINGLE_STOCK_VOLATILITY_RISK_PREMIA)                                                           |
| 投資信託リターンのモメンタム                                 | `0.414`        | `13.6%`        | `四半期`   | [QuantConnect](./static/strategies/momentum-in-mutual-fund-returns.py)                                 | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1462408)                                                                                           |
| セクター・モメンタム – ローテーションシステム                | `0.401`        | `14.1%`        | `月次`     | [QuantConnect](./static/strategies/sector-momentum-rotational-system.py)                               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517)                                                                                           |
| スマートファクターモメンタムと市場ポートフォリオの組み合わせ | `0.388`        | `8.2%`         | `月次`     | [QuantConnect](./static/strategies/combining-smart-factors-momentum-and-market-portfolio.py)           | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3745517)                                                                                           |
| 株式のモメンタムとリバーサルをボラティリティ効果と組み合わせ | `0.375`        | `17%`          | `月次`     | [QuantConnect](./static/strategies/momentum-and-reversal-combined-with-volatility-effect-in-stocks.py) | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1679464)                                                                                           |
| 市場センチメントとオーバーナイトアノマリー                   | `0.369`        | `3.6%`         | `日次`     | [QuantConnect](./static/strategies/market-sentiment-and-an-overnight-anomaly.py)                       | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3829582)                                                                                           |
| 1月バロメーター                                              | `0.365`        | `7.4%`         | `月次`     | [QuantConnect](./static/strategies/january-barometer.py)                                               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1436516)                                                                                           |
| 研究開発費と株式リターン                                     | `0.354`        | `8.1%`         | `年次`     | [QuantConnect](./static/strategies/rd-expenditures-and-stock-returns.py)                               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227564)                                                                                            |
| バリューファクター – 各国内のCAPE効果                        | `0.351`        | `20.2%`        | `年次`     | [QuantConnect](./static/strategies/value-factor-effect-within-countries.py)                            | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2129474)                                                                                           |
| 株式クロスセクション・リターンの12ヶ月サイクル               | `0.34`         | `43.7%`        | `月次`     | [QuantConnect](./static/strategies/12-month-cycle-in-cross-section-of-stocks-returns.py)               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=687022)                                                                                            |
| 株式インデックスの月末効果                                   | `0.305`        | `7.2%`         | `日次`     | [QuantConnect](./static/strategies/turn-of-the-month-in-equity-indexes.py)                             | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=917884)                                                                                            |
| 給与日アノマリー                                             | `0.269`        | `3.8%`         | `日次`     | [QuantConnect](./static/strategies/payday-anomaly.py)                                                  | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257064)                                                                                           |
| 国別ETFのペアズトレーディング                                | `0.257`        | `5.7%`         | `日次`     | [QuantConnect](./static/strategies/pairs-trading-with-country-etfs.py)                                 | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1958546)                                                                                           |
| 残差モメンタムファクター                                     | `0.24`         | `9.7%`         | `月次`     | [QuantConnect](./static/strategies/residual-momentum-factor.py)                                        | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2319861)                                                                                           |
| 決算発表プレミアム                                           | `0.192`        | `3.7%`         | `月次`     | [QuantConnect](./static/strategies/earnings-announcement-premium.py)                                   | [論文](https://www.nber.org/system/files/working_papers/w13090/w13090.pdf)                                                                                    |
| 株式のROA効果                                                | `0.155`        | `8.7%`         | `月次`     | [QuantConnect](./static/strategies/roa-effect-within-stocks.py)                                        | [論文](https://static1.squarespace.com/static/5e6033a4ea02d801f37e15bb/t/5f61583e88f43b7d5b7196b5/1600215105801/Chen_Zhang_JF.pdf)                            |
| 株式の52週高値効果                                           | `0.153`        | `19%`          | `月次`     | [QuantConnect](./static/strategies/52-weeks-high-effect-in-stocks.py)                                  | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1787378)                                                                                           |
| ファンダメンタルFSCOREと株式短期リバーサルの組み合わせ       | `0.153`        | `17.6%`        | `月次`     | [QuantConnect](./static/strategies/combining-fundamental-fscore-and-equity-short-term-reversals.py)    | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3097420)                                                                                           |
| 国際株式インデックスのBetting Against Betaファクター         | `0.142`        | `9.1%`         | `月次`     | [QuantConnect](./static/strategies/betting-against-beta-factor-in-country-equity-indexes.py)           | [論文](https://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf)                                                                                   |
| コンシステント・モメンタム戦略                               | `0.128`        | `28.8%`        | `6ヶ月`    | [QuantConnect](./static/strategies/consistent-momentum-strategy.py)                                    | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2652592)                                                                                           |
| 空売り残高効果 – ロング/ショートバージョン                   | `0.079`        | `6.6%`         | `月次`     | [QuantConnect](./static/strategies/short-interest-effect-long-short-version.py)                        | [論文](https://www.semanticscholar.org/paper/Why-Do-Short-Interest-Levels-Predict-Stock-Returns-Boehmer-Erturk/06418ef437dc7156229532a97d0f8392373eb297?p2df) |
| 資産成長効果と組み合わせたモメンタムファクター               | `0.058`        | `25.1%`        | `月次`     | [QuantConnect](./static/strategies/momentum-factor-combined-with-asset-growth-effect.py)               | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1684767)                                                                                           |
| 株式のモメンタムファクター効果                               | `-0.008`       | `21.8%`        | `月次`     | [QuantConnect](./static/strategies/momentum-factor-effect-in-stocks.py)                                | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2435323)                                                                                           |
| モメンタムファクターとスタイルローテーション効果             | `-0.056`       | `10%`          | `月次`     | [QuantConnect](./static/strategies/momentum-factor-and-style-rotation-effect.py)                       | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1276815)                                                                                           |
| 自社株買いと組み合わせた決算発表                             | `-0.16`        | `0.1%`         | `日次`     | [QuantConnect](./static/strategies/earnings-announcements-combined-with-stock-repurchases.py)          | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2589966)                                                                                           |
| 決算品質ファクター                                           | `-0.18`        | `28.7%`        | `年次`     | [QuantConnect](./static/strategies/earnings-quality-factor.py)                                         | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2179247)                                                                                           |
| 発生主義アノマリー                                           | `-0.272`       | `13.7%`        | `年次`     | [QuantConnect](./static/strategies/accrual-anomaly.py)                                                 | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=546108)                                                                                            |
| ESG、価格モメンタムと確率的最適化                            | `N/A`          | `N/A`          | `月次`     |                                                                                                        | [論文](https://quantpedia.com/strategies/esg-price-momentum-and-stochastic-optimization/)                                                                     |
| 企業開示の類似性と株式リターン                               | `N/A`          | `N/A`          | `月次`     |                                                                                                        | [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690461)                                                                                           |

# 書籍

クオンタティブトレーダー向けの **55冊** の総合リストです。

## 入門

| タイトル                                                                                                                                                            | レビュー数                                          | 評価                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------- |
| [株式市場入門：今日から利益を出し始めるために必要なすべて - Matthew R. Kratter](https://amzn.to/3QN2VdU)                                                            | ![](https://badgen.net/badge/reviews/14%20161/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [デイトレードで生きる方法：取引ツール・戦術・資金管理・規律・取引心理学の初心者ガイド - Andrew Aziz](https://amzn.to/3bmehFv)                                       | ![](https://badgen.net/badge/reviews/12%20278/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [常識的な投資の小さな本：株式市場リターンの正当な分け前を確保する唯一の方法 - John C. Bogle](https://amzn.to/3A4mgkR)                                               | ![](https://badgen.net/badge/reviews/6%20969/blue)  | ![](https://badgen.net/badge/rating/4.7/blue) |
| [投資クイックスタートガイド：株式市場のナビゲート、資産形成、安全な財務的将来の作り方の簡易初心者ガイド - Ted D. Snow](https://amzn.to/3A5aRkX)                     | ![](https://badgen.net/badge/reviews/2%20537/blue)  | ![](https://badgen.net/badge/rating/4.5/blue) |
| [デイトレードクイックスタートガイド：勝利するトレードプラン・市場の攻略・成功するデイトレーダーになるための簡易初心者ガイド - Troy Noonan](https://amzn.to/3HPZijw) | ![](https://badgen.net/badge/reviews/1%20229/blue)  | ![](https://badgen.net/badge/rating/4.4/blue) |
| [アルゴ取引入門：個人トレーダーがプロのトレーダーと競争して成功する方法 - Kevin J Davey](https://amzn.to/39Tf7JC)                                                   | ![](https://badgen.net/badge/reviews/131/blue)      | ![](https://badgen.net/badge/rating/4/blue)   |
| [アルゴリズム取引とDMA：直接アクセス取引戦略入門 - Barry Johnson](https://amzn.to/3xYb0UN)                                                                          | ![](https://badgen.net/badge/reviews/69/blue)       | ![](https://badgen.net/badge/rating/4.4/blue) |

## 伝記

| タイトル                                                                                                    | レビュー数                                     | 評価                                          |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| [クオントとしての私の人生：物理学と金融の回顧 - Emanuel Derman](https://amzn.to/3A8KudR)                    | ![](https://badgen.net/badge/reviews/192/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [私はいかにしてクオントになったか：ウォール街エリート25人の洞察 - Barry Schachter](https://amzn.to/3Alf8kz) | ![](https://badgen.net/badge/reviews/27/blue)  | ![](https://badgen.net/badge/rating/3.7/blue) |

## コーディング

| タイトル                                                                                                                                          | レビュー数                                     | 評価                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| [金融のためのPython：データ駆動型金融の習得 - Yves Hilpisch](https://amzn.to/3NhkTlP)                                                             | ![](https://badgen.net/badge/reviews/249/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [Trading Evolved：Pythonで強力なトレーディング戦略を誰でも構築できる - Andreas F. Clenow](https://amzn.to/3A0jcGB)                                | ![](https://badgen.net/badge/reviews/173/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [アルゴリズム取引のためのPython：アイデアからクラウドデプロイメントまで - Yves Hilpisch](https://amzn.to/3bpkd0C)                                 | ![](https://badgen.net/badge/reviews/90/blue)  | ![](https://badgen.net/badge/rating/4.4/blue) |
| [Pythonによるアルゴリズム取引：定量的手法と戦略開発 - Chris Conlan](https://amzn.to/3u3cxYo)                                                      | ![](https://badgen.net/badge/reviews/48/blue)  | ![](https://badgen.net/badge/rating/4.2/blue) |
| [アルゴリズム取引を学ぶ：PythonとAdvanced Data Analysisを使ったアルゴリズムシステムの構築とデプロイ - Sebastien Donadio](https://amzn.to/3NqNghA) | ![](https://badgen.net/badge/reviews/46/blue)  | ![](https://badgen.net/badge/rating/4.1/blue) |

## 暗号資産

| タイトル                                                                                                             | レビュー数                                         | 評価                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------- |
| [ビットコイン本位制：中央銀行への非中央集権的代替 - Saifedean Ammous](https://amzn.to/3QMJgec)                       | ![](https://badgen.net/badge/reviews/5%20136/blue) | ![](https://badgen.net/badge/rating/4.7/blue) |
| [ビットコイン億万長者：天才・裏切り・贖罪の実話 - Ben Mezrich](https://amzn.to/39SkdWt)                              | ![](https://badgen.net/badge/reviews/1%20787/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [Bitcoinのマスタリング：オープンブロックチェーンのプログラミング - Andreas M. Antonopoulos](https://amzn.to/3NniZ3p) | ![](https://badgen.net/badge/reviews/955/blue)     | ![](https://badgen.net/badge/rating/4.7/blue) |
| [なぜBitcoinを買うのか：明日のお金に今日投資する - Andy Edstrom](https://amzn.to/3OMcKqZ)                            | ![](https://badgen.net/badge/reviews/192/blue)     | ![](https://badgen.net/badge/rating/4.7/blue) |

## 一般

| タイトル                                                                                                                                                                                                                                                                                                      | レビュー数                                          | 評価                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------- |
| [賢明なる投資家：バリュー投資の決定版 - Benjamin Graham, Jason Zweig](https://www.amazon.fr/gp/product/0060555661/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0060555661&linkId=aba73910e4e3873b6cc8364487662bd6)                                              | ![](https://badgen.net/badge/reviews/38%20087/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [私のお金の投資方法：金融専門家が貯蓄・支出・投資を明かす - Joshua Brown, Brian Portnoy](https://amzn.to/3A4rsoU)                                                                                                                                                                                             | ![](https://badgen.net/badge/reviews/892/blue)      | ![](https://badgen.net/badge/rating/4.3/blue) |
| [Naked Forex：インジケーターなしで取引するための高確率テクニック - Alex Nekritin](https://amzn.to/3NkrAUj)                                                                                                                                                                                                    | ![](https://badgen.net/badge/reviews/720/blue)      | ![](https://badgen.net/badge/rating/4.7/blue) |
| [投資の四本柱：勝利するポートフォリオ構築のレッスン - William J. Bernstein](https://www.amazon.fr/gp/product/B0041842TW/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=B0041842TW&linkId=d9bc2fec4f3faa41ca4f24aed3c72122)                                        | ![](https://badgen.net/badge/reviews/441/blue)      | ![](https://badgen.net/badge/rating/4.7/blue) |
| [オプションのボラティリティとプライシング：高度な取引戦略・技法 第2版 - Sheldon Natenberg](https://amzn.to/3btOxXL)                                                                                                                                                                                           | ![](https://badgen.net/badge/reviews/388/blue)      | ![](https://badgen.net/badge/rating/4.6/blue) |
| [テクニカル分析の技術と科学：市場構造・価格行動・取引戦略 - Adam Grimes](https://www.amazon.fr/gp/product/1118115120/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118115120&linkId=d5dc1f0e6727b2663d2186a110a31ad0)                                           | ![](https://badgen.net/badge/reviews/305/blue)      | ![](https://badgen.net/badge/rating/4.7/blue) |
| [新・生きるためのトレーディング：心理学・規律・取引ツール・システム・リスク管理・取引管理 - Alexander Elder](https://www.amazon.fr/gp/product/1118467450/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118467450&linkId=67ee502653bc52a5240ced9fc88eb76d)       | ![](https://badgen.net/badge/reviews/242/blue)      | ![](https://badgen.net/badge/rating/4.5/blue) |
| [勝利するアルゴリズム取引システムの構築：データマイニングからモンテカルロシミュレーション、ライブトレーディングまでのトレーダーの旅 - Kevin J Davey](https://amzn.to/39QnsxA)                                                                                                                                 | ![](https://badgen.net/badge/reviews/163/blue)      | ![](https://badgen.net/badge/rating/4.2/blue) |
| [システマティックトレーディング：取引・投資システム設計のユニークな新手法 - Robert Carver](https://www.amazon.fr/gp/product/0857194453/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0857194453&linkId=32d8bffc32c01041cde066bacab76c04)                         | ![](https://badgen.net/badge/reviews/123/blue)      | ![](https://badgen.net/badge/rating/4.2/blue) |
| [定量モメンタム：モメンタムベースの銘柄選択システム構築の実践ガイド - Wesley R. Gray, Jack R. Vogel](https://www.amazon.fr/gp/product/111923719X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=111923719X&linkId=b825cb65462a4a9254af3b7dc5328131)               | ![](https://badgen.net/badge/reviews/105/blue)      | ![](https://badgen.net/badge/rating/4.3/blue) |
| [アルゴリズム取引：勝利戦略とその根拠 - Ernest P. Chan](https://amzn.to/3xWi8kd)                                                                                                                                                                                                                              | ![](https://badgen.net/badge/reviews/100/blue)      | ![](https://badgen.net/badge/rating/4.3/blue) |
| [レバレッジトレーディング：すべてのトレーダーのためのFX・証拠金株式・CFD・スプレッドベット・先物のプロアプローチ - Robert Carver](https://amzn.to/3Nhl6p7)                                                                                                                                                    | ![](https://badgen.net/badge/reviews/98/blue)       | ![](https://badgen.net/badge/rating/4.4/blue) |
| [取引システム：システム開発とポートフォリオ最適化への新アプローチ - Emilio Tomasini, Urban Jaekle](https://www.amazon.fr/gp/product/1905641796/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1905641796&linkId=61e6634242c497498338f73641ce0a80)                 | ![](https://badgen.net/badge/reviews/67/blue)       | ![](https://badgen.net/badge/rating/4.3/blue) |
| [取引と取引所：実践者のための市場マイクロストラクチャー - Larry Harris](https://www.amazon.fr/gp/product/0195144708/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0195144708&linkId=e47e596fc0696cbd624726cce05b4500)                                            | ![](https://badgen.net/badge/reviews/61/blue)       | ![](https://badgen.net/badge/rating/4.3/blue) |
| [取引システム第2版：システム開発とポートフォリオ最適化への新アプローチ - Emilio Tomasini, Urban Jaekle](https://www.amazon.fr/gp/product/085719755X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=085719755X&linkId=97aa558484a8dc2bf57a5296e7f38cad)            | ![](https://badgen.net/badge/reviews/42/blue)       | ![](https://badgen.net/badge/rating/4/blue)   |
| [マシントレーディング：コンピューターアルゴリズムで市場を征服する - Ernest P. Chan](https://amzn.to/3OIBe4o)                                                                                                                                                                                                  | ![](https://badgen.net/badge/reviews/53/blue)       | ![](https://badgen.net/badge/rating/4/blue)   |
| [定量的エクイティポートフォリオ管理：ポートフォリオ構築と管理へのアクティブアプローチ - Ludwig B Chincarini, Daehwan Kim](https://amzn.to/3yl9u0c)                                                                                                                                                            | ![](https://badgen.net/badge/reviews/51/blue)       | ![](https://badgen.net/badge/rating/4.5/blue) |
| [アクティブポートフォリオ管理：優れたリターンを生み出しリスクをコントロールするための定量的アプローチ - Richard Grinold, Ronald Kahn](https://amzn.to/3xMKaic)                                                                                                                                                | ![](https://badgen.net/badge/reviews/46/blue)       | ![](https://badgen.net/badge/rating/4/blue)   |
| [定量テクニカル分析：取引システム開発と取引管理への統合アプローチ - Dr Howard B Bandy](https://www.amazon.fr/gp/product/0979183855/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0979183855&linkId=8ef7bda69477bdccf90f5ac02ee495b0)                             | ![](https://badgen.net/badge/reviews/37/blue)       | ![](https://badgen.net/badge/rating/3.8/blue) |
| [アクティブポートフォリオ管理の進歩：定量投資の新展開 - Richard Grinold, Ronald Kahn](https://amzn.to/3xUTK2z)                                                                                                                                                                                                | ![](https://badgen.net/badge/reviews/19/blue)       | ![](https://badgen.net/badge/rating/4.7/blue) |
| [プロフェッショナル自動取引：理論と実践 - Eugene A. Durenard](https://amzn.to/3yhfOpw)                                                                                                                                                                                                                        | ![](https://badgen.net/badge/reviews/15/blue)       | ![](https://badgen.net/badge/rating/4.3/blue) |
| [アルゴリズム取引と定量戦略 - Raja Velu, Maxence Hardy, Daniel Nehren](https://amzn.to/3xUTQXZ)                                                                                                                                                                                                               | ![](https://badgen.net/badge/reviews/11/blue)       | ![](https://badgen.net/badge/rating/4.2/blue) |
| [定量取引：アルゴリズム・分析・データ・モデル・最適化 - Xin Guo, Tze Leung Lai, Howard Shek, Samuel Po-Shing Wong](https://www.amazon.fr/gp/product/0367871815/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0367871815&linkId=3f2ba1cbc0e1fe02e255da740423b2fb) | ![](https://badgen.net/badge/reviews/2/blue)        | ![](https://badgen.net/badge/rating/3/blue)   |

## 高頻度取引

| タイトル                                                                                                                                                                                                                                                                                        | レビュー数                                    | 評価                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| [ブラックボックスの内側：定量的・高頻度取引の簡易ガイド - Rishi K. Narang](https://www.amazon.fr/gp/product/1118362411/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1118362411&linkId=35e02d4e636350366531a5033597a541)                           | ![](https://badgen.net/badge/reviews/76/blue) | ![](https://badgen.net/badge/rating/4.3/blue) |
| [アルゴリズム・高頻度取引 - Álvaro Cartea, Sebastian Jaimungal, José Penalva](https://www.amazon.fr/gp/product/1107091144/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1107091144&linkId=64e3ceb66482d8db6827830964b85613)                        | ![](https://badgen.net/badge/reviews/52/blue) | ![](https://badgen.net/badge/rating/4.1/blue) |
| [HFTの問題 – 高頻度取引と株式市場構造改革に関する論文集 - Haim Bodek](https://www.amazon.fr/gp/product/1481978357/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1481978357&linkId=2f3acf998de645990b681e2ac9f0217c)                                | ![](https://badgen.net/badge/reviews/38/blue) | ![](https://badgen.net/badge/rating/4/blue)   |
| [高頻度金融入門 - Ramazan Gençay, Michel Dacorogna, Ulrich A. Muller, Olivier Pictet, Richard Olsen](https://www.amazon.fr/gp/product/0122796713/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0122796713&linkId=7e6c098026204f399e45d7fbb803dcca) | ![](https://badgen.net/badge/reviews/11/blue) | ![](https://badgen.net/badge/rating/4.6/blue) |
| [実践における市場マイクロストラクチャー - Charles-Albert Lehalle, Sophie Laruelle](https://www.amazon.fr/Market-Microstructure-Practice-Sophie-Laruelle/dp/9813231122)                                                                                                                          | ![](https://badgen.net/badge/reviews/8/blue)  | ![](https://badgen.net/badge/rating/3.9/blue) |
| [市場流動性の金融数学 - Olivier Gueant](https://www.amazon.com/Financial-Mathematics-Market-Liquidity-Execution/dp/1498725473)                                                                                                                                                                  | ![](https://badgen.net/badge/reviews/6/blue)  | ![](https://badgen.net/badge/rating/4.6/blue) |
| [高頻度取引 - Maureen O'Hara, David Easley, Marcos M López de Prado](https://www.amazon.fr/gp/product/178272009X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=178272009X&linkId=082f861ff6bbe4cca4ef7ccbe620a2c4)                                 | ![](https://badgen.net/badge/reviews/1/blue)  | ![](https://badgen.net/badge/rating/3/blue)   |

## 機械学習

| タイトル                                                                                                                                                                                                                                                                                              | レビュー数                                     | 評価                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| [ダークプール：AIトレーディングマシンの台頭とウォール街への脅威 - Scott Patterson](https://www.amazon.fr/gp/product/0307887189/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0307887189&linkId=2572cae24ed7de0b279580312daf0f03)                         | ![](https://badgen.net/badge/reviews/532/blue) | ![](https://badgen.net/badge/rating/4.5/blue) |
| [金融機械学習の進歩 - Marcos Lopez de Prado](https://www.amazon.fr/gp/product/1119482089/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1119482089&linkId=7eff4d3f3d9f2d00d05032f726386e53)                                                               | ![](https://badgen.net/badge/reviews/446/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [アルゴリズム取引のための機械学習：市場・代替データからシグナルを抽出する予測モデル 第2版 - Stefan Jansen](https://www.amazon.fr/gp/product/1839217715/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1839217715&linkId=80e3e93e1b6027596858ed0f1fbf10c2) | ![](https://badgen.net/badge/reviews/229/blue) | ![](https://badgen.net/badge/rating/4.4/blue) |
| [資産管理のための機械学習 - Marcos M López de Prado](https://www.amazon.fr/gp/product/1108792898/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1108792898&linkId=8eb7e3c369d38b36df8dfecf05a622db)                                                       | ![](https://badgen.net/badge/reviews/96/blue)  | ![](https://badgen.net/badge/rating/4.6/blue) |
| [金融における機械学習：理論から実践へ - Matthew F. Dixon, Igor Halperin, Paul Bilokon](https://www.amazon.fr/gp/product/3030410676/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=3030410676&linkId=5f5f1df6be62ae96ef7a0c536c3ecdb4)                     | ![](https://badgen.net/badge/reviews/76/blue)  | ![](https://badgen.net/badge/rating/4.6/blue) |
| [金融における人工知能：Pythonベースのガイド - Yves Hilpisch](https://www.amazon.fr/gp/product/1492055433/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=1492055433&linkId=7c20249be4d35badb127d6a5423fc495)                                               | ![](https://badgen.net/badge/reviews/38/blue)  | ![](https://badgen.net/badge/rating/4.3/blue) |
| [アルゴリズム取引手法：高度な統計・最適化・機械学習技法を使った応用 - Robert Kissell](https://www.amazon.fr/gp/product/0128156309/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=darchimbaud-21&creative=6746&linkCode=as2&creativeASIN=0128156309&linkId=0a197c0b547a0ee63ccd19389bb42edd)                      | ![](https://badgen.net/badge/reviews/15/blue)  | ![](https://badgen.net/badge/rating/4.7/blue) |

# 動画

| タイトル                                                                                                                                                            | いいね数                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [Krish Naik - 機械学習チュートリアルと株価予測への応用](https://www.youtube.com/watch?v=H6du_pfuznE)                                                                | ![](https://badgen.net/badge/likes/6.3k/blue) |
| [QuantInsti Youtube - 取引のための機械学習に関するウェビナー](https://www.youtube.com/user/quantinsti/search?query=machine+learning)                                | ![](https://badgen.net/badge/likes/6.1k/blue) |
| [Siraj Raval - ディープラーニングによる株式市場予測動画](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A/search?query=trading)                             | ![](https://badgen.net/badge/likes/1.7k/blue) |
| [Quantopian - 取引のための機械学習に関するウェビナー](https://www.youtube.com/channel/UC606MUq45P3zFLa4VGKbxsg/search?query=machine+learning)                       | ![](https://badgen.net/badge/likes/1.5k/blue) |
| [Sentdex - FX・株式分析とアルゴリズム取引のための機械学習](https://www.youtube.com/watch?v=v_L9jR8P-54&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO)                     | ![](https://badgen.net/badge/likes/1.5k/blue) |
| [QuantNews - アルゴリズム取引のための機械学習 3部作](https://www.youtube.com/playlist?list=PLHJACfjILJ-91qkw5YC83S6COKGscctzz)                                      | ![](https://badgen.net/badge/likes/806/blue)  |
| [Sentdex - 金融のためのPythonプログラミング（機械学習含む数本の動画）](https://www.youtube.com/watch?v=Z-5wNWgRJpk&index=9&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ) | ![](https://badgen.net/badge/likes/735/blue)  |
| [Chat with Traders EP042 - Bert Moulerとアルゴリズム取引のための機械学習](https://www.youtube.com/watch?v=i8FNO8r7PaE)                                              | ![](https://badgen.net/badge/likes/687/blue)  |
| [Tucker Balch - 取引への深層強化学習の適用](https://www.youtube.com/watch?v=Pka0DC_P17k)                                                                            | ![](https://badgen.net/badge/likes/487/blue)  |
| [Ernie Chan - 定量取引のための機械学習ウェビナー](https://www.youtube.com/watch?v=72aEDjwGMr8&t=1023s)                                                              | ![](https://badgen.net/badge/likes/436/blue)  |
| [Chat with Traders EP147 - Tom Starkeと実行可能な取引戦略への探偵的取り組み](https://www.youtube.com/watch?v=JjXw9Mda7eY)                                           | ![](https://badgen.net/badge/likes/407/blue)  |
| [Chat with Traders EP142 - Bert Moulerと人間の欠点を回避する自動化アルゴトレーダー](https://www.youtube.com/watch?v=ofL66mh6Tw0)                                    | ![](https://badgen.net/badge/likes/316/blue)  |
| [エセックス大学修士論文発表 - 指値注文板の分析、ディープラーニングアプローチ](https://www.youtube.com/watch?v=qxSh2VFmRGw)                                          | ![](https://badgen.net/badge/likes/264/blue)  |
| [Howard Bandy - 機械学習取引システム開発ウェビナー](https://www.youtube.com/watch?v=v729evhMpYk&t=1s)                                                               | ![](https://badgen.net/badge/likes/253/blue)  |
| [Chat With Traders EP131 - Morgan Sladeと機械学習による取引戦略](https://www.youtube.com/watch?v=EbWbeYu8zwg)                                                       | ![](https://badgen.net/badge/likes/229/blue)  |
| [Chat with Traders Quantopian 5 - Max Margenotと金融における機械学習の良い活用法](https://www.youtube.com/watch?v=Zj5sXWv9SDM)                                      | ![](https://badgen.net/badge/likes/198/blue)  |
| [Hitoshi Harada（Alpaca CTO） - 金融におけるディープラーニング講演](https://www.youtube.com/watch?v=FoQKCeDuPiY)                                                    | ![](https://badgen.net/badge/likes/147/blue)  |
| [Better System Trader EP028 - David Aronsonが強気・弱気相場を識別するインジケーター研究を共有](https://www.youtube.com/watch?v=Q4rV0Y9NokI)                         | ![](https://badgen.net/badge/likes/97/blue)   |
| [Prediction Machines - 金融講演でのPythonによるディープラーニング](https://www.youtube.com/watch?v=xvm-M-R2fZY)                                                     | ![](https://badgen.net/badge/likes/87/blue)   |
| [Better System Trader EP064 - Bert Moulerと暗号通貨と機械学習](https://www.youtube.com/watch?v=YgRTd4nLJoU)                                                         | ![](https://badgen.net/badge/likes/35/blue)   |
| [Better System Trader EP023 - ポートフォリオマネージャーMichael HimmelがAIと機械学習について語る](https://www.youtube.com/watch?v=9tZjeyhfG0g)                      | ![](https://badgen.net/badge/likes/29/blue)   |
| [Better System Trader EP082 - Kris Longmoreと機械学習](https://www.youtube.com/watch?v=0syNgsd635M)                                                                 | ![](https://badgen.net/badge/likes/18/blue)   |

# ブログ

| タイトル                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------- |
| [AAA Quants, Tom Starke Blog](http://aaaquants.com/category/blog/)                                                           |
| [AI & Systematic Trading](https://blog.paperswithbacktest.com/)                                                              |
| [Blackarbs blog](http://www.blackarbs.com/blog/)                                                                             |
| [Hardikp, Hardik Patel blog](https://www.hardikp.com/)                                                                       |
| [Max Dama on Automated Trading](https://bit.ly/3wVZbh9)                                                                      |
| [Medallion.Club on Systematic Trading（フランス語）](https://medallion.club/trading-algorithmique-quantitatif-systematique/) |
| [Proof Engineering: The Algorithmic Trading Platform](https://bit.ly/3lX7zYN)                                                |
| [Quantsportal, Jacques Joubert's Blog](http://www.quantsportal.com/blog-page/)                                               |
| [Quantstart - 取引のための機械学習記事](https://www.quantstart.com/articles)                                                 |
| [RobotWealth, Kris Longmore Blog](https://robotwealth.com/blog/)                                                             |

# コース

| タイトル                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------ |
| [AI in Finance](https://cfte.education/)                                                                                                   |
| [AI & Systematic Trading](https://paperswithbacktest.com/course)                                                                           |
| [PythonによるAlgorithmic Trading for Cryptocurrencies](https://github.com/tudorelu/tudorials/tree/master/trading)                          |
| [Coursera, NYU - 金融における機械学習のガイドツアー](https://www.coursera.org/learn/guided-tour-machine-learning-finance)                  |
| [Coursera, NYU - 金融における機械学習の基礎](https://www.coursera.org/learn/fundamentals-machine-learning-in-finance)                      |
| [Coursera, NYU - 金融における強化学習](https://www.coursera.org/learn/reinforcement-learning-in-finance)                                   |
| [Coursera, NYU - 金融における強化学習の高度な手法の概要](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance)   |
| [Hudson and Thames Quantitative Research](https://github.com/hudson-and-thames)                                                            |
| [NYU: 金融における強化学習の高度な手法の概要](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance/home/welcome) |
| [Udacity: 取引のための人工知能](https://www.udacity.com/course/ai-for-trading--nd880)                                                      |
| [Udacity, Georgia Tech - 取引のための機械学習](https://www.udacity.com/course/machine-learning-for-trading--ud501)                         |
