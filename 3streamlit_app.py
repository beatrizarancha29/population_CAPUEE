import requests
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from api_connection import get_population_data
from api_connection import get_area
from api_connection import country_data
from api_connection import get_language
from api_connection import get_capital
import time

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Data download complete!", state="complete", expanded=False)


base='light'
backgroundColor ='white'
st.write("""
# Country Data Web App 
""")

st.write(" ### Welcome to the Country Data Web App. Take a look at global data or select a country to find out more details. Enjoy!")


col1, col2, col3, = st.columns(3)
# Display the images in the columns
col1.image('worldimage.jpg')
col2.image('flags.jpg')
col3.image('people.jpg')
st.write("""

### World population: 8.1 Billion""" )

#########################################################################################################################################################
st.write( """
## Top 3 most populous countries
""")

col1, col2, col3, = st.columns(3)

population = get_population_data("China", "CN")
numeric_area = get_area("China", "CN")
col1.image('china.png')
col1.write("China")
population_in_millions = population / 1000000
area_in_millions = numeric_area/100000
col1.write(f" Population: {population_in_millions:.2f} Million")
col1.write(f"Area: {area_in_millions} Million sq. km")

population = get_population_data("India", "IN")
numeric_area = get_area("India", "IN")
col2.image('india')
col2.write("India")
population_in_millions = population / 1000000
area_in_millions = numeric_area/100000
col2.write(f" Population: {population_in_millions:.2f} Million")
col2.write(f"Area: {area_in_millions} Million sq. km")

population = get_population_data("United States", "US")
numeric_area = get_area("United States", "US")
col3.image('usa.png')
col3.write("USA")
population_in_millions = population / 1000000
area_in_millions = numeric_area/100000
col3.write(f" Population: {population_in_millions:.2f} Million")
col3.write(f"Area: {area_in_millions} Million sq. km")

st.write( """
## Top 3 largest countries
""")

col1, col2, col3, = st.columns(3)

population = get_population_data ("Russia", "RU")
numeric_area = get_area("Russia", "RU")
col1.image('Flag_of_Russia.svg.png')
col1.write("Russia")
population_in_millions = population / 1000000
area_in_millions = numeric_area/100000
col1.write(f" Population: {population_in_millions:.2f} Million")
col1.write(f"Area: {area_in_millions} Million sq. km")

population = get_population_data ("Canada", "CA")
numeric_area = get_area("Canada", "CA")
col2.image('canada.png')
col2.write("Canada")
col2.write(f" Population: {population} Million")
population_in_millions = population / 1000000
area_in_millions = numeric_area/100000
col2.write(f" Population: {population_in_millions:.2f} Million")
col2.write(f"Area: {area_in_millions} Million sq. km")

population = get_population_data ("Brazil", "BR")
numeric_area = get_area("Brazil", "BR")
col3.image('brazil.png')
col3.write("Brazil")
population_in_millions = population / 1000000
area_in_millions = numeric_area/100000
col3.write(f" Population: {population_in_millions:.2f} Million")
col3.write(f"Area: {area_in_millions} Million sq. km")


st.toast('The world ...',)
time.sleep(.5)
st.toast('... is like a book',)
time.sleep(.5)
st.toast('Who doesn´t travel...')
time.sleep(.5)
st.toast('... only reads the first page')


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
st.bar_chart(df.set_index('Country'), color="#00FF00")
#####################################################################################################################
##################################################################################################
st.write( "# Area of Countries")

countries = []
numeric_areas = []

# Fetch data and store in lists
for country, iso_code in country_data:
    numeric_area = get_area(country, iso_code)
    countries.append(country)
    numeric_areas.append(numeric_area)
    
data = {'Country': countries, 'Area': numeric_areas}
df = pd.DataFrame(data)

# Create a bar chart using Streamlit
st.bar_chart(df.set_index('Country'), color="#FF0000")
#######################################################################################################3

##################################################################################################
densities = []
countries = []
populations = []
countries = []
numeric_areas = []

for country, iso_code in country_data:
    population = get_population_data(country, iso_code)
    numeric_area = get_area(country, iso_code)
    density = population / numeric_area
    
    countries.append(country)
    numeric_areas.append(numeric_area)
    populations.append(population)
    
    densities.append(density)

data = {'Area': numeric_areas,'Density': densities, 'Population':populations, 'Country': countries}
df = pd.DataFrame(data)

st.write("# Population Density Bubble Chart")

fig = px.scatter(df,x='Area',y='Density', size='Population', hover_name='Country',log_x=True)
st.plotly_chart(fig, use_container_width=True)

#####################################################################################################
selected_country = st.selectbox('Select a Country', [country[0] for country in country_data])
selected_iso_code = [country[1] for country in country_data if country[0] == selected_country][0]

selected_country = st.text_input('Enter the desired country:', country_data[0][0])

# Check if the entered country is in the list
if selected_country not in [country[0] for country in country_data]:
    st.warning("Please enter a valid country.")
else:
    selected_iso_code = [country[1] for country in country_data if country[0] == selected_country][0]

numeric_area = get_area(selected_country, selected_iso_code)
population = get_population_data(selected_country, selected_iso_code)
population_density = population / numeric_area

population_in_millions = population / 1000000
area_in_millions = numeric_area/100000

language = get_language(selected_country, selected_iso_code)
capital_name = get_capital(selected_country, selected_iso_code)


st.write(f"Selected Country: {selected_country}")
st.write(f" Area: {area_in_millions} Million sq. km")
st.write(f"Population: {population_in_millions} Million")
st.write(f"Density: {population_density} People per sq km")
st.write(f"Languag(es): {language}")
st.write(f" Capital: {capital_name}")

st.toast('A different language...')
time.sleep(.5)
st.toast('... means ...')
time.sleep(.5)
st.toast('...a different version...')
time.sleep(.5)
st.toast('... of life)


############################################################################################################3
st.title("World Map")

st.map()
       
st.write('Made by Beatriz Garcia, Oscar Arenas and Abdullah Rashed')



         
st.balloons() 
#############################################################################################################


