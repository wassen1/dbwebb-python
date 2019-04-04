#!/usr/bin/env python3

"""
935b9e3359aa727c0ecc0874290ff690
python
lab2
v3
fraa18
2018-09-05 08:46:39
v3.1.0 (2018-08-17)

Generated 2018-09-05 10:46:39 by dbwebb lab-utility v3.1.0 (2018-08-17).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 2, `dice2` = 6
# and `dice3` = 1.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#
dice1 = 2
dice2 = 6
dice3 = 1
result = dice1 > dice2





ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

diceSum = dice1 + dice2 + dice3
if diceSum > 11:
    result = "big"
else:
    result = "small"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 3 and `dice5` = 3 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#
dice4 = 3
dice5 = 3
diceSum = diceSum + dice4 + dice5
if diceSum < 11:
    result = "small"
elif diceSum >= 11 and diceSum < 21:
    result = "intermediate"
else:
    result = "big"







ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'sunshine'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

# summer_word = "sunshine"
# if 's' in summer_word:
#     result = True
# else:
#     result = False

summer_word = "sunshine"
result = bool('s' in summer_word)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = ""
for i in range(11):
    result = result + str(i) + ","




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#
result = ""
konsStr = "bcdfghjklmnpqrstvwxz"

# for word in summer_word:
#     for kons in konsStr:
#         if word == kons:
#             result = result + word
for word in summer_word:
    if word in konsStr:
        result = result + word



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 28 to 79 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#
startVal = 28
result = 0
for startVal in range(28, 80):
    if startVal % 2 != 0:
        result = result + int(startVal)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 6 and ends when the value is
# greater than 44, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
value = 6
valStr = ""

while value <= 44:
    valStr = valStr + str(value) + ","
    value = value + 3





ANSWER = valStr

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that adds 6 to the number 11, 44 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#
value = 11
count = 0
while count < 44:
    value = value + 6
    count = count + 1

# count = 0
# value = 11
# while True:
#     if count >= 44:
#         break
#     value = value + 6
#     count = count + 1






ANSWER = value

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that subtracts 7 from 60, 24 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#
count = 0
value = 60

while count < 24:
    value = value - 7
    count += 1






ANSWER = value

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'internationalization'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#
string = "internationalization"
newString = ""

for letter in string:
    newString = letter + newString






ANSWER = newString

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), on how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Order matters, so only use 1 +-*/ 2 = 3 and not 2 +-/* 1 = 3.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

# first = 0
# second = 0
# third = 0
# count = 0
# number_of_plates_hits = 0

################
hundredth = 0
tenth = 0
single = 1
number_of_plates_hits = 0

while hundredth < 10:
    while tenth < 10:
        while single < 10:
            # print(hundredth, tenth, single)

            try:
                if hundredth + tenth == single:
                    number_of_plates_hits += 1
                    # print('+', number_of_plates_hits)
                elif hundredth - tenth == single:
                    number_of_plates_hits += 1
                    # print('-', number_of_plates_hits)

                elif hundredth * tenth == single:
                    number_of_plates_hits += 1
                    # print('*', number_of_plates_hits)

                elif hundredth / tenth == single:
                    number_of_plates_hits += 1
                    # print('/', number_of_plates_hits)
            except ZeroDivisionError:
                pass
            single += 1
        single = 0
        tenth += 1
    tenth = 0
    hundredth += 1
# print(number_of_plates_hits)



ANSWER = number_of_plates_hits

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
