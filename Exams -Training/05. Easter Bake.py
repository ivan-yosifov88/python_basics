import sys
from math import ceil

number_of_breads = int(input())
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
quantity_of_sugar = 0
quantity_of_flour = 0
for breads in range(number_of_breads):
    used_sugar = int(input())
    used_flour = int(input())
    quantity_of_sugar += used_sugar
    quantity_of_flour += used_flour
    if used_sugar > max_sugar:
        max_sugar = used_sugar
    if used_flour > max_flour:
        max_flour = used_flour
sugar_packages = ceil(quantity_of_sugar / 950)
flour_packages = ceil(quantity_of_flour / 750)
print(f"Sugar: {sugar_packages}")
print(f"Flour: {flour_packages}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")