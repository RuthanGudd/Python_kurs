"""
JSON

json.dumps(data) - zapisuje dane do postaci stringowej JSON
json.dump(data, nameOfFile, ensure_ascii = False) - zapisuje dane do pliku w postaci JSON

json.loads(jsonstring) - przetwarza jsonstring na dane typu Python
json.load(filePointer) - wczytuje json z pliku i zwraca jako wynik metody dane typu python

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

encodedRetrievedMovie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oskar": true, "actors": ["Arkadiusz Włodarczyk", "Wioletta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodedMovie = json.loads(encodedRetrievedMovie)
print(decodedMovie)

with open("sample.json", "r", encoding="UTF-8") as file:
        wynik = json.load(file)
        print(wynik)