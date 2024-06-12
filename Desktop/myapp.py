import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDf = tickerData.history(period = "1d",start="2020-5-31" ,end="2024-5-31")
# Open	High	Low	Close	Volume	Dividends	Stock Splits
# info = tickerData.info
# major_holders = tickerData.major_holders

# st.write("Historical Data (1 month):")
# st.write(tickerDf)

# st.write("\nStock Info:")
# st.write(info)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
