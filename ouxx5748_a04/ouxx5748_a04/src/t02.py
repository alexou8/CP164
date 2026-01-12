"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

source = Queue()

source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)

target = Queue()

target.insert(1)
target.insert(2)
target.insert(3)
target.insert(4)
target.insert(5)

equals = source == target

print(equals)
