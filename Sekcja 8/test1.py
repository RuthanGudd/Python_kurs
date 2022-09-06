liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)


potegiDwojki2 = [element**2
                 for element in liczby
                 ]

liczbyParzyste2 = [element
                   for element in liczby
                   if (element % 2 == 0)
                   ]

print("liczby", liczby)
print("potegiDwojki", potegiDwojki)
print("liczbyParzyste", liczbyParzyste)
print("potegiDwojki2", potegiDwojki2)
print("liczbyParzyste2", liczbyParzyste2)

"""
[co_zrobić_na_elemencie
 for_element_in_stara_lista
 warunek_oparty_na_elemencie]
"""
