"""
-------------------------------------------------------
Lab 6, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-25"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from List_linked import List

file_variable = open("foods.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

for value in foods:
    new_list.append(value)

print(new_list.count(foods[5]))

print()
print(new_list.max())

print()
print(new_list.min())
