'''Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.'''

num1 = int(input("Please enter a number between 1 - 10 "))
num2 = int(input("Please enter another number between 1-10 "))

if (num1 and num2) in range(1,11):
    z = num1 + num2
    result = z + 30
    print(result)
else:
    print("Invalid numbers entered")