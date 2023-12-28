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

col1, col2, col3 = st.columns(3)

# Display the text in each column
col1.write("USA")
col2.write("China")
col3.write("India")

##############################################################################

def get_us_population():
    
    url = "https://world-geo-data.p.rapidapi.com/countries/US"
    header = {
	"X-RapidAPI-Key": "e8dcb32d36msh2417d6829510541p15ff3ajsnf7e49772d415",
	"X-RapidAPI-Host": "world-geo-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=params)
outputs = response.json()
population = outputs['population']
return population

population = get_us_population()
st.write(f"Population USA: {population}")
