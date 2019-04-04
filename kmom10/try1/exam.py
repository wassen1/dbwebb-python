#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""

def analyze_text():
    """
    Analyses the text for spaces, letters and specials
    """
    import analyze_functions as an

    while True:
        choice = input("Välj alternativ: s / spaces, l / letters eller c / specials. Avsluta med q eller quit --> ")

        if choice in ("q", "quit"):
            break

        elif choice in ("s", "spaces"):
            print(an.number_of_spaces("value-of-time.txt"))

        elif choice in ("l", "letters"):
            print(an.number_of_letters("value-of-time.txt"))

        elif choice in ("c", "specials"):
            print(an.number_of_specials("value-of-time.txt"))

        else:
            print("Not an option!")

    return True

def validate_mobile(num):
    """
    Validates mobile number xxx-xxx xx xx
    """
    import re

    PREFIX = ("070", "072", "073", "076", "079")
    if len(num) == 13:
        if num.find("-") == 3: #bindestreck
            lst1 = num.split("-")
            if lst1[0] in PREFIX: #Matches prefix
                if re.search('[^0-9 ]+', lst1[1]) is None:
                    suffix = lst1[1].split(" ")
                    if len(suffix) == 3 and len(suffix[0]) == 3 and len(suffix[1]) == 2 and len(suffix[2]) == 2:
                        return True

    return False

def verify_credit_card(num):
    """
    Verifies credit card number
    """
    # for num in number:
    kontroll = num[-1]
    rest_nr = []
    
    for index, el in enumerate(num[:-1]):
        if index % 2 == 0:
            el = int(el) * 2
        rest_nr.append(int(el))

    for index, el in enumerate(rest_nr):
        if el > 9:
            summy = 0
            for e in str(el):
                summy += int(e)
            rest_nr[index] = summy
    
    sum_of_rest = sum(rest_nr)
    mult_9 = sum_of_rest * 9
    if str(mult_9)[-1] == kontroll:
        return True
    #     print("TRUE")
    # else:
    #     print("False")

    # print(num)
    # print("Rest", rest_nr)
    # print("sum", sum_of_rest)
    # print("mult", mult_9)
    
    # print(str(mult_9)[-1])
    # print("kontroll: ", kontroll)



    return False

def find_difference(items, items2):
    """
    Returns differences
    """
    
    dict1 = {}
    dict2 = {}
    result = list()

    for el in items:
        el = el.lower()
        dict1[el] = el

    for el in items2:
        el = el.lower()
        dict2[el] = el
    # print(dict1)
    # print(dict2)
    
    for el in dict1:
        #print(el)
        if el in dict2:
            pass
        else:
            result.append(el)
            #print(result)
    
    for el in dict2:
        #print(el)
        if el in dict1:
            pass
        else:
            result.append(el)
            #print(result)
    
    return sorted(result)


    
    # return items, items2

def validate_date_time():
    """
    Assignment 5
    """
    return True

if __name__ == '__main__':


    analyze_text()
    validate_mobile("")
    verify_credit_card("")
    find_difference([], [])
    validate_date_time()
