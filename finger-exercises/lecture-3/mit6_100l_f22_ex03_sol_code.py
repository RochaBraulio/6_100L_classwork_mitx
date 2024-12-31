#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:07:04 2024

@author: rocha
"""

# =============================================================================
# Assume you are given a positive integer variable named N.
# Write a piece of Python code that prints hello world
# on separate lines, N times. You can use either a while loop or a for loop.
# =============================================================================

reps = int(input("Please choose a positive number: "))

for i in range(reps):
    print("hello world")