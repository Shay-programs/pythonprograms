'''Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12'''

s = "abcSdefPghijQkl"
up = 0
low = 0

for i in s:
    if i.isupper():
        up += 1
    if i.islower():
        low += 1

print(f'No. of Uppercase characters : {up} No. of Lower case Characters : {low}')