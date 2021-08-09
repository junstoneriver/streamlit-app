import pandas as pd
import yfinance as yf
import altair as alt
import datetime
import streamlit as st

trk = pd.read_csv('ticker.csv')

tickers_list = trk[['Company','Symbol']]
tickers_list = tickers_list.set_index('Company')
tickers = tickers_list.to_dict()
tickers = tickers['Symbol']

df_ticker = pd.DataFrame(tickers_list)

st.sidebar.title('Choose Parameters')
name = st.sidebar.selectbox('Choose Company Name',tickers)

date_term = {'5days':'5d',
              '1month':'1mo',
              '3moth':'3mo',
              '6month':'6mo',
              '1year':'1y',
              '2years':'2y',
              '5years':'5y',
              '10years':'10y',
              'Year to Date':'ytd'}

term = st.sidebar.selectbox('Date Term', list(date_term))


trk = yf.Ticker(tickers[name])
price = trk.history(period=(f'{date_term[term]}'), interval='1d')
df = price['Close']
df = df.reset_index()
df.columns  = ('Date', 'Stock Price($)')

ymin=30
ymax=300

chart = (alt.Chart(data=df)
        .mark_line(opacity=0.8, clip=True)
        .encode(x = 'Date:T', 
                y = alt.Y('Stock Price($):Q',
                stack = None,
                scale = alt.Scale(domain=[ymin,ymax])),
                color=alt.value('white'))
).interactive()

st.title('Dow Jones Industrial Average index')

st.write(f"""
## Company Name : **{name}**
""")

st.write("""
## Stock Price Chart
""")
st.altair_chart(chart, use_container_width=True)


performance = (df['Stock Price($)']/df['Stock Price($)'].iloc[0]-1)*100
df_performance = pd.DataFrame(data=performance)
df_index = df.Date
performance_data = pd.concat([df_index,df_performance], axis=1)
performance_data.columns = ('Date', 'Performance(%)')

st.write("""
## Stock Performance Data
""")
st.dataframe(performance_data)

ymin=-30.0
ymax=100

performane_chart = (alt.Chart(data=performance_data)
        .mark_line(opacity=0.8, clip=True, color='red')
        .encode(x = 'Date:T', 
                y = alt.Y('Performance(%):Q',
                stack = None,
                scale = alt.Scale(domain=[ymin,ymax])),
                color = alt.value('red'))
).interactive()



st.write("""
## Stock Performance Chart
""")
st.altair_chart(performane_chart, use_container_width=True)