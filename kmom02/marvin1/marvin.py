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
while True:
    # print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Robbie. I know almost all and will do my best to serve you. What can I do for you?")
    print("1) Present yourself to Marvin.")
    print("2) Convert C to F.")
    print("3) Word multiplication.")
    print("4) Calculate average.")
    print("5) Compare numbers.")
    print("6) Modify string.")
    print("7) Isogram.")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = input("What is your name? ")
        print("\nMarvin says:\n")
        print("Hello %s - your awesomeness!" % name)
        print("What can I do you for?!")
    
    elif choice == "2":
        degreeC = input("What degree in C do you want to convert to F? ")
        degreeF = int(degreeC) * 9 / 5 + 32
        print("\nRobbie says:\n")
        print("I converted %s C in to %s !" % (degreeC, degreeF))
        
    elif choice == "3":
        multiplyWord = input("Please provide a word. ")
        multiplyNumber = input("Please provide a number. ")
        print(int(multiplyNumber) * multiplyWord)
    
    elif choice == "4":
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
    
    elif choice == "5":
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

    elif choice == "6":
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
    
    elif choice == "7":
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
    
    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
