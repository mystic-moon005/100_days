'''
TOPIC: sets

- using discard and remove methods
to remove elements from a set()
'''


# initializing a set
myset = {1, 2, 3, 4, 5}
print(myset)

# discard an element that is present
myset.discard(1)
print(myset)

# discarding multiple elements -- try
'''
myset.discard(4, 5)
print(myset)

ERROR: TypeError: set.discard() takes exactly one argument (2 given)
so only one arg is allowed
'''

# discarding an element that is not present
myset.discard(6)
print(myset)

#removeing and element from the list
myset.remove(2)
print(myset)

# removing multiple elements from the set
'''
myset.remove(3, 4)
print(myset)

ERROR: TypeError: set.remove() takes exactly one argument (2 given)
'''

# removing an element that is not present
'''
myset.remove(2)
print(myset)  # this will return an error

# ERROR: KeyError: 2
'''
