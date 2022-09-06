"""
JSONplaceholder - miejsce zastępcze na przyszły plik JSON
"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    print("jest OK")
    print(tasks[0])