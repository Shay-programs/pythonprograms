''' Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98'''

nums = input("Enter a series of comma-separated numbers: ")
#print(nums)

l1 = [n for n in nums.split(',') ]
t1 = tuple(l1)

print(l1, t1)


