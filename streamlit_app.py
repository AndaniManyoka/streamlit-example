
import pandas as pd
import streamlit as st


st.title("My first Streamlit app")
st.write("Streamlit is fun")

st.title('My Streamlit App')

st.write('Welcome to my Streamlit app!')

x = st.slider('Select a value for x', 0, 10)
st.write('You selected:', x)

cars = pd.read_csv("cars",sep=";")
st.bar_chart(cars, x="col1", y="col2")
