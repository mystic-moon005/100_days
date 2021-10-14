'''
topic: sets

- boolean functions with sets
* max()
* min()
'''

# on what basis does it return the max and minvalue?

'''
# initializing a set with multiple values
set0 = {1, 2, 3.4, 'm', "spam", (8, (9.8, 0))}

# print max - check
print(max(set0))
'''
'''
OUTPUT:
TypeError: '>' not supported between instances of 'int' and 'tuple'

-- lets try similar datatypes
'''

# initialize a set with only ints
set1 = {1, 2, 3, 6, 10, 0}
print(max(set1))  # max
print(min(set1))  # min

# initialize a list with only tuples
# try tuples within tuples
set2 = {(1, 2, 3), (4, 5, 6), (7, (8, 9))}
print(max(set2))  # max
print(min(set2))  # min
'''
NOTE :::
tuple within tuple is the max value
''' 
