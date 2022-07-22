"""
Buy and hold strategy
"""
from datetime import datetime
import multiprocessing

import click
import matplotlib.pyplot as plt
import pandas as pd
import pytz
from trading import (
    BacktestEngine,
    StrategyBase,
    TickEvent,
)
from trading.data_loader import (
    load_futures_chain,
    load_futures_hist_prices,
    load_futures_meta,
)
import trading.performance.plot as perf_plot
import trading.performance.metrics as perf_metrics


class BuyAndHoldStrategy(StrategyBase):
    """
    Buy and hold strategy.
    """

    def __init__(
        self,
        symbol: str,
        n_roll_ahead: int = 0,  # 0 is last day roll, 1 is penultimate day, and so on
        n_rollout: int = 0,  # 0 is front month, 1 is second month, and so on
    ):
        super().__init__()
        self.n_roll_ahead = n_roll_ahead
        self.n_rollout = n_rollout
        self.sym = symbol
        self.current_time = None
        self.df_meta = load_futures_meta(ticker=self.sym)
        self.holding_contract = None

    def on_tick(self, tick_event: TickEvent):
        """
        Front_contract decides when to roll
        if not roll ==> if no holding_contract, buy rollout_contract; else do nothing
        if roll ==> if no holding_contract, buy rollin contract (rollout+1);
        else sell rollout, buy rollin contract

        Parameters
        ----------
            tick_event: TickEvent
                Tick event.
        """
        super().on_tick(tick_event)
        self.current_time = tick_event.timestamp
        df_time_idx = self._data_board.get_hist_time_index()

        df_live_futures = load_futures_chain(
            ticker=self.sym, asofdate=self.current_time.replace(tzinfo=None)
        )  # remove tzinfo
        rollout_contract = df_live_futures.index[self.n_rollout]
        rollin_contract = df_live_futures.index[self.n_rollout + 1]
        exp_date = pytz.timezone("US/Eastern").localize(
            df_live_futures.LTD[0]
        )  # front contract
        dte = df_time_idx.searchsorted(exp_date) - df_time_idx.searchsorted(
            self.current_time
        )  # 0 is expiry date

        if self.n_roll_ahead < dte:  # not ready to roll
            if self.holding_contract is None:  # empty
                print(f"{self.current_time}, dte {dte}, buy {rollout_contract}")
                self.adjust_position(
                    rollout_contract,
                    size_from=0,
                    size_to=1,
                    timestamp=self.current_time,
                )
                self.holding_contract = rollout_contract
        else:
            if self.holding_contract is None:  # empty
                print(f"{self.current_time}, dte {dte}, buy {rollin_contract}")
                self.adjust_position(
                    rollin_contract, size_from=0, size_to=1, timestamp=self.current_time
                )
                self.holding_contract = rollin_contract
            else:
                if (
                    self.holding_contract == rollin_contract
                ):  # already rolled this month
                    pass
                else:
                    print(
                        f"{self.current_time}, dte {dte}, roll {rollout_contract} {rollin_contract}"
                    )
                    self.adjust_position(
                        rollout_contract,
                        size_from=1,
                        size_to=0,
                        timestamp=self.current_time,
                    )
                    self.adjust_position(
                        rollin_contract,
                        size_from=0,
                        size_to=1,
                        timestamp=self.current_time,
                    )
                    self.holding_contract = rollin_contract


def parameter_search(
    symbol: str,
    init_capital: float,
    start_date: datetime,
    end_date: datetime,
    df_data: pd.DataFrame,
    params: dict,
    target_name: str,
    return_dict: dict,
):
    """
    This function should be the same for all strategies.
    The only reason not included in systematic-trading is because of
    its dependency on pyfolio (to get perf_stats)

    Parameters
    ----------
        symbol: str
            Future ticker.

        init_capital: float
            Initial capital.

        start_date: datetime
            Start date.

        end_date: datetime
            End date.

        df_data: pd.DataFrame
            Dataframe of futures prices.

        params: dict
            Parameters for the strategy.

        target_name: str
            Name of the target.

        return_dict: dict
            Dictionary to store the results.
    """
    # pylint: disable=too-many-arguments
    strategy = BuyAndHoldStrategy(symbol=symbol)
    strategy.set_capital(init_capital)
    strategy.set_symbols([symbol])
    engine = BacktestEngine(start_date, end_date)
    engine.set_capital(init_capital)  # capital or portfolio >= capital for one strategy
    engine.add_data(symbol, df_data)
    strategy.set_params(
        {"n_roll_ahead": params["n_roll_ahead"], "n_rollout": params["n_rollout"]}
    )
    engine.set_strategy(strategy)
    ds_equity, _, _ = engine.run()
    try:
        strat_ret = ds_equity.pct_change().dropna()
        perf_stats_strat = perf_plot.timeseries.perf_stats(strat_ret)
        target_value = perf_stats_strat.loc[target_name]  # first table in tuple
    except KeyError:
        target_value = 0
    return_dict[(params["n_roll_ahead"], params["n_rollout"])] = target_value


