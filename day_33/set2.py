'''
TOPIC: Sets

- Modifying sets in python
1. add()
2. update()

- tuple
- string
- list
- set
=== add() and modify() will take one or more
of the above datatypes
    -- compare the outputs + Errors
'''


# creating an empty set
myset = set()
print(myset)  # OUTPUT: empty set is printed

# adding an integer and a float
myset.add(2)
myset.add(2.4)
print(myset)  # works!

# adding a tuple with multiple values
myset.add((3, 4, 5.1))
print(myset)  # works!

# adding a string
myset.add("hello")
print(myset)  # works!

# adding a list
'''
myset.add([9, 8, 7])
print(myset)
# error: TypeError: unhashable type: 'list'
'''
# adding a list with one item
'''
myset.add([9])
print(myset)
# error: TypeError: unhashable type: 'list'
'''
# ----- list cannot be added using the .add() method

# adding a set
'''
myset.add({7, 8, 9.3})
print(myset)
# TypeError: unhashable type: 'set'
'''
# adding a set with single element
'''
myset.add({9})
print(myset)
# TypeError: unhashable type: 'set'
'''
# ----- set cannot be added using the .add() method

# printing the second element of the set
'''
print(myset[1])  # this will give an error
# TypeError: 'set' object is not subscriptable
'''

print()


# -- using .update() method

# adding multiple tuples
myset.update((0.9, (8), 7.9), ("spam", "eggs"))
print(myset)  # works!!

# adding multiple strings
myset.update("hello", "world")
print(myset)

# adding multiple lists
myset.update([1], [3, 5.4])
print(myset)  # works!
'''
NOTE: Lists within lists are not allowed --ERROR
'''

# adding multiple sets
myset.update({33, 55.9}, {9, 26})
print(myset)  # works!
'''
NOTE: sets within sets are not allowed -- ERROR
'''

# adding one list and one set
myset.update([9, 8], {6, 6})
print(myset)


# NOTE that duplicates are avoided in all cases 
