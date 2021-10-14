'''
topic: sets

- copy() method
Create a set
create another empty set --- set()
Copy it to a new set
Add an element to the new set
Print both
Clear the main set
Print both
'''


# initializing a set
A = {1, 2, 3, 4, 5}

# creating an empty set
B = set()

# printing both
print(A)
print(B)

# copy A into B
B = A.copy()  # NOTE the usage

# printing
print(A)
print(B)

# adding an element to B
B.add(10)

# printing
print(A)
print(B)

# clearing main set (A)
A.clear()  # NOTE the usage

# printing both again
print(A)  # an empty set set()
print(B)
