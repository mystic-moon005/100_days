'''
topic: sets

- boolean functions with sets
* enumerate
'''


# initializing a set
myset = {9, 8, 78, 4.5, (9, 0, 2.6), "spam", "eggs", "a"}

# enumerating and printing
print(enumerate(myset))
# out is just a reference

# storing enumerated object in a separate var
newset = enumerate(myset)

# calling + printing the newset()
# since calling a func set() - use parenthesis
print(set(newset))  # works


'''
METHOD:
- store the enumerated set in a new var
- use the set() func to print it 
'''
