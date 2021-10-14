'''
topic: sets

- boolean functions with sets

* all()
'''


set0 = {1, 2, 3, 4}  # all True values
print(all(set0))

set1 = set()  # empty set
print(all(set1))

set2 = {5, 6, 7, 8}  # all True values
print(all(set0 | set2))



# Question: when does it return false?

# add 'false' as an element
set3 = {1, 4, 3, False}
print(all(set3))  # False

# 0 as a value also returns false
set4 = {0}
print(all(set4))
