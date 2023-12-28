""" This script store the function required to stream data from the API of your choice"""

import requests
import json
import pandas as pd
import numpy as np

# create GET request

def get_data_from_api():
    
    url = "https://world-geo-data.p.rapidapi.com/countries/US"
    header = {
	"X-RapidAPI-Key": "e8dcb32d36msh2417d6829510541p15ff3ajsnf7e49772d415",
	"X-RapidAPI-Host": "world-geo-data.p.rapidapi.com"
}
    params = 

    response = requests.get(url, headers=headers, params=params)
    outputs = response.json()

    return outputs
