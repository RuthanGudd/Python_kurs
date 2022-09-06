from math import sqrt
from random import randint


class Rocket:
    nextId = 1

    def __init__(self, speed=1, altitude=0, longitude=0):

        self.altitude = altitude
        self.speed = speed
        self.longitude = longitude
        self.id = Rocket.nextId
        Rocket.nextId += 1

    def moveUp(self):
        """poruszamy się do góry (altitude) z szybkością (speed)
        """
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    # Nie można używać self, można wywołać poprzez nazwę klasy (lepiej, czytelniej),
    # lub instancję klasy
    def get_distance(obj: Rocket, obj2: Rocket) -> float:
        alt = (obj.altitude - obj2.altitude) ** 2
        long = (obj.longitude - obj2.longitude) ** 2
        return sqrt(alt + long)

    def get_amount_of_rockets(self):
        return len(self.rockets)

    # Można użyć metody w klasie w której została zaimplementowana, przydatne choć pewnie rzadko
    def __len__(self):
        return self.get_amount_of_rockets()
