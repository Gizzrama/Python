tuple1 = (1, 2, 3.4, "Srihari", True)
tuple2 = tuple(reversed(tuple1))

while True:
    print(f"The elements present in the tuple are", tuple1)
    print(f"The first element stored in this tuple is", tuple1[0])
    print(f"The last element in the tuple is", tuple1[-1])

    print(f"The first three elements are", tuple1[0:3])
    print(f"The last three elements in the tuple are", tuple1[-3: len(tuple1) + 1])
    print("The reverse order of the tuple is", tuple2)
    break

#Tupels
#What a tuple is
#    A built-in Python data type
#    An ordered collection of items
#    Written with parentheses, items separated by commas (the commas are what make it a tuple, so 10, 2 works without brackets)

#Key properties
#    Ordered: items keep their position
#    Indexed: items are accessed by position, starting at 0 (negative indexes count from the end
#    Immutable: items cannot be changed, added, or removed after creation
#    Allows duplicates: the same value can appear more than once
#    Can hold any type: mixed types and other tuples or lists are allowed
#    Fixed size: the length cannot change
#    Hashable: can be used as a dictionary key or set member (if all its items are hashable)

#Common operations
#    Access by index or slice
#    Get the length with len()
#    Count occurrences with count()
#    Find a position with index()
#    Concatenate with + and repeat with * (both create a new tuple)
#    Test membership with in and not in
#    Loop over items with a for loop
#    Unpack into variables: a, b = (10, 2)
#    Compare with ==, <, > (item by item)
#    Use min(), max(), sum(), sorted() (sorted() returns a list)

#Only two methods
#   Tuples have just count() and index(), because they cannot be modified

#Special cases
#    Empty tuple: ()
#    Single-item tuple needs a trailing comma: (5,) (without it, (5) is just the number 5)
#    A tuple containing a mutable item (like a list) can still have that inner item changed

#Tuples and expressions
#    A tuple literal like (10, 2) is an expression that evaluates to a tuple object
#    eval("10, 2") returns the tuple (10, 2)
#    numerator, denominator = eval(input(...)) works through tuple unpacking


#The only way to change or alter the items inside a tuple is by converting it into a mutable data structure (preferably list) usint list() and then converting it back into a tuple using tuple()