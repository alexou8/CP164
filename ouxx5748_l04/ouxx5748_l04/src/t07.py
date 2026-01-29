"""
-------------------------------------------------------
Lab 4, Task 7
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-03"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test

file = open("foods.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)
