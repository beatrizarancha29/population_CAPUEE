import requests
import streamlit as st
from api_connection import get_population_data
from api_connection import country_data
mport streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

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

##############################################################################
#population = get_us_population()
#st.write(f"Population USA: {population}")
#population = get_population_data("India", "IN")
#st.write(f" Population: {population}")

#####################################################################################3
populations = []
for country, iso_code in country_data:
    population = get_population_data(country, iso_code)
    populations.append((country, population))
   

st.write("# Population of Countries")

if populations:
    countries, population_values = zip(*populations)

    # Use st.bar_chart to display the bar chart
    st.bar_chart(dict(zip(countries, population_values)))

    # Optionally, you can add a title and labels using st.write
    

else:
    st.warning("No population data available.")

################################################################################################
if populations:
    _, population_values = zip(*populations)

    # Use st.histogram to display the histogram
    st.histogram(population_values, bins=30, color="skyblue", edgecolor="black")

    # Optionally, you can add a title and labels using st.write
    st.write("# Population Distribution of Countries")
    st.write("### X-axis: Population")
    st.write("### Y-axis: Frequency")
else:
    st.warning("No population data available.")

##############################################################################################################333

#if populations:
    # Create a pie chart using matplotlib
   # fig, ax = plt.subplots()
    #ax.pie(populations, labels=None, autopct='%1.1f%%', startangle=90)
    #ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
   # st.pyplot(fig)

    # Optionally, you can add a title
   # st.title('Population Distribution Pie Chart')
#else:
   # st.warning("No population data available.")






