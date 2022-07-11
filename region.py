import json
import uuid


with open('continent.json') as f:
  continents = json.load(f)

with open('calling-code.json') as f:
  calling_codes = json.load(f)

regions = []

for cont in continents:
    if not cont['region'] == 'Asia':
        if not cont['sub-region'] in regions:
            regions.append(cont['sub-region'])
            with open('region_seeder.ts', 'a') as f:
                f.write(f"""[CoreLocalisationServiceRegionInformations.{cont['sub-region'].upper().replace(' ', '_')}]: {{
                            id: '{uuid.uuid4()}',
                            continent_id: {cont['region']},
                            name: '{cont['sub-region'].upper()}',
                            name_bn: '{cont['sub-region'].upper()}',
                            is_active: true,
                            deleted_at: null,
                        }},""")
# for r in regions:
#   with open('region_list.txt', 'a') as f:
#     f.write(f"{r.upper().replace(' ', '_')} = '{r}',\n")
print(regions)