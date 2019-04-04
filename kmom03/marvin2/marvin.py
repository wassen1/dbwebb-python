#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
 ..............
 .  *      *  .
[.      '     .]
 .            .
 .  ( ~~~~ )  .
 ..............
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""



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
    print("\nRobbie says:\n")
    print("I converted %s C in to %s F!" % (degreeC, degreeF))


def multiply(number, word):
    """
    Multiplies number with word
    """
    return int(number) * word


def word_multiplier():
    """
    Multiplies word
    """
    multiplyWord = input("Please provide a word. ")
    multiplyNumber = input("Please provide a number. ")
    
    #print(int(multiplyNumber) * multiplyWord)
    print(multiply(multiplyNumber, multiplyWord))


def average_calc():
    """
    Calculates the average of numbers from input
    """
    addCount = 0
    addSum = 0
    
    while True:
        addInput = input("Please provide a number to add. Quit with 'done' ")
        if addInput == 'done':
            break
        
        addCount += 1
        addSum = addSum + int(addInput)
        addAveradge = addSum / addCount
        
        print("Total sum: ", addSum)
        print("Average: ", addAveradge)


def compare_numbers():
    """
    Compares input number with the latest number
    """
    compareOld = None

    while True:
        compareInput = input("Please provide a number. Quit with 'done'")
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
    modString = input("Please write a string. ")
    modNewStr = ""
    modCount = 1

    for letter in modString:
        if modCount < 2:
            modNewStr = letter
        else: 
            modNewStr = modNewStr + "-" + letter * modCount

        modCount += 1
    
    print("New string: ", modNewStr)


def isogram():
    """
    Detects if an input string is an isogram
    """
    isoString = input("Please write a string. ")
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
        print("Match")
    else:
        print("No match")


def randomise_string():
    """
    Randomises all letters position in a input string
    """
    import random

    to_rand_str = input("Write a string to randomise. ")
    randomised_str = ""
    len_str = len(to_rand_str)

    while len_str > 0:
        random_number = random.randint(0, (len_str - 1))
        rand_letter = to_rand_str[random_number]
        randomised_str += rand_letter

        # cuts off the random element from input string
        to_rand_str = to_rand_str[:random_number] + to_rand_str[(random_number + 1):]
        len_str = len(to_rand_str)
        print("Length of string:", len_str)

    print(randomised_str)


def anagram():
    """
    Checks if two strings are an anagram
    """

    str_1 = input("Write first string. ")
    str_2 = input("Write second string. ")

    lower_sorted_str1 = sorted(str.lower(str_1))
    lower_sorted_str2 = sorted(str.lower(str_2))

    if lower_sorted_str1 == lower_sorted_str2:
        print("Match")
    else:
        print("No match")


def akronom():
    """
    Picks the upper case letters and concatenates them into a new string
    """
    akro_str = input("Write a sentance with both upper case and lower case letters. ")
    akronomed_str = ""
    for letter in akro_str:
        if str.isupper(letter):
            akronomed_str += letter

    print(akronomed_str)


def str_mask():
    """
    Masks a string of numbers with # but leaves the last 4 digits
    """
    mask_input = input("Provide a long number. ")
    mask_length = len(mask_input)
    last4 = mask_input[-4:]
    mask = multiply(mask_length - 4, "#")
    masked_str = mask + last4
    print(masked_str)


def menu():
    """
    The main menu
    """

    while True:
        print(marvin_image)
        print("Hi, I'm Robbie. I know almost all and will do my best to serve you. What can I do for you?")
        print("1) Present yourself to Marvin.")
        print("2) Convert C to F.")
        print("3) Word multiplication.")
        print("4) Calculate average.")
        print("5) Compare numbers.")
        print("6) Modify string.")
        print("7) Isogram.")
        print("8) Randomise string. ")
        print("9) Anagram. ")
        print("10) Akronom. ")
        print("11) Akronom. ")
        print("q) Quit.")

        choice = input("--> ")
        
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            greeter()
        
        elif choice == "2":
            temp_converter()
            
        elif choice == "3":
            word_multiplier()
        
        elif choice == "4":
            average_calc()

        elif choice == "5":
            compare_numbers()

        elif choice == "6":
            modify_string()
        
        elif choice == "7":
            isogram()
        
        elif choice == "8":
            randomise_string()
        
        elif choice == "9":
            anagram()

        elif choice == "10":
            akronom()

        elif choice == "11":
            str_mask()
        
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

menu()
