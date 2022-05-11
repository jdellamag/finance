# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

# Token Variables (can rename variables but need to keep ticker,period,interval the same)
data1 = yf.download(tickers='BTC-USD', period = '4h', interval = '1h')

data2 = yf.download(tickers='ETH-USD', period = '4h', interval = '1h')

data3 = yf.download(tickers='MATIC-USD', period = '4h', interval = '1h')

print("BTC-USD")
print(data1)
print("ETH-USD")
print(data2)
print("MATIC-USD")
print(data3)







# https://medium.com/analytics-vidhya/python-how-to-get-bitcoin-data-in-real-time-less-than-1-second-lag-38772da43740
