import json
import uuid
import re

data = {}
all_country = []

with open('countries-details.json') as f:
  countries = json.load(f)

for country in countries:
    name = country['name']['common']
    official_name = country['name']['official']
    numeric_code = country['ccn3']
    alpha_2 = country['cca2']
    alpha_3 = country['cca3']
    currencies = country['currencies']
    capital = country['capital']
    continent = country['region']
    region = country['subregion']
    languages = country['languages']
    lat = country['latlng'][0]
    long = country['latlng'][1]
    borders = country['borders']
    area = country['area']
    calling_codes = country['callingCodes']
    data["name"] =  name
    data["official_name"] = official_name
    data["country_code"] = numeric_code
    data["alpha_2"] = alpha_2
    data["alpha_3"] = alpha_3
    data["currencies"] = currencies
    data["capital"] = capital
    data["continent"] = continent
    data["region"] = region
    data["languages"] = languages
    data["lat"] = lat
    data["long"] = long
    data["borders"] = borders
    data["area"] = area
    data["calling_codes"] = calling_codes
    all_country.append(data)
    with open('countries-details-short.json',  'a', encoding='utf-8') as file:
      json.dump(data, file)