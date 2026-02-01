"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-14"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Food import Food


hs = Hash_Set(3)  

print("Inserting: ")
hs.insert(Food("Spring Rolls", 1, True, 200))
hs.insert(Food("Chicken Kabob", 2, False, 167))
hs.insert(Food("Pasta", 7, True, 350))
hs.insert(Food("Sushi", 6, False, 250))  


print("Rehash:")
hs.debug()