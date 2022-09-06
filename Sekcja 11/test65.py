"""
Napisz funkcję, która zasymuluje jak działa lotto (wybierz 6 unikalnych liczb z 49)
"""

import random
from collections import Counter

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen", 
            "King", "King", "King", "King", 
            "Ace", "Ace", "Ace", "Ace", 
            "Joker", "Joker"]

random.shuffle(cardList)

#Zrtobić tak, żeby były dwie listy z kartami obu graczy i żeby każdy miał unikalne karty

def rozdanie_wojna(cardlist):
    gracz1 = []
    gracz2 = []
    while len(cardlist) > 0:
        gracz1.append(cardList.pop())
        gracz2.append(cardList.pop())
    print(gracz1)
    print(len(gracz1), Counter(gracz1))
    print(gracz2)
    print(len(gracz2), Counter(gracz2))

print(cardList, "\n", len(cardList))
rozdanie_wojna(cardList)


def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

def choose_random_numbers2(amount, total_amount):
    chosen = []
    i = 0
    while i < amount:
        x = random.randint(0, total_amount + 1)
        if len(chosen) == 0:
            chosen.append(x)
            i += 1
            continue
        else:
            if x in chosen:
                continue
            else:
                chosen.append(x)
                i += 1  
    print(chosen)

def another_one(amount, total_amount):
    chosen = []
    i = 0
    c = 0
    while i < amount:
        c += 1
        x = random.randint(0, total_amount + 1)
        if x in chosen:
            continue
        else:
            chosen.append(x)
            i += 1
    print(chosen)

#choose_random_numbers(6, 49)
#choose_random_numbers2(6, 49)
#another_one(6, 49)

