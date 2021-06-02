import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


#Create a new dictionary:
dict_={'a':[11,21,31],'b':[12,22,32]}

#Create a Pandas object with Dataframe constructor >> for create a API instance
df=pd.DataFrame(dict_)
type(df)

#Method head to communicates the dataframe with API
df.head()

#Method mean to API calculates the mean and return the value

df.mean()

#REST APIs (request and response)

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency ='usd', days = 30)

type(bitcoin_data)

bitcoin_price_data = bitcoin_data['prices']
bitcoin_price_data[0:5]

#Turn this data omtp a Pandas Dataframe:
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp','prices'])

#Converting the timestamp to datetime and save as column Date
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

#Using this modified dataset we can now group by the Date
#and find the min, max, open, and close for the candlesticks

candlestick_data = data.groupby(data.Date.dt.date, as_index=False).agg({'prices':['min', 'max', 'first', 'last']})

#Using plotly to create Candlestick Chart:

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=candlestick_data['prices']['first'], 
                high=candlestick_data['prices']['max'],
                low=candlestick_data['prices']['min'], 
                close=candlestick_data['prices']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()
