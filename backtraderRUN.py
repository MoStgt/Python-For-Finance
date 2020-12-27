import backtrader as bt
import os, sys, argparse
from Strategies.GoldenCross import GoldenCross
from Strategies.BuyHold import BuyHold
import pandas as pd


strategies = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyHold
}
parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="which strategy to run", type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("Invalid strategy, must be one of {}".format(strategies.keys()))
    sys.exit()

cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000000)

spy_prices=pd.read_csv('data/spy.csv', index_col='date', parse_dates=True)

feed=bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)


cerebro.addstrategy(strategies[args.strategy])

cerebro.run()

cerebro.plot()
