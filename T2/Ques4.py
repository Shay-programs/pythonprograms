'''Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over
If user enters a positive number just continue in the loop and print “Good Going”'''

go = True

while go == True:
    try:
        num = int(input('Please enter a number. '))
        if num < 0:
            print("It's Over!")
            go = False
            break
        elif num >= 0:
            print("Good Going!")
            continue
        else:
            go = False
            pass
    except:
        print ('Invalid Input')
        go = False
