"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-28"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts


arr = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]

a = List()

for value in arr:
    a.append(value)

Sorts.radix_sort(a)

print(", ".join(str(value) for value in a))
