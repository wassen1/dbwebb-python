#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""

def analyze_text():
    """
    Analyses text
    """
    import analyze_functions as an


    while True:
        choice = input("Välj alternativ: v, p eller u. Avsluta med q eller quit -->")

        if choice in ("q", "quit"):
            break

        elif choice == "v":
            print(an.number_of_vowels("manifesto.txt"))

        elif choice == "p":
            print(an.number_of_dots("manifesto.txt"))

        elif choice == "u":
            print(an.number_of_upper("manifesto.txt"))

        else:
            print("Not an option!")

    return True

def list_median(values):
    """
    Returns the median value from values given
    """
    median = 0
    length_list = len(values)
    values.sort()
    
    if length_list % 2 == 0:
        position = int(length_list / 2)
        median = (values[position - 1] + values[position]) / 2
        
    else:
       
        median = values[int(length_list / 2)]

    return(round(median, 1))

def find_duplicates(values):
    """
    Returns duplicates
    """
    dubbel = {}

    for index, el in enumerate(values):
        values[index] = el.lower()
    for el in values:
        dubbel[el] = dubbel.get(el, 0) + 1
    
    lst = list()
    for k, v in dubbel.items():
        if v > 1:
            lst.append(k)
    lst = sorted(lst)

    
    return lst

def types(items):
    """
    Checks data types
    """
    result = ""

    for el in items:
        if isinstance(el, int):
            if el:
                result += "The square of {i} is {x}. ".format(
                    i=el,
                    x=pow(el, 2)
                )

        elif isinstance(el, str):
            if el:
                result += "The secret word is {s}. ".format(
                    s=el
                )
        
        elif isinstance(el, list):
            if el:
                string = ""
                for ch in el:
                    string += ch + ", "
                result += "The list contains " + string[:-2] + ". "

        else:
            # print(" ELSE ")
            return result

    return result[:-1]

def validate_email(email):
    """
    Validates email
    """
    import re
    if email.count("@") == 1: # - innehåller endast ett "@".
        lst = email.split("@")
        end = lst[1]
        if lst[0]: #- det ska finnas minst en karaktär framför "@". 
            if "." in end: #- efter @, ska det finnas minst en punkt, ".", 
                lst = end.split(".")
                for elm in lst:
                    if elm: #- andra karaktärer framför respektive punkt.
                        pass
                    else:
                        return False
                if end.rfind(".") >= len(end) - 4: #- efter den sista punkten ska det finnas 2 eller 3 karaktärer. 
                    if re.search('[^a-z0-9@._-]+', email) is None: #endast karaktärerna a-z och 0-9 
                        #samt ".", "_", "-", "@". - endast små bokstäver.
                        return True
             
    return False

if __name__ == '__main__':
    analyze_text()
    list_median([])
    find_duplicates([])
    types([])

  

    # for el in not_match:
    #     if validate_email(el) is True:
    #         print("TRUE: ", el)
    #     elif validate_email(el) is False:
    #         print("FALSE: ", el)
    #     else:
    #         print("annat: ", el)
