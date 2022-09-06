print("Program doda trzy liczby parzyste, nieparzystych nie")

wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj liczbę parzystą, dodatnią: "))
    if x <= 0:
        print("Liczba nie jest liczbą dodatnią")
        continue
    elif x % 2 != 0:
        print("Liczba nie jest liczbą parzystą")
        continue
    wynik += x
    print("Aktualny wynik dodawania to:", wynik)
    i += 1
