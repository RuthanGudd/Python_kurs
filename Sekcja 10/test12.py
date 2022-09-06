"""

    obiekt to zmienna, która ma więcej możliwości,
    można wywołać na nim "funkcj"
    może mieć więcej niż 1 wartość

    immutable - niezmienny
    mytable - zmienny

    obiekty immutable: bool, int, float, tuple, str

    znak '=' to ZMIANA miejsca wskazywania na nowy adres, na inny obiekt
"""

a = 4

listSample = [1, 3, 12, 24]

listSample2 = listSample

listSample2.append(465)

b = a

b = 7
