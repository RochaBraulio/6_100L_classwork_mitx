#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 08:50:10 2025

@author: rocha
"""

# Implement the function that meets the specification below.:
def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0
    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    if exp == 0:
        return 1
    else: 
        return base * recur_power(base, exp - 1)

# Examples:    
print(recur_power(2,5)) # prints 32
