"""
Operacje na plikach
w   write - pisanie do pliku. Jeśli plik istniał to go usunie, jeśli nie istniał to go stworzy
r   read - (domyślne) czytanie z pliku
a   append - dopisywanie do pliku

read
readline
readlines
splitlines

tell - wskaźnik końca operacji na pliku
seek - zmienia miejsce wskaźnika na to wskazane w kodzie

r+  read+write - do czytania i pisania
w+  write+read - do pisania i czytania (różnica to usunięcie pliku gdy istnieje, lub stworzenie gdy nie istnieje)
a+  append+read - dopisywanie i czytanie (jak plik nie istniał to go stworzy)
                    wskźnik dopisywania zawsze na końcu

w tych trybach trzebqa pamiętać o manipulacji wskaźnikiem przy czytaniu
"""
with open("oceany2.txt", "a+", encoding = "UTF-8") as file:
    file.write("\nKolejny Ocean")
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("\nJakiś jeszcze ocean")
    file.seek(0)
    print(file.read().splitlines())