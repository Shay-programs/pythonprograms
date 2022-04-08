'''Flatten the list [1,2,3,4,5,6,7] into 1234567 
using reduce().
'''
from functools import reduce
list1 =  [1,2,3,4,5,6,7]
## reduce(function, sequence) -> value
flatlist = reduce(lambda a,b: 10*a+b, list1)
print(flatlist)