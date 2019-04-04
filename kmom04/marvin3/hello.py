#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Answers from Marvin
"""
import random

msgs = ['Ja, vad kan jag göra för Dig?', 'Låt mig hjälpa dig med dina strävanden.', 'Ursäkta, vad önskas?', \
'Kan jag stå till din tjänst?', 'Jag kan svara på alla dina frågor.', 'Ge me hög-fem!', \
'Jag svarar endast inför mos, det är min enda herre.', 'mos är kungen!', \
'Oh, ursäkta, jag slumrade visst till.', \
'Fråga, länka till exempel samt source.php/gist/codeshare och vänta på svaret.']

helloes = ['Hej själv! ', 'Trevligt att du bryr dig om mig. ', 'Det var länge sedan någon var trevlig mot mig. ', \
'Halloj, det ser ut att bli mulet idag. ']

smilies = [':-D', ':-P', ';-P', ';-)', ':-)', '8-)']

lunchQuote = ['ska vi ta %s?',\
'ska vi dra ned till %s?', \
'jag tänkte käka på %s, ska du med?', \
'På %s är det mysigt, ska vi ta där?']

lunchStan = ['Olles krovbar', \
'Lila thai stället', \
'donken', \
'tex mex stället vid subway', \
'Subway', \
'Nya peking', \
'kebab house', \
'Royal thai', \
'thai stället vid hemmakväll', \
'Gelato', \
'Indian garden', \
'Sumo sushi', \
'Pasterian i stan', \
'Biobaren', \
'Michelangelo']

def hello():
    """
    Greeting phrases
    """

    msg = random.choice(msgs)
    hi = random.choice(helloes)
    smiley = random.choice(smilies)

    return hi + " " + msg + " " + smiley

def lunch():
    """
    Returns lunch suggestions
    """
    lunch_quote = random.choice(lunchQuote)
    lunch_stan = random.choice(lunchStan)

    return lunch_quote % lunch_stan
