"""
    funkcje anonimowe
"""

def podwoj(x):
    return x * 2

print(podwoj(4))

test = lambda x: x * 2

print((lambda x: x * 2)(6))

my_list = [2, 14, 22, 6, 7, 5, 8, 13]

my_list_filtered = list(filter(lambda x: x % 2 == 0, my_list) )
my_list_filtered2 = [x for x in my_list if(x % 2) != 0]

print(my_list_filtered)
print(my_list_filtered2)
