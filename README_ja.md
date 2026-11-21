<div align="center">
  <img src="static/images/awesome-systematic-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

[中文版はこちら](./README_zh.md)<br>
[English version here](./README.md)

システマティックトレーディング（クオンタティブ・トレーディング）戦略の発見・開発・運用に役立つ論文、ソフトウェア、書籍、記事のリストを収集しています。

<!-- omit in toc -->
### Papers With Backtest で最初の論文を再現する

公開論文の戦略と、その Python コード・データから始めます。
自分のワークスペースに複製して、ブラウザでバックテストを実行できます。

**[バリュー・サイズ効果の例を試す →](https://paperswithbacktest.com/strategies/value-and-size-effect-now-you-see-it-now-you-don-t?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_ja_primary)**

カード登録もローカル環境の準備も不要です。無料アカウントには、
**戦略の完全な閲覧権 1 件、複製 1 回、リサーチエージェントの利用枠 1 ドル分**が含まれます。
各アカウントにつき一度限りで、利用枠はリセットされません。開いた戦略は引き続き閲覧できます。

無料の閲覧枠で試す戦略を一つ選んでください。

| 検証したい問い | 例を開く |
|---|---|
| バリューとサイズは株式リターンにどう影響するか？ | [バリュー・サイズ効果](https://paperswithbacktest.com/strategies/value-and-size-effect-now-you-see-it-now-you-don-t?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_ja_equity) |
| 相関を使うと商品モメンタム戦略は改善するか？ | [商品モメンタム](https://paperswithbacktest.com/strategies/how-to-improve-commodity-momentum-using-intra-market-correlation?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_ja_commodity) |
| ビットコインでトレンドと平均回帰はどう振る舞うか？ | [ビットコインの季節性・トレンド・平均回帰](https://paperswithbacktest.com/strategies/seasonality-trend-following-and-mean-reversion-in-bitcoin?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_ja_bitcoin) |

<details>
<summary>最初のバックテストの手順</summary>

1. 例を開き、無料アカウントを作成して、その戦略のコードと結果を閲覧できるようにします。
2. 自分のワークスペースに複製すると、戦略のチャットでバックテストが始まります。
3. 結果とコードを確認します。利用枠を使って、含まれる取引コストと結果への影響をエージェントに質問できます。

追加の調査には残りのエージェント利用枠を使うか、利用枠をチャージできます。
**Backtester** には、月 100 件の戦略閲覧枠、市場データセット、講座、
月 10 ドル分のブラウザエージェント利用枠と、手元の Claude・Codex・Cursor から
MCP 経由で戦略カタログにアクセスする権限が含まれます。
[無料・有料プランを比較](https://paperswithbacktest.com/pricing?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_ja_pricing) ·
[自分の AI アシスタントを接続](https://paperswithbacktest.com/docs/mcp/?utm_source=github&utm_medium=referral&utm_campaign=awesome_systematic_trading&utm_content=readme_ja_mcp)

</details>

<!-- omit in toc -->

### ここで見つかるもの

- リサーチとライブトレーディング向けの [103のライブラリ・パッケージ](#ライブラリとパッケージ)。停止済み・休止中のプロジェクトには印を付けています
- 公開論文からの [戦略](#戦略)。それぞれの売買ルールと実行可能な Python 付き
- 初心者からプロ向けの [55冊の書籍](#書籍)
- [22本の動画](#動画) とインタビュー
- また [ブログ](#ブログ) や [コース](#コース) も掲載

<!-- omit in toc -->

### 複製結果はどう見えるか

これらの論文のうち 4,843 本をコード化し、それぞれの全期間で実行しました。実装する戦略を選ぶ前に、
知っておく価値のある数字がいくつかあります。

- 複製結果の**シャープレシオ中央値は 0.37**、**t 値 1.96 を超えるのは 48%** です。
  つまり公開された文献の半分は、自身のサンプル上でゼロと区別できません。
- 検証期間の中央値は **34 年**。戦略が自らを証明するにはおおよそ `(1.96 / シャープレシオ)²` 年が
  必要で、シャープレシオ 0.4 なら約 24 年かかります。
- 戦略の S&P 500 に対する**ベータ中央値は +0.17**。これを取り除くと情報比率の中央値は **0.21** まで
  下がります。公開された超過収益のかなりの部分は、技量ではなく指数エクスポージャーだということです。
- 公表日の前後に記録がある 2,838 本の論文では、市場環境を調整したうえで**公表後の減衰は測定できません**
  でした。誤差は年あたり 0.2 パーセントポイント以内です。

手法と注意点は[ウィキ](https://paperswithbacktest.com/wiki)にまとめています。


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
  - [株式](#株式)
  - [債券](#債券)
  - [コモディティ](#コモディティ)
  - [通貨](#通貨)
  - [暗号資産](#暗号資産)
  - [デリバティブ](#デリバティブ)
  - [マルチアセット](#マルチアセット)
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

_トレーディングボット、バックテスター、インジケーター、プライサーなどを実装した **103のライブラリ・パッケージ** のリストです。各ライブラリはプログラミング言語ごとに分類され、人気順（スター数の降順）に並んでいます。_

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
| [pwb-toolbox](https://github.com/paperswithbacktest/pwb-toolbox) | Hugging Face 上の Papers With Backtest データセット 32 件のローダー。株式・ETF・指数・通貨・コモディティの 1962 年からの日次価格、国債イールドカーブ、四半期財務諸表、FRED-MD マクロ系列、そして米国株の1 分足 57 億行。カードとスキーマは誰でも読めますが、ダウンロードには承認が必要です。 | ![GitHub stars](https://badgen.net/github/stars/paperswithbacktest/pwb-toolbox) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

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

*以下の各項目は、公開された論文をコード化し、その全期間で実行したものです。表は公開カタログから [`scripts/build_strategies_table.py`](./scripts/build_strategies_table.py) が生成するため、カタログが動けば一覧も動きます。*

<!-- STRATEGIES:START - generated by scripts/build_strategies_table.py -->

*公開済みの戦略 84 件を、資産クラスごとに最大 12 件、アルファベット順に掲載しています。各リンクから Papers With Backtest 上の論文、その売買ルール、Python コードを開けます。*

## 株式

| 戦略 | コードとバックテスト |
|---|---|
| 1/N | [開く](https://paperswithbacktest.com/strategies/n) |
| 130/30 investing: just another hype or here to stay? | [開く](https://paperswithbacktest.com/strategies/investing-just-another-hype-or-here-to-stay) |
| 25 years of Dutch IPOs | [開く](https://paperswithbacktest.com/strategies/years-of-dutch-ipos) |
| 4-Factor Model for Overnight Returns | [開く](https://paperswithbacktest.com/strategies/4-factor-model-for-overnight-returns) |
| 50 Years in PEAD Research | [開く](https://paperswithbacktest.com/strategies/years-in-pead-research) |
| A Backtesting Protocol in the Era of Machine Learning | [開く](https://paperswithbacktest.com/strategies/a-backtesting-protocol-in-the-era-of-machine-learning) |
| A Behavioral Factor Model for China A-share Market | [開く](https://paperswithbacktest.com/strategies/a-behavioral-factor-model-for-china-a-share-market) |
| A Better Three-Factor Model That Explains More Anomalies | [開く](https://paperswithbacktest.com/strategies/a-better-three-factor-model-that-explains-more-anomalies) |
| A Case Study in Multiperiod Portfolio Optimization: A Classic Problem Revisited | [開く](https://paperswithbacktest.com/strategies/a-case-study-in-multiperiod-portfolio-optimization-a-classic-problem-revisited) |
| A closed-form solution for optimal mean-reverting trading strategies | [開く](https://paperswithbacktest.com/strategies/a-closed-form-solution-for-optimal-mean-reverting-trading-strategies) |
| A Combined Signal Approach to Technical Analysis On | [開く](https://paperswithbacktest.com/strategies/a-combined-signal-approach-to-technical-analysis-on) |
| A comparative analysis of ability of mimicking portfolios in representing the background factors | [開く](https://paperswithbacktest.com/strategies/a-comparative-analysis-of-ability-of-mimicking-portfolios-in-representing-the-background-factors) |

## 債券

| 戦略 | コードとバックテスト |
|---|---|
| A comparison of the historical performance of rolling bond ladders and bond index funds | [開く](https://paperswithbacktest.com/strategies/a-comparison-of-the-historical-performance-of-rolling-bond-ladders-and-bond-index-funds) |
| A Credit-Based Theory of the Currency Risk Premium | [開く](https://paperswithbacktest.com/strategies/a-credit-based-theory-of-the-currency-risk-premium) |
| A Frequency-Specific Factorization to Identify Commonalities with an Application to the European Bond Markets | [開く](https://paperswithbacktest.com/strategies/a-frequency-specific-factorization-to-identify-commonalities-with-an-application-to-the-european-bond-markets) |
| A Key Rate Approach to Replicating Annuities with U.S. Treasury Funds | [開く](https://paperswithbacktest.com/strategies/a-key-rate-approach-to-replicating-annuities-with-u-s-treasury-funds) |
| A research-based approach to fixed income factor portfolio implementation | [開く](https://paperswithbacktest.com/strategies/a-research-based-approach-to-fixed-income-factor-portfolio-implementation) |
| A Sharper Angle on Optimization | [開く](https://paperswithbacktest.com/strategies/a-sharper-angle-on-optimization) |
| A Study on the Effectiveness of China Bond Market ESG Investment Practice | [開く](https://paperswithbacktest.com/strategies/a-study-on-the-effectiveness-of-china-bond-market-esg-investment-practice) |
| An agent-based model of dynamics in corporate bond trading | [開く](https://paperswithbacktest.com/strategies/an-agent-based-model-of-dynamics-in-corporate-bond-trading) |
| Are Bond Returns Predictable with Real-Time Macro Data? | [開く](https://paperswithbacktest.com/strategies/are-bond-returns-predictable-with-real-time-macro-data) |
| Are there pricing spillovers within ETFs? Evidence from Emerging Market Corporate Bonds | [開く](https://paperswithbacktest.com/strategies/are-there-pricing-spillovers-within-etfs-evidence-from-emerging-market-corporate-bonds) |
| Asymmetric Violations of the Spanning Hypothesis | [開く](https://paperswithbacktest.com/strategies/asymmetric-violations-of-the-spanning-hypothesis) |
| Banks’ exposure to interest rate risk, their earnings from term transformation, and the dynamics of the term structure | [開く](https://paperswithbacktest.com/strategies/banks-exposure-to-interest-rate-risk-their-earnings-from-term-transformation-and-the-dynamics-of-the-term-structure) |

## コモディティ

| 戦略 | コードとバックテスト |
|---|---|
| A Trend Factor in Commodity Futures Markets: Any Economic Gains from Using Information over Investment Horizons? | [開く](https://paperswithbacktest.com/strategies/a-trend-factor-in-commodity-futures-markets-any-economic-gains-from-using-information) |
| Alternative Beta Strategies in Commodities | [開く](https://paperswithbacktest.com/strategies/alternative-beta-strategies-in-commodities) |
| Decomposing Alpha in a Machine-Learning Gold Timing System: Trend Following, Forecast Quality, and the Cost of Look-Ahead Bias | [開く](https://paperswithbacktest.com/strategies/decomposing-alpha-in-a-machine-learning-gold-timing-system-trend-following-forecast) |
| Diversification Return, Portfolio Rebalancing, and the Commodity Return Puzzle | [開く](https://paperswithbacktest.com/strategies/diversification-return-portfolio-rebalancing-and-the-commodity-return-puzzle) |
| Dynamic Regime Strategy for Stress Testing and Optimizing Institutional Investor Portfolios | [開く](https://paperswithbacktest.com/strategies/dynamic-regime-strategy-for-stress-testing-and-optimizing-institutional-investor-port) |
| Ensembling ARIMAX Model in Algorithmic Investment Strategies on Commodities Market | [開く](https://paperswithbacktest.com/strategies/ensembling-arimax-model-in-algorithmic-investment-strategies-on-commodities-market) |
| Financialization and Commodity Markets Serial Dependence | [開く](https://paperswithbacktest.com/strategies/financialization-and-commodity-markets-serial-dependence) |
| Forecasting Crude Oil Prices: Does Global Financial Uncertainty Matter? | [開く](https://paperswithbacktest.com/strategies/forecasting-crude-oil-prices-does-global-financial-uncertainty-matter) |
| Forecasting Real Oil Returns Using a Deep Forest Ensemble Approach | [開く](https://paperswithbacktest.com/strategies/forecasting-real-oil-returns-using-a-deep-forest-ensemble-approach) |
| Gold and Oil Prices: Abnormal Returns, Momentum and Contrarian Effects | [開く](https://paperswithbacktest.com/strategies/gold-and-oil-prices-abnormal-returns-momentum-and-contrarian-effects) |
| How Do Portfolio Weighting Schemes Affect Commodity Futures Risk Premia? | [開く](https://paperswithbacktest.com/strategies/miffre-faff-how-do-portfolio-weighting-schemes-affect-commodity-futures-risk-premia) |
| How to Improve Commodity Momentum Using Intra-Market Correlation | [開く](https://paperswithbacktest.com/strategies/how-to-improve-commodity-momentum-using-intra-market-correlation) |

## 通貨

| 戦略 | コードとバックテスト |
|---|---|
| A Habit-Based Explanation of the Exchange Rate Risk Premium | [開く](https://paperswithbacktest.com/strategies/a-habit-based-explanation-of-the-exchange-rate-risk-premium) |
| A Hamiltonian Phase-Space Approach to Foreign Exchange: Physics-Based Predictive Distributions without Curve Fitting | [開く](https://paperswithbacktest.com/strategies/a-hamiltonian-phase-space-approach-to-foreign-exchange-physics-based-predictive-distributions-without-curve-fitting) |
| A Liquidity-Based Resolution of the Uncovered Interest Parity Puzzle | [開く](https://paperswithbacktest.com/strategies/a-liquidity-based-resolution-of-the-uncovered-interest-parity-puzzle) |
| A Low-Risk Strategy based on Higher Moments in Currency Markets | [開く](https://paperswithbacktest.com/strategies/a-low-risk-strategy-based-on-higher-moments-in-currency-markets) |
| A Multi-Strategy Approach to Trading Foreign Exchange Futures | [開く](https://paperswithbacktest.com/strategies/a-multi-strategy-approach-to-trading-foreign-exchange-futures) |
| A Test of Momentum Trading Strategies in Foreign Exchange Markets | [開く](https://paperswithbacktest.com/strategies/a-test-of-momentum-trading-strategies-in-foreign-exchange-markets-evidence-from-the-g) |
| Algorithmic Trading Model for Manifold Learning in FX | [開く](https://paperswithbacktest.com/strategies/algorithmic-trading-model-for-manifold-learning-in-fx) |
| Alpha Asymmetry in Foreign Exchange Markets An Investigation of Exploitability | [開く](https://paperswithbacktest.com/strategies/alpha-asymmetry-in-foreign-exchange-markets-an-investigation-of-exploitability) |
| An Interpretation of Carry Trade Profitability | [開く](https://paperswithbacktest.com/strategies/an-interpretation-of-carry-trade-profitability) |
| Analyst Forecasts and Currency Markets | [開く](https://paperswithbacktest.com/strategies/analyst-forecasts-and-currency-markets) |
| ANANTA: A Systematic Quantitative FX Trading Strategy | [開く](https://paperswithbacktest.com/strategies/a-systematic-quantitative-fx-trading-strategy) |
| Anatomy of Alpha Illusion in Daily FX Markets | [開く](https://paperswithbacktest.com/strategies/anatomy-of-alpha-illusion-in-daily-fx-markets) |

## 暗号資産

| 戦略 | コードとバックテスト |
|---|---|
| A Filtered-Label Calibrated XGBoost Framework with Walk-Forward Validation for Robust Bitcoin Direction Prediction | [開く](https://paperswithbacktest.com/strategies/a-filtered-label-calibrated-xgboost-framework-with-walk-forward-validation-for-robust) |
| A Prospect Theory Model for Predicting Cryptocurrency Returns | [開く](https://paperswithbacktest.com/strategies/a-prospect-theory-model-for-predicting-cryptocurrency-returns) |
| Algorithmic Predatory Equilibrium: Multi-Agent Reinforcement Learning and Market Manipulation in Decentralized Finance | [開く](https://paperswithbacktest.com/strategies/algorithmic-predatory-equilibrium-multi-agent-reinforcement-learning-and-market-manipulation-in-decentralized-finance) |
| Analysis of an Algo Trading Strategy Based on the Kaufman Adaptive Moving Average (KAMA) and Statistical Validation Using Bootstrap and Bayesian Optimization | [開く](https://paperswithbacktest.com/strategies/analysis-of-an-algo-trading-strategy-based-on-the-kaufman-adaptive-moving-average-kama-and-statistical-validation-using-bootstrap-and-bayesian-optimization) |
| Backtesting of Algorithmic Cryptocurrency Trading Strategies | [開く](https://paperswithbacktest.com/strategies/backtesting-of-algorithmic-cryptocurrency-trading-strategies) |
| Behavioral Anomalies in Cryptocurrency Markets | [開く](https://paperswithbacktest.com/strategies/behavioral-anomalies-in-cryptocurrency-markets) |
| Bitcoin Price Dynamics: The Stark Contrast between P2P and Exchange Trading | [開く](https://paperswithbacktest.com/strategies/bitcoin-price-dynamics-the-stark-contrast-between-p-p-and-exchange-trading) |
| Bitcoin: Speculative Asset or Innovative Technology? | [開く](https://paperswithbacktest.com/strategies/bitcoin-speculative-asset-or-innovative-technology) |
| Bitcoin: Systematic Force of Cryptocurrency Portfolio | [開く](https://paperswithbacktest.com/strategies/bitcoin-systematic-force-of-cryptocurrency-portfolio) |
| Common risk factors in the returns on cryptocurrencies | [開く](https://paperswithbacktest.com/strategies/common-risk-factors-in-the-returns-on-cryptocurrencies) |
| Constant Harmonic Market Maker A Way to Address Impermanent Loss | [開く](https://paperswithbacktest.com/strategies/constant-harmonic-market-maker-a-way-to-address-impermanent-loss) |
| Constructing Cointegrated Cryptocurrency Portfolios for Statistical Arbitrage | [開く](https://paperswithbacktest.com/strategies/constructing-cointegrated-cryptocurrency-portfolios-for-statistical-arbitrage) |

## デリバティブ

| 戦略 | コードとバックテスト |
|---|---|
| A Derivatives Trading Recommendation System: the Mid-Curve Calendar Spread Case | [開く](https://paperswithbacktest.com/strategies/a-derivatives-trading-recommendation-system-the-mid-curve-calendar-spread-case) |
| A Leveraged Portfolio Management Approach Applying The CBOE Russell 2000 PutWrite Index | [開く](https://paperswithbacktest.com/strategies/a-leveraged-portfolio-management-approach-applying-the-cboe-russell-putwrite-index) |
| A semiparametric factor model for CDO surfaces dynamics | [開く](https://paperswithbacktest.com/strategies/a-semiparametric-factor-model-for-cdo-surfaces-dynamics) |
| A Spectral Decomposition of the Credit Default Swap Indices | [開く](https://paperswithbacktest.com/strategies/a-spectral-decomposition-of-the-credit-default-swap-indices) |
| A Theory of Model Sophistication and Operational Risk | [開く](https://paperswithbacktest.com/strategies/a-theory-of-model-sophistication-and-operational-risk) |
| A transaction data study of the forward bias puzzle | [開く](https://paperswithbacktest.com/strategies/a-transaction-data-study-of-the-forward-bias-puzzle) |
| A “Bad Beta, Good Beta” Anatomy of Currency Risk Premiums and Trading Strategies | [開く](https://paperswithbacktest.com/strategies/a-bad-beta-good-beta-anatomy-of-currency-risk-premiums-and-trading-strategies) |
| An Integrated Approach to Currency Factor Investing | [開く](https://paperswithbacktest.com/strategies/an-integrated-approach-to-currency-factor-investing) |
| An intraday trend-following trading strategy on equity derivatives in India | [開く](https://paperswithbacktest.com/strategies/an-intraday-trend-following-trading-strategy-on-equity-derivatives-in-india) |
| Analise do Desempenho de Regras da Analise Tecnica Aplicada ao Mercado Intradiario do Contrato Futuro do Indice Ibovespa | [開く](https://paperswithbacktest.com/strategies/analise-do-desempenho-de-regras-da-analise-tecnica-aplicada-ao-mercado-intradiario-do-contrato-futuro-do-indice-ibovespa) |
| Anchoring Credit Default Swap Spreads to Firm Fundamentals | [開く](https://paperswithbacktest.com/strategies/anchoring-credit-default-swap-spreads-to-firm-fundamentals) |
| Approximate Hedging of Contingent Claims under Transaction Costs for General Pay-offs | [開く](https://paperswithbacktest.com/strategies/approximate-hedging-of-contingent-claims-under-transaction-costs-for-general-pay-offs) |

## マルチアセット

| 戦略 | コードとバックテスト |
|---|---|
| 0DTE Asset Pricing | [開く](https://paperswithbacktest.com/strategies/dte-asset-pricing) |
| 0DTE option pricing | [開く](https://paperswithbacktest.com/strategies/dte-option-pricing) |
| 0DTE Trading Rules | [開く](https://paperswithbacktest.com/strategies/dte-trading-rules) |
| 0DTEs: Trading, Gamma Risk and Volatility Propagation | [開く](https://paperswithbacktest.com/strategies/dtes-trading-gamma-risk-and-volatility-propagation) |
| 1/N and Long Run Optimal Portfolios: Results for Mixed Asset Menus | [開く](https://paperswithbacktest.com/strategies/n-and-long-run-optimal-portfolios-results-for-mixed-asset-menus) |
| 150 Years of Return Predictability Around the World: A Holistic View Across Assets | [開く](https://paperswithbacktest.com/strategies/years-of-return-predictability-around-the-world-a-holistic-view-across-assets) |
| 151 Trading Strategies | [開く](https://paperswithbacktest.com/strategies/trading-strategies) |
| 1998 Pricing Performance of Market Advisory Services for Corn and Soybeans | [開く](https://paperswithbacktest.com/strategies/pricing-performance-of-market-advisory-services-for-corn-and-soybeans) |
| 1999 Pricing Performance of Market Advisory Services for Corn and Soybeans | [開く](https://paperswithbacktest.com/strategies/pricing-performance-of-market-advisory-services-for-corn-and-soybeans-1) |
| 20 Myths About Long-Short | [開く](https://paperswithbacktest.com/strategies/myths-about-long-short) |
| A Bayesian Approach to Detecting Nonlinear Risk Exposures in Hedge | [開く](https://paperswithbacktest.com/strategies/a-bayesian-approach-to-detecting-nonlinear-risk-exposures-in-hedge) |
| A Bayesian Stochastic Discount Factor for the Cross-Section of Individual Equity Options | [開く](https://paperswithbacktest.com/strategies/a-bayesian-stochastic-discount-factor-for-the-cross-section-of-individual-equity-options) |

<!-- STRATEGIES:END -->

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
