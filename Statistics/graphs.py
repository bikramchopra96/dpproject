import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#from mpl_finance import candlestick_ohlc 
import seaborn as sns
import datetime as dt
from matplotlib import style
def create_graph():
    sns.set(color_codes = True)
    stock_yearly = pd.read_csv("Yearly.csv")
    stock_yearly.head()
    stock_yearly.info()
    style.use("ggplot")
    start = dt.datetime(2020,1,1)
    end = dt.datetime.now()
    data = web.get_data_yahoo("AMRN",start,end)
    data["Adj Close"].plot()
    plt.savefig('/static/plots/plot1.png', bbox_inches='tight')
    plt.close()
# plt.show()
start = dt.datetime(2020,1,1)
end = dt.datetime.now()
style.use("ggplot")
data = web.get_data_yahoo("AMRN",start,end)
data["High"].plot()
plt.savefig('static/plots/plot2.png', bbox_inches='tight')
# plt.close()
# # plt.show()
# style.use("ggplot")
# data = web.get_data_yahoo("AMRN",start,end)
# data["Low"].plot()
# plt.savefig('FinalProject/Statistics/static/plots3/plot3.png', bbox_inches='tight')
# plt.close()
# # plt.show()
# style.use("ggplot")
# data = web.get_data_yahoo("AMRN",start,end)
# data["Volume"].plot()
# plt.savefig('FinalProject/Statistics/static/plots3/plot4.png', bbox_inches='tight')
# plt.close()
# # plt.show()
# #
# #
# data = data [['Open','High','Low','Close']]
# data.reset_index(inplace = True)
# data['Date'] = data['Date'].map(mdates.date2num)
# ax = plt.subplot()
# ax.grid(True)
# ax.set_axisbelow(True)
# ax.set_facecolor('black')
# ax.figure.set_facecolor('#121212')
# ax.tick_params(axis = 'x', colors = 'white')
# ax.tick_params(axis = 'y', colors = 'white')
# ax.xaxis_date()
# candlestick_ohlc(ax, data.values, width = 0.5, colorup = '#00ff00')
# plt.savefig('FinalProject/Statistics/static/plots3/plot5.png', bbox_inches='tight')
# plt.close()
# plt.show()




