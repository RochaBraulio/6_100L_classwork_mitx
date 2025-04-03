# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:47:46 2025

@author: rocha
"""

# Implement the function that meets the specification below.:


def remove_and_sort(Lin, k):
    """ Lin is a list of ints
    k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    if k >= len(Lin):
        Lin.clear()
    else:
        while k != 0:
            del(Lin[0])
            k -=1
        Lin.sort()


# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L) # prints the list [3, 6]