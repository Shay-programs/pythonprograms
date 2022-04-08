'''Take user input for Addition, Subtraction, division, multiplication and average
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”'''

def cal_task(choice=0,n1=0,n2=0,n3=0,n4=0):

    if choice == 0: 
        print('No option was selected') 

    #Addition
    if choice == 1:
        return (n1+n2)
    #Subtraction    
    elif choice ==2:
        return (n1-n2)
    #Division    
    elif choice == 3:
        if n2 != 0: return(n1/n2)
    #Multiplication        
    elif choice == 4:
        return(n1*n2)
    #Average
    elif choice == 5:
        return ((n1+n2+n3+n4)/4)
    else:
        print ('Something went wrong, Try again!')
        

user_choice = int(input('Choose the task number to perform: \n 1.Addition \n 2.Subtraction \n 3.Division \
                    \n 4.Multiplication \n 5.Average \t'))

num1, num2 = input('Please enter 2 numbers: ').split(',',2)
num1 = int(num1)
num2 = int(num2)
num3 = 0
num4 = 0

if user_choice == 5:
    num3, num4 = input('Please enter 2 numbers: ').split(',',2)
    num3 = int(num3)
    num4 = int(num4)

value = cal_task(user_choice, num1,num2,num3,num4)
if value == abs(value):
    print(value)
else:
    print('Negative')




