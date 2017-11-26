from pandas_datareader import data as web
import matplotlib.pyplot as plt 
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick

jpy = web.DataReader('DEXJPUS', 'fred')
cad = web.DataReader('DEXCAUS', 'fred')
eur = web.DataReader('DEXUSEU', 'fred')
print(jpy)
print(cad)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(cad, color="lightblue", linewidth=2)
#candlestick(axes, cad, width=0.6)
plt.show()