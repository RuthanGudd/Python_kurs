import requests
import json
from pprint import pprint

params = {
    "api_key" : "0301a3107ae913f0ed60949300536c87ac0c77fa",
    "country" : "pl",
    "year" : 2022,
    "month" : 12
         }

r = requests.get("https://calendarific.com/api/v2/holidays/", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("sły format")
else:
    pprint(content)