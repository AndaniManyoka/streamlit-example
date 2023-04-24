
import pandas as pd
import streamlit as st
import numpy as np


st.title("Data Analysis with Python")
st.write("This dashboard will showcase interesting facts about the OpenFlights Organisation")


st.write(" Interesting fact about the Airlines dataframe")
##visualizing the dataframe
df = pd.read_csv('airlines1.csv',sep =",")
df.columns = ['Airline ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']

#df2 = df.groupby(['Country', 'active'])['Name'].count().reset_index()

df2 = df.groupby('Country','Active'=="Y")['Name'].count().reset_index()
st.write('Number of Active airlines per Country')
st.bar_chart(df2,x='Country',y='Name')

##looking at the airpots data
airpots = pd.read_csv('airports1.csv', sep=",", encoding='utf-8')
airpots.columns = ['Airport ID','Name','City','Country','IATA','ICAO','Latitude','Longitude','Altitude','Timezone','DST','Tz database time zone',
'Type','Source']
airpotsDist = airpots[['Latitude','Longitude']].rename(columns={'Latitude': 'latitude'})
st.write('Distribution of the airports across the globe')
st.map(data=airpotsDist)



