"""

    Funkcja - blok kodu, do którego można się odwołać w każdej
              chwili, aby otrzymać pożadany przez nas wynik.

    def nazwa_funkcji():
        instrukcja1
        instrukcja2

    nazwa_funkcji()

"""

def wiadomosc_powitalna(imie):
    print("Witaj", imie, "w moim programie")

imiona = ["Arku", "Wiolu", "Bartku"]

for imie in imiona:
    wiadomosc_powitalna(imie)
