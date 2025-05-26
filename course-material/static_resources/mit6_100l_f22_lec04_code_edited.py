#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:53:30 2024

@author: rocha
"""

# =============================================================================
# #Find the cube root of a perfect cube
# x = int(input("Enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#     #print("Value of the decrementing function abs(x) - ans**3 is", (abs(x) - ans**3))
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print("Cube root of", x, "is", ans)
# =============================================================================

# =============================================================================
# # Check how large must max_val be for one to notice the calculation time
# max_val = int(input('Enter a positive integer: '))
# i = 0
# while i < max_val:
#     i += 1
# print(i)
# =============================================================================

# =============================================================================
# test_prime = int(input('Enter a positive integer: '))
# 
# divisores = []
# 
# for divisor in range(2,test_prime,1):
#     if test_prime%divisor == 0:
#         divisores.append(divisor)
# 
# if len(divisores) == 0:
#     print(f"Number provided ({test_prime}) is prime")
# else:
#     smallest_divisor = min(divisores)
#     print(f"Number ({test_prime}) is not prime and smallest divisor is {smallest_divisor}")
# =============================================================================



# #Test if an int > 2 is prime. If not, print smallest divisor
# x = int(input('Enter an integer greater than 2: '))
# largest_divisor = None
# for guess in range (2,x):
#     if x%guess == 0:
#         largest_divisor = guess
#         #break
# if largest_divisor != None:
#     print("Largest divisor of", x, "is", largest_divisor)
# else:
#     print(x, "is a prime number")


        
# #Test if an int > 2 is prime. If not, print smallest divisor
# x = int(input('Enter an integer greater than 2: '))
# smallest_divisor = None
# for guess in range (2,x):
#     if x%guess == 0:
#         smallest_divisor = guess
#         break
# if smallest_divisor != None:
#     print("Largest divisor of", x, "is", int(x/smallest_divisor))
# else:
#     print(x, "is a prime number")

# Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect.

# Ch 3.1 - First finger exercise
user_int = int(input("Please provide an integer: "))
root = None
pwr = None

if user_int <= 0:
    print("No two integers exist for root and pwr that satisfy conditions stated.")
elif user_int == 1:
    root = 1
    #pwr can be any integer in range 2 to 5, so let's return 2.
    pwr = 2
    print(f'Root is {root} and pwr is {pwr}.' + '\n' + 
          'Moreover, pwr can also be 3,4 or 5')
else:
    #TODO: add missing solution 




