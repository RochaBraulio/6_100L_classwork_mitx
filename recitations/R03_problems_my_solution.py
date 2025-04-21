####################################################################################
# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0
high = x
ans = 0 #

if x < 1: 
    # Forth root of a number less than 1 is greater than the number itself, e.g.
    # the forth root of 0.6 is 0.88 
    high = 1
else:
    high = x
    
ans = (low + high)/2 # initial guess of forth root
    
while abs(ans**4 - x) > epsilon:
    if ans**4 - x > 0:
        high = ans
    else:
        low = ans
    ans = (low + high)/2
print(ans)

####################################################################################
# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 

def check_within_range(user_num, user_rng_min, user_rng_max):
    if user_rng_min <= user_num <= user_rng_max:
        return(f'Number {user_num} falls within the {user_rng_min} - {user_rng_max} range')
    else:
        return(f'Number {user_num} falls outside the {user_rng_min} - {user_rng_max} range')
        
print(check_within_range(3, 1, 5))
print(check_within_range(3, 5, 7))  
        
####################################################################################
# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).

def check_perfect_number(user_num):
    div = []
    for num in range(1, user_num):
        if user_num % num == 0:
            div.append(num)
    if sum(div) == user_num:
        return(f'{user_num} is a perfect number')
    else:
        return(f'{user_num} is not a perfect number')
        
print(check_perfect_number(6))
print(check_perfect_number(28))
print(check_perfect_number(50))

####################################################################################
# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0

while True:
    x = float(input("Using an approximation algorithm calculate the forth root of: " ))
    if x >= 0:
        break
    print('Number cannot be negative')

while abs(ans**4 - x) > epsilon and ans**4 < x:
    ans += increment
    num_guesses += 1
if abs(ans**4 - x) > epsilon:
    print(f'Failed at calculating the forth root of: {x}')
    print(f'Number of iterations required: {num_guesses}')
    
else:
    print(f'Approximation for the forth root of {x} is: {ans}')
    print(f'Number of iterations required: {num_guesses}')
    



