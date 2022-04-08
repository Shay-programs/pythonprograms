'''Create a function that takes a list and 
returns a new list with unique elements of the first list.
'''
l1 = [1,1,2,4,5,3,4,5,6,2,1,5,6,7,7,8,8,9,11]

def unique_list(num):
    newlist = []
    newlist = set(num)
    print(newlist)

unique_list(l1)