import requests
import json
import webbrowser
from pprint import pprint


r = requests.get("https://dog.ceo/api/breed/basenji/images/random/5")

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("sły format")
else:
    for i in content['message']:
        webbrowser.open_new_tab(i)