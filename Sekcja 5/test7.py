"""
Program ma pytać użytkownika o liczbę i sprawdzał czy jest równa sekretnej liczbie,
ma informować użytkownika czy jest blisko szukanej liczby i od której strony (czy za mało itd)
"""

print("Spróbuj zgadnąć sekretną liczbę")

x = 3890

while 0 == 0:
    a = int(input("Podaj liczbę: "))
    if a > x:
        print("Twoja liczba jest większa od sekretnej")
        continue
    elif a < x:
        print("Twoja liczba jest mniejsza od sekretnej")
        continue
    else:
        print("Udało Ci się zgadnąć! Sekretna liczba to:", a)
        break
