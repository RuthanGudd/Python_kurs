"""

Znajdź liczby od 100 do 470 włącznie, które są podzielne przez 7 ale niepodzielne przez 5

Z czego skorzystasz?
1) generatora
2) wyrażenia listowego
3) wyrażenia zbioru
4) wyrażenia słownikowego

Zastanów się, czy odpowiedź na to pytanie jest zawsze taka sama?

"""

numbers = [
    number
    for number in range(100,471)
    if number % 7 == 0
    if number % 5 != 0
]

print(numbers)
