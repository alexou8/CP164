"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)