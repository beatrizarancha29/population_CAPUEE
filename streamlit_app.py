import requests
import streamlit as st
from api_connection import get_population_data

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

population_us = get_population_data("United States", "US")
col1.image('usa.png')
col1.write("USA")
col1.write(f" Population: {population_us}")

population_in = get_population_data("India", "IN")
col2.image('india')
col2.write("India")
col2.write(f" Population: {population_in}")

population_cn = get_population_data("China", "CN")
col2.image('china.png')
col2.write("China")
col2.write(f" Population: {population_cn}")

# Display the text in each column
#col1.write("USA")
#col2.write("China")
#col3.write("India")

##############################################################################
#population = get_us_population()
#st.write(f"Population USA: {population}")
#population = get_population_data("India", "IN")
#st.write(f" Population: {population}")


