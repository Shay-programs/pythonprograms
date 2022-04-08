'''Write a program that accepts a string as an input from the user and calculate the number of digits
and letters. 
'''

user_input = input('Enter your input: ')
numlist = []
charlist = []

for n in user_input:
    #append number list if character is a digit
    if n.isdigit(): numlist.append(n)
    #append alphabet list is character is an alphabet
    if n.isalpha(): charlist.append(n)

print (f'Letters: {len(charlist)} \t Digits: {len(numlist)}')
#print (charlist)
#print (numlist)


