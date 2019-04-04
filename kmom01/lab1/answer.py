#!/usr/bin/env python3

"""
a2fa30ef27d8591093cc923460a9961f
python
lab1
v3
fraa18
2018-09-03 14:26:36
v3.1.0 (2018-08-17)

Generated 2018-09-03 16:26:36 by dbwebb lab-utility v3.1.0 (2018-08-17).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 99.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#
num_one = 99





ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 27. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_two = 27
result = num_two + num_one



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 23.
#
# Create another variable called `num_four` and give it the value 24.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_three = 23
num_four = 24
result = num_four - num_three + result




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = num_one * num_three




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 99.11.
#
# Create another variable called `float_two` and give it the value 71.1.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number.
#
# Write your code below and put the answer into the variable ANSWER.
#

float_one = 99.11
float_two = 71.1
result = float_one + float_two




ANSWER = round(result, 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = num_three + num_one - num_four
result = result * num_two + float_two - float_one




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'device' and 'beach' and
# answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = 'device' + 'beach'




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'beach' with the integer 99, with a space between the
# two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#
result = 'beach' + ' ' + '99'





ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 99 with the word 'device' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 27 and the word 'beach' with a space between between
# the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = '99' + ' ' + 'device'
result = result + ' and '
result = result + '27' + ' ' + 'beach'




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = '30'
actual_number = 5
result = int(string_number) / actual_number




ANSWER = round(result)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# BTH have two plugin-hybrid cars. A new car and an old car. The new car has
# a fast charging mode where 80% of the battery can be charged in 30 minutes.
# The remaining 20% of the battery and the entire battery of the old car is
# charged by 5% every 30 minutes.
#
# During fast charging the effect of the charger is 200W and during normal
# charging the effect of the charger is 100W.
#
# The formula for calculating the amount of energy based on effect and time
# is: `energy = effect * time`. To get the amount of energy in kWh the
# formula is `energy = (effect in W * time in hours) / 1000`.
#
# Calculate the total amount of energy used to fully charge the two cars.
# Answer with the amount of energy in kWh.
#
# Write your code below and put the answer into the variable ANSWER.
#

new_car_kWh = (200 * 0.5 + 100 * 2) / 1000
old_car_kWh = (100 * 10) / 1000

result = new_car_kWh + old_car_kWh


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#
hours = 52 * 9 / 60
resultStr = 'Peter calls from 0731415926 to Anna on 0727182818 for ' + str(hours) + ' hours every year.'





ANSWER = resultStr

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
