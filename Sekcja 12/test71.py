"""
Operacje na plikach
write - pisanie do pliku. Jeśli plik istniał to go usunie, jeśli nie istniał to go stworzy
read - (domyślne) czytanie z pliku
append - dopisywanie do pliku

read
readline
readlines
splitlines

"""
with open("oceany.txt", "r", encoding = "UTF-8") as file:
    #oceany = file.read().splitlines()
    #oceany = file.readline()
    #oceany = file.readlines()
    #print(oceany)
    for line in file:
        print(line)