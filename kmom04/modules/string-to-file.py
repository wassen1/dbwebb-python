#!/usr/bin/env python3
"""
String to file
"""
# import os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(THIS_FOLDER, '../file/items.txt')

filename = "../file/items.txt"

def remove_item():
    """
    Removes items
    """
    content = readfile()
    remove = input("What item should be removed: ")

    if remove in content: # check if item to remove exists
        if content.index(remove) == 0: # if the item is the first line in the file
            modified_content = content.replace(remove, "")
        else:
            modified_content = content.replace("\n" + remove, "")
        #need to check if remove is part of a longer word before removal
        write_to_file(modified_content.strip(), "w")

def replace_content():
    """
    Replaces content
    """
    item = ""
    result = ""
    while item != "q":
        result += item + "\n"
        item = input("Item to add: ")
    write_to_file(result.strip(), "w")


def write_to_file(content, mode):
    """
    Write new content, removes the old content
    """
    with open(filename, mode) as filehandler:
        if len(content) > 1:
            filehandler.write(content)


def readfile():
    """
    Reads file and returns content
    """
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        content = filehandle.read()
    return content
    

def menu():
    """
    Menu
    """
    print(
        """
1. Show file content
2. Add item, append
3. Replace content
4. Remove an item
        """
        )
    return int(input("Choice: "))

def choice(inp):
    """
    Takes user input choice
    """
    if inp == 1:
        print(readfile())
    elif inp == 2:
        write_to_file("\n" + input("Item to append to file: "), "a")
    elif inp == 3:
        replace_content()
    elif inp == 4:
        remove_item()
    else:
        exit()

if __name__ == "__main__":
    while(True):
        choice(menu())
