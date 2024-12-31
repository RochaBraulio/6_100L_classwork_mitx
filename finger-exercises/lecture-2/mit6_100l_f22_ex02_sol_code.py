#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:48:24 2024

@author: rocha
"""

# Assume you are given a variable named number (has a numerical value).
# Write a piece of Python code that prints out one of the following strings:
#    - positive if the variable number is positive
#    - negative if the variable number is negative
#    - zero if the variable number is equal to zero

# number = int(input("Please choose a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")