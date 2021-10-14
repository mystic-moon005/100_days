'''
topic: sets

set membership test
= in
= not in
'''


# initializing a set
# with a single string
myset = set("apple")  # note the usage of set() func here
print(myset)
'''
NOTE --- the string is broken down to chars in set

-- so these tests are running thorugh a set of
chars -
'''

# check if a single character is present
print('a' in myset)

# check for multiple chars
print('a' and 'p' in myset)  # works

# check for multiple chars (1 char is not in string)
print('a' and 't' in myset)  # false

# check for multiple chars -- or cond.
print('a' or 't' in myset)
# returns the char that exists


# what if the set has multiple strings?
# update
myset.update("banana", "milk")

# printing
print(myset)
'''
- even when new strings are added to the set, they are
broken down to chars ...
-- all these have excluded duplicates
-- refer to print() statements to understand
'''
