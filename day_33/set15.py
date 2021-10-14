'''
topic: sets

- symmetric_difference_update()
SYNTAX: A.symmetric_difference_update(B)

= use two methods
1. symmetric_difference
2. symmetric_difference_update
'''


# initializing two sets
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }
# elements not common in both sets

# taking symmetric difference
print(A ^ B)

# printing original set A
print(A)

# taking symmetric_difference_update
A.symmetric_difference_update(B)

# printing original set again
# values will be changed to {a, e}
print(A) 
