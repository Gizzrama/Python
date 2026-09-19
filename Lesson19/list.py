#DATASTRUCTURES
#Data structures are ways of organizing and storing data so it can be accessed and modified efficiently. Python's four main built-in types are lists, tuples, dictionaries, and sets. 
#Lists are ordered and mutable, used for collections that change. Tuples are ordered but immutable, used for fixed data that shouldn't be altered. Dictionaries store key-value pairs, used for fast lookups by key. Sets hold unique, unordered items, used for removing duplicates and quick membership checks. 
#Choosing the right structure improves code speed, clarity, and memory use, and prevents errors.


number = [1, 6, 7, 2]
print(number)

print(number[0])
number.append(96)
number.append(104)

print(number)

print(number[2:5])
print(number[3:6])

print("The length of the list is", len(number))

for i in range(len(number)):
    print(i, number[i])

number.reverse()
print(number)

number.sort()
print(number)

number.remove(104)
print(number)

number.pop()
print(number)

#This is a list
#What a list is
#    A built-in Python data type
#    An ordered collection of items
#    Written with square brackets, items separated by commas

#Key properties

#    Ordered: items keep their position
#    Indexed: items are accessed by position, starting at 0 (negative indexes count from the end)
#    Mutable: items can be changed, added, and removed after creation
#    Allows duplicates: the same value can appear more than once
#    Can hold any type: mixed types and other lists are allowed
#    Dynamic size: grows and shrinks as items are added or removed

#Common operations

#    Access by index [0] or slice [0:3] 
#    Add items with append() and insert(index, element)
#    Remove items with remove() and pop()
#    Sort with sort() --> ascending order
#    Get the length with len()
#    Loop over items with a for loop

#Lists and expressions

#   A list literal like [1, 2, 3] is an expression that evaluates to a list object
#   Indexing a list, like [1, 2, 3][0], is also an expression