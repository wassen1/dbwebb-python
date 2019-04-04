# main.py
"""
Main
"""

import energy_calculation as ec

emil_time = 2.5 / 60
emil_energy = ec.calculate_energy(emil_time)
emil_cost = ec.calculate_cost(emil_energy)

emil_string = "Emil använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=emil_energy,
    cost=emil_cost
)
print(emil_string)
# Emil använder 0.0333 kWh och detta kostar 0.0260 kr
