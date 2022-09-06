"""
JSON

json.dumps(data) - zapisuje dane do postaci stringowej JSON
json.dump(data, nameOfFile, ensure_ascii = False) - zapisuje dane do pliku w postaci JSON

json.loads(jsonstring) - przetwarza jsonstring na dane typu Python
json.load(filePointer) - wczytuje json z pliku i zwraca jako wynik metody dane typu python

indent = 4
sort_keys = True

pprint - biblioteka do ładnego wypisywania plików z JSON

"""
import json

film = {
        "title": "Ale ja nie będę tego robił!",
        "release_year": 1969,
        "won_oskar": True,
        "actors": ("Arkadiusz Włodarczyk", "Wioletta Włodarczyk"),
        "budget": None,
        "credits": {
                "director": "Arkadiusz Włodarczyk",
                "writer": "Alan Burger",
                "animator": "Anime Animatrix"
                }
}

encodedFilm = json.dumps(film, ensure_ascii = False, indent=4, sort_keys = True)
#print(encodedFilm)

with open("sample.json", "w", encoding="UTF-8") as file:
        json.dump(film, file, ensure_ascii=False, indent=4, sort_keys = False)

with open("sample.json", "r", encoding="UTF-8") as file:
        wynik = json.load(file)
        
#print(json.dumps(wynik, ensure_ascii = False, indent=4, sort_keys = True))

import pprint

pprint.pprint(wynik)