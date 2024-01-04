import re
import requests
import json
import pandas as pd
import numpy as np

country_data = [
    ("Russia", "RU"),
    ("Canada", "CA"),
    ("United States", "US"),
    ("China", "CN"),
    ("Brazil", "BR"),
    ("Australia", "AU"),
    ("India", "IN"),
    ("Argentina", "AR"),
    ("Kazakhstan", "KZ"),
    ("Algeria", "DZ"),
    ("Democratic Republic of the Congo", "CD"),
    ("Greenland", "GL"),
    ("Saudi Arabia", "SA"),
    ("Mexico", "MX"),
    ("Indonesia", "ID"),
    ("Libya", "LY"),
    ("Iran", "IR"),
    ("Mongolia", "MN"),
    ("Peru", "PE"),
    ("Chad", "TD"),
    ("Niger", "NE"),
    ("Sudan", "SD"),
    ("Angola", "AO"),
    ("Mali", "ML"),
    ("South Africa", "ZA"),
    ("Colombia", "CO"),
    ("Ethiopia", "ET"),
    ("Botswana", "BW"),
    ("Mozambique", "MZ"),
    ("Chile", "CL"),
    ("Tanzania", "TZ"),
    ("Nigeria", "NG"),
    ("Egypt", "EG"),
    ("Tunisia", "TN"),
    ("Morocco", "MA"),
    ("South Sudan", "SS"),
    ("Seychelles", "SC"),
    ("Pakistan", "PK"),
    ("Afghanistan", "AF"),
    ("Iraq", "IQ"),
    ("Philippines", "PH"),
    ("Vietnam", "VN"),
    ("Malaysia", "MY"),
    ("Thailand", "TH"),
    ("Myanmar", "MM"),
    ("South Korea", "KR"),
    ("North Korea", "KP"),
    ("Japan", "JP"),
    ("Cambodia", "KH"),
    ("Laos", "LA"),
    ("Bangladesh", "BD"),
    ("Nepal", "NP"),
    ("Bhutan", "BT"),
    ("Sri Lanka", "LK"),
    ("Maldives", "MV"),
]


# population data all countries
url_base = "https://world-geo-data.p.rapidapi.com/countries/"
headers = {
    "X-RapidAPI-Key": "e8dcb32d36msh2417d6829510541p15ff3ajsnf7e49772d415",
    "X-RapidAPI-Host": "world-geo-data.p.rapidapi.com"
}

def get_population_data(country, iso_code):
    url = url_base + iso_code
    response = requests.get(url, headers=headers)

    country_data_json = response.json()
    population = country_data_json.get('population')
    return population
    
for country, iso_code in country_data:
    population = get_population_data(country, iso_code)


def get_area(country, iso_code):
    url = url_base + iso_code
    response = requests.get(url, headers=headers)

    area_data_json = response.json()
    area = area_data_json.get('area_size')
    numeric_area = int(re.search(r'\d+', area).group())
    return numeric_area
    
for country, iso_code in country_data:
    numeric_area = get_area(country, iso_code)




