from random import randint


class Rocket:
    def __init__(self, speed=1):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed


rockets = [Rocket(randint(1, 6)) for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, 4)
    rockets[rocketIndexToMove].moveUp()

"""
for i in range(5):
    newRocket = Rocket()
    rockets.append(newRocket)


print(rockets)

rockets[0].moveUp()
rockets[1].moveUp()
rockets[2].moveUp()
rockets[2].moveUp()
rockets[2].moveUp()
"""
for rocket in rockets:
    print(rocket.altitude)
