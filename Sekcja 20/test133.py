from user import User

"""a = User("Arkadiusz")
b = User("Wiola")
c = User("Karol")

a.name = "xDDD"

print(a.id)
print(b.id)
print(c.id)
print(User.nextId)"""

users = [User() for __ in range(8)]

for user in users:
    print(user.id)

print("Następny id będzie równy: ", User.nextId)
