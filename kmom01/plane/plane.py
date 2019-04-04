#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Converting celcius to farenheit
"""
heightMeter = input("Mata in höjd över havet (meter): ")
speedKmH = input("Mata in hastighet (km/h): ")
tempC = input("Mata in temperatur utanför flygplanet (Celsius)")

heightFeet = int(heightMeter) * 3.28084
speedMph = int(speedKmH) * 0.62137
tempF = int(tempC) * 9 / 5 + 32

print("Höjd över havet (feet): ", heightFeet)
print("Hastighet (mph): ", speedMph)
print("Temperatur utanför flygplanet (Farenheit): ", tempF)
