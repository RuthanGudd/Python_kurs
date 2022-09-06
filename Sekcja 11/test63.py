"""
choice -        zwraca losowy element
choices -       zwraca listę elementów i ma większe możliwości
"""

import random
from collections import Counter

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

#print(random.choice(movieList))

print(Counter(random.choices(nagrodaZeSkrzynki, [80, 15, 4, 1], k = 100)))