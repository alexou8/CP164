"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, average_calories

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

average = average_calories(foods)

print(f"Average Calories: {average}")
