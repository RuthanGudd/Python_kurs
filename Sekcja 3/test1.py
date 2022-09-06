imie = "Andrzej" #deklaracja zmiennej string

print(imie) #funkcja print wywołująca argument będący zmienną typu string
            #zadeklarowaną wyżej. "print" to nazwa funkcji, "( )" to wywołanie
            #funkcji, a "imie" to argument funkcji


#stronka z bibliotekami pythona to "docs.python.org"

import math     #importowanie biblioteki "math" zawierającej funkcje matematyczne

a = math.sqrt(4)    #deklaracja zmiennej zawierającej funkcję pierwiastkującą

print(a) 

from math import sqrt   #importowanie funkcji z biblioteki
                        #nie musisz wtedy pisać nazwy biblioteki przed funkcją
                        #ale możesz użyć tylko tej jednej funkcji w ten sposób

b = sqrt(16)

print(b) 

from math import *  #importowanie wszystkich funkcji z biblioteki
                    #tak że nie trzeba pisać nazwy biblioteki przed funkcjami

