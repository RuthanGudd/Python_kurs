"""
Stworzyć funkcję generującą w nieskończoność liczby będące swoim kwadratem, czyli 1*1, 2*2, 3*3 itd.
najpierw wygeneruj 20 elementów, potem kolejne 30
zapisać wygenerowane liczby w jednej liście
"""

def generate_infinite_powered_numbers():
    x = 1
    while True:
        yield (x ** 2)
        x += 1

generatedNumbers = []

numberGenerator = generate_infinite_powered_numbers()

for k in range(20):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)

for j in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)

numbers = []
a = 1
for element in generatedNumbers:
    numbers.append(element / a)
    a += 1

print(numbers)