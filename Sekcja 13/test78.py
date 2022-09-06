"""
JSON

json.dumps(data) - zapisuje dane do postaci stringowej JSON
json.dump(data, nameOfFile, ensure_ascii = False) - zapisuje dane do pliku w postaci JSON
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

print(json.dumps(film))
print(type(json.dumps(film)))
print(json.dumps(film, ensure_ascii = False))

encodedFilm = json.dumps(film, ensure_ascii = False)

with open("sample.json", "w", encoding="UTF-8") as file:
        json.dump(film, file, ensure_ascii=False)

"""
{
        "title": "Ale ja nie będę tego robił!",
        "release_year": 1969,
        "won_oskar": true,
        "actors": [
            "Arkadiusz Włodarczyk", 
            "Wioletta Włodarczyk"
        ],
        "budget": null,
        "credits": {
                "director": "Arkadiusz Włodarczyk",
                "writer": "Alan Burger",
                "animator": "Anime Animatrix"
                }
}
"""