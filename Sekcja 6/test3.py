# len() - ilość elementów w liście
# .append() - dodaje jeden element na końcu listy
# .extend() - dodaje wiele elementów na końcu listy
# .insert(index, co) - dodaje element w środku listy, trzeba podać indeks
# .index() - indeks danego elementu
# sort(reverse = True) - sortowanie rosnąco/malejąco
# max() - zwraca największą wartość z listy
# min() - zwraca najmniejszą wartość z listy
# .count() - ile razy wystąpił element w liście
# .pop() - usuwa ostatni element
# .remove() - usuwa pierwszy napotkany element
# .clear() - usuwa wszystkie elementy z listy
# .reverse() - odwraca kolejność elementów w liście

lista1 = [54, 1, -2, 20, 1]
lista2 = ["Arkadiusz", "Wioletta"]

print(len(lista1))

lista1.append(4)
print(lista1)

lista1.extend([23, 656, 1, 767])
print(lista1)

lista2.insert(0, "Jakub")
print(lista2)

print(lista1.index(1))

lista1.sort(reverse = True)
print(lista1)

print(lista1.count(1))

lista1.remove(1)
print(lista1)
