'''
topic: python

- set symmetric difference
'''


# initializing sets A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)
# output: 1, 2, 3, 6, 7, 8   YESSS

# initalizing a third set C
C = {4, 5, 6, 7}

print(A.symmetric_difference(B.symmetric_difference(C)))
# lol shouldve used this above :P
# output: 1, 2, 3, 8  :/

'''
B ^ C = 8
A ^ ( B ^ C ) = 1, 2, 3, 4, 5, 8

-_-

'''
