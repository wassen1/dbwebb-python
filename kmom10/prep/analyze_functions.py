"""
Functions for analyzing text
"""
# text = "manifesto.txt"
def read_file(filename):
    """
    Returns the file from given filename
    """
    with open(filename) as fh:
        return fh.read()

def number_of_vowels(filename):
    """
    Calculate how many vowels a string contains
    """
    content = read_file(filename)

    nr_of_vowels = 0
    vowel_string = "aeiouy"
    str_lower = str.lower(content)

    for vowel in vowel_string:
        nr_of_vowels += str_lower.count(vowel)
    return nr_of_vowels

def number_of_dots(filename):
    """
    Calculate number of dots
    """
    content = read_file(filename)

    nr_of_dots = 0

    nr_of_dots = content.count(".")
    
    return nr_of_dots

def number_of_upper(filename):
    """
    Returns number of upper case letters in text
    """
    nr_of_upper = 0
    content = read_file(filename)

    for letter in content:
        if letter.isupper():
            nr_of_upper += 1
    
    return nr_of_upper
