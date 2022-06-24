from datetime import datetime
import hashlib
import os
import pytz

import click
import matplotlib.pyplot as plt
import empyrical as ep
import pandas as pd
import pyfolio as pf
from trading.data.client import Client
from trading.data.constants import FUTURES
from trading.v2 import BacktestEngine
from trading.v2.util import read_data, save_one_run_results
from trading.v2.strategy import StrategyBase


class BuyAndHoldStrategy(StrategyBase):
    """
    buy on the first tick then hold to the end
    """

    def __init__(self):
        super(BuyAndHoldStrategy, self).__init__()
        self.invested = False

    def on_tick(self, event):
        symbol = self.symbols[0]
        if not self.invested:
            df_hist = self._data_board.get_hist_price(symbol, event.timestamp)
            close = df_hist.iloc[-1].Close
            target_size = int(self._position_manager.initial_capital / close)
            self.adjust_position(
                symbol, size_from=0, size_to=target_size, timestamp=event.timestamp
            )
            self.invested = True


@click.command()
@click.option("--mode", default=None)
def main(mode: str) -> None:
    """
    cd $HOME/Documents/quanttraders
    pip install -r requirements.txt
    cd $HOME/Documents/quanttraders/examples
    python buy_and_hold_strategy.py --mode download
    python buy_and_hold_strategy.py --mode backtest
    """
    run_in_jupyter = False
    if mode == "backtest":
        df = read_data(
            filepath="./test.csv", instrument="37241eecabf1e7223b9db07d2c04fe2c"
        )
        print(df)
        init_capital = 100_000.0
        test_start_date = datetime(
            1990, 1, 1, 8, 30, 0, 0, pytz.timezone("America/New_York")
        )
        test_end_date = datetime(
            2022, 6, 24, 6, 0, 0, 0, pytz.timezone("America/New_York")
        )
        strategy = BuyAndHoldStrategy()
        strategy.set_capital(init_capital)
        strategy.set_symbols(["TTT"])
        strategy.set_params(None)

        backtest_engine = BacktestEngine(test_start_date, test_end_date)
        backtest_engine.set_capital(
            init_capital
        )  # capital or portfolio >= capital for one strategy
        backtest_engine.add_data("TTT", df)
        backtest_engine.set_strategy(strategy)
        ds_equity, df_positions, df_trades = backtest_engine.run()
        # save to excel
        save_one_run_results(".", ds_equity, df_positions, df_trades)

        # ------------------------- Evaluation and Plotting -------------------------------------- #
        strat_ret = ds_equity.pct_change().dropna()
        strat_ret.name = "strat"
        # bm = read_ohlcv_csv(os.path.join('../data/', f'{benchmark}.csv'))
        # bm_ret = bm['Close'].pct_change().dropna()
        # bm_ret.index = pd.to_datetime(bm_ret.index)
        # bm_ret = bm_ret[strat_ret.index]
        # bm_ret.name = 'benchmark'
        bm_ret = strat_ret.copy()
        bm_ret.name = "benchmark"
        print(strat_ret)

        perf_stats_strat = pf.timeseries.perf_stats(strat_ret)
        perf_stats_all = perf_stats_strat
        perf_stats_bm = pf.timeseries.perf_stats(bm_ret)
        perf_stats_all = pd.concat([perf_stats_strat, perf_stats_bm], axis=1)
        perf_stats_all.columns = ["Strategy", "Benchmark"]

        drawdown_table = pf.timeseries.gen_drawdown_table(strat_ret, 5)
        monthly_ret_table = ep.aggregate_returns(strat_ret, "monthly")
        monthly_ret_table = monthly_ret_table.unstack().round(3)
        ann_ret_df = pd.DataFrame(ep.aggregate_returns(strat_ret, "yearly"))
        ann_ret_df = ann_ret_df.unstack().round(3)

        print("-------------- PERFORMANCE ----------------")
        print(perf_stats_all)
        print("-------------- DRAWDOWN ----------------")
        print(drawdown_table)
        print("-------------- MONTHLY RETURN ----------------")
        print(monthly_ret_table)
        print("-------------- ANNUAL RETURN ----------------")
        print(ann_ret_df)

        if run_in_jupyter:
            pf.create_full_tear_sheet(
                strat_ret,
                benchmark_rets=bm_ret,
                positions=df_positions,
                transactions=df_trades,
                round_trips=False,
            )
            plt.show()
        else:
            f1 = plt.figure(1)
            pf.plot_rolling_returns(strat_ret, factor_returns=bm_ret)
            f1.show()
            f2 = plt.figure(2)
            pf.plot_rolling_volatility(strat_ret, factor_returns=bm_ret)
            f2.show()
            f3 = plt.figure(3)
            pf.plot_rolling_sharpe(strat_ret)
            f3.show()
            f4 = plt.figure(4)
            pf.plot_drawdown_periods(strat_ret)
            f4.show()
            f5 = plt.figure(5)
            pf.plot_monthly_returns_heatmap(strat_ret)
            f5.show()
            f6 = plt.figure(6)
            pf.plot_annual_returns(strat_ret)
            f6.show()
            f7 = plt.figure(7)
            pf.plot_monthly_returns_dist(strat_ret)
            plt.show()
            f8 = plt.figure(8)
            pf.create_position_tear_sheet(strat_ret, df_positions)
            plt.show()
            f9 = plt.figure(9)
            pf.create_txn_tear_sheet(strat_ret, df_positions, df_trades)
            plt.show()
            f10 = plt.figure(10)
            pf.create_round_trip_tear_sheet(strat_ret, df_positions, df_trades)
            plt.show()
    elif mode == "download":
        hash_key = os.getenv("HASH_KEY")
        original_columns_to_keep = ["Date", "Close"]
        frames = []
        for ticker in FUTURES:
            dfm, _ = Client().get_public_dataset(ticker=ticker)
            if len(dfm) == 0:
                continue
            original_columns = dfm.columns
            dfm.loc[:, "Instrument"] = hashlib.md5(
                (ticker + hash_key).encode()
            ).hexdigest()
            dfm.loc[:, "Close"] = dfm.NavLong / 1e9
            dfm.drop(
                columns=list(set(original_columns) - set(original_columns_to_keep)),
                inplace=True,
            )
            frames.append(dfm)
        dfm = pd.concat(frames)
        dfm.to_csv("test.csv", index=False, sep=",")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
