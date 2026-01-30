"""
-------------------------------------------------------
Lab 7, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst1 = List()

lst2 = List()

array = [1, 2, 3, 4, 5]

array2 = [2, 3, 4, 5, 1]

for value in array:
    lst1.append(value)

for value in array2:
    lst2.append(value)

print(lst1.is_identical_r(lst2))
