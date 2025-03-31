# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 19:12:34 2025

@author: rocha
"""

#Implement the function that meets the specification below.:
def all_true(n, Lf):
    """ n is an int
    Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called
    with n as a parameter. Otherwise returns False.
    """
    Lf_return = []
    for func in Lf:
        Lf_return.append(func(n))
    if len(Lf) == Lf_return.count(True):
        return True
    else:
        return False
   

# Examples:
# I commented the call because not arguments were provided
# to test function requested
#all_true() # prints 6

