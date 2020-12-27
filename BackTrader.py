import backtrader
import datetime
from BacktraderStrategies import TestStrategy

cerebro = backtrader.Cerebro()
cerebro.broker.set_cash(1000000)

data=backtrader.feeds.YahooFinanceCSVData(
    dataname='oracle.csv',
    #Do not pass values before this date
    fromdate=datetime.datetime(2000,1,1),
    #Do not pass values after this date
    todate=datetime.datetime(2000,12,31),
    reverse=False)
cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()
