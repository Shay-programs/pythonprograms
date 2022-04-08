'''Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]'''

list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]

#pop out the last element
list1.pop()

# use extend to add each element of second list to first list
list1.extend(list2)

print(list1)