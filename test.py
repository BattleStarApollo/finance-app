# from get_finance_data import GetData
# from build_profile import Build
from datetime import date

ticker = 'SPX'
size = 'full'
# myint = 13
#
#
#
# def testing(myint):
#     return myint-5
#
# class Test:
#
#     def __init__(self,ticker,size, myint):
#         self.ticker = ticker
#         self.size = size
#         self.myint = testing(myint)
#         self.data, self.meta_data = GetData(ticker, size)



# t = Test(ticker,size, myint)
# print t.ticker
# print t.size
# print t.myint
# print t.data
# t = Build(ticker,size)
# print t.ticker



# sizes = ['ytd','thmon','sixmon','twmon','thyr', 'fiyr', 'teyr','start','end','all']
# 1. convert dates to start dates and end dates
# 2. check if in bounds
# 3. create class data profile with raw data
# 4. create class

sizes_dict = {
    'ytd': {'start': str(date(date.today().year, 1, 1)), 'end': str(date.today()},
}


print sizes_dict









#
# def __init__(self, name, surname, birthdate, address, telephone, email):
#     self.name = name
#     self.surname = surname
#     self.birthdate = birthdate
#
#     self.address = address
#     self.telephone = telephone
#     self.email = email
#
# def age(self):
#     today = datetime.date.today()
#     age = today.year - self.birthdate.year
#
#     if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#         age -= 1
#
#     return age
