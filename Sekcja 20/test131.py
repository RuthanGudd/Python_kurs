from rocket import Rocket, RocketBoard

myRocket = Rocket(altitude=3, longitude=4)
anotherRocket = Rocket(altitude=1, longitude=31)

x: int = RocketBoard.get_distance(myRocket, anotherRocket)

print(x)
