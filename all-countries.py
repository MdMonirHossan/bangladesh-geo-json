import json
import uuid
import re

with open('bd-upazilas.json') as f:
  upazilas = json.load(f)

with open('bd-districts.json') as f:
  districts = json.load(f)

with open('bd-divisions.json') as f:
  divisions = json.load(f)

with open('continent.json') as f:
  continents = json.load(f)

with open('calling-code.json') as f:
  calling_codes = json.load(f)

asia_regions = ['Southern Asia', 'Western Asia', 'South-eastern Asia', 'Eastern Asia', 'Central Asia']

asia_regions_id = [
    'southernAsiaId', 'westernAsiaId', 'southEasternAsiaId', 'easternAsiaId', 'centralAsiaId'
]

africa_regions_id = [
  'northernAfricaId',
  'subSaharanAfricaId'
]

region_id = ""

# for cont in continents:
#   if cont['region'] == 'Africa':
#     with open('countries.txt', 'a') as f:
#       f.write(f"{cont['name'].upper().replace(' ', '_')} = '{cont['name'].upper()}',\n")
#     for calling in calling_codes:
#       if calling['code'] == cont['alpha-2']:
#         for africa_region_id in africa_regions_id:
#           reg = cont['sub-region'].replace(' ', '')
#           rep = reg.replace('-', '')
#           if re.search(rep, africa_region_id, re.IGNORECASE):
#               region_id = africa_region_id
#               with open('africa_countries_seeder.ts', 'a') as f:
#                 f.write(f"""[CoreLocalisationServiceCountryInformations.{cont['name'].upper().replace(' ', '_')}]: {{
#                             id: '{uuid.uuid4()}',
#                             continent_id: africaContinentId,
#                             region_id: {region_id},
#                             name: '{cont['name']}',
#                             name_bn: '{cont['name']}',
#                             iso_code_one: '{cont['alpha-2']}',
#                             iso_code_two: '{cont['alpha-3']}',
#                             numeric_code: '{cont['country-code']}',
#                             calling_code: '{calling['dial_code']}',
#                             is_active: true,
#                             deleted_at: null,
#                         }},""")

countries = []
for cont in continents:
  if not cont['name'] in countries:
    countries.append(cont['name'])
for c in countries:
  with open('countries.txt', 'a') as f:
    f.write(f"{c.upper().replace(' ', '_')} = '{c.upper()}',\n")

print(countries)