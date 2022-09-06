"""
Operacje na plikach
write - pisanie do pliku. Jeśli plik istniał to go usunie, jeśli nie istniał to go stworzy
read - (domyślne) czytanie z pliku
append - dopisywanie do pliku

read
readline
readlines
splitlines

tell - wskaźnik końca operacji na pliku
seek - zmienia miejsce wskaźnika na to wskazane w kodzie

"""
with open("oceany.txt", "a", encoding = "UTF-8") as file:
    print(file.tell())
    file.write("\nKolejny")