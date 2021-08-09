import pandas as pd
import yfinance as yf
import streamlit as st

trk = pd.read_csv('ticker.csv')

tickers = trk[['Company','Symbol']]
tickers = tickers.set_index('Company')
tickers = tickers.to_dict()
tickers = tickers['Symbol']

def get_data(tickers):
        df = pd.DataFrame()

        for company in tickers.keys():
                trk = yf.Ticker(tickers[company])
                trk_info = trk.info

        keys_list = []
        values_list = []

        for key, value in zip(trk_info.keys(), trk_info.values()):
        keys_list.append(key)
        values_list.append(value)
        
        df_keys = pd.DataFrame(keys_list)
        df_values = pd.DataFrame(values_list)
        
        company_info = pd.concat([df_keys,df_values],axis=1)
        company_info.columns=('Category', 'Details')

        company_info.to_csv('company.csv', index=False)
        company_info = pd.read_csv('company.csv',index_col='Category')



#Streamlits
comnany_name = st.sidebar.selectbox('Choose Company Name', list(tickers.keys()))
st.write(f"""
## Company Name: **{comnany_name}**
""")

st.write('Company Information')
st.dataframe(company_info)