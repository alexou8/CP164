"""
-------------------------------------------------------
Asignment 9, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_sorted import Hash_Set
from functions import insert_words, comparison_total

hs = Hash_Set(20)

with open('otoos610.txt', 'rt') as file:
    insert_words(file, hs)

total, max_value = comparison_total(hs)

print("Using array-based Sorted List Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{max_value.word}': {max_value.comparisons:,}")
