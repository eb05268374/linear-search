import random

from cool_print import cool_print

def linear_search(list_to_search, target):
    for i in range(0, len(list_to_search)):
        if str(list_to_search[i]) == target:
            cool_print(f"Item found at {i}.\n", 0.5)
            return
    cool_print("Item not found.\n", 0.5)

def linear_search_2d(list_to_search, target):
    for i in range(0, len(list_to_search)):
        for j in range(0, len(list_to_search[i])):
            if list_to_search[i][j] == target:
                cool_print(f"Item found at [{i}][{j}].\n", 0.5)
                return
    cool_print("Item not found.\n", 0.5)

lst = [2,3,12,22,3,23,44,32,44,32,42,43,4,5,6,46,4,4,1]

lst_2d = [[random.randint(0,1000) for _ in range(1000)] for _ in range(1000)]

for _ in range(25):
    cool_print("Target:", 0.5)
    linear_search_2d(lst_2d, int(input()))
