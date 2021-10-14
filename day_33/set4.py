'''
topic: sets

- using pop() and clear() methods
'''


# initializing a set
set0 = {1, 2, 3, 4, "hello", "spam", "eggs"}

# using .pop() directly with the print statement
print(set0.pop())  # random element is removed and returned

# using again
print(set0.pop())

# using .clear()
print(set0.clear())
# NONE is returned .. means set() is cleared of all elements 
