from rocket import Rocket, RocketBoard

board = RocketBoard(3)
rocket = Rocket(altitude=4)
print(rocket.altitude)

board[0].x = 4

print(board[0].get_distance(board[1]))
