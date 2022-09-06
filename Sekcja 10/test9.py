import time

def function_performance(func, how_many_times = 1, *arg):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

def is_element_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False

print(function_performance(is_element_in, 500000, 25, setContainer))
print(function_performance(is_element_in, 500000, 25, listContainer))

#Dla wielu nienazwanych argumentów dajesz jedną gwiazdkę i sie to jako krotka zapisuje.
#Gdy chcesz wiele nazwancyh argumentów do nienazwanego argumentu zapisać dajesz dwie gwiazdki i to sie jako słownik zapisuje 
#Dawaj zawsze argumenty nienazwane po nazwanych