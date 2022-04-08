'''Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given list
Use map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.
'''
list1 = [n for n in range(0,21)]
list1 = list(filter(lambda x : x % 2 == 0, list1))
llist1 = list(map(lambda x : x**2, list1))
print(list1)