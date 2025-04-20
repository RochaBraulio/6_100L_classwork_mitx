#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 21:59:13 2025

@author: rocha
"""

# Implement the function that meets the specification below.:
def sum_str_lengths(L):
    """
    L is a non-empty list containing either:
    * string elements or
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and
    lengths of strings in the sublists of L. If L contains an
    element that is not a string or a list, or L's sublists
    contain an element that is not a string, raise a ValueError.
    """
    
    total = 0
    try:
        for el in L:
            if type(el) is str:
                total += len(el)
            else:
            #assumed everything else would be a list instead of checking
                for sub_el in el:
                    total += len(sub_el)
        return total
    except:
        raise ValueError
    
    # total = 0
    # for el in L:
    #     if type(el) == str:
    #         total += len(el)
    #     elif type(el) == list:
    #         for sub_el in el:
    #             if type(sub_el) == str:
    #                 total += len(sub_el)
    #             else:
    #                 raise ValueError
    #     else:
    #         raise ValueError
    # return total
    
# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]])) # prints 7
# print(sum_str_lengths([12, ["e", "fg"]])) # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]])) # raises ValueError

