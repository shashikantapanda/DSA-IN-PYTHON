# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:12:29 2024

@author: Shashikanta Panda
"""
# -----------------------------------------------------------------------------
#                                   DAY - 1
# -----------------------------------------------------------------------------
#                      1. Introduction to Lists in Python
# -----------------------------------------------------------------------------

# a list is a built in data structure in python that is
# mutable(modifiable) and can store a collection of items of same type or
# a mix of different types.

# Creating a list
my_list = [10, 20, 30, 40, 50]

# Mixed data type list
mixed_list = [1, "hello", 3.5, True]

print("Integer List:", my_list)
print("Mixed List:", mixed_list)

# -----------------------------------------------------------------------------
#                             2. Types of Lists
# -----------------------------------------------------------------------------

# Lists can vary based on the types of elements they hold.
# Homogeneous Lists (same type): Often used for numerical computations like 
# prefix sums, cumulative frequency, etc.
# Heterogeneous Lists: Useful for complex structures like adjacency lists in graphs.
# Nested Lists: Ideal for matrix representation or storing tree/graph nodes.

# Homogeneous List (all elements are of the same type)
numbers = [1, 2, 3, 4, 5]

# Heterogeneous List (elements of different types)
data = [10, "Python", 3.14, False]

# Nested List (a list within a list)
nested = [[1, 2], [3, 4], [5, 6]]

print("Homogeneous List:", numbers)
print("Heterogeneous List:", data)
print("Nested List:", nested)

# -----------------------------------------------------------------------------
#                   3. List Declaration and Initialization
# -----------------------------------------------------------------------------

# There are multiple ways to declare and initialize lists.
# Empty list
empty_list = []

# Initialize with values
fruits = ["apple", "banana", "cherry"]

# Using range() to generate a sequence
numbers = list(range(1, 11))

# Initialize with repetitive values
repeated = [0] * 5

print("Empty List:", empty_list)
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Repeated Values:", repeated)

# -----------------------------------------------------------------------------
#                           4. Basic List Operations
# -----------------------------------------------------------------------------
# You can perform a variety of operations on lists like accessing elements, 
# adding/removing items, and finding the length.

# Accessing elements
fruits = ["apple", "banana", "cherry"]
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Adding elements
fruits.append("orange")  # Adds at the end
fruits.insert(1, "grape")  # Adds at index 1
print("After Adding Fruits:", fruits)

# Removing elements
fruits.remove("banana")  # Removes the first occurrence
last_fruit = fruits.pop()  # Removes and returns the last element
print("After Removing Fruits:", fruits)
print("Popped Fruit:", last_fruit)

# Length of a list
print("Number of Fruits:", len(fruits))

# -----------------------------------------------------------------------------
#                              5. List Traversal
# -----------------------------------------------------------------------------
# Traversing a list means accessing and working with its elements one by one.

# Using a for loop
numbers = [10, 20, 30, 40]
for num in numbers:
    print("Number:", num)

# Using a while loop
i = 0
while i < len(numbers):
    print("Number at index", i, ":", numbers[i])
    i += 1

# List comprehension for traversal
squared = [x**2 for x in numbers]
print("Squared Numbers:", squared)























































