"""
    wyrażenie słownikowe
"""

names = {"andrzej", "Julianna", "aleksander", "Piotr", "irena", "Janina", "Jakub", "wioletta", "arkadiusz", "michał"}

names = {
    name.capitalize()
    for name in names
}

print(names)

