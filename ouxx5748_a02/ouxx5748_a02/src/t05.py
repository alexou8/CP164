"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, food_table, food_search

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

search = food_search(foods, 6, 0, False)

food_table(search)
