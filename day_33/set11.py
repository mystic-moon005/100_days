'''
topic: sets

- intersection
- intersection_update

The intersection_update() method
removes the items that is not present in both sets
(or in all sets if the comparison is done between more than two sets).

The intersection_update() method is different
from the intersection() method,
because the intersection() method returns a new set,
without the unwanted items,
and the intersection_update() method
removes the unwanted items from the original set.
'''


# use 3-4 sets to try this out

#initializing
A = {1, 2, 3, 4}
B = {1, 4, 5, 6, 7}
C = {2, 3, 8, 9}

# intersection of A and B
print(A & B)

# print A and B
# note that the original sets are not changed
print(A)
print(B)

# applying intersection_update method
# syntax: set.intersection_update(set1, set2 ... etc)
A.intersection_update(B, C)
print(A)
'''
nothing is common between B and C
hence answer to that is an empty set()
then A has nothing in common with the set()
so A ... the original set ... also becomes an empty set() 
'''
