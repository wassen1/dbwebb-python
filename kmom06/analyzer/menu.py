#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The menu
"""
def menu1():
    """
    Prints: Välj i menyn nedan: 
    """
    print("\n")
    print("*********************************************")
    print("Välj i menyn nedan: ")

def menu2():
    """
    Prints menu keys: quit/change
    """
    print("\nquit: Avsluta programmet")
    print("change: Byt text fil")

def menu3(filnamn):
    """
    Prints menu keys
    """
    print("lines: Analysera antalet rader i filen {}.".format(filnamn))
    print("words: Analysera antalet ord i filen {}.".format(filnamn))
    print("letters: Analysera antalet bokstäver i filen {}.".format(filnamn))
    print("word_frequency: Analysera ord frekvensen i filen {}.".format(filnamn))
    print("letter_frequency: Analysera bokstavsfrekvensen i filen {}.".format(filnamn))
    print("all: Analysera {}.".format(filnamn))

def u_input(output):
    """
    Returns user input/waits for input
    """
    choice = input("\n" + output)
    if choice != "\n":
        return choice
    return
