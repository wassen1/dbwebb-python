#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The main for Marvin
"""

import marvin as ma
import quote as qu
import choise_12 as ch12
import hello as he

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
        print("11) Masking. ")
        print("12) Print current info. ")
        print("q) Quit.")

        choice = input("--> ")

        
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif "citat"in choice.lower():
            print("\n", qu.readquote().rstrip())
        
        elif "hej"in choice.lower():
            print("\n", he.hello().rstrip())

        elif "lunch"in choice.lower():
            print("\n", he.lunch().rstrip())

        elif choice == "1":
            ma.greeter()
        
        elif choice == "2":
            ma.temp_converter()
            
        elif choice == "3":
            ma.word_multiplier()
        
        elif choice == "4":
            ma.average_calc()

        elif choice == "5":
            ma.compare_numbers()

        elif choice == "6":
            ma.modify_string()
        
        elif choice == "7":
            ma.isogram()
        
        elif choice == "8":
            ma.randomise_string()
        
        elif choice == "9":
            ma.anagram()

        elif choice == "10":
            ma.akronom()

        elif choice == "11":
            ma.str_mask()
        
        elif choice == "12":
            ch12.choice_12()
        
        else:
            print("\nThat is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
menu()
