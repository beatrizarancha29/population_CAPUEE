import requests
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot
from api_connection import get_population_data
from api_connection import country_data

base='light'
backgroundColor ='white'
st.write("""
# Simple Population Web App 
""")
col1, col2, col3, = st.columns(3)
# Display the images in the columns
col1.image('worldimage.jpg')
col2.image('flags.jpg')
col3.image('people.jpg')
st.write("""

### World population: 8081718834""" )

st.write( """
## Countries with the largest population
""")

col1, col2, col3, col4, = st.columns(4)

population = get_population_data("United States", "US")
col1.image('usa.png')
col1.write("USA")
col1.write(f" Population: {population}")

population = get_population_data("India", "IN")
col2.image('india')
col2.write("India")
col2.write(f" Population: {population}")

population = get_population_data("China", "CN")
col3.image('china.png')
col3.write("China")
col3.write(f" Population: {population}")

population = get_population_data("Canada", "CA")
st.write("Canada")
st.write(f" Population: {population}")


###########################################################################################   
st.write("# Population of Countries")

#if populations:
    #countries, population_values = zip(*populations)
    # Use st.bar_chart to display the bar chart
    #st.bar_chart(dict(zip(countries, population_values)))
#else:
    #st.warning("No population data available.")

################################################################################################
populations = []
countries = []

for country, iso_code in country_data:
    population = get_population_data(country, iso_code)
    populations.append(population)
    countries.append(country)
    
data = {'Country': countries, 'Population': populations}
df = pd.DataFrame(data)

# Create a bar chart using Streamlit
st.bar_chart(df.set_index('Country'))
##################################################################################################
st.title("Population Distribution by Country")
st.plotly_chart(figure=px.pie(df, values='Population', names='Country', title='Population Distribution'))



#xxx


