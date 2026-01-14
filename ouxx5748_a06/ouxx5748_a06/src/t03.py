"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-26"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

queue = Deque()

print("Queue empty: ")
print(queue.is_empty())

queue.insert_front(1)

queue.insert_rear(2)

print()
print("Length: ")
print(len(queue))

print()
print("Front: ")
print(queue.peek_front())

print()
print("Rear: ")
print(queue.peek_rear())

print()
print("Value Removed: ")
print(queue.remove_front())

print()
print("Value Removed: ")
print(queue.remove_rear())

queue.insert_front(1)

queue.insert_rear(2)

queue.insert_rear(3)

queue.insert_rear(4)

queue._swap(queue._rear, queue._front)

print()
print("Values in queue: ")
for value in queue:
    print(value)
