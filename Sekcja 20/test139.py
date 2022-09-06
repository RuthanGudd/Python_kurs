"""
    Asocjacja - przyporządkowanie obiektu do innej klasy
    Agregacja - tworzenie obiektu składowego
    Kompozycja - agregacja ale obiekt przyporządkowywany nie może istnieć
                 bez klasy do której przyporządkowywujemy
"""

from figure import Square, Rectangle, Cube, Cuboid

square = Square(5)
rectangle = Rectangle(3, 6)
cube = Cube(Square(8))
cuboid = Cuboid(Rectangle(6, 7), 7)

print(cuboid.calculate_surface_area())
print(cube.calculate_surface_area())
