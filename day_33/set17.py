'''
topic: sets

iterating through a set

- strings
- integers
- multiple datatypes
'''


# initializing a set of strings
'''
A = set("spam", "eggs")
print(A)
OUTPUT:
TypeError: set expected at most 1 argument, got 2
'''

# initializing using set() func
A = set("eggs")
print(A)  # chars

# initializing directly
B = {"spam"}
print(B)  # string

# taking union
print(A | B)

# adding a string to a
A.add("milk")
print(A)  # remains strings

# --- back to question

# iterate through a set of strings
# initializing a set with multiple strings
myset = {"spam", "eggs", "milk"}
print(myset)  # okay question yet not solved :/

# --- FOUND THE ANSWER ---
'''
NOTE: It does not break down --- it just removes the duplicates

1. in "eggs" ..
it removes the second 'g' and returns the rest of the string
since the removal breaks it down, its no longer ONE complete string --
instead its just chars

2. in 'milk'
there is no repetition ... so no char needs to be removed
therefore it remains a string
3. same goes with the 'spam'
'''

# -- srsly back to question !!

# myset = {"spam", "eggs", "milk"}
# now we need to iterate using for loop
for word in myset:
    print(word)
'''
NOTE: THEY REMIAN AS WORDS
WHYYYYYYYYYYYYYYYYYYY
'''

# -- anyways back to question

# initializing a set of integers
intset = {1, 2, 3, 4, 5, 6}

# running for loon
for n in intset:
    print(n)

# initializing a set with multiple datatypes
bigset = {'a', 'apple', 'spam', 1, 2, 3, (4, 5), (6, (9.2, 8))}

# now print it !!
for value in bigset:
    print(value)
# ERROR: TypeError: unhashable type: 'list'
# removing list within list
# ERROR: TypeError: unhashable type: 'list'
# removing single list also

# WORKS
