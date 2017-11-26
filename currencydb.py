import pyodbc
from pandas_datareader import data as web
#import matplotlib.pyplot as plt 
#from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick

jpy = web.DataReader('DEXJPUS', 'fred')
cad = web.DataReader('DEXCAUS', 'fred')
eur = web.DataReader('DEXUSEU', 'fred')
print(jpy)
print(cad)

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=currency;UID=me;PWD=pass')
cursor = connection.cursor()

connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cursor.execute()