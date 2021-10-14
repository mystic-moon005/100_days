'''
topic: sets


- set union
'''


# first set
A = {1, 2, 3}
B = {4, 5, 6}

# printing union using | operator
print(A | B)

# printing union of 3 sets
C = {7, 8, 9}
print(A | B | C)

# printion union using .union() method
# within print() statement
print(A.union(B))
print(A.union(B.union(C)))


# it all works 
