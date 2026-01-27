"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import stack_test

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)