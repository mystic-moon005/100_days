'''
topic: sets

- boolean functions with sets
* sorted()
'''


'''
# initializing a set with multiple datatypes
set0 = {1, 2, 3.4, 'm', "spam", (8, (9.8, 0))}

# sorting and printing
print(sorted(set0))
'''
'''
OUTPUT:
TypeError: '<' not supported between instances of 'int' and 'tuple'
-- so it does not work with multiple datatypes
'''


# only ints
set1 = {1, 2, 3, 6, 10, 0}
print(sorted(set1))  # sorted in ascending order

# only tuples
# tuples within tuples
set2 = {(10, (8, 9), 7), (4, 5, 6), (1, 2, 3)}
print(sorted(set2))  # sorted in ascending order 
