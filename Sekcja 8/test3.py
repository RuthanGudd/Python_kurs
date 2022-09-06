"""
    wyrażenie słownikowe
"""

names = {"Andrzej", "Julianna", "Aleksander", "Piotr", "Irena"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -13, 't3': -4, 't4': 0, 't5': 7, 't6': 17, 't7': 24, 't8': 36.6}

namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

print(namesLength)

multipliedNumbers = {
    number : number**2
    for number in numbers
}

print(multipliedNumbers)

fahrenheit = {
    key : celcius * 1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 10
}

print(fahrenheit)
