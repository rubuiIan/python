list_example = ["one", "two", "three", "four","four","three"]
set_example = {"one", "two", "three", "four","four", "three"}
tuple_example_one = ("one", "two", "three", "four","four", "three")
tuple_example_two = "one", "two", "three", "four","four", "three"

'''
To find out the type of a variable, we use the inbuilt function  type() which takes in our variable as its argument, and returns the datatype if our variables
'''


print(type(list_example))
print(type(set_example))
print(type(tuple_example_one))
print(type(tuple_example_two))

print(list_example)
print(set_example)
print(tuple_example_one)
print(tuple_example_two)

'''
Lists
- Alis t can take in any datatype, it also indexes each item inside it
Collection Properties
1. List 
   Characteristics
   a. uses indexes to arrange list items
   b. Is mutable; chamgeable, we can add, remove/modify items inside it
   c. Can take in any datatype
   d. Can take in any initial number of of items
   List Operations
     1.ADDING ITEMS
   We can addd an item at the end of our lists items using the append() function
   Eg: list_a = ["one","two", "three"]
        list_a.append("four")
    Assignmet
    How to add an item at the start of the list_a
    FINDING THE LENGTH OF A LIST
    -We use the inbuilt functio len() and give it our list as its argument
    Eg: len(list_a): This will return 4 as list_a has 4 items 
            max(list_a)- This returns the largest item in our list
            min(list_a)- This returns the smallest item in ourn list
'''

# Adding items at the end of our list
list_example.append("six")
print(f"EDITED LIST_EXAMPLE: {list_example}")
#Getting the number of items in a list
print(len(list_example))


list_b = [10, 6, 88, 0]
# Getting the maximum value in a list
print(max(list_b))

# Getting minimum value in a list
print(min(list_b))

# Getting a particular item by its index
#NB: Indexing in a collection will always start at 0
print(list_example[-6])

# Modifying an item in our list
list_example[-1] = "ten"
print(list_example)

# Removing an item from a list
# Removing  an aitem from a particular value 
list_example.remove("ten")
print(list_example)

# removing an item at the end of our list
list_example.pop()
print(list_example)

# Iterating through our list items
# We iterets through our list using the  for .. in loop
for item in list_example:
    print(f"Item {item}")