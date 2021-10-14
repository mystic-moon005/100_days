'''
RecursionError example

- removing the base condition and seeing what happens 
OUTPUT: RecursionError 
'''


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


'''
Traceback (most recent call last):
File "<string>", line 15, in <module>
  File "<string>", line 11, in factorial
File "<string>", line 11, in factorial
  File "<string>", line 11, in factorial
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
'''