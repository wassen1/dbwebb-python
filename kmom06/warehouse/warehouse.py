"""
example code from course
"""
from operator import itemgetter
warehouse = {
    "köttfärs" : 20,
    "grädde" : 80,
    "krossade tomater": 33,
    "gul lök" : 42
}

print(warehouse["krossade tomater"])

warehouse["krossade tomater"] = 58

warehouse["röd lök"] = 7

print(warehouse)

for key, value in warehouse.items():
    print(key, value)

print("---")
for key in sorted(warehouse.keys()):
    print(key, warehouse[key])


for key, value in sorted(warehouse.items(), key=itemgetter(1), reverse=True):
    print(key, value)

print("---")

warehouse_deluxe = {
    "köttfärs" : {"stock" : 20, "price" : 50},
    "grädde" : {"stock" : 80, "price" : 20},
    "krossade tomater": {"stock" : 33, "price" : 10},
    "gul lök" : {"stock" : 42, "price" : 5}
}

for key in sorted(warehouse_deluxe.keys()):
    print(key, warehouse_deluxe[key]["price"])
