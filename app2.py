import pandas as pd
import yfinance as yf
import streamlit as st
import altair as alt

st.title('DJI Chart Application')

st.sidebar.write("""
# DJI Stock Prices
## This is an application for stock price chart
# """)

st.sidebar.write("""
## Date Range 
# """)

days = st.sidebar.slider('Date Range Bar',1,1000,100)
st.write(f"""
## Data Range: **{days}** days
""")

@st.cache
def get_data(days, tickers):

    df = pd.DataFrame()

    for company in tickers.keys():
        ticker = yf.Ticker(tickers[company])

        hist = ticker.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]

        hist = hist.T
        hist.index.name = 'Name'

        df = pd.concat([df, hist])
            
    return df


st.sidebar.write("""
## Stock Price Range
""")

ymin, ymax = st.sidebar.slider('Stock Price Range', 0.0,500.0, (0.0, 500.0))

tickers = pd.read_csv('ticker.csv')
tickers = tickers[['Company','Symbol']]
tickers = tickers.set_index('Company')
tickers = tickers.to_dict()
tickers = tickers['Symbol']

tickers = tickers

df = get_data(days,tickers)

companies = st.multiselect('Enter Company Name',
list(df.index),
default=['Amgen','IBM']
)

if not companies:
    st.error('Enter company name')
else:
    data = df.loc[companies]
    st.write("""
    ## Stock Price Data""", data.sort_index())

    data = data.T.reset_index()
    data = pd.melt(data, id_vars=['Date']).rename(columns={'value':'Stock Prices(USD)'})

    chart = (alt.Chart(data=data)
        .mark_line(opacity=0.8, clip=True)
        .encode(x = 'Date:T', 
                y = alt.Y('Stock Prices(USD):Q',
                stack = None,
                scale = alt.Scale(domain=[ymin,ymax])),
                color='Name:N')
    )

st.write("""
## Stock Price Chart""")
st.altair_chart(chart, use_container_width=True)