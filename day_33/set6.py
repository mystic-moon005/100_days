'''
topic: sets

- set intersection
'''


A = {1, 2, 3, 4, 5, 6}
B = {1, 3, 7, 8}
C = {1, 4, 5}

# printing intersection of A and B using & operator
print(A & B)
# output 1

# printing the same using .intersection() method
print(A.intersection(B))

# intersection of A B and C
# all have 1 as the common element
print(A & B & C)

# what if there is no common element
D = {9, 10, 11}
print(A & B & C & D)
# empty set is returned: set()
