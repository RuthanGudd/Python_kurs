class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_surface_area(self):
        return (self.width * self.height)


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


"""class Cube(Square):
    def calculate_surface_area(self):
        return (super().calculate_surface_area() * 6)

    def calculate_volume(self):
        return (super().calculate_surface_area() * self.height)
"""


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.height = square.height

    def calculate_surface_area(self):
        return self.square.calculate_surface_area() * 6

    def calculate_volume(self):
        return self.square.calculate_surface_area() * self.height


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def calculate_surface_area(self):
        return (2 * self.base.calculate_surface_area() +
                2 * self.base.width * self.height +
                2 * self.base.height * self.height)

    def calculate_volume(self):
        return (self.base.calculate_surface_area() * self.height)
