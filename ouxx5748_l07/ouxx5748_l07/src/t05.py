"""
-------------------------------------------------------
lab 7, Task 5
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

lst3 = List()

array = [1, 2, 3, 4, 5]

array2 = [1, 2, 3, 5, 4]

for value in array:
    lst1.append(value)

for value in array2:
    lst2.append(value)

lst3.union_r(lst1, lst2)

for value in lst3:
    print(value)
