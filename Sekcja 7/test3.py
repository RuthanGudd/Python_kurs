"""

czy:    el.unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy       NIE         TAK                 TAK                 TAK
krotki      NIE         TAK                 NIE                 NIE
słowniki    TAK         NIE                 TAK                 TAK
zbioby      TAK         NIE                 NIE                 TAK

            ZBIORY: BONUS w postaci | & - ^
"""

A = {1, -5, 4, 20, -4, 20}      #takie słowniki bez kluczy, elementy są sortowane

print(A)

B = {10, 2, 7, -6, 4}

print(B)

print(A&B)

print(A|B)

print(A-B)

print(A^B)
