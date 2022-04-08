'''Write a function to compute 5/0 and use 
try/except to catch the exceptions
'''
def div(n1,n2):
    try:
        print(n1/n2)
    except ZeroDivisionError:
        print ('Division by Zero Error')

div(5,0)