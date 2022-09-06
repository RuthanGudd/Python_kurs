"""
random() -              losuje z podanego przedziału, gdy damy jedną liczbę to przedział zaczyna się od 0
uniform() -             random ale na floatach
randrange() -           podajesz koniec zakresu z którego ma wylosować liczbę całkowitą, lub podajesz zakres z którego ma losować i po przecinku np. 2 to wylosuje parzyste z tego zakresu - 
randrange(0, 15, 2) -   poprzednia linia
randint() -             podajesz zakres z którego ma wylosować liczbę
"""

import random
from collections import Counter

x = 0

while x < 100:
    #print(random.random())
    #print(random.uniform(0, 100))
    x += 1 

def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"

x = 0
listHit = []

while x < 100:
    listHit.append(will_weapon_hit(50))
    x += 1 

dictionaryHit = Counter(listHit)

#print(listHit)
print(dictionaryHit)

x = 0

while x < 100:
    #print(random.randrange(10))
    print(random.randint(0, 10))
    x += 1 
