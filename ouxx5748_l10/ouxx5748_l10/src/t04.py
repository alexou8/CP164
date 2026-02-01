"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from test_Sorts_List_linked import SORTS, test_sort

print(
    f"n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for title, sort_function in SORTS:
    test_sort(title, sort_function)

