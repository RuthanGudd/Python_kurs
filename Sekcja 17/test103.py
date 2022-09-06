from numpy import number


def generate_infinite_powered_numbers():
    number = 0
    while True:
        number = yield (number ** 2)

generatedNumbers = []

numberGenerator = generate_infinite_powered_numbers()

#print(next(numberGenerator))
print(numberGenerator.send(None))
print(numberGenerator.send(20))


for i in range(20):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)

for i in range(20, 50):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)
"""
numbers = []
a = 1
for element in generatedNumbers:
    numbers.append(element / a)
    a += 1

print(numbers)
"""