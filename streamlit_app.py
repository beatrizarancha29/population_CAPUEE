import requests
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot
#import plotly
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
## Selected countries
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

#######################################################################################################3
st.title("World Map")

st.map()
##################################################################################################

st.write('Made by Beatriz Garcia, Oscar Arenas and Abdullah')

#############################################################################################################

# Create a pie chart using Streamli
#fig = go.Figure(data=[go.Pie(labels=df['Country'], values=df['Population'])])
#fig.update_layout(title='Population Distribution by Country')
#fig.update_traces(textinfo='none')  # This line removes the labels

st.title("Population Distribution by Country")
#st.plotly_chart(fig)

st.pie_chart(df.set_index('Country'))

# Create a Pie chart using Plotly Express
#fig = px.pie(df, names='Country', values='Population', title='Population Distribution')

# Display the chart using Streamlit
#st.plotly_chart(fig)

#plt.pie(df['Population'], labels=df['Country'], autopct='%1.1f%%', startangle=90)
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Set chart title
plt.title('Population Distribution')

# Display the chart using Streamlit
st.pyplot()
