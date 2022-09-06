import requests
import json
import webbrowser
import credentials
from pprint import pprint

def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format", response.text)
    else:
        return content

def get_favourite_cats(userId):
    params = {
        "sub_id" : userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params, headers=credentials.headers)

    return get_json_content_from_response(r)

def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search', headers=credentials.headers)

    return get_json_content_from_response(r)

def add_favourite_cat(catId, userId):
    catData = {
        "image_id" : catId,
        "sub_id" : userId
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites', json = catData, headers=credentials.headers)

    return get_json_content_from_response(r)

def delete_favourite_cat(favouriteCatId, userId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/' + favouriteCatId, headers=credentials.headers)

    return get_json_content_from_response(r)

print("Zaloguj się")
#pobranie loginu i hasła od użytkownika
#porównanie danytch logowania z bazą danych
#logowanie zaszło poprawnie
#pobranie z bazy danych userId i nazwę użytkownika

userId = "agh2m"
name = "Arkadiusz"

print("Siema " + name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione koty ", favouriteCats)
randomCAt = get_random_cat()
print("Losowy kot: ", randomCAt[0]['url'])
#webbrowser.open_new_tab(randomCAt[0]['url'])

addFavouriteCat = input("Chcesz go dodać do ulubionych? (T/N) ")

if addFavouriteCat.upper() == "T":
    print(add_favourite_cat(randomCAt[0]['id'], userId))
else:
    print("LIPA")

favouriteCatsById = {
    favouriteCat['id'] : favouriteCat['image']['url']
    for favouriteCat in favouriteCats
}

print(favouriteCatsById)
catToBeDeleted = input("Wybierz kota do usunięcia ")
print(delete_favourite_cat(catToBeDeleted, userId))