#!/usr/bin/env python3

"""
97b7c35d0d1edd3b0c8389cec1146696
python
lab5
v3
fraa18
2018-10-18 13:17:14
v3.1.3 (2018-09-13)

Generated 2018-10-18 15:17:14 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [bobcat, flute] and [Dafoe, Berenger].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#
x = ["bobcat", "flute"]
y = ["Dafoe", "Berenger"]

z = x + y

ANSWER = z

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [table, wall, desk, chair, floor].
#
# Add the words 'icecream' and 'jacket' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
furniture = ["table", "wall", "desk", "chair", "floor"]
furniture.insert(1, "icecream")
furniture.insert(2, "jacket")


ANSWER = furniture

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [table, wall, desk, chair, floor].
#
# Replace the third word with: 'light'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = ["table", "wall", "desk", "chair", "floor"]
x[2] = 'light'



ANSWER = x

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [wasp, fly, butterfly, bumblebee, mosquito]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
x.sort(reverse=True)

ANSWER = x

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'guitar'
#
# from the list:
#
# > [flute, guitar, drums, piano, bass]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = ["flute", "guitar", "drums", "piano", "bass"]
x.remove("guitar")



ANSWER = x

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [45, 22, 2, 498, 78]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#
x = [45, 22, 2, 498, 78]
y = sum(x)


ANSWER = y

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [67, 50, 2, 39, 15]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = [67, 50, 2, 39, 15]
sum_list = sum(x)
average = sum_list / len(x)




ANSWER = average

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?grass?is?growing"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#

the_string = "The?grass?is?growing"
the_string_list = the_string.split("?")

separator = " "
the_string_str = separator.join(the_string_list)


ANSWER = the_string_str

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [a, b, c, d, e]
#
# and replace the second and third element with
#
# > "picture, canvas"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = ["a", "b", "c", "d", "e"]
x[1:3] = ["picture", "canvas"]


ANSWER = x

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [d, c, b, a, e]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ["d", "c", "b", "a", "e"]
list2 = list1[:]


ANSWER = list1 is list2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list3 = list1


ANSWER = list1 is list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "x"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1[0] = "x"




ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [123, 4, 125, 69, 155]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
lista = [123, 4, 125, 69, 155]

def sort_list_10(li):
    """
    Returns the list passed as argument sorted in
    numerical and ascending order. Also multiply all values with 10.
    """
    new_list = []

    li.sort()

    for item in li:
        new_list.append(item * 10)
    
    return new_list


ANSWER = sort_list_10(lista)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [67, 50, 2, 39, 15]
#
# as argument.
#
# The function should multiply all even numbers by 3 and add 9 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#

lista = [67, 50, 2, 39, 15]

def sort_list(li):
    """
    Returns list in descending order and multiply all even numbers by 3 and add 9 to all odd
    numbers.
    """
    new_list = []
    
    for item in li:
        if item % 2 == 0:
            new_list.append(item * 3)
        else:
            new_list.append(item + 9)
    
    new_list.sort(reverse=True)
    return new_list




ANSWER = sort_list(lista)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
