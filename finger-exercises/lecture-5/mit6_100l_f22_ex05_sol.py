#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:37:10 2025

@author: rocha
"""

# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string containing
# the even indexed characters of my_str. For example, if my_str = "abcdefg"
# then your code should print out aceg.

my_str = input("Please provide a sequence of letters or a word: ")
new_str_even_indexes = ""

for i in range(len(my_str)):
    if i%2 == 0:
        new_str_even_indexes += my_str[i]
print(new_str_even_indexes)