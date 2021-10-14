'''
TOPIC: sets

- issuperset
SYNTAX: set.issuperset(set)

The issuperset() method returns True
if all items in the specified set exists in the original set,
otherwise it retuns False.

= initialize 2 sets - same elements
= apply method and store result in a var
= initialize 2 more sets - same + diff elements
= apply method and store result in a var
= print
'''


A = {1, 2, 3, 4, 5, 6, 7}
B = {4, 5, 6}
x = A.issuperset(B)
# all elements of B are in A 

C = {1, 2, 3, 4, 5}
D = {1, 2, 8}
y = C.issuperset(D)

print(x)
print(y)
