"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

q = Queue(5)

print(len(q))

print(q.is_empty())

q.insert(10)

print(len(q)) 

value = q.peek()
print(value)  

removed = q.remove()
print(removed) 

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.insert(50)

print(q.is_full())
