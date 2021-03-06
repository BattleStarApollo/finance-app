import re
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta

from get_finance_data import GetData


def ConvertPandaDT(string):
    year = string[0:4]
    month = string[5:7]
    day = string[8:10]
    # print year, month, day
    dt = date(int(year), int(month), int(day))
    return dt

'''
AllTickerData : Class holding all available daily data for the given ticker
'''

class AllTickerData:

    def TranslateDates(self, data):
        a = ConvertPandaDT(data.index.values[0])
        b = ConvertPandaDT(data.index.values[-1])
        return data.index.values[0], data.index.values[-1], float((b-a).days), float((b-a).days)/365.25

    class DateTime:
        start_date = ""
        end_date = ""
        period_days = 0
        period_years = 0

    def __init__(self,ticker):
        self.ticker = ticker
        self.data, self.meta_data = GetData(ticker)
        self.DateTime.start_date, self.DateTime.end_date, self.DateTime.period_days, self.DateTime.period_years = self.TranslateDates(self.data)


'''
PeriodTickerMetic : Class holding financial metrics for a given ticker, for a given period
'''

class PeriodTickerMetic:

    def GetPeriodData(self, data, a, b):
        for i in range(0,np.size(data.index.values)):
            if data.index.values[i] > a:
                data_out = data[i:]
                break
        return data_out

    def PerPeriod(self, data):
        prrr = []
        prr = []
        this_prrr = 0
        for i in range(0, len(data['close'])-1):
            this_prrr = (data['dividend amount'].iloc[i] + data['close'].iloc[i+1])/data['open'].iloc[i]
            prrr.append(this_prrr)
            prr.append(this_prrr-1)
            this_prrr = 0
        return prrr, prr

    def __init__(self, alltickerdata, a, b):
        self.ticker = alltickerdata.ticker
        self.data = alltickerdata.data
        self.meta_data = alltickerdata.meta_data
        self.period_data = self.GetPeriodData(self.data, a, b)
        self.start = self.period_data.index.values[0]
        self.end = self.period_data.index.values[-1]
        self.income_total = np.sum(self.period_data['dividend amount'])
        self.hprr = (self.income_total + self.period_data['close'].iloc[-1])/self.period_data['close'].iloc[0]
        self.prrr, self.prr = self.PerPeriod(self.period_data)
        self.amr = np.mean(self.prr)
        self.hprr_total = reduce(lambda x, y: x*y, self.prrr)
        self.gmr = (self.hprr ** (1./len(self.prrr))) - 1


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


periods_dict_begin_dates = {
    'ytd': str(date(date.today().year, 1, 1)),
    'thmon': str(date.today() - relativedelta(months=+3)),
    'sixmon': str(date.today() - relativedelta(months=+6)),
    'onyr': str(date.today() - relativedelta(years=+1)),
    'fiyr': str(date.today() - relativedelta(years=+5)),
    'teyr': str(date.today() - relativedelta(years=+10)),
}

def Build(ticker, periods):

    # Translates period in string form to date form
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

    # Get AllTickerData
    alltickerdata = AllTickerData(ticker)

    # For Each Period, Get PeriodTickerMetic
    # Return nothing periods that are out of range
    for period in periods:
        regexp = re.compile(r'\d+')
        if regexp.search(period) and str(ConvertPandaDT(period)) > alltickerdata.DateTime.start_date:
            periodtickermetric = PeriodTickerMetic(alltickerdata,
                str(period[:4] + "-" + period[4:6] + "-" + period[6:8]),
                str(period[8:12] + "-" + period[12:14] + "-" + period[14:]))
            PrettyPrint2(periodtickermetric)
        else:
            if not regexp.search(period):
                a, b = TranslateD(alltickerdata, period)
                print a
                if a != 'null':
                    periodtickermetric = PeriodTickerMetic(alltickerdata, a, b)
                    # print periodtickermetric.ticker
                    PrettyPrint2(periodtickermetric)

    return alltickerdata

# periods = ['ytd','thmon','sixmon','twmon','thyr', 'fiyr', 'teyr','start','end','all']
# periods = ['ytd','thmon','sixmon','onyr']
periods = ['2016010220170725','sixmon']
ticker = 'SPX'

instance = Build(ticker,periods)
