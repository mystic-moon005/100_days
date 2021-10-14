'''
topic: sets

- difference
- difference update


The difference_update() method
removes the items that exist in both sets.

The difference_update() method is different
from the difference() method,
because the difference() method returns a new set,
without the unwanted items, and the difference_update() method
removes the unwanted items from the original set.


- take two sets
- apply .difference() method --
- apply difference_update
- print

--- NOTE:
the difference() just 'returns' a new set-
it doesnt change the original set --
make sure to print the original set
after applying both methods to understand the difference.
'''


# initializing
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print(A - B)
#output: 1, 2, 3

# printing
print(A)  # see here, the original set is not changed

# applyling difference_update
# syntax: set.difference_update(set)
A.difference_update(B)

# printing
print(A)  # original will be changeed 
