import requests
import streamlit as st
from api_connection.py import get_us_population

base='light'
backgroundColor ='white'
st.write("""
# Simple Population Web App 
""")
col1, col2 = st.columns(2)
# Display the images in the columns
col1.image('worldimage.jpg')
col2.image('flags.jpg')
st.write( """
## Countries with the largest population
""")

col1, col2, col3 = st.columns(3)

# Display the text in each column
col1.write("USA")
col2.write("China")
col3.write("India")

population = get_us_population()
st.write(f"Population USA: {population}")
