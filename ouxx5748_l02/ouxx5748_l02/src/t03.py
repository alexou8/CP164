"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)
