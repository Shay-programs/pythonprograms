'''Sample Codes
What is the output of the following codes:
'''
### 1. -------------------------------------------------------
def foo(): 
    try: 
        return 1 
    finally: 
        return 2
k = foo()
print(k)
## It prints 2 as output

### 2.----------------------------------------------------------
def a(): 
    try: 
        f(x, 4) 
    finally: 
        print('after f') 
        print('after f?')
a()

## gives error as f(x,4) is not defined