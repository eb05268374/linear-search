import random

from cool_print import cool_print

def linear_search(list_to_search, target):
    for i in range(0, len(list_to_search)): # iterate through each item
        if list_to_search[i] == target: # if the items what we're looking for
            cool_print(f"Item found at {i}.\n", 0.5) # state where it was found
            return # end the subroutine
    cool_print("Item not found.\n", 0.5) # else not found state so

def linear_search_2d(list_to_search, target):
    for i in range(0, len(list_to_search)): # basically the same as the last one but using a 2d list instead
        for j in range(0, len(list_to_search[i])):
            if list_to_search[i][j] == target:
                cool_print(f"Item found at [{i}][{j}].\n", 0.5)
                return
    cool_print("Item not found.\n", 0.5)

def linear_search_count_all(list_to_search, target):
    found = 0
    for i in range(0, len(list_to_search)): # iterate through each item
        if list_to_search[i] == target: # if the items what we're looking for
            found += 1 # instead of ending the subroutine when found, keep going and count how many are found
    if found > 0:
        cool_print(f"Item found {found} times.\n", 0.5) # say how many found
    else:
        cool_print("Item not found.\n", 0.5) # if none found say so

# debugging stuff
lst_1d = [random.randint(0,100) for _ in range(10000)]
lst_2d = [[random.randint(0,1000) for _ in range(1000)] for _ in range(1000)]

cool_print("Target:", 0.1)
linear_search_count_all(lst_1d, int(input()))

