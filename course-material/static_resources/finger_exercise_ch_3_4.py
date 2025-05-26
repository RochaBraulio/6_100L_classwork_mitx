#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:42:52 2025

@author: rocha
"""

# Comparison of Newton-Raphson vs. Bisection search when
# calculating the square root of a positive integer


epsilon = 0.01
k = 987654321 # number for which we want to find its square root

# Using Newton-Raphson method to find square root of k

guess_newton = k/2.0
num_guesses_newton = 0

while abs(guess_newton**2 - k) >= epsilon:
    num_guesses_newton += 1
    guess_newton = guess_newton - (((guess_newton**2) - k)/(2*guess_newton))
print(f'Newton-Rapshon took {num_guesses_newton} guesses')
print(f'Using Newton-Raphson, the square root found for {k} is {guess_newton}')

# Using Bisection search method to find square root of k

num_guesses_bisection = 0

if k >= 1:
   low = 1.0
   high = k
else:
   low = k
   high = 1.0
guess_bisection = (high + low)/2

while abs(guess_bisection**2 - k) >= epsilon:
   if guess_bisection**2 < k:
       low = guess_bisection
   else:
       high = guess_bisection
   guess_bisection = (high + low)/2.0
   num_guesses_bisection += 1
print(f'Bisection Search took {num_guesses_bisection} guesses')
print(f'Using Bisection Search, the square root found for {k} is {guess_bisection}')