
import requests
import json
import pandas as pd
import numpy as np

# create GET request

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
