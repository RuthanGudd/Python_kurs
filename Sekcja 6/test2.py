# in
# not in
# Operacje na listach

imiona = ["Arkadiusz", "Wojtek", "Wioletta", "Karol", "Joanna", "Jakub"]
liczby = [3, 12, 42, -6, -76, 54, -34]

print("Arkadiusz" in imiona)
print("asdfas" in imiona)

if ("Wojtek" in imiona):
    print("Cześć Wojtek")

if (2 not in liczby):
    print("Nie ma dwójeczki")
else:
    print("Jednak jest xD")

print(liczby)
liczby = [6, 34, -56, 234] + liczby
print(liczby)
print(3 * imiona)
