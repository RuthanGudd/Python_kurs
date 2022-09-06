"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
"""

Slownik = {                                                             #Słownik, niejako baza danych na której program będzie operować
        'bułka': 'Taki mały chleb',
        'chleb': 'podukt pszenny o dużej zawartości węglowodanów',
        'owoc': 'cośtam gówno'
        }

menu = [                                #Lista z pozycjami z menu opcji użytkownika, co by nie trzeba było listy wklejać do pętli
    "1. Znajdź definicję w słowniku",
    "2. Dodaj nową definicję",
    "3. Usuń istniejącą definicję",
    "4. Zakończ działanie programu"
        ]

while 0 == 0:                                                                   #Pętla głowna programu
    print("\n", menu[0], "\n", menu[1], "\n", menu[2], "\n", menu[3], "\n")     #Wypisanie opcji z menu, tak żeby wyglądały ładnie - jak menu
    opcja = int(input(" Wybierz odpowiednią funkcję: "))                        #pole do wpisania dla użytkownika żeby mógł wybrać opcję progamu
    while opcja == 1:                                                           #pętla z opcją pierwszą - znalezienie definicji w słowniku. 
        print("\n", "Jeśli chcesz wyjść do menu głównego napisz 'wyjdź'")       #Informacja o metodzie wyjścia do menu głównego - przerwaniu pętli
        szukana = input(" Podaj szukaną definicję: ")                           #Pole do wpisania dla użytkownika szukanej definicji, od razu przypisuje ciąg znaków od użytkownika do zmiennej, która będzie służyła do znalezienia definicji
        if szukana in Slownik:                                                  #Instrukcja warunkowa nr. 1 (warunek to zmienna z ciągiem znaków od użytkownika) - jeśli definicja jest w słowniku to program ją wypisuje na ekranie i można powtórzyć operację
            print("\n", szukana, "-", Slownik[szukana])
            continue
        elif szukana == 'wyjdź':                                                #Instrukcja warunkowa nr. 2 (warunek jak wyżej) - jeśli wartość zmiennej szukana to komenda wyjścia z pętli, pętla się przerywa
            break
        elif szukana not in Slownik:                                            #Instrukcja warunkowa nr. 3 - jeśli w słowniku nie ma szukanej definicji to program wyświetla stosowną informację
            print("\n", "Nie ma takiej definicji w Słowniku")
            continue
    while opcja == 2:                                                           #Pętla do dodania definicji do słownika
        print("")
        klucz = input(" Podaj nazwę definicji: ")                               #pole do wpisania, ciąg znaków od użytkownika jest wpisywany do zmiennej klucz - słowa definiowanego przez wartosc
        wartosc = input(" Podaj treść definicji: ")                             #pole do wpisania, ciąg znaków od użytkownika jest wpisywany do zmiennej wartosc - definicji klucza
        Slownik[klucz] = wartosc                                                #komenda dodająca definicję do słownika
        print("\n", klucz, ":", Slownik[klucz], "\n")                                       #komenda wypisująca nową definicję na ekranie
        kolejna = input(" Chcesz dodać kolejną definicję? (Wpisz 'nie' by wyjść do Menu): ")        #pole do wpisania - można dodać kolejną definicję lub wyjść z pętli do menu głównego
        if kolejna == 'nie':                                                    #Instrukcja warunkowa. Jeśli ciąg znaków wpisany przez użytkownika to komenda wyjścia z pętli to wraca do menu głownego, w przeciwnym wypadku można dodać kolejną definicję
            break
        else:
            continue
    while opcja == 3:       #pętla do usunięcia definicji ze słownika
        print("")
        usun = input(" Podaj nazwę definicji do usunięcia (Wpisz 'wyjdź' by wrócić do głównego menu): ")    #pole do wpisania nazwy definicji do usunięcia
        if usun == 'wyjdź':             #jeśli użytkownik wpisze komendę wyjścia, nastąpi powrót do menu głównego
            break
        elif usun in Slownik:         #jeśli jest taka definicja w słowniku, zostanie ona usunięta, program wyświetli o tym informację, a pętla będzie zrestartowana - można usunąć kolejną
            del Slownik[usun]
            print("\n", "Definicja", usun, "została usunięta.")
            continue
        else:                   #jeśli nie będzie szukanej definicji to będzie wyświetlona informcja a pętla zrestartowana
            print("\n", "Nie znaleziono definicji, spróbuj ponownie")
            continue
    if opcja == 4:      #Jeśli użytkownik wybierze opcję 4 z menu głownego to progam się wyłączy
        break
