'''
Topic: Sets 

- sets of different types of elements
1. integers
2. multiple

- set of duplicates
- set created from a list
'''


# set of integers
my_set0 = {1, 2, 3}
print(my_set0)

# set of multiple datatypes (immutable elements only)
# float, string, tuple
my_set1 = {1.0, "hello world", (3, 5, 6)}
print(my_set1)

# set of duplicates
my_set2 = {1, 2, 3, 4, 2, 1, 5, 5}
print(my_set2)  # OUTPUT: duplicates removed

# set created from a list --- USING THE KEYWORD set()
my_set3 = set([1, 2, 3, 4])
print(my_set3)

# creating another set from a list 
# this time including different datatypes
# don't forget the KEYWORD set()
my_set4 = set([1, 2, 3, "hello", 2.4])
print(my_set4)  # it works! 

# creating yet another set from -- 2 lists 
'''
my_set5 = set([1, 2, 3], [4, 5, 6])
print(my_set5)
'''
# output: set expected at most 1 argument, got 2

# what if theres a list within the single list
'''
my_set6 = set([1, 2, [3, 4]])
print(my_set6)
'''
# output: TypeError: unhashable type: 'list'

# what if a 'self-declared' set contains a list?
'''
my_set7 = {1, 2, 3, [4, 5, 6]}
print(my_set7)
'''
# output: TypeError: unhashable type: 'list'
