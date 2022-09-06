import requests
import json
from pprint import pprint

animalType = input("Podaj typ zwierzęcia (cat/dog): ")
print(animalType)

params = {
            "amount" : 5,
            "animal_type" : animalType
         }

r = requests.get("https://cat-fact.herokuapp.com/facts/random/", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Zły format")
else:
    i = 1
    for item in content:
        print("Fact nr", i, "\n", item['text'], "\n")
        i += 1