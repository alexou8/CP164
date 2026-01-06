"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-21"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_foods, by_origin

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin:\n{Food.origins()} "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")