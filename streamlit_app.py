
import pandas as pd
import streamlit as st
import numpy as np


st.title("My first Streamlit app")
st.write("Streamlit is fun")

st.title('My Streamlit App')

st.write('Welcome to my Streamlit app!')

x = st.slider('Select a value for x', 0, 10)
st.write('You selected:', x)

import pandas as pd
import streamlit as st

# Define the airlines data
airlines = [...]

# Creating the dataframe and set column names
airlines = pd.DataFrame(airlines, columns=('Airline ID', 'Name', 'Alias', 'IATA', 'ICAO', 'Callsign', 'Country', 'Active'))

# Displaying the dataframe in Streamlit
st.dataframe(data=airlines, width=None, height=None)




