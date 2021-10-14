'''
topic: sets

* frozensets
'''


# initialization
# frozenset() func
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A)
# it takes sq. brackets are sets ... not lists

'''
# what if its without the list?
C = frozenset(1, 2, 3)
print(C)
'''
'''
ERROR:
TypeError: frozenset expected at most 1 argument, got 3
'''

D = frozenset("hello")
print(D)

E = frozenset({2, 4, 5})
print(E)


# applying diff methods

# 1. isdisjoint()
print(A.isdisjoint(B))

# 2. difference()
print(A.difference(B))

# 3. union()
print(A | B)

# 4. try add - this will give error
# A.add(3)
# AttributeError: 'frozenset' object has no attribute 'add'
