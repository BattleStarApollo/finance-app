import sys

# import matplotlib.pyplot as plt
#
# ts = TimeSeries(key='G9RVRT562GWL8YZB', output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='VFIFX',interval='60min', outputsize='full')
# data['close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()
#
# from alpha_vantage.globalstockquotes import GlobalStockQuotes
# from pprint import pprint
#
# gsq = GlobalStockQuotes(key='486U')
# data, meta_data = gsq.get_global_quote(symbol="ETR:DB1")
# pprint(data)

# from alpha_vantage.timeseries import TimeSeries
# import matplotlib.pyplot as plt
#
# ts = TimeSeries(key='G9RVRT562GWL8YZB', output_format='pandas')
# data, meta_data = ts.get_daily(symbol='VFIFX', outputsize='full')
# data['close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()


from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np
from datetime import date

def convert_pd_datetime(string):

    year = string[0:4]
    month = string[5:7]
    day = string[8:]
    dt = date(int(year), int(month), int(day))

    return dt


ticker = 'SPX'

duration = ''

begin_time = ''
end_time = ''

ts = TimeSeries(key='G9RVRT562GWL8YZB', output_format='pandas')
data, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='compact')

def return_dates():

    print("First Date", data.index.values[0])
    print("Last Date", data.index.values[-1])

    a = convert_pd_datetime(data.index.values[0])
    b = convert_pd_datetime(data.index.values[-1])
    print("Period in days", float((b-a).days))
    print("Period in years", float((b-a).days)/365.25)

    return data.index.values[0], data.index.values[-1], float((b-a).days), float((b-a).days)/365.25
return_dates()
# data.index.values[-1]
# data.index.values[0]
# pprint(data[['dividend amount','close']])
# print(np.mean(data['close']))
# print(np.std(data['close']))



total_income = np.sum(data['dividend amount'])
print("Total dividend income",total_income)
# print(data['close'].iloc[0])

hprr =(total_income + data['close'].iloc[-1])/data['close'].iloc[0]
print("hpr", hprr-1)

prrr = []
prr = []
this_prrr = 0
for i in range(0, len(data['close'])-1):
    this_prrr = (data['dividend amount'].iloc[i] + data['close'].iloc[i+1])/data['open'].iloc[i]
    prrr.append(this_prrr)
    prr.append(this_prrr-1)
    this_prrr = 0

amr = np.sum(prr)/len(prr)
print("amr", amr)
amr1 = np.mean(prr)
print("also amr", amr1)


hprr_total = reduce(lambda x, y: x*y, prrr)
print("hprr", hprr_total)
print("hpr entire period", hprr_total-1)

gmr = (hprr ** (1./len(prrr))) - 1
print("gmr",gmr)
