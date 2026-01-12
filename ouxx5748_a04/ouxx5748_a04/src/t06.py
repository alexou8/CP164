"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()

source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)

key = 3

target1, target2 = source.split_key(key)

print("Target 1:")
while not target1.is_empty():
    print(target1.remove())
    
print("Target 2:")
while not target2.is_empty():
    print(target2.remove())
