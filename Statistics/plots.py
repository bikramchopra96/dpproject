import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import datetime as dt
import seaborn as sns

yearly_file = 'Statistics/Yearly.csv'
# def first():

def create_plots():
    sns.set(color_codes=True)
    stock_yearly = pd.read_csv(yearly_file)
    stock_yearly.head()
    stock_yearly.info()
    style.use("ggplot")
    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()
    data = web.get_data_yahoo("AMRN", start, end)
    data["Adj Close"].plot()
    plt.savefig('Statistics/static/plots/yearly-plot13.png', bbox_inches='tight')
    # plt.draw()



    style.use("ggplot")
    data = web.get_data_yahoo("AMRN", start, end)
    data["High"].plot()
    plt.savefig('Statistics/static/plots/yearly-plot23.png', bbox_inches='tight')

# create_plots()
