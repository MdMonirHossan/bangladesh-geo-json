import json

data = {}
data['divisions'] = []
data['districts'] = []

with open('bd-divisions.json') as f:
  divisions = json.load(f)

with open('bd-districts.json') as f:
  districts = json.load(f)

with open('bd-upazilas.json') as f:
  upazilas = json.load(f)

with open('bd-postcodes.json') as f:
  post_offices = json.load(f)

for division in divisions['divisions']:
    division_id = division['id']
    division['districts'] = []
    data['divisions'].append(division)
    # with open('output.json', 'w') as outfile:
        # json.dump(data, outfile)
    for district in districts['districts']:
        district_id = district['id']
        district['upazilas'] = []
        if division_id == district['division_id']:
            division['districts'] .append(district)
        for upazila in upazilas['upazilas']:
            upazila_name = upazila['name']
            upazila['post_offices'] = []
            if district_id == upazila['district_id']:
                district['upazilas'].append(upazila)
                with open('output.json', 'w', encoding='utf-8') as outfile:
                        json.dump(data, outfile)
            # for post_office in post_offices['postcodes']:
            #     if upazila_name == post_office['upazila']:
            #         upazila['post_offices'].append(post_office)
            #         with open('output.json', 'w') as outfile:
            #             json.dump(data, outfile)

# for district in districts['districts']:
#     district_id = district['id']
#     print(district['name'])