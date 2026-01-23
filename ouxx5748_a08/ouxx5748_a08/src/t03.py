"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-15"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

# Takes a long time to compute

DATA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

bst = BST()

for value in DATA:
    letter = Letter(value)
    bst.insert(letter)

file = open('otoos610.txt', 'rt')

do_comparisons(file, bst)

file.close()

letter_table(bst)
