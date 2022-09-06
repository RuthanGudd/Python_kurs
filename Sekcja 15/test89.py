import requests
import json
import pprint

params = {
            "site" : "stackoverflow", 
            "sort" : "votes", 
            "order" : "desc",
            "fromdate" : "2022-07-20",
            "tagged" : "python",
            "min" : "10"
         }

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint.pprint(questions)