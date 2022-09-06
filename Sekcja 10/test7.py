"""
    Argumenty kluczowe i pozycyjne
    kluczowy - w postaci: klucz - wartość (domyślny)
    pozycyjne - takie, których kolejność przy wywołaniu ma znaczenie
"""

def greet(name, message = "Jak się masz", separator=" "):
    print(message, name, sep=separator)

greet("Andrzej", "Witaj", "\n")

greet("Chuju", separator="\n")
