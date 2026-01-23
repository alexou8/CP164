"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-15"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()

arr = [2, 0, 4, 1, 3, 5, 6]

for value in arr:
    bst.insert(value)

print("Valid?: ")
print(bst.is_valid())

print()
print("Balanced?: ")
print(bst.is_balanced())

bst2 = BST()

for value in [1, 2, 3, 4]:
    bst2.insert(value)

print()
print("Minimum: ")
print(bst.min())

print()
print("Nodes with 0 children: ")
print(bst.leaf_count())

print()
print("Nodes with 1 child: ")
print(bst.one_child_count())

print()
print("Nodes with 2 children: ")
print(bst.two_child_count())

print()
print("Values in order: ")
print(bst.inorder())

print()
print("Values in preorder: ")
print(bst.preorder())

print()
print("Values in postorder: ")
print(bst.postorder())

print()
print("Values in levelorder: ")
print(bst.levelorder())

print()
print("Removed: ")
print(bst.remove(3))

print()
print("Updated BST: ")
for value in bst:
    print(value)
