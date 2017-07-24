import sys

# import matplotlib.pyplot as plt
#
# ts = TimeSeries(key='G9RVRT562GWL8YZB', output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='VFIFX',interval='60min', outputperiod='full')
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
# data, meta_data = ts.get_daily(symbol='VFIFX', outputperiod='full')
# data['close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()


from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
from get_finance_data import GetData



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

def PrettyPrint1(AllTickerData):
     print "Ticker: " + AllTickerData.ticker
     print "period: " + AllTickerData.period
     print "Start Date: " + AllTickerData.DateTime.start_date
     print "End Date: " + AllTickerData.DateTime.end_date
     print "Number of Days in Period: " + str(AllTickerData.DateTime.period_days)
     print "Number of Years in Period: " + str(AllTickerData.DateTime.period_years)
     print AllTickerData.income_total
     print AllTickerData.hprr
    #  print AllTickerData.prrr, AllTickerData.prr

class AllTickerData:

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




# def GetPeriodData(data, a, b):
#     for i in range(0,np.size(data.index.values)):
#         if data.index.values[i] > a:
#             data_out = data[i:]
#             break
#
#     # print type(a)
#     # print type(data_out.index.values[0])
#     #
#     # print a
#     # print data_out.index.values[0]
#     # print data_out.index.values[-1]
#     return data_out

def PrettyPrint2(periodtickermetric):
     print "Ticker: " + periodtickermetric.ticker

     print "Start Date: " + periodtickermetric.start
     print "End Date: " + periodtickermetric.end
     print "Total Income This Period " + str(periodtickermetric.income_total)
     print "Holding Period Return " + str(float(periodtickermetric.hprr) -1)
     print "Arithmetic Mean Return " + str(periodtickermetric.amr)
     print "Holding Period Return (Multiplicative): " + str(float(periodtickermetric.hprr_total) -1)
     print "Geometric Mean Return: " + str(periodtickermetric.gmr)
    #  print periodtickermetric.prrr, periodtickermetric.prr

class PeriodTickerMetic:

    def GetPeriodData(self, data, a, b):
        for i in range(0,np.size(data.index.values)):
            if data.index.values[i] > a:
                data_out = data[i:]
                break
        return data_out

    def __init__(self, alltickerdata, a, b):
        self.ticker = alltickerdata.ticker
        self.data = alltickerdata.data
        self.meta_data = alltickerdata.meta_data
        self.period_data = self.GetPeriodData(self.data, a, b)
        self.start = self.period_data.index.values[0]
        self.end = self.period_data.index.values[-1]
        self.income_total = np.sum(self.period_data['dividend amount'])
        self.hprr = (self.income_total + self.period_data['close'].iloc[-1])/self.period_data['close'].iloc[0]
        self.prrr, self.prr = PerPeriod(self.period_data)
        self.amr = np.mean(self.prr)
        self.hprr_total = reduce(lambda x, y: x*y, self.prrr)
        self.gmr = (self.hprr ** (1./len(self.prrr))) - 1




periods_dict_begin_dates = {
    'ytd': str(date(date.today().year, 1, 1)),
    'thmon': str(date.today() - relativedelta(months=+3)),
    'sixmon': str(date.today() - relativedelta(months=+6)),
    'onyr': str(date.today() - relativedelta(years=+1)),
    'fiyr': str(date.today() - relativedelta(years=+5)),
    'teyr': str(date.today() - relativedelta(years=+10)),
}
# Sends in one string period choices, returns corrected version

def TranslateD(alltickerdata, period):
    start_claim = periods_dict_begin_dates[period]
    if period == 'all':
        start = alltickerdata.DateTime.start_date
        end = alltickerdata.DateTime.end_date
    elif start_claim < alltickerdata.DateTime.start_date:
        # print  "no"
        # print("earliest date", alltickerdataDateTime.start_date)
        start = 'null'
        end = 'null'
    else:
        start = periods_dict_begin_dates[period]
        end = alltickerdata.DateTime.end_date
        # print period, start, end
    return start, end





def Build(ticker, periods):
    alltickerdata = AllTickerData(ticker)

    # List_PeriodTickerMetrics a list of pp_AllTickerDatas for existing periods
    List_PeriodTickerMetrics = []
    for period in periods:
        a, b = TranslateD(alltickerdata, period)
        # print a, b
        if a != 'null':
            periodtickermetric = PeriodTickerMetic(alltickerdata, a, b)
            # print periodtickermetric.ticker
            PrettyPrint2(periodtickermetric)

# periods = ['ytd','thmon','sixmon','twmon','thyr', 'fiyr', 'teyr','start','end','all']
periods = ['ytd','thmon','sixmon','onyr']
ticker = 'VGSTX'

instance = Build(ticker,periods)
