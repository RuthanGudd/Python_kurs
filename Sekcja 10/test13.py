"""
    copy - płyka
    deepcopy - głęboka
"""
import copy

def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0] = 20

myList = [1, 3, 5, 1, 54, 4]

print(id(myList))
evil_function(myList.copy())


def evil_function2(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0][0] = 20

myList2 = [[1, 3], [5, 1], [54, 4]]

print(id(myList2))
evil_function2(copy.deepcopy(myList2))


