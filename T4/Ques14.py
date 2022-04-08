'''Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.
'''
def chk3(num):
    chklist = []
    for n1 in num:
        if (n1 % 3) != 0:
            chk7(n1)
        
        def chk7(n2):
            if (n2 % 7) == 0:
                chklist.append(n2)
    print(chklist)

l1 = [3,7,21,24,32,70,28]
chk3(l1)