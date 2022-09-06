wybor = input(" * - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if (wybor == "*"):
    print("Wynik: ", a, "*", b, "=", a * b)
elif(wybor == "/"):
    print("Wynik: ", a, "/", b, "=", a / b)
elif(wybor == "+"):
    print("Wynik: ", a, "+", b, "=", a + b)
elif(wybor == "-"):
    print("Wynik: ", a, "-", b, "=", a - b)
else:
    print("Błąd")
