"""
Domyślne argumenty

Jak dasz argument i po nim '=' i wartość to będzie to domyślna wartość argumentu, jeśli nie podasz jego wartości w programie
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

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum += (end - start)

    return sum

def show_massage(message):
    print(message)

    
def increment(x, amount = 1):
    return x + amount

print(function_performance(sumuj_do, liczba))
print(function_performance(sumuj_do2, liczba))
print(function_performance(sumuj_do3, liczba))

