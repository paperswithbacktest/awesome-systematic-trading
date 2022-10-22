# https://quantpedia.com/strategies/term-structure-effect-in-commodities/
#
# This simple strategy buys each month the 20% of commodities with the highest roll-returns and shorts the 20% of commodities with the lowest 
# roll-returns and holds the long-short positions for one month. The contracts in each quintile are equally-weighted. 
# The investment universe is all commodity futures contracts.
#
# QC implementation:

import numpy as np
from datetime import time
from AlgorithmImports import *

class TermStructure(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2009, 1, 1)
        self.SetCash(100000)

        symbols = {
                        'CME_S1': Futures.Grains.Soybeans,
                        'CME_W1' : Futures.Grains.Wheat,
                        'CME_SM1' : Futures.Grains.SoybeanMeal,
                        'CME_C1' : Futures.Grains.Corn,
                        'CME_O1' : Futures.Grains.Oats,
                        'CME_LC1' : Futures.Meats.LiveCattle,
                        'CME_FC1' : Futures.Meats.FeederCattle,
                        'CME_LN1' : Futures.Meats.LeanHogs,
                        'CME_GC1' : Futures.Metals.Gold,
                        'CME_SI1' : Futures.Metals.Silver,
                        'CME_PL1' : Futures.Metals.Platinum,

                        'CME_HG1' : Futures.Metals.Copper,
                        'CME_LB1' : Futures.Forestry.RandomLengthLumber,
                        'CME_NG1' : Futures.Energies.NaturalGas,
                        'CME_PA1' : Futures.Metals.Palladium,
                        'CME_DA1' : Futures.Dairy.ClassIIIMilk,
                        
                        'CME_RB1' : Futures.Energies.Gasoline,
                        'ICE_WT1' : Futures.Energies.CrudeOilWTI,
                        'ICE_CC1' : Futures.Softs.Cocoa,
                        'ICE_O1' : Futures.Energies.HeatingOil,
                        'ICE_SB1' : Futures.Softs.Sugar11CME,
                        }
    
        self.futures_info:dict = {}
        self.quantile:int = 5
        self.min_expiration_days:int = 2
        self.max_expiration_days:int = 360
        
        self.price_data:dict[Symbol, RollingWindow] = {}
        self.period:int = 60
        self.SetWarmup(self.period, Resolution.Daily)
        
        for qp_symbol, qc_future in symbols.items():
            # QP futures
            data:Security = self.AddData(QuantpediaFutures, qp_symbol, Resolution.Daily)
            data.SetFeeModel(CustomFeeModel())
            data.SetLeverage(5)
            self.price_data[data.Symbol] = RollingWindow[float](self.period)
            
            # QC futures
            future:Future = self.AddFuture(qc_future, Resolution.Daily, dataNormalizationMode=DataNormalizationMode.Raw)
            future.SetFilter(timedelta(days=self.min_expiration_days), timedelta(days=self.max_expiration_days))
            self.futures_info[future.Symbol.Value] = FuturesInfo(data.Symbol)
        
        self.recent_month:int = -1

    def find_and_update_contracts(self, futures_chain, symbol) -> None:
        near_contract:FuturesContract = None
        dist_contract:FuturesContract = None

        if symbol in futures_chain:
            contracts:list = [contract for contract in futures_chain[symbol] if contract.Expiry.date() > self.Time.date()]

            if len(contracts) >= 2:
                contracts:list = sorted(contracts, key=lambda x: x.Expiry, reverse=False)
                near_contract = contracts[0]
                dist_contract = contracts[1]

        self.futures_info[symbol].update_contracts(near_contract, dist_contract)

    def OnData(self, data):
        if data.FutureChains.Count > 0:
            for symbol, futures_info in self.futures_info.items():
                # check if near contract is expired or is not initialized
                if not futures_info.is_initialized() or \
                    (futures_info.is_initialized() and futures_info.near_contract.Expiry.date() == self.Time.date()):
                    self.find_and_update_contracts(data.FutureChains, symbol)
        
        roll_return:dict[Symbol, float] = {}
        rebalance_flag:bool = False

        # roll return calculation
        for symbol, futures_info in self.futures_info.items():
            # futures data is present in the algorithm
            if futures_info.quantpedia_future in data and data[futures_info.quantpedia_future]:
                # store daily data
                self.price_data[futures_info.quantpedia_future].Add(data[futures_info.quantpedia_future].Value)
                if not self.price_data[futures_info.quantpedia_future].IsReady:
                    continue

                # new month rebalance
                if self.Time.month != self.recent_month and not self.IsWarmingUp:
                    self.recent_month = self.Time.month
                    rebalance_flag = True

                if rebalance_flag:
                    if futures_info.is_initialized():
                        near_c:FuturesContract = futures_info.near_contract
                        dist_c:FuturesContract = futures_info.distant_contract
                        if self.Securities.ContainsKey(near_c.Symbol) and self.Securities.ContainsKey(dist_c.Symbol):
                            raw_price1:float = self.Securities[near_c.Symbol].Close * self.Securities[symbol].SymbolProperties.PriceMagnifier
                            raw_price2:float = self.Securities[dist_c.Symbol].Close * self.Securities[symbol].SymbolProperties.PriceMagnifier

                            if raw_price1 != 0 and raw_price2 != 0:
                                roll_return[futures_info.quantpedia_future] = raw_price1 / raw_price2 - 1

        if rebalance_flag:
            weights:dict[Symbol, float] = {}
            
            long:list[Symbol] = []
            short:list[Symbol] = []
            if len(roll_return) >= self.quantile:

                # roll return sorting
                sorted_by_roll:list = sorted(roll_return.items(), key = lambda x: x[1], reverse=True)
                quantile:int = int(len(sorted_by_roll) / self.quantile)
                long = [x[0] for x in sorted_by_roll[:quantile]]
                short = [x[0] for x in sorted_by_roll[-quantile:]]

            # trade execution
            invested:list[Symbol] = [x.Key for x in self.Portfolio if x.Value.Invested]
            for symbol in invested:
                if symbol not in long + short:
                    self.Liquidate(symbol)

            for symbol in long:
                self.SetHoldings(symbol, 1 / len(long))
            
            for symbol in short:
                self.SetHoldings(symbol, -1 / len(short))

class FuturesInfo():
    def __init__(self, quantpedia_future:Symbol) -> None:
        self.quantpedia_future:Symbol = quantpedia_future
        self.near_contract:FuturesContract = None
        self.distant_contract:FuturesContract = None
    
    def update_contracts(self, near_contract:FuturesContract, distant_contract:FuturesContract) -> None:
        self.near_contract = near_contract
        self.distant_contract = distant_contract
    
    def is_initialized(self) -> bool:
        return self.near_contract is not None and self.distant_contract is not None
    
# Custom fee model.
class CustomFeeModel():
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))

# Quantpedia data.
# NOTE: IMPORTANT: Data order must be ascending (datewise)
class QuantpediaFutures(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource("data.quantpedia.com/backtesting_data/futures/{0}.csv".format(config.Symbol.Value), SubscriptionTransportMedium.RemoteFile, FileFormat.Csv)

    def Reader(self, config, line, date, isLiveMode):
        data = QuantpediaFutures()
        data.Symbol = config.Symbol
        
        if not line[0].isdigit(): return None
        split = line.split(';')
        
        data.Time = datetime.strptime(split[0], "%d.%m.%Y") + timedelta(days=1)
        data['back_adjusted'] = float(split[1])
        data['spliced'] = float(split[2])
        data.Value = float(split[1])

        return data