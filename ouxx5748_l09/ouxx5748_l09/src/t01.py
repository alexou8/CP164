"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-14"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_food
from functions import hash_table


food1 = get_food()

print()
food2 = get_food()

print()
hash_table(4, [food1, food2])