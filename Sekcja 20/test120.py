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
    name = ""

    def print_user(self):
        print("imię: ", self.name, "\nwiek: ", self.age)


user1 = User()
user2 = User()

userList = [User(), User()]

userList[0].age = 99
userList[0].name = "Ktoś"

userList[1].age = 23
userList[1].name = "inny"

userList[0].print_user()
userList[1].print_user()

user1.age = 22
user1.name = "Arek"

user2.age = 24
user2.name = "Mirek"

user1.print_user()
user2.print_user()


# print(seba.age)
# print(mirek.age)
# print(age)
