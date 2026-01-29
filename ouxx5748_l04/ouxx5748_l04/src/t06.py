"""
-------------------------------------------------------
Lab 4, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-03"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array

llist = List()

source = [0, 1, 2, 3, 4, 5]

array_to_list(llist, source)

print("List: ")
for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("List: ")
for value in source:
    print(value)
