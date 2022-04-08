'''Write a program in Python to multiply the elements of a list by 
itself using a traditional function
and pass the function to map() to complete the operation.
'''

def prod_num(n):
    return n*n
  
inputlst = [2,3,4,5,6]
result = list(map(prod_num, inputlst))
print (result)