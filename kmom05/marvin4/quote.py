#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quote functions
"""

import random
filename = "quotes.txt"

def readquote():
    """
    Returns a random line
    """
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        lines = filehandle.readlines()
        line = random.choice(lines)
    return line
