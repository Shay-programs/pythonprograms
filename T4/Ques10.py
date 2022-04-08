'''Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)'''

newlist = [n for n in range(0,21)]
result = list(filter(lambda x: x % 2 == 0 , newlist))
print(result)