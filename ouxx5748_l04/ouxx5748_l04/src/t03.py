"""
-------------------------------------------------------
Lab 4, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-03"
-------------------------------------------------------
"""
# Imports
from List_array import List

list1 = List()

list1.append(10)

print(len(list1))

list1.insert(0, 18)

print(len(list1))

remove = list1.remove(18)

print(remove)
