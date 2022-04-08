''' Create a list of elements such that it contains the squares of the 
first and last 5 elements between 1 and30 (both included).'''

list1 = []

for num in range(1,31):
    if (num <= 5) or (num >= 25):
        list1.append(num**2)
    else:
        list1.append(num)
print(list1)