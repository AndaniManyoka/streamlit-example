
import pandas as pd
import streamlit as st
import numpy as np


st.title("My first Streamlit app")
st.write("Streamlit is fun")

st.title('My Streamlit App')

st.write('Welcome to my Streamlit app!')

x = st.slider('Select a value for x', 0, 10)
st.write('You selected:', x)

##Visualizinng the airlines data frame
# Define the airlines data
airlines =pd.read_csv('airlines.csv',sep = ';')

# Displaying the dataframe in Streaml
st.table(airlines)



