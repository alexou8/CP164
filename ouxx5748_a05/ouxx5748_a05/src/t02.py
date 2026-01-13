"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-11"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_foods
from Sorted_List_array import Sorted_List

file = open("foods.txt", "rt")
foods = read_foods(file) 
file.close()

lst = Sorted_List()

for food in foods[:5]:  
    lst.insert(food)

test_food = foods[0]
print(f"Contains '{test_food.name}': {test_food in lst}")

lst2 = Sorted_List()
for food in foods[:5]:  
    lst2.insert(food)

print(f"Equal: {lst == lst2}")

print(f"Getitem: {lst[2]}")

lst.insert(test_food)  
print("Print:")
for value in lst:
    print(f"{value.name}")
    
lst.clean()  
print("Cleaned:")
for value in lst:
    print(f"{value.name}")

test_count = lst.count(test_food)
print(f"Count: {test_count}")

found_food = lst.find(test_food)
print(f"Found: {found_food}")

test_index = lst.index(test_food)
print(f"Index: {test_index}")

lst3 = Sorted_List()
lst3.insert(foods[3])
lst3.insert(foods[4])
lst4 = Sorted_List()
lst4.insert(foods[4])
lst4.insert(foods[2])

lst5 = Sorted_List()
lst5.intersection(lst3, lst4)
print("Intersection:")
for value in lst5:
    print(f"{value.name}")

print("Max:", lst.max().name)
print("Min:", lst.min().name)

print("Peek:", lst.peek().name)

lst.remove(test_food)
print(f"Removed:")
for value in lst:
    print(f"{value.name}")

lst.remove_front()
print("Removed front:")
for value in lst:
    print(f"{value.name}")

lst.insert(foods[1])
lst.insert(foods[1])

print(f"Before:")
for value in lst:
    print(f"{value.name}")
    
lst.remove_many(foods[1])
print(f"Removed many:")
for value in lst:
    print(f"{value.name}")

target1, target2 = lst.split()
print("After split, target1:")
for value in target1:
    print(f"{value.name}")
print("After split, target2:")
for value in target2:
    print(f"{value.name}")

target3, target4 = target1.split_alt()

print("Split_alt:")
for value in target3:
    print(f"{value.name}")
    
print("Split_alt:")
for value in target4:
    print(f"{value.name}")

split_key_food = foods[3]
target5, target6 = lst.split_key(split_key_food)

print(f"Key split:")
for value in target5:
    print(f"{value.name}")
    
print(f"Key split::")
for value in target6:
    print(f"{value.name}")

lst3.union(target1, target2)

print("Union:")
for value in lst3:
    print(f"{value.name}")

