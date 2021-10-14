'''
topic: Indirect Recursion

example with exp.
'''


# func for even numbers
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


# func for odd numbers
def is_odd(x):
    # use print statement to see how output decrements 
    # print(x)
    return not is_even(x)  # whatever is the answer of is_even() .. reverse it


# calling is_odd() for an odd num + printing
print(is_odd(17))

# calling is_even() for an odd num + printing   - thats odd lol
print(is_even(23))


'''
Working: 
- for is_odd(17) -- the final statement will be
  === return not is_even(17)
  * since 17 is not an even num, so the answer to is_even() alone will be False
  === return not False
  * now the 'not' operator will change it to True
  === return True
  * hence True will be answer for is_odd(17)
  
- for is_even(23)
  * 23 is passed to is_even() where IF the num is not equal to 0
  === return is_odd(x - 1)
  === return is_odd(22)  
  -- with print() statement, check that 23 never gets printed
  * now the final statement again becomes 
  === return not is_even(22)
  * 22 is even ... so
  === return not True
  * hence it will return False 


hadd hi ho gai  
'''