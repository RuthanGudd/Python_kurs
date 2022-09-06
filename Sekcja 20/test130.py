from rocket import Rocket, RocketBoard

board = RocketBoard(3)

print(RocketBoard.get_distance(board[0], board[1]))

rocket1 = Rocket(altitude=2)
rocket2 = Rocket(altitude=7)

print(RocketBoard.get_distance(rocket1, rocket2))
