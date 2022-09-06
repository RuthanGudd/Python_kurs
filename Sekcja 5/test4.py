wynik = 0

"""
i = 0
while i < 4:
    x = int(input("Podaj liczbe: "))
    wynik += x
    i += 1

print("Wynik dodawania liczb to:", wynik)
"""

for i in range(0, 4):       #funkcja range() nie potrzebuje pierwszego argumentu, można pisać samą 4 i też się wykona 4 razy bo zawsze liczy od zera gdy zdefiniujemy przedział
    x = int(input("Podaj liczbe: "))
    wynik += x

print("Wynik dodawania liczb to:", wynik)
