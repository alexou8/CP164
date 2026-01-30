"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

array = [1, 2, 3, 4, 5]

for value in array:
    lst.append(value)

p, c, i = lst._linear_search_r(3)

print(p._value)
print(c._value)
print(i)