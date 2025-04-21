####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

user_name = input('Please enter your name: ')
print(len(user_name) - 5)


####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

test_string = "We want to remove the nth character from this string"
n = 8

print("The old string is \n", test_string)
new_string_ls = []
new_string_ls = [test_string[i] for i in range(len(test_string)) if i != n-1]
new_string = "".join(new_string_ls)
print("The new string is \n", new_string)

# Solution involved slicing the original string until the break point,
# skip the nth character, get the rest of the string and concatenate
# the two parts together in a new string


####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

my_string = "This is my string"  # example string - modify to test

if len(my_string) > 10 or len(my_string) < 5:
    print(True)
else:
    print(False)
    
####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"

if "e" in my_string:
    counter = 0
    for ch in my_string:
        if ch == "e":
            counter += 1
    print("There are", counter, "e's within the string")
else:
    print("There are no e's within the string")

