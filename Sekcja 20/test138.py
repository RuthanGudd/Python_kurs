"""
    Stwórz trzy klasy:
    1) Rectangle - prostokąt
    2) Square - kwadrat
    3) Cube - sześcian

    a) Konstruktory (__init__)
    b) Metody obliczające powierzchnię figur/brył
    c) Metodę obliczającą objętość sześcianu

    Postaraj się wykorzystać dziedziczenie
"""
from figure import Square, Rectangle, Cube

square = Square(5)
rectangle = Rectangle(3, 6)
cube = Cube(5)

print(square.calculate_surface_area())
print(rectangle.calculate_surface_area())
print(cube.calculate_surface_area())
print(cube.calculate_volume())
