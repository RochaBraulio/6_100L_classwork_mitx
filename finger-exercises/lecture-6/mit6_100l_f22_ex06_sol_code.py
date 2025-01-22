#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:42:13 2025

@author: rocha
"""

# Assume you are given an integer 0 <= N <= 1000.
# Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines:
# count: with how many guesses it took to find N, and 
# answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers,
# choose the smaller one.

N = int(input('Please choose an integer N between 0 and 1000: '))
             
# Using bisection search to guess N
low = 0
high = 1000
guess = (low + high)//2
count = 1
while guess != N:
    if guess < N:
        low = guess
    else:
        high = guess
    guess = (low + high)/2
    count += 1
answer = guess
print(f'How many guesses it took to find N: {count}')
print(f'N is: {answer}')