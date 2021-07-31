import streamlit as st
import pandas as pd 
import numpy as np 
#from PIL import Image
import time

st.title('Streamlit Application')

st.write('DataFrame')

#df = pd.DataFrame(({'1列目':[1,2,3,4],'2列目':[10,20,30,40],}))
df = pd.DataFrame(np.random.rand(20,3), columns=['a','b','c'])
df_yokohama = pd.DataFrame(np.random.rand(100,2)/[50,50] + [35.43, 139.63], columns=['lat','lon'])

#st.write(df)
#st.dataframe(df,width=1000, height=1000)#縦横の設定をするならこのケース
st.dataframe(df.style.highlight_max(axis=0))#ハイライトをつける


st.write('Graph & Chart')
if st.checkbox('ShowGraph & Chart'):
    st.line_chart(df)#折線グラフの作成
    st.area_chart(df)#エリアチャートの作成
    st.bar_chart(df)#バーチャートの作成

#マップの作成
if st.checkbox('Show Map'):
    st.write('Mapping')
    st.map(df_yokohama)

#画像のアップロード
#st.write('Display Image - Night View')
#if st.checkbox('Display Image'):
    #image = Image.open('YKHM.jpg')
    #st.image(image, caption='Night View', use_column_width=True)

#selectboxの設定
option = st.selectbox('Enter Figures you want', options=list(range(1,11)))
'You selected', option, '!'

#テキスト入力
st.sidebar.write('Interactive Widgets')
text = st.text_input('What is your name?')
'My name is :', text
text = st.text_input('What is your country(nationarity)')
'My country is :', text
text = st.text_input('What is your email')
'My country is :', text

#スライダーの設定
condition = st.slider('Enter Condition Level from 1 to 10',0,100,50)#最小、最大、始まりの各値をoptionで設定
'My condtion: ', condition

#サイドバーの設定
condition = st.sidebar.select_slider(label='Status Level',options=list(range(1,11)))
details = st.sidebar.text_input('Details')
'Status Level:  ', condition
'Details:    ', details

#2カラムレウアウト（左右に表示）
st.write('Columns')
left_column, right_column = st.beta_columns(2)
button = left_column.button('Left Column')

if button:
    right_column.write('You enter button and Right Column is displayed')

#エクスパンダーの設定
expander1 = st.beta_expander('Contact1')
expander1.write('Answer1')

expander2 = st.beta_expander('Contact2')
expander2.write('Answer2')

#エクスパンダーサイドバータイプ
expander3 = st.sidebar.text_input(label='Contact Form')
'Your questions:  ', expander3

#Progress Barの設定（レクチャー13）
st.write('Show Progress Bar')
'Start !!'

latest_iteration = st.empty()
bar = st.progress(value=0)

for i in range(100):
    latest_iteration.text((f'Iteration {i + 1}'))
    bar.progress(i + 1)
    time.sleep(0.05)
'Done !!'