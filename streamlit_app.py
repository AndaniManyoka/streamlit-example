
import numpy as np
import pandas as pd
import streamlit as st


st.title['Overview of Cars']
st.write['This project explores cars']

df = pd.read_csv('cars',sep=';',skiprows=[1]

#df2 = df.groupby('Origin')['Cars'].count().reset_index()

st.write('My First Table')
st.table(df)
