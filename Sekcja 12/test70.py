"""
Operacje na plikach
write - pisanie do pliku. Jeśli plik istniał to go usunie, jeśli nie istniał to go stworzy
read - (domyślne) czytanie z pliku
append - dopisywanie do pliku

"""

with open("test.txt", "w") as file: 
    file.write("sample")

    print(0 / 0)
    file.write("sample2")
