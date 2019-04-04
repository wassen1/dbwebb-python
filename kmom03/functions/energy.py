#!/usr/bin/env python3
""" 
Test how function syntax works in Python3
"""

def calculate_energy(time_in_microwave, effect=800):
    """
    Calculates the energy consumption i kWh
    Returns the consumption
    """
    energy = effect * time_in_microwave / 1000
    return energy

def calculate_cost(energy, price_per_kwh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    cost = energy * price_per_kwh / 100
    return cost

emil_time = 2.5 / 60
emil_energy = calculate_energy(emil_time)
emil_cost = calculate_cost(emil_energy)

nice_string = "Emil använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=emil_energy,
    cost=emil_cost
)
print(nice_string)
