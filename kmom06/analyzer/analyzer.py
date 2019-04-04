#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Textanalyzing functions
"""
import re


def count_lines(filename):
    """
    Returns number of lines in text
    """
    count = 0
    with open(filename) as filehandle:
        for line in filehandle.readlines():
            if len(line) > 1:

                count += 1
    return count


def count_words(filename):
    """
    Returns number of words in text
    """
    count = 0

    with open(filename) as filehandle:
        for line in filehandle.readlines():
            if len(line) > 1:

                words = re.split('[^a-zA-Z-]+', line)
                count += len(words) - 1
    return count

def count_letters(filename):
    """
    Returns number of letters in text
    """
    count = 0

    with open(filename) as filehandle:
        for line in filehandle.readlines():
            if len(line) > 1:

                words = re.split('[^a-zA-Z]+', line)

                for word in words:
                    count += len(word)

    return count


def count_word_frequency(filename):
    """
    Returns word frequency in text
    """
    countedWords = dict()

    
    with open(filename) as filehandle:
        for line in filehandle.readlines():
            if len(line) > 1:
 
                words = re.split('[^a-zA-Z-]+', line)
                words.remove('')
 
                for word in words:
                    word = word.lower()
                    countedWords[word] = countedWords.get(word, 0) + 1

    lst = list()
    for k, v in countedWords.items():
        lst.append((v, k))
    lst = sorted(lst, reverse=True)
    
    return lst

def count_letter_frequency(filename):
    """
    Returns letter frequency in text
    """
    countedLetters = dict()

    with open(filename) as filehandle:
        for line in filehandle.readlines():
            if len(line) > 1:
    

                words = re.split('[^a-zA-Z]+', line)
                words.remove('')
 
                for word in words:
                    word = word.lower()
                    for letter in word:
                        countedLetters[letter] = countedLetters.get(letter, 0) + 1

    lst = list()
    for k, v in countedLetters.items():
        lst.append((v, k))
    lst = sorted(lst, reverse=True)
    
    return lst
  

def printer(filename, **answers):
    """
    Prints answers
    """

    if "lines" in answers:
        print("\nAntal rader i filen {}: {}".format(filename, answers["lines"]))

    if "words" in answers:
        print("\nAntal ord i filen {}: {}".format(filename, answers["words"]))

    if "letters" in answers:
        print("\nAntal tecken i filen {}: {}".format(filename, answers["letters"]))

    if "word_frequency" in answers:
        lst = answers["word_frequency"]
        total = sum(value for (value, __) in lst)

        print("\nSju mest förekommande ord i texten: ")
        for v, k in lst[:7]:
            perc = round(v / total *100, 2)
            
            print("{key} {value} %".format(key=k, value=perc))
    
    if "letter_frequency" in answers:
        lst = answers["letter_frequency"]
        total = sum(value for (value, __) in lst)

        print("\nSju mest förekommande bokstäver i texten: ")
        for v, k in lst[:7]:
            perc = round(v / total *100, 2)
            
            print("{key} {value} %".format(key=k, value=perc))
