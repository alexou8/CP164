"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

source1 = Stack()

array_to_stack(source1, [1, 2, 3, 4, 5])

source1.reverse()

while not source1.is_empty():
    value = source1.pop()
    print(value)
