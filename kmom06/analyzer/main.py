#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main for text analyser
"""
import analyzer as an
import menu as me


while True:
    
    print("\033[H\033[J")

    me.menu1()
    me.menu2()
    choice1 = me.u_input("Skriv in ett filnamn att analysera eller välj i menyn: ")

    if "quit" in choice1:
        print("\nBye, bye - and welcome back anytime!")
        break

    elif "change" in choice1:
        continue

    me.u_input("Tryck enter för att komma vidare")

    while True:

        filename = choice1
        answers = dict()
        commands = dict()

        print("\033[H\033[J")

        #Menu presentations
        me.menu1()
        me.menu3(choice1)
        me.menu2()


        choice2 = me.u_input("Välj ett sätt att analysera filen: ")

        #The commands connected to functions:
        # commands["quit"] = an.quit_fn
        commands["lines"] = an.count_lines
        commands["words"] = an.count_words
        commands["letters"] = an.count_letters
        commands["word_frequency"] = an.count_word_frequency
        commands["letter_frequency"] = an.count_letter_frequency
        
        #The execusion of the choices
        if choice2 in commands:
            answers[choice2] = commands[choice2](filename)
            an.printer(filename, **answers)
        
        elif choice2 == "all":
            answers["lines"] = an.count_lines(filename)
            answers["words"] = an.count_words(filename)
            answers["letters"] = an.count_letters(filename)
            answers["word_frequency"] = an.count_word_frequency(filename)
            answers["letter_frequency"] = an.count_letter_frequency(filename)
            an.printer(filename, **answers)
      
        elif "change" in choice2:
            break

        elif "quit" in choice2:
            print("\nBye, bye - and welcome back anytime!")
            raise SystemExit

        else:
            print("\nCommand not found")

        me.u_input("Tryck enter för att komma vidare")
      