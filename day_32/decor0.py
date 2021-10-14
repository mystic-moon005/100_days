'''
topic: decorators

Question---
add a decorator, which adds 3 hashtags before and after the bill data
so that the start and end of a printed bill can be identified

-- since i dont have the code for the bill data, i'll use sample text 
-- replacing the function later with the following text:
# bill data goes here
'''


'''
pseudo code
1. original function
2. enclosed function that takes the original function as an arg
   - enclosed func must return the inner func. in the last line .. 
3. decorator func. 
   -prints 3 hashtags
   -calls the original func
   -prints 3 hashtags
4. remember to mention the enclosing func. above the original func. using @ symbol
5. write statements to call the enclosing func.
'''


# defining enclosing func
def identify(func):
    def hashtag():
        print("###")
        func()  # calling original func
        print("###")
    
    return hashtag
    

# defining the original func.
# mentioning enclosing func.
@identify
def bill():
    print("pretend this is the bill and im tired lol :/")


'''
python shell command:
bill()

- no comments---    -_-
'''
