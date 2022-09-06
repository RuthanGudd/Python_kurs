"""
defaultdict() - domyślny słownik, podajesz typ danych, który ma generować i Ci generuje, nie muisz się 
                martwić odwołaniami do nieistniejących rekordów i tym stuffem
"""
import requests
import json
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def get_keys_with_top_value(dictionary):
    return ([
            key
            for key, value in dictionary.items()
            if value == max(dictionary.values())
    ])

def get_values_per_key(jsonFile):
    valuesPerKey = defaultdict(int)
    for record in jsonFile:
        if record['completed'] == True:
            valuesPerKey[record['userId']] += 1

    return(valuesPerKey)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    valuesPerKey = get_values_per_key(tasks)
    keysWithTopValues = get_keys_with_top_value(valuesPerKey)
    print("Najlepsi to", keysWithTopValues)

#sposób 1 na pobranie danych użytkownika
print("\n######### SPOSÓB 1 #########\n")
r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    if user["id"] in keysWithTopValues:
        print("Najlepszy", user["name"])

#sposób 2 na pobranie danych użytkownika
print("\n######### SPOSÓB 2 #########\n")
for userId in keysWithTopValues:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users/", params = "id=" + str(userId))
    user = r.json()
    #print(user)
    #print("Najlepszy", user["name"])
    print("Najlepszy", user[0]["name"])

#sposób 3 na pobranie danych użytkownika
print("\n######### SPOSÓB 3 #########\n")

def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="
    lastIterationNumber = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIterationNumber):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="

    return conj_param

conj_param = change_list_into_conj_of_param(keysWithTopValues)

r = requests.get("https://jsonplaceholder.typicode.com/users/", params=conj_param)

users = r.json()

for user in users:
    print("Najlepszy", user["name"])