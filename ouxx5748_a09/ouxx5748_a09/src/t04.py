"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-23"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()

arr = [1, 2, 3, 4, 5, 6, 7, 8]

for value in arr:
    bst.insert(value)

zero, one, two = bst.node_counts()

print("Nodes with no children: ")
print(zero)

print()
print("Nodes with one child: ")
print(one)

print()
print("Nodes with two children: ")
print(two)

print()
print("BST contains 8: ")
print(8 in bst)

print()
print("Parent Node for 8: ")
print(bst.parent(8))

print()
print("Parent Node for 8 (recursive): ")
print(bst.parent_r(8))
