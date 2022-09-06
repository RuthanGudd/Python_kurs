"""

OOP - object oriented programming

obiekty - pojemniki do przechowywania zmiennych i funkcji tematycznie ze sobą powiązanych do dalszego łatwiejszego ponownego użycia

klasy - szablony do tworzenia egzemplarzy obiektów
atrybut - cehca opisująca obiekt
metoda - funkcja operująca na obiekcie

instancja klasy - obiekt który wyszedł z szablonu (klasy)

"""


class User:
    age = 0


class Monitor:
    width = 0
    height = 0
    dimension = 0


seba = User()
mirek = User()

#seba.age = 16
mirek.age = 24

age = 40

print(seba.age)
print(mirek.age)
print(age)

AOC = Monitor()
AOC.width = 32
AOC.height = 20
AOC.dimension = 27

print(type(AOC), AOC, AOC.width, AOC.height, AOC.dimension)
