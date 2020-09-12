import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
print(stock)

start_year=2020
start_month=1
start_day=1

start = dt.datetime(start_year, start_month, start_day)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

#print(df)

ma = 50

smaString = "Sma_" + str(ma)

df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

#print(df)

df = df.iloc[ma:]

#print(df)

numH=0
numC=0

for i in df.index:
    if(df["Adj Close"][i]>df[smaString][i]):
        print("The close is higher")
        numH += 1
    else:
        print("The close is lower")
        numC += 1

print(str(numH))
print(str(numC))

