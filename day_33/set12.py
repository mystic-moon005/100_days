'''
TOPIC: sets

- isdisjoint()
syntax: set.isdisjoint(set)

= initialize 2 sets
= apply isdisjoint() and save the result in a new var
= print
'''


# initializing seta A and B
# contain common elements
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

x = A.isdisjoint(B)
print(x)

# initializing sets C and D
# no common elements
C = {1, 2, 3}
D = {4, 5, 6}

y = C.isdisjoint(D)
print(y)
