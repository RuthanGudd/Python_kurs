# TYPY ZAGNIEŻDŻONE

imie = "Andrzej"
wiek = 24
plec = "mężczyzna"

imie2 = "Janina"
wiek2 = 67
plec2 = "kobieta"

osoba1 = ('Andrzej', 24, 'mężczyzna')
osoba2 = ('Janina', 67, 'kobieta')
osoba3 = ('Jakub', 33, 'mężczyzna')

listaGosci = {
                ('Andrzej', 24, 'mężczyzna'),
                ('Janina', 67, 'kobieta'),
                ('Jakub', 33, 'mężczyzna')
            }

listaGosci2 = {
                ('Janina', 67, 'kobieta'),
                ('W', 56, 'kobieta'),
                ('K', 23, 'mężczyzna')
            }


listaGosci3 =  listaGosci & listaGosci2
