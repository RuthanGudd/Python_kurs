"""
Operacje na plikach
write - pisanie do pliku. Jeśli plik istniał to go usunie, jeśli nie istniał to go stworzy
read - (domyślne) czytanie z pliku
append - dopisywanie do pliku

"""

a = 5

file = open("Sekcja 12/test", "w")

file.write("sample")
file.close()