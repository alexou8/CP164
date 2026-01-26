"""
-------------------------------------------------------
Lab 1, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-11"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

for food in foods:
    print(food, end="\n\n")