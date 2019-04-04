#!/usr/bin/env python3

"""
c55862ff334a595079a4947b90d982db
python
lab3
v3
fraa18
2018-10-02 10:30:47
v3.1.3 (2018-09-13)

Generated 2018-10-02 12:30:48 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In these exercises we will work with functions.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function called `greeter` that returns `"Hi, the weather is nice
# today!"`.
#
# Answer with the return value from a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def greeter():

    """
    Returns a greeting phrase
    """
    return "Hi, the weather is nice today!"




ANSWER = greeter()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Assign the words: 'cabbage' and 'pringles' to two different variables.
#
# Create a function and pass the two words as arguments to it. Your function
# should return them as a single word.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

variable1 = "cabbage"
variable2 = "pringles"

def assign_vars(var1, var2):
    """
    Returns the given arguments
    """
    return var1 + var2




ANSWER = assign_vars(variable1, variable2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function called `funny_word` that takes one argument and prepends
# it to the string ' is a funny word'. **EXAMPLE:** If the argument is
# 'water', the function should return: `"water is a funny word"`.
#
# Use the argument 'music' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def funny_word(word):
    """
    Concatenates a given word to  a string
    """


    return word + " is a funny word"




ANSWER = funny_word("music")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function called `summation` that takes two arguments. The function
# should return the sum of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 79 and 20.
#
# Write your code below and put the answer into the variable ANSWER.
#
def summation(arg1, arg2):
    """
    Adds two given numbers
    """

    summary = arg1 + arg2
    return summary






ANSWER = summation(79, 20)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a function called `multiplication` that takes two arguments. The
# function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 79 and 20.
#
# Write your code below and put the answer into the variable ANSWER.
#

def multiplication(arg1, arg2):
    """
    Multiplies two given numbers
    """

    return arg1 * arg2




ANSWER = multiplication(79, 20)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a function called `in_range` that takes one argument. The function
# should return `True` if the argument is higher than 50 and lower than 100.
# If the number is out of range, the function should return `False`. The
# return type should be boolean.
#
# Use the argument 71 and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def in_range(arg):
    """
    Tests wether the given number is in range
    """
    return arg > 50 and arg < 100




ANSWER = in_range(71)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a function called `multiplicator`. Inside the function create a loop
# that iterates from 4 to 24 (both included). For each number use the
# `multiplication` function from above to get the square of the current
# number. The function should return a comma-separated string of the squared
# numbers,  without an ending `,`.
#
# Answer with a call to the function `multiplicator`.
#
# Write your code below and put the answer into the variable ANSWER.
#
def multiplicator():
    """
    Calculates the squares of the numbers in range 4-24
    """
    string = ""
    for number in range(4, 25):
        multiple = str(multiplication(number, number))
        string += multiple
        if number < 24:
            string += ","
    return string



ANSWER = multiplicator()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a function called `decider`. The function takes one argument. If the
# argument is a string return a call to `funny_word()`, if the argument is an
# integer return the square of the argument by using the `multiplication`
# function.
#
# Answer with a call to the function `decider` with the value `blunderbuss`
# as argument.
#
# Write your code below and put the answer into the variable ANSWER.
#
def decider(user_input):
    """
    Checks if the input is a string or an int
    """
    if isinstance(user_input, str):
        return funny_word(user_input)

    elif isinstance(user_input, int):
        return multiplication(user_input, user_input)


ANSWER = decider("blunderbuss")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9 (1 points)
#
# Create a function called `double_decider`. The function takes two
# arguments. For each argument call the `decider` function. Concatenate the
# returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# fartlek and 39 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#
def double_decider(arg1, arg2):
    """
    Checks the input and builds a new string
    """
    argument1 = decider(arg1)
    argument2 = decider(arg2)
    
    return str(argument1) + " and the square is " + str(argument2)


ANSWER = double_decider("fartlek", 39)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.9", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Create a function that returns a binary string value of a given integer.
# Return only the binary number and not any identification that it is a
# binary number.
#
# Example: Calling the function with the number 3 should return `"11"`.
#
# Answer with a call to the function with the argument 71.
#
# Write your code below and put the answer into the variable ANSWER.
#
def binary_string(number):
    """
    Returns the binary string from an int
    """
    bin_string = bin(number)[2:]
    return bin_string

ANSWER = binary_string(71)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (3 points)
#
# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters. The function should return a
# string with the format "Lower case letters: #, upper case letters: #". Only
# count letters, you can ignore space and special characters.
#
# Answer with a call to the function with the argument: `"How vexingly Quick
# Daft zeBras jumP!"`.
#
# Write your code below and put the answer into the variable ANSWER.
#
def count_upper_lower_case(string):
    """
    Counts upper and lower case appearance in a string
    """
    lower_count = 0
    upper_count = 0

    for letter in string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1

    return "Lower case letters: {lower}, upper case letters: {upper}".format(
        lower=lower_count, 
        upper=upper_count)


ANSWER = count_upper_lower_case("How vexingly Quick Daft zeBras jumP!")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)


dbwebb.exit_with_summary()
