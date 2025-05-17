#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 16 15:26:42 2025

@author: rocha
Comment: I was not able to solve the problem without
looking at the solution:(
"""

#Implement the function that meets the specification below:
# Comment: I was not able to solve the problem without
# Comment: looking at the solution:( Need to work more on recursion

    
def flatten(L):
    """
    L: a list
    Returns a copy of L, which is a flattened version of L
    """
    flat_L = []
    for el in L:
        if type(el) != list:
            flat_L.append(el)
        else:
            flat_L.extend(flatten(el))
    return flat_L

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]

