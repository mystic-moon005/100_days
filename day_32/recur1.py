'''
RecursionError example
'''


def recursor():
    recursor()
recursor()


'''
Output:

Traceback (most recent call last):
  File "<string>", line 3, in <module>
File "<string>", line 2, in recursor
  File "<string>", line 2, in recursor
  File "<string>", line 2, in recursor
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
'''