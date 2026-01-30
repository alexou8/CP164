"""
-------------------------------------------------------
Lab 7, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

array = [1, 2, 3, 4, 5]

for value in array:
    lst.append(value)

odd, even = lst.split_alt_r()

print("Printing Even: ")
for value in even:
    print(value)

print()
print("Printing Odd: ")
for value in odd:
    print(value)
