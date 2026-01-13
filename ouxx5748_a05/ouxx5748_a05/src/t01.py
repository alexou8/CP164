"""
-------------------------------------------------------
Assignment 5, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-10-11"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_food, read_foods
from List_array import List
from utilities import array_to_list

file = open("foods.txt", "rt")
foods = read_foods(file)
file.close()

lst = List()

array_to_list(lst, foods)


test = Food("test", 0, False, 800)

lst.append(test)

print("Print:")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")

lst.clean()

print()
print("Print:")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")

temp = [
    read_food("test1|2|True|100"),
    read_food("test2|4|False|200")
]

lst2 = List()

lst2.append(temp[0])

lst2.append(temp[1])

lst3 = List()

lst3.combine(lst, lst2)

print()
print("Print:")
for value in lst3:
    print(f"{value.name}")

print()
print("Print:")
print(lst3[10])

lst2.append(temp[0])

lst2.append(temp[1])

lst4 = List()

lst4.intersection(lst2, lst3)

print()
print("Print:")
for value in lst4:
    print(f"{value.name}")

lst4.prepend(temp[0])

print()
print("Print:")
for value in lst4:
    print(f"{value.name}")

lst4.remove_front()

print()
print("Print:")
for value in lst4:
    print(f"{value.name}")

lst4.append(temp[0])

lst4.remove_many(temp[0])

print()
print("Print:")
for value in lst4:
    print(f"{value.name}")

target1, target2 = lst3.split()

print()
print("Print:")
for value in target1:
    print(f"{value.name}")


print()
print("Print:")
for value in target2:
    print(f"{value.name}")

target3, target4 = target1.split_alt()

print()
print("Print:")
for value in target3:
    print(f"{value.name}")

print()
print("Print:")
for value in target4:
    print(f"{value.name}")

lst3.union(target3, target4)

print()
print("Print:")
for value in lst3:
    print(f"{value.name}")
