#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
For retrieve current infos
"""

import datetime
import random

def choice_12():
    """
    Returns current info for Marvin
    """
    filename = 'my_text.txt'

    with open(filename) as filehandle:
        content = filehandle.read()
    
    cur_time = datetime.datetime.now()


    # time = str(cur_time.hour) + ":" + str(cur_time.minute)
    time = str(cur_time.time())[:-7]
    date = cur_time.date()

    #Moods
    moods = ["glad", "ledsen", "deprimerad", "arg", "orolig", "uttråkad", "förvirrad", "uppspelt", "ensam"]
    mood = random.choice(moods)

    intnr = random.randint(0, 1000000000)
    floatnr = random.uniform(0, 100)
        
    print("\n", content.format(time=time, date=date, mood=mood, intnr=intnr, floatnr=floatnr))
    