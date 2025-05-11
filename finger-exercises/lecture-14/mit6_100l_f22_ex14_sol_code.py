#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 11 18:28:35 2025

@author: rocha
"""

# Question 1

# Implement the function that meets the specification below:
def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    results = []  
    for k,v in aDict.items():
        if v == target:
            results.append(k)
    results.sort()
    return results

aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target)) # prints the list [1,5]

# Question 2
# Implement the function that meets the specification below:
def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a
    positive value.
    """
    results = []
    for k,v in d.items():
        if sum(v) > 0:
            results.append(k)
    results.sort()
    return results
    

d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d)) # prints the list [1, 2]