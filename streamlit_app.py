import requests
import streamlit as st
import pandas as pd 
import numpy as np
import geopandas as gpd
import matplotlib.pyplot
import plotly.graph_objects as go
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

col1, col2, col3, = st.columns(3)

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

col1, col2, col3, = st.columns(3)

population = get_population_data ("Brazil", "BR")
col1.image('brazil.png')
col1.write("Brazil")
col1.write(f" Population: {population}")

population = get_population_data ("Nigeria", "NG")
col2.image('¡nigeria.png')
col2.write("Nigeria")
col2.write(f" Population: {population}")

population = get_population_data ("Indonesia", "ID")
col3.image('indonesia.png')
col3.write("Indonesia")
col3.write(f" Population: {population}")

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
# Create a pie chart using Streamlit
fig = go.Figure(data=[go.Pie(labels=df['Country'], values=df['Population'])])
#fig.update_layout(title='Population Distribution by Country')
fig.update_traces(textinfo='none')  # This line removes the labels

st.title("Population Distribution by Country")
st.plotly_chart(fig)
#######################################################################################################3
# Load world map data with country coordinates
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the population data with country coordinates
merged_df = world.merge(df, left_on='iso_a3', right_on='Country')

# Create a bubble chart on a map using Streamlit
st.title("Population Bubble Chart on Map")
fig = px.scatter_geo(merged_df, locations='iso_a3', size='Population',
                     title='Population Bubble Chart on Map', projection='natural earth')
fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
st.plotly_chart(fig)

########################################################################################################3





#xxx


