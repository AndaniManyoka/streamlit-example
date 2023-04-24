
import pandas as pd
import streamlit as st
import numpy as np


st.title("Data Analysis with Python")
st.write("This dashboard will showcase interesting facts about the OpenFlights Organisation")


st.write(" Interesting fact about the Airlines dataframe")
##visualizing the dataframe
df = pd.read_csv('airlines1.csv',sep =",")
df.columns = ['Airline ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']

df2 = df.groupby('Country')['Name'].count().reset_index()
st.write('Number of airlines per Country')
st.table(df2)



