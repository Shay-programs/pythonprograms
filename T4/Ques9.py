'''Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
'''

def showNumbers(limit):
    for num in range(0,limit+1):
        if (num % 2) == 0:
            print (num, 'EVEN')
        else:
            print (num, 'ODD')

showNumbers(20)