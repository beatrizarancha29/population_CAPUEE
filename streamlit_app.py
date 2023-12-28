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
   

# Display the bar chart in a Streamlit app
if populations:
    countries, population_values = zip(*populations)

    # Use st.bar_chart to display the bar chart
    st.bar_chart(dict(zip(countries, population_values)))

    # Optionally, you can add labels and title
    st.xlabel('Country')
    st.ylabel('Population')
    st.title('Population of Countries')
else:
    st.warning("No population data available.")







