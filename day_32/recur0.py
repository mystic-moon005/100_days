'''
topic: python recursion

- example: finding the factorial of a number
-- this will be a recursive function
'''


# defining the factorial func
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print(factorial(num))


'''
working:

factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call
'''