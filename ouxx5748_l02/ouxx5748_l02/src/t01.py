"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

stack = Stack()

if stack.is_empty():
    print("Stack: empty")
else:
    print("Stack: not empty")

stack.push(1)

value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("bottom")

stack.push("top")

print(stack.peek())

