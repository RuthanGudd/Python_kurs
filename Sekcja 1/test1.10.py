imie = "Andrzej" #deklaracja zmiennej typu string zawierającej imię

nazwisko = "Adahs" #deklaracja zmiennej typu string zawierającej nazwisko

pelne = imie + " " + nazwisko

print(pelne) 

dlugiString = "To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym\
To jest jakiś tekst o niczym"   #deklaracja zmiennej typu string z
                                #wieloliniowym stringiem, metoda pierwsza

print(dlugiString)

dlugiString2 = """To jest jakiś tekst o niczym 
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym
To jest jakiś tekst o niczym """    #deklaracja zmiennej typu string z
                                    #wieloliniowym stringiem, metoda druga

print(dlugiString2)

print(imie[4]) #wypisanie konkretnej pozycji stringa licząc od początku
               #ciągu znaków

print(imie[-1]) #wypisanie konkretnej pozycji stringa licząc od końca
                #ciągu znaków

print(imie[2:5]) #komenda wypisania konkretnego ciągu pozycji w stringu
                    #czyli od 2 do 5, bez 5

