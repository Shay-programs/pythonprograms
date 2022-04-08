'''Write a program in Python which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200.
'''
numlist = []
for num in range(2000,3201):
    if (num % 7 == 0) and (num % 5 != 0):
        numlist.append(num)

print (numlist)