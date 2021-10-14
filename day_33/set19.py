'''
topic: sets

- boolean functions with sets

* any()
'''


# even if a single element is True, any() will return True
# False if the set is empty

# initializing set
set0 = set()  # empty set
print(any(set0))

# all true values
set1 = {True, 1, 2, 3}
print(any(set1))

# only one value true
set2 = {0, False, 1}
print(any(set2))
