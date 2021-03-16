import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st

st.write( """
# Simple Stock Price App
are the stock ***closing price*** and ***volume*** of Google
Shown

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id',start='2010-5-31',end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
