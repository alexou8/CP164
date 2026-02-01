"""
-------------------------------------------------------
Lab 9, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-14"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

hset = Hash_Set(20)

hset.insert(10)

hset.insert(20)

hset.insert(30)

print("Printing hset: ")
for value in hset:
    print(value)

removed = hset.remove(20)

print()
print("Removed Value: ")
print(removed)

print()
print("Printing hset: ")
for value in hset:
    print(value)
