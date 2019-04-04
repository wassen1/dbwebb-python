#!/usr/bin/env python3

"""
6d86f349fd18b301d2cbab2fdde15ba8
python
lab6
v3
fraa18
2018-10-23 19:32:02
v3.1.3 (2018-09-13)

Generated 2018-10-23 21:32:02 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from operator import itemgetter
from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Solo, Skywalker, Vader
#
# and corresponding numbers
#
# > 55511243, 55568711, 55590858
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook = {"Solo" : 55511243, "Skywalker" : 55568711, "Vader" : 55590858}




ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#
length = len(phonebook)

ANSWER = length

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Skywalker'.
#
# Write your code below and put the answer into the variable ANSWER.
#

sky_phone = phonebook.get("Skywalker")

ANSWER = sky_phone

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#
key_list = []
for key in sorted(phonebook.keys()):
    key_list.append(key)


ANSWER = key_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

nr_list = []
for key, value in sorted(phonebook.items(), key=itemgetter(1), reverse=False):
    nr_list.append(value)

ANSWER = nr_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Skywalker' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Skywalker" in phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Skywalker' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

copy_phonebook = phonebook.copy()
copy_phonebook.pop("Skywalker")

ANSWER = copy_phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'bear, 65, 6.47, chair, 5'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = len(("bear", 65, 6.47, "chair", 5))

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (bear, 65, 6.47, chair, 5).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#

t = ("bear", 65, 6.47, "chair", 5)

a, b, c, d, e = t

ANSWER = d

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [45, 22, 2, 498, 78]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

l = [45, 22, 2, 498, 78]

a, b = l[:2]

ANSWER = a

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (snake, 89, 9.63, bookshelf, 1)
#
# Convert it to a list and replace the second element with:
#
# > "fire"
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#

t = ("snake", 89, 9.63, "bookshelf", 1)
l = list(t)
l[1] = "fire"
t2 = tuple(l)

string = ""

l2 = t2[:3]

for count, element in enumerate(l2, start=1):
    string += str(element)
    if count < 3:
        string += ","


ANSWER = string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#
string = ""

for name, value in sorted(phonebook.items(), key=itemgetter(0), reverse=False):
    string += name + " " + str(value) + "\n"

ANSWER = string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#
for name, number in phonebook.items():
    phonebook[name] = '+1-' + str(number)

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
