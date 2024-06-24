
import json
import requests

with open('leaders.json', 'r', encoding='utf-8') as f:
    leaders_per_country = json.load(f)

for country_code, leaders_data in leaders_per_country.items():
    for leader in leaders_data:
        if 'birth_date' in leader:
            print(f"Country Code: {country_code}")
            print(f"Leader: {leader['first_name']} {leader['last_name']}")
            print(f"Birth Date: {leader['birth_date']}")
            print()
