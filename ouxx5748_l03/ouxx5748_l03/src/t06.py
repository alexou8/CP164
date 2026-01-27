"""
-------------------------------------------------------
Lab 3, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-25"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test


pq = Priority_Queue()

source = [1, 2, 3, 4, 5]

array_to_pq(pq, source)

while len(pq) > 0:
    value = pq.remove()
    print(value)
    source.append(value)

array_to_pq(pq, source)

pq_to_array(pq, source)

print(source)

file_variable = open("foods.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

priority_queue_test(foods)