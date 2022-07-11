import json
import uuid

data = {}
data['divisions'] = []
data['districts'] = []
all_districts = []


with open('bd-districts.json') as f:
  districts = json.load(f)

with open('bd-divisions.json') as f:
  divisions = json.load(f)

division = ""

for district in districts['districts']:
    all_districts.append(district['name'].upper())
    district_upper = district['name'].upper()
    for div in divisions['divisions']:
        if div['id'] == district['division_id']:
            division = div['name']
    with open('district_seeder.ts', 'a') as f:
        f.write(f"""[CoreLocalisationServiceDistrictInformations.{district_upper}]: {{
                    id: '{uuid.uuid4()}',
                    country_id: bangladeshCountryId,
                    state_id: '{division}',
                    name: '{district_upper}',
                    name_bn: '{str(district['bn_name'])}',
                    iso_code: '',
                    is_active: true,
                    deleted_at: null,
                }},""")
    with open('district_list.txt', 'a') as f:
        f.write(f'{district_upper} = "{district_upper}",\n')

# for d in all_districts:
#     with open('district_seeder.txt', 'a') as f:
#         f.write(f"""[CoreLocalisationServiceDistrictInformations.DHAKA]:
#                     id: '{uuid.uuid4()}',
#                     country_id: bangladeshCountryId,
#                     name: '{d}',
#                     name_bn: '{str(d)},
#                     iso_code: '',
#                     is_active: true,
#                     deleted_at: null,
#                 ,""")

print(all_districts)