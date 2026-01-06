"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, food_table

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

food_table(foods)
