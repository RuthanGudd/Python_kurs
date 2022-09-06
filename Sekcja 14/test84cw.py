"""
Napisać skrypt, przy użyciou danych z tąd https://jsonplaceholder.typicode.com/todos
który znajdzie użytkownika z największą liczbą wykonanych zadań i go za to nagrodzi 

napisz to tak by funkcja była uniwersalna
"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def get_keys_with_top_value(dictionary):
    return ([
            key
            for key, value in dictionary.items()
            if value == max(dictionary.values())
    ])

def get_values_per_key(jsonFile):
    valuesPerKey = dict()
    for record in jsonFile:
        if record['completed'] == True:
            try:
                valuesPerKey[record['userId']] += 1
            except KeyError:
                valuesPerKey[record['userId']] = 1

    return(valuesPerKey)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    valuesPerKey = get_values_per_key(tasks)
    keysWithTopValues = get_keys_with_top_value(valuesPerKey)
    print("Najlepsi to", keysWithTopValues)
    