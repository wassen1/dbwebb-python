#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quote functions
"""


filename = "inv.data"

def readinv():
    """
    Returns a string from datafile
    """
    inventar = []
    # with - as for reading a file automatically closes it after reading is done
    with open(filename, "r") as filehandle:
        doc = filehandle.read()
        if doc:
            inventar = doc.split(';')
    return inventar

def writeinv(array):
    """
    Writes the array into data file
    """
    with open(filename, "w") as filehandle:
        filehandle.write(";".join(array))

def pick(choice, inv_list):
    """
    Manage the pick choice
    """
    pic_item = choice.split("pick ")
    if len(pic_item) > 1:
        inv_list.append(pic_item[1])

        writeinv(inv_list)
        return "You have picked up: " + str(pic_item[1])
    return "You have given a wrong command: " + str(choice)

def drop(choice, inv_list):
    """
    Manages the drop choice
    """
    drop_item = choice.split("drop ")
        
    if len(drop_item) < 2:
        answer = input("\nAre you sure (y/n)")
        if answer.lower() == "y":
            inv_list = []
            writeinv(inv_list)
            return "You have dropped the whole inventory, look: \n" \
                "Inventory: {}".format(inv_list) 

        return "You have choosen to keep your inventory, look: \n" \
            "Inventory: {}".format(inv_list)

    try:
        inv_list.remove(drop_item[1])
    except ValueError:
        return "There are no {} in your inventory.".format(drop_item[1])
        
    writeinv(inv_list)
    return "You have dropped: " + str(drop_item[1])

def inventory(choice):
    """
    Manages the choices of the inventory
    """
    inv_list = readinv()

    if "pick" in choice.lower():
        return pick(choice, inv_list)

    elif "drop" in choice.lower():
        return drop(choice, inv_list)
        # drop_item = choice.split("drop ")
        
        # if len(drop_item) < 2:
        #     answer = input("Are you sure (y/n)")
        #     if answer.lower() == "y":
        #         inv_list = []
        #         writeinv(inv_list)
        #         return "You have dropped the whole inventory, look: \n" \
        #             "Inventory: {}".format(inv_list) 
    
        #     return "You have choosen to keep your inventory, look: \n" \
        #         "Inventory: {}".format(inv_list)

        # try:
        #     inv_list.remove(drop_item[1])
        # except ValueError:
        #     return "There are no {} in your inventory.".format(drop_item[1])
            
        # writeinv(inv_list)
        # return "You have dropped: " + str(drop_item[1])

    else:

        if not inv_list:
            return "It is empty.\n" \
                "Inventory: " + str(inv_list)
        return "You have {} thing(s): {}".format(len(inv_list), inv_list)
