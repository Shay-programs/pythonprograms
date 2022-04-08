## Swap two numbers using a third variable and do the same task without using any third variable.

num1 = 20
num2 = 50
# swap using third variable
num3 = num1
num1 = num2
num2 = num3
print(f'First number is {num1} and second number is {num2} .')

# swap without a third variable
n1 = 12
n2 = 25
n1,n2 = n2,n1
print(f'First number is {n1} and second number is {n2} .')