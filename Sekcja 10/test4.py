"""
Funkcja jako argument innej funkcji
"""

import time

liczba = int(input("Podaj liczbę: "))

def sumuj_do(liczba):
    suma = 0
    
    for cyfra in range(1, liczba + 1):
        suma += cyfra
        
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])

def sumuj_do3(liczba):
    return (1 + liczba) / 2 * liczba

def finish_timer(start):
    end = time.perf_counter()
    return end - start

def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

def show_massage(message):
    print(message)

print(function_performance(sumuj_do, liczba))
print(function_performance(sumuj_do2, liczba))
print(function_performance(sumuj_do3, liczba))

"""
start = time.perf_counter()
print(sumuj_do(liczba))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(liczba))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do3(liczba))
print(finish_timer(start))
"""
