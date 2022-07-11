import json
import uuid

district = ""
division = ''

with open('bd-upazilas.json') as f:
  upazilas = json.load(f)

with open('bd-districts.json') as f:
  districts = json.load(f)

with open('bd-divisions.json') as f:
  divisions = json.load(f)


for div in divisions['divisions']:
    for dis in districts['districts']:
        if div['id'] == dis['division_id']:
            division = div['name']
            for u in upazilas['upazilas']:
                upazila_upper = u['name'].upper()
                if dis['id'] == u['district_id']:
                    district = dis['name']
                if dis['id'] == u['district_id']: 
                    with open('upazila_seeder.ts', 'a') as f:
                        f.write(f"""[CoreLocalisationServiceUpazilaInformations.{upazila_upper}]: {{
                                    id: '{uuid.uuid4()}',
                                    country_id: bangladeshCountryId,
                                    state_id: '{division}',
                                    district_id: '{district}',
                                    name: '{upazila_upper}',
                                    name_bn: '{str(u['bn_name'])}',
                                    iso_code: '',
                                    is_active: true,
                                    deleted_at: null,
                                }},""")