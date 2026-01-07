"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-26"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

print(stack_maze(maze))