def add():
    global c
    c = c + 4
    print(c)

def sth(a, amount = 1):
    a = a + amount
    print(a)

c = 1
add()
print(c)

a = 1
sth(a)
print(a)
