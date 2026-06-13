import yfinance as yf 
import streamlit as st
import pandas as pd

#yfinance library
s=yf.Ticker("AAPL")
print(s.info)
print(s.history(period="1d"))
print(s.history(period="5d",interval="1d"))

#print(s.download)
p=yf.download(
    ['AAPL','GOOGL'],
    start="2026-06-11",
    end='2026-12-12'
)

print(s.financials)
print(s.balance_sheet)
print(s.cashflow)
print(s.dividends)
print(s.splits)
print(s.institutional_holders)


# st.line_chart(df[Close])
# st.line_chart(s.Open)
# st.line_chart(s.Volume)
# st.line_chart(s.High)
# st.line_chart(s.Low)


st.write('''# simple stock price app
         It showes the stock price of the Apple''')
df = s.history(period="1y")

st.line_chart(df["Close"])
st.line_chart(df["Open"])
st.line_chart(df["Volume"])
st.line_chart(df["High"])
st.line_chart(df["Low"])