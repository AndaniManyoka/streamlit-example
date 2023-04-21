
import pandas as pd
import streamlit as st
import numpy as np


st.title("My first Streamlit app")
st.write("Streamlit is fun")

st.title('My Streamlit App')

st.write('Welcome to my Streamlit app!')

x = st.slider('Select a value for x', 0, 10)
st.write('You selected:', x)

st.write("Airlines dataframe")
##visualizing the dataframe
df = pd.read_csv('airlines1.csv',sep =";")
df.columns = ['Airline ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']

st.table(df)



