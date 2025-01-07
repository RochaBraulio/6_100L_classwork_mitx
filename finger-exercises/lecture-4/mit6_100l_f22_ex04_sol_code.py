#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:41:56 2025

@author: rocha
"""

# =============================================================================
# Assume you are given a positive integer variable named N.
# Write a piece of Python code that finds the cube root of N.
# The code prints the cube root if N is a perfect cube
# or it prints error if N is not a perfect cube.
# Hint: use a loop that increments a counter -- 
# you decide when the counter should stop.
# =============================================================================

N = int(input("Please choose an positive integer: "))

guess_root = 0
perfect_cube = False


while N - guess_root**3 >= 0:
    if N == guess_root**3:
        perfect_cube = True
        break
    guess_root += 1

if perfect_cube:
    print(f'The cube root of {N} is {guess_root}')
else:
    print(f'{N} is not a perfect cube')