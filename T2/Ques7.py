'''Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
Expected output: 0 1 2 4 5
Note: Use continue statement'''

n = 0
while n <=6 :
    if (n == 3) or (n == 6):
        n += 1
        continue
    else:
        print (n)
    n += 1

