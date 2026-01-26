"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-28"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts


arr = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]

a = Deque()

for value in arr:
    a.insert_rear(value)

Sorts.gnome_sort(a)

print(", ".join(str(value) for value in a))
