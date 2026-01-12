"""
-------------------------------------------------------
Assignment 4, Task 4
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

target1, target2 = source.split_alt()

print("Target 1:")
while not target1.is_empty():
    print(target1.remove())

print("Target 2:")
while not target2.is_empty():
    print(target2.remove())