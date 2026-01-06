"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, calories_by_origin

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

average = calories_by_origin(foods, 6)

print(f"Average Calories: {average}")
