"""
-------------------------------------------------------
Lab 3, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-25"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

queue = Queue()

value = input("Enter a value: ")

queue.insert(value)

print(len(queue))
