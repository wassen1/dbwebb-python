#!/usr/bin/env python3
"""
Check ammount of apples left
"""
for number_of_apples in range(3, 15):
    if number_of_apples > 10:
        print("Du har mer än 10 äpplen")
    elif number_of_apples <= 10 and number_of_apples > 5:
        print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
    else:
        print("Du har nog varit hungrig och ätit upp dina äpplen")
