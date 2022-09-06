"""
Wczytaj imiona i nazwiska z pliku imionanazwiska.txt

1. Rozdziel je tak by powstała lista krotek, gdzie krotki to pary imię/nazwisko
2. Zapisz imiona do pliku imiona.txt
3. Zapisz nazwiska do pliku nazwiska.txt

PROBLEM - co zrobić gdy przy imieniu nie ma nazwiska
"""

imionanazwiska = []

with open("imionanazwiska.txt", "r", encoding = "UTF-8") as file:
    for line in file:
        imionanazwiska.append(tuple(line.replace("\n", "").split(" ")))

with open("imiona.txt", "w", encoding = "UTF-8") as file:
    for item in imionanazwiska:
        file.write(item[0] + "\n")

with open("nazwiska.txt", "w", encoding = "UTF-8") as file:
    for item in imionanazwiska:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
        
        """if (len(item) == 2):
            file.write(item[1] + "\n")
        else:
            file.write("\n")"""