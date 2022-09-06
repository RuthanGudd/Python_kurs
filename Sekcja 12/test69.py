"""
Operacje na plikach
write - pisanie do pliku. Jeśli plik istniał to go usunie, jeśli nie istniał to go stworzy
read - (domyślne) czytanie z pliku
append - dopisywanie do pliku

"""

try:
    file = open("test.txt", "w")
    file.write("sample")

    print(0 / 0)
    file.write("sample2")

finally:
    file.close()