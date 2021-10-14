
'''
topic: python decorators

Question:
add the upper_case decorator to modify the simple row of text
from user input
'''


'''
- take input from user
- use upper() method.
- return the decorated result

1. how to take user input
'''


'''
writing a simple code to take and return user input - string
'''
'''
# defining ordinary func. -- takes in user input
def ordinary():
    text = input("Enter your text here: ")
    print(text)
    
    
# calling this func. 
ordinary()
'''


'''
- keeping the ordinary func. as it is:
- returning the text in uppercase
- calling the func

___ NOTE the syntax in which upper() method is used
'''
'''
def ordinary():
    text = input("Enter your text here: ")
    print(text.upper())
 

ordinary()
'''


'''
- moving the upper method to a separate func
- name the enclosing func. as decorator
- name the inner func as make_upper
-
'''


# defining enclosing func
def decorator(func):
    def make_upper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    
    return make_upper
    

@decorator
def ordinary():
    text = input("Enter your text here: ")
    return text


'''
Python shell command
>>> ordinary()
'''
