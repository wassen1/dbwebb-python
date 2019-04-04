#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for analyzing text
"""
import re

# text = "value-of-time.txt"
def read_file(filename):
    """
    Returns the file from given filename
    """
    with open(filename) as fh:
        return fh.read()

def number_of_spaces(filename):
    """
    Returns number of spaces in given text
    """

    content = read_file(filename)
    nr_of_spaces = 0

    # paragr = content.split("\n")
    # print(paragr)
    nr_of_spaces = content.count(" ")

    return nr_of_spaces


def number_of_letters(filename):
    """
    Returns number of letters in given text
    """
    count = 0

    with open(filename) as filehandle:
        for line in filehandle.readlines():
            if len(line) > 1:
                letters = re.split('[^a-zA-Z]+', line)

                for letter in letters:
                    count += len(letter)

    return count

def number_of_specials(filename):
    """
    Calculate how many vowels a string contains
    """
    content = read_file(filename)

    SPECIALS = "(),\".:-'?"
    specials = []
    paragrafs = content.split("\n")

    for para in paragrafs:
        nr_of_specials = 0
        if len(para) > 1:
            for special in SPECIALS:
                # print("special: ", special)
                nr_of_specials += para.count(special)
            # print("Append nr: ", nr_of_specials)
            specials.append(nr_of_specials)
    
    specials.sort(reverse=True)
    # print("specials", specials)
    return specials[0]
