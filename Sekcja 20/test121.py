"""
__init__ - inicjalizacja, czyli ustawienie startowych wartości dla atrybutów

w innych języch __init__ to konstruktor

"""


class User:
    def __init__(self, age, name):
        print("Gówno, stworzyłem obiekt")

        self.age = age
        self.name = name

    def print_user(self):
        print("imię: ", self.name, "\nwiek: ", self.age)


user1 = User(22, "Arek")
user2 = User(24, "Mirek")

user1.print_user()
user2.print_user()
