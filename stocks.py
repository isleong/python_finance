import pandas_datareader as pdr
import datetime
import pandas
# import quandl
aapl = pdr.get_data_yahoo('AAPL', 
                          start=datetime.datetime(2006, 10, 1), 
                          end=datetime.datetime(2012, 1, 1))
print(aapl.head())
print("\n\n")
print(aapl.tail())

aapl.to_csv("apple.csv")