"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ
Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC
Skrzynki mają różne kolory. Kolor skrzynki oznacza jak rzadka jest ta skrzynka:
zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota - 1%

Ustaw, że kest 40% szansy na NIC, 60% na skrzynkę
Ustaw Gold jako drop:
zielony - 100
pomarańczowy - 400
fioletowy - 900
złoty - 1600

pamiętaj o:
1. czystym kodzie
2. nazywaniu zmiennych tak by były samoopisujące się
3. po angielsku
"""

import random
from enum import Enum

def findApproximateValue(value, percentRange):
    lowestValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowestValue, highestValue)

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }

eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

Color = Enum('Color', 
                    {'Green': 'green',
                    'Orange': 'orange',
                    'Purple': 'purple',
                    'Gold': 'gold'
                    })

chestColorDictionary = {
                               Color.Green: 0.75,
                               Color.Orange: 0.2,
                               Color.Purple: 0.04,
                               Color.Gold: 0.01
                             }

chestColorList = tuple(chestColorDictionary.keys())
chestColorProbability = tuple(chestColorDictionary.values())

rewardsForChest = {
                    chestColorList[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(chestColorList))
                  }

rounds = 5
goldAcquired = 0

print("Welcome to the GAME!\nYou have 5 rounds.")

while rounds > 0:
    gamerAnswer = input("Are you ready?")
    if (gamerAnswer == "yes"):
        print("OK, LET'S GO!")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("You've drawn CHEST!")
            drawnChest = random.choices(chestColorList, chestColorProbability)[0]
            print("Chest color is", drawnChest.value)
            gamerReward = findApproximateValue(rewardsForChest[drawnChest], 10)
            print("You've acquired", gamerReward)
            goldAcquired += gamerReward
        elif (drawnEvent == Event.Empty):
            print("You're unlucky, you've drawn NOTHING")

    else:
        print("You must be ready...")
        continue

    rounds -= 1

print("Total gold you've acquired is", goldAcquired)