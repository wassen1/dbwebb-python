#!/usr/bin/env python3
"""
Checking ammount of apples with while loop
"""

while True:
    user_input = input("Skriv in antal äpplen (eller q för avslut): ")
    if user_input == "q":
        print("Du är nu klar med att äta äpplen.")
        print("Hej då!")
        break
    else:
        try:
            number_of_apples = int(user_input)
        except ValueError:
            print("Uups det blev ett fel! Fyll endast i heltal!")
            continue

        if number_of_apples > 10:
            print("Du har mer än 10 äpplen")
        elif number_of_apples <= 10 and number_of_apples > 5:
            print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
        else:
            print("Du har nog varit hungrig och ätit upp dina äpplen")
