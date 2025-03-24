# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 10:46:30 2025

@author: rocha
"""

# Implement the function that meets the specifications below:

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    (len_tuple, pairwise_product, sum_pairwise_prod) = (0,[], 0)
    len_tuple = len(tA) # assuming tA and tB are of the same length, it does
    # not matter which one is passed as argument to len()
    for i in range(len_tuple):
        # create list with pairwise products from tA * tB
        pairwise_product.append(tA[i] * tB[i])
    for el in pairwise_product:
        # loops over previous list and sums up its element
        sum_pairwise_prod += el
    return(len_tuple, sum_pairwise_prod)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)
