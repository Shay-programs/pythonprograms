'''Write a program in Python to perform the following operation:
1.If a number is divisible by 3 it should print “Divisible by 3” as a string
2.If a number is divisible by 5 it should print “Divisible by 5” as a string
3.If a number is divisible by both 3 and 5 it should print “Divisible by 3 and 5” as a
string.
'''

def divisible_3_5(num):

    if num == 0: return 0

    if ((num % 3) == 0 and (num % 5) == 0):
        print('Divisible by 3 and 5')
    elif (num % 3) == 0:
        print('Divisible by 3')
    elif (num % 5) == 0:
        print('Divisible by 5')
    else:
        print('Not divisible by either 3 or 5')


divisible_3_5(3000)


    


