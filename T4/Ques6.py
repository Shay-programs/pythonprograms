'''Define a function that can receive two integral numbers in string form 
and compute their sum and print it in the console.
'''

def sum_numstring(n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    print (n1+n2)

n1 = '123'
n2 = '456'
sum_numstring(n1,n2)