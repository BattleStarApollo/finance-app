import sys

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt


# ticker = 'SPX'
# size = 'compact'

def GetData(ticker, size):
    ts = TimeSeries(key='G9RVRT562GWL8YZB', output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize=size)
    return data, meta_data

# data, meta_data = GetData(ticker, size)
# print(data['close'])
