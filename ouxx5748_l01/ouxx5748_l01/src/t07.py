"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-11"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, get_vegetarian

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

veggies = get_vegetarian(foods)

for food in veggies:
    print(food, end="\n\n")
