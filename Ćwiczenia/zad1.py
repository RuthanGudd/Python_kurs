"""
Wypisać liczby nieparzyste, poniżej 50 malejąco
"""

n = 50
while n > 0:
    if n % 2 != 0:
        print(n)
    n -= 1
