'''Write a program to check the data type of the entered values.'''

def checktype(*args):
    for i in args:
        print( f'{i} is of type  {type(i)}')

checktype(1,3,4.5,"test", {'a':0,'b':1},(1,2,3,4,5),[2,4])

