"""

Napisać program, który liczy pole:
1) prostokąta
2) kwadratu
3) trójkąta
4) trapezu
5) koła

Korzystać z funkcji, program ma być w formie menu

"""

import math

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a ** 2

def pole_trojkata(a, h):
    return (a * h) / 2

def pole_trapezu(a, b, h):
    return ((a + b) * h) / 2

def pole_kola(r):
    return math.pi * (r ** 2)

while 0 == 0:
    print(" Wybierz co chcesz policzyć: \n 1. Pole prostokąta\n 2. Pole kwadratu\n 3. Pole trójkąta\n 4. Pole trapezu\n 5. Pole koła\n Lub wpisz 'exit' by wyjść")
    x = input()

    if x == 'exit':
        break
    
    elif x == '1':
        a = int(input("Podaj długość pierwszego boku: "))
        b = int(input("Podaj długość drugiego boku: "))
        print("Pole prostokąta: ", pole_prostokata(a, b), "\n")
        continue
    
    elif x == '2':
        a = int(input("Podaj długość boku: "))
        print("Pole kwadratu: ", pole_kwadratu(a), "\n")
        continue

    elif x == '3':
        a = int(input("Podaj długość boku: "))
        h = int(input("Podaj wysokość: "))
        print("Pole trójkąta: ", pole_trojkata(a, h), "\n")
        continue

    elif x == '4':
        a = int(input("Podaj długość pierwszej podstawy: "))
        b = int(input("Podaj długość drugiej podstawy: "))
        h = int(input("Podaj wysokość: "))
        print("Pole trapezu: ", pole_trapezu(a, b, h), "\n")
        continue

    elif x == '5':
        r = int(input("Podaj promień: "))
        print("Pole koła: ", pole_kola(r), "\n")
        continue

    else:
        print("Nieprawidłowa komenda")
