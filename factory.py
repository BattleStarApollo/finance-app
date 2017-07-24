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
from get_finance_data import GetData

ticker = 'VGSTX'


def TranslateDates(data):

    def ConvertPandaDT(string):
        year = string[0:4]
        month = string[5:7]
        day = string[8:]
        dt = date(int(year), int(month), int(day))
        return dt

    a = ConvertPandaDT(data.index.values[0])
    b = ConvertPandaDT(data.index.values[-1])
    return data.index.values[0], data.index.values[-1], float((b-a).days), float((b-a).days)/365.25

def PerPeriod(data):
    prrr = []
    prr = []
    this_prrr = 0
    for i in range(0, len(data['close'])-1):
        this_prrr = (data['dividend amount'].iloc[i] + data['close'].iloc[i+1])/data['open'].iloc[i]
        prrr.append(this_prrr)
        prr.append(this_prrr-1)
        this_prrr = 0
    return prrr, prr

# def PrettyPrint(profile):
#      print "Ticker: " + profile.ticker
#      print "Start Date: " + profile.DateTime.start_date
#      print "End Date: " + profile.DateTime.end_date
#      print "Number of Days in Period: " + str(profile.DateTime.period_days)
#      print "Number of Years in Period: " + str(profile.DateTime.period_years)
#      print profile.income_total
#      print profile.hprr
#      print profile.prrr, profile.prr

class ProfileRawData:

    class DateTime:
        start_date = ""
        end_date = ""
        period_days = 0
        period_years = 0

    def __init__(self,ticker):
        self.ticker = ticker
        self.data, self.meta_data = GetData(ticker)
        self.DateTime.start_date, self.DateTime.end_date, self.DateTime.period_days, self.DateTime.period_years = TranslateDates(self.data)

        self.income_total = np.sum(self.data['dividend amount'])
        self.hprr = (self.income_total + self.data['close'].iloc[-1])/self.data['close'].iloc[0]
        self.prrr, self.prr = PerPeriod(self.data)
        self.amr = np.mean(self.prr)
        self.hprr_total = reduce(lambda x, y: x*y, self.prrr)
        self.gmr = (self.hprr ** (1./len(self.prrr))) - 1






#
# Need to make time intervals and ability to choose time windows
#
# Intervals:
#   YTD
#   Last 3 months
#   Last 6 Months
#   Last 12 months
#   Last 3 Years
#   Last Five Years
#   Last Ten Years
#
#
#   Start Date, End Date
#
#
# size = {'ytd','3mon','6mon','12mon','3yr', '5yr', '10yr','start','end'}
#
# def Intervals(profile, size):

# def TimeTransformData(profile, size):
#

    # return data['close'] for interval




class Profile:
    def __init__(self, ticker, size):
        self.profile_raw_data = ProfileRawData(ticker)
        self.data = TimeTransformData(self.profile_raw_data, size)
    def Build(size):
        if 'ytd' in size:






# sizes = ['ytd','thmon','sixmon','twmon','thyr', 'fiyr', 'teyr','start','end','all']
# 1. convert dates to start dates and end dates
# 2. check if in bounds
# 3. create class data profile with raw data
# 4. create class

sizes_dict = {
    ytd: {}
}


def TimeTranslator(profile, size):
    if size == 'ytd':
        end = profile.DateTime.end_date
        start =
    return start, end





size = 'ytd'
def Build(ticker, sizes):
    for size in sizes:
        yield factory(ProfileRawData(ticker), size)
    return Profile(ticker, size)

# Need to return array of classes for each size

instance = Build(ticker,size)
# PrettyPrint(instance)
print instance.profile_raw_data.ticker
# t = ProfileRawData(ticker,size)
# print t.ticker
# print t.size
# print t.data




# data.index.values[-1]
# data.index.values[0]
# pprint(data[['dividend amount','close']])
# print(np.mean(data['close']))
# print(np.std(data['close']))
# sys.exit()
# duration = ''
#
# begin_time = ''
# end_time = ''
#
# total_income = np.sum(data['dividend amount'])
# print("Total dividend income",total_income)
# # print(data['close'].iloc[0])
#
# hprr =(total_income + data['close'].iloc[-1])/data['close'].iloc[0]
# print("hpr", hprr-1)
#
# prrr = []
# prr = []
# this_prrr = 0
# for i in range(0, len(data['close'])-1):
#     this_prrr = (data['dividend amount'].iloc[i] + data['close'].iloc[i+1])/data['open'].iloc[i]
#     prrr.append(this_prrr)
#     prr.append(this_prrr-1)
#     this_prrr = 0
#
# amr = np.sum(prr)/len(prr)
# print("amr", amr)
# amr1 = np.mean(prr)
# print("also amr", amr1)
#
#
# hprr_total = reduce(lambda x, y: x*y, prrr)
# print("hprr", hprr_total)
# print("hpr entire period", hprr_total-1)
#
# gmr = (hprr ** (1./len(prrr))) - 1
# print("gmr",gmr)
