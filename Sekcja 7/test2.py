# dictionary - słownik

pokoje = {49: 'Andrzej Adahs', 69: 'Julianna Adahs'}        #jest KLUCZ (49) i WARTOŚĆ ('Andrzej Adahs') i może być jedna wartość na klucz

print(pokoje)

pokoje[49] = 'Jan Kowalski'         #zmiana wartości klucza

print(pokoje)

pokoje[50] = 'Kazimierz Nowak'      #dodanie klucza, nie są posortowane

print(pokoje)

# klucz definiuje typ zmiennej (tak jakby), a wartość to wartość, można zrobić klucz string ale trzeba się odwołać jak do stringa

pokoje['imie'] = 'Michał'

print(pokoje)
