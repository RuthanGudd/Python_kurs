def count(*arg):
    sum = 0
    
    for i in arg:
        sum += i
    
    return sum

print(count(2, 4, 1, 2, 4, 5, 10))