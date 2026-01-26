"""
-------------------------------------------------------
Lab 1, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-11"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_food, write_foods

ravioli = read_food('Ravioli|2|True|300')

spanakopita = read_food('Spanakopita|5|True|260')

file = open("new_foods.txt", "wt")

write_foods(file, [ravioli, spanakopita])

file.close()