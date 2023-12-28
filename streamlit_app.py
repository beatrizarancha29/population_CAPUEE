import requests
import streamlit as st

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
col1, col2, col3 = st.columns (3)

col1.write("China")
col2.write("USA")
col3.write("India")

population =get_us_population()
st.write(f"Population USA: {population}")