@click.command()
@click.option("--mode", default=None)
def main(mode: str) -> None:
    # pylint: disable=too-many-locals,too-many-statements,undefined-variable
    """
    Main function.

    Parameters
    ----------
        mode: str
            Either backtest, optimize.
    """
    ticker = "ES"
    init_capital = 100_000.0
    df_future = load_futures_hist_prices(ticker=ticker)
    df_future.index = pd.to_datetime(df_future.index)
    df_future.index = df_future.index.tz_localize("US/Eastern")
    test_start_date = datetime(1990, 1, 1, 0, 0, 0, 0, pytz.timezone("US/Eastern"))
    test_end_date = datetime(2022, 7, 7, 0, 0, 0, 0, pytz.timezone("US/Eastern"))
    init_capital = 50.0
    if mode == "backtest":
        strategy = BuyAndHoldStrategy(symbol=ticker)
        strategy.set_capital(init_capital)
        strategy.set_symbols([ticker])
        strategy.set_params({"n_roll_ahead": 0, "n_rollout": 0})

        # Create a Data Feed
        backtest_engine = BacktestEngine(test_start_date, test_end_date)
        backtest_engine.set_capital(
            init_capital
        )  # capital or portfolio >= capital for one strategy
        backtest_engine.add_data(ticker, df_future)
        backtest_engine.set_strategy(strategy)
        ds_equity, df_positions, df_trades = backtest_engine.run()

        # ------------------------- Evaluation and Plotting -------------------------------------- #
        strat_ret = ds_equity.pct_change().dropna()
        strat_ret.name = "strat"
        benchmark_ret = strat_ret.copy()
        benchmark_ret.name = "benchmark"

        perf_stats_strat = perf_plot.timeseries.perf_stats(strat_ret)
        perf_stats_all = perf_stats_strat
        perf_stats_bm = perf_plot.timeseries.perf_stats(benchmark_ret)
        perf_stats_all = pd.concat([perf_stats_strat, perf_stats_bm], axis=1)
        perf_stats_all.columns = ["Strategy", "Benchmark"]

        drawdown_table = perf_plot.timeseries.gen_drawdown_table(strat_ret, 5)
        monthly_ret_table = perf_metrics.aggregate_returns(strat_ret, "monthly")
        monthly_ret_table = monthly_ret_table.unstack().round(3)
        ann_ret_df = pd.DataFrame(perf_metrics.aggregate_returns(strat_ret, "yearly"))
        ann_ret_df = ann_ret_df.unstack().round(3)

        print("-------------- PERFORMANCE ----------------")
        print(perf_stats_all)
        print("-------------- DRAWDOWN ----------------")
        print(drawdown_table)
        print("-------------- MONTHLY RETURN ----------------")
        print(monthly_ret_table)
        print("-------------- ANNUAL RETURN ----------------")
        print(ann_ret_df)

        perf_plot.create_full_tear_sheet(
            strat_ret,
            benchmark_rets=benchmark_ret,
            positions=df_positions,
            transactions=df_trades,
            round_trips=False,
        )
        plt.show()
    elif mode == "optimize":
        params_list = []
        for n_roll_ahead in range(20):
            for n_rollout in range(5):
                params_list.append(
                    {"n_roll_ahead": n_roll_ahead, "n_rollout": n_rollout}
                )
        target_name = "Sharpe ratio"
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        jobs = []
        for params in params_list:
            job = multiprocessing.Process(
                target=parameter_search,
                args=(
                    ticker,
                    init_capital,
                    test_start_date,
                    test_end_date,
                    df_future,
                    params,
                    target_name,
                    return_dict,
                ),
            )
            jobs.append(job)
            job.start()

        for proc in jobs:
            proc.join()
        for key, value in return_dict.items():
            print(key, value)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
