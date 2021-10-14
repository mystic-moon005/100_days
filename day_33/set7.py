'''
topic: PYTHON

- set difference
'''


# initializing two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
print(B.difference(A))

# initializing a third set
C = {4, 5, 6, 7}

# difference of C and B and then A
print(A - (B - C))

'''
B - C
= (4, 5, 6, 7, 8) - (4, 5, 6, 7)
= (8)

A - (B - C)
= (1, 2, 3, 4, 5) - (8)
= (1, 2, 3, 4, 5)
'''
