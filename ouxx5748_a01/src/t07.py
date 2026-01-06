"""
-------------------------------------------------------
Assignment 1, Task 7
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-12"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

a = [[1, 2, 3], [5, 6, 7]]

small, large, total, average = matrix_stats(a)

print(f'Smallest: {small}')
print(f"Largest: {large}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
