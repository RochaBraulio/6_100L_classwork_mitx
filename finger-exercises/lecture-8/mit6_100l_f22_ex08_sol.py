# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 11:07:55 2025

@author: rocha
"""

# Implement the function that meets the specification below:

def same_chars(s1, s2):
    """s1 and s2 are strings
    Returns boolean True if a character in s1 is also in s2, and vice
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    compare = True
    
    for char in s1:
        if char not in s2:
            compare = False
            return compare
        
    for char in s2:
        if char not in s1:
            compare = False
            return compare
        
    return compare
        
    
# Examples:
print(same_chars("abc", "cab")) # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa")) # prints False
print(same_chars("abcabc", "cabz")) # prints False