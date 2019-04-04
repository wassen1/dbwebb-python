#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
import random



def greeter():
    """
    Greets the user with the parameter as the phrase
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def temp_converter():
    """
    Converts from C to F
    """
    degreeC = input("What degree in C do you want to convert to F? ")
    degreeF = int(degreeC) * 9 / 5 + 32
    print("\nRobbie says:")
    print("\nI converted %s C in to %s F!" % (degreeC, degreeF))


def multiply(number, word):
    """
    Multiplies number with word
    """
    return int(number) * word


def word_multiplier():
    """
    Multiplies word
    """
    multiplyWord = input("\nPlease provide a word. ")
    multiplyNumber = input("Please provide a number. ")
    
    #print(int(multiplyNumber) * multiplyWord)
    print("\n", multiply(multiplyNumber, multiplyWord))


def average_calc():
    """
    Calculates the average of numbers from input
    """
    addCount = 0
    addSum = 0
    
    while True:
        addInput = input("\nPlease provide a number to add. Quit with 'done' ")
        if addInput == 'done':
            break
        
        addCount += 1
        addSum = addSum + int(addInput)
        addAveradge = addSum / addCount
        
        print("\nTotal sum: ", addSum)
        print("Average: ", addAveradge)


def compare_numbers():
    """
    Compares input number with the latest number
    """
    compareOld = None

    while True:
        compareInput = input("\nPlease provide a number. Quit with 'done'. ")
        if compareInput == 'done':
            break
        
        try:
            compareNumber = int(compareInput)

            if compareOld is None:
                print("This is your first number")
            elif compareNumber == compareOld:
                print("Your number is the same as before!")
            elif compareNumber < compareOld:
                print("Your number is less than before!")
            elif compareNumber > compareOld:
                print("Your number is bigger than before!")
            compareOld = compareNumber
        except ValueError:
            print("You need to provide a number")


def modify_string():
    """
    Modifies an input string
    """
    modString = input("\nPlease write a string. ")
    modNewStr = ""
    modCount = 1

    for letter in modString:
        if modCount < 2:
            modNewStr = letter
        else: 
            modNewStr = modNewStr + "-" + letter * modCount

        modCount += 1
    
    print("\nNew string: ", modNewStr)


def isogram():
    """
    Detects if an input string is an isogram
    """
    isoString = input("\nPlease write a string. ")
    notIso = False

    for character in isoString:
        isoCount = 0

        for letter in isoString:
            if character == letter:
                isoCount += 1
    
        if isoCount > 1:
            notIso = True
            break
    
    if notIso is False:
        print("\nMatch")
    else:
        print("\nNo match")


def randomise_string():
    """
    Randomises all letters position in a input string
    """
    # import random

    to_rand_str = input("\nWrite a string to randomise. ")
    randomised_str = ""
    len_str = len(to_rand_str)

    while len_str > 0:
        random_number = random.randint(0, (len_str - 1))
        rand_letter = to_rand_str[random_number]
        randomised_str += rand_letter

        # cuts off the random element from input string
        to_rand_str = to_rand_str[:random_number] + to_rand_str[(random_number + 1):]
        len_str = len(to_rand_str)

    print("\n", randomised_str)


def anagram():
    """
    Checks if two strings are an anagram
    """

    str_1 = input("\nWrite first string. ")
    str_2 = input("\nWrite second string. ")

    lower_sorted_str1 = sorted(str.lower(str_1))
    lower_sorted_str2 = sorted(str.lower(str_2))

    if lower_sorted_str1 == lower_sorted_str2:
        print("\nMatch")
    else:
        print("\nNo match")


def akronom():
    """
    Picks the upper case letters and concatenates them into a new string
    """
    akro_str = input("\nWrite a sentance with both upper case and lower case letters. ")
    akronomed_str = ""
    for letter in akro_str:
        if str.isupper(letter):
            akronomed_str += letter

    print("\n", akronomed_str)


def str_mask():
    """
    Masks a string of numbers with # but leaves the last 4 digits
    """
    mask_input = input("\nProvide a long number. ")
    mask_length = len(mask_input)
    last4 = mask_input[-4:]
    mask = multiply(mask_length - 4, "#")
    masked_str = mask + last4
    print("\n", masked_str)
