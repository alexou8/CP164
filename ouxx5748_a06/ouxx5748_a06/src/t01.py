"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-26"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

queue = Queue()

print("Queue empty: ")
print(queue.is_empty())

print()
print("Queue Full: ")
print(queue.is_full())

print()
print("Length: ")
print(len(queue))

queue.insert(5)

print()
print("Length: ")
print(len(queue))

queue.insert(7)

print()
print("Removed Node: ")
print(queue.remove())

print()
print("First in queue: ")
print(queue.peek())

queue1 = Queue()

queue1.insert(8)

queue2 = Queue()

queue2.combine(queue, queue1)

print()
print("Queue2: ")
for value in queue2:
    print(value)

target1, target2 = queue2.split_alt()

print()
print("Target1: ")
for value in target1:
    print(value)

print()
print("Target2: ")
for value in target2:
    print(value)
