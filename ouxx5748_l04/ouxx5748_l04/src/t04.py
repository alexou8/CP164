"""
-------------------------------------------------------
Lab 4, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-03"
-------------------------------------------------------
"""
# Imports
from List_array import List

list1 = List()

list1.append(7)
list1.append(8)
list1.append(9)
list1.append(-1)
list1.append(-2)

print(list1.index(-1))
print(list1.find(-1))

if 9 in list1:
    print("9 is in list 1")
else:
    print("Not in list 1")

print(list1.count(0))

print(list1.min())
print(list1.max())