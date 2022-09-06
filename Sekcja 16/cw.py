import json
import requests
import webbrowser

from pprint import pprint
from credentials import header

def get_json_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("\nWrong Format\n", response.text)
    else:
        return content

def get_favourite_dogs(userId):
    params = {
        "sub_id" : userId
    }

    r = requests.get("https://api.thedogapi.com/v1/favourites", params=params, headers=header)

    return get_json_from_response(r)

def add_image_to_favourites(dogId, userId):
    dogData = {
        "image_id" : dogId,
        "sub_id" : userId
    }

    r = requests.post("https://api.thedogapi.com/v1/favourites", json=dogData, headers=header)

    return get_json_from_response(r)

def get_random_dog():
    r = requests.get("https://api.thedogapi.com/v1/images/search", headers=header)

    return get_json_from_response(r)[0]

userId = "agh2m"
name = "Arkadiusz"

randomDog = get_random_dog()
imageid = randomDog['id']

#add_image_to_favourites(id, userId)
#pprint(get_favourite_dogs(userId))

