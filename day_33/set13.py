'''
topic: sets

- issubset()
SYNTAX: set.issubset(set)

The issubset() method returns True
if all items in the set exists in the specified set,
otherwise it retuns False.

= initialize 2 sets - same elements
= apply method and store result in a var
= initialize 2 more sets - same + diff elements
= apply method and store result in a var
= print
'''

A = {1, 2, 3}
B = {1, 2, 3, 4, 5, 6}
x = A.issubset(B)
# all elements of A are in B 

C = {1, 2, 3}
D = {2, 3, 4}
y = C.issubset(D)

print(x)
print(y)
