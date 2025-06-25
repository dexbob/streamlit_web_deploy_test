import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

st.set_page_config(
    page_icon="✨",
    page_title="Streamlit 배포 연습",
    layout="wide"
)

st.header('환영합니다. 👋')
st.subheader('맛보기...')
cols = st.columns((1,1,2))
cols[0].metric('10/11', '15℃', '2')
cols[0].metric('10/12', '17℃', '2℉')
cols[0].metric('10/13', '15℃', '2')
cols[1].metric('10/14', '17℃', '2℉')
cols[1].metric('10/15', '14℃', '-3℉')
cols[1].metric('10/16', '13℃', '-1℉')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a','b','c'])
print(chart_data)
cols[2].line_chart(chart_data)