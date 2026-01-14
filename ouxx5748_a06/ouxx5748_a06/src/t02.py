"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-26"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

queue = Priority_Queue()

print("Queue empty: ")
print(queue.is_empty())

print()
print("Length: ")
print(len(queue))

queue.insert(1)

print()
print("Length: ")
print(len(queue))

queue.insert(2)

print()
print("Removed Node: ")
print(queue.remove())

print()
print("First in queue: ")
print(queue.peek())

queue1 = Priority_Queue()

queue1.insert(3)

queue2 = Priority_Queue()

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

queue2.insert(1)

queue2.insert(2)

queue2.insert(3)

queue2.insert(4)

target3, target4 = queue2.split_key(3)

print()
print("Target1: ")
for value in target3:
    print(value)

print()
print("Target2: ")
for value in target4:
    print(value)
