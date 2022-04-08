'''Create a new list which contains the specified numbers after removing the even numbers from a
predefined list. '''

given_list = [2,4,3,1,5,6,7,8,9,11,12,15,20,99]

#take out all even nos from the list
new_list = []
for num in given_list:
    if (num % 2) == 0:
        pass
    else:
        new_list.append(num)

print (new_list)
