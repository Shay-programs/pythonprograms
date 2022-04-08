''' Write a program to get the sum and multiply of all the items in a given list.'''
newlist = [2,3,4,5,6,7,2]

# function to sum all the elements of a list
def sum_num(num):
    sum = 0
    for n in num:
        sum += n
    return sum

# function to multiply all the elements of a list
def prod_num(num):
    prod = 1
    for n in num:
        prod *= n
    return prod

sum_result = sum_num(newlist)
prod_result = prod_num(newlist)

print(f'The sum of the elements is {sum_result} \nThe product of the elements is {prod_result}  ')