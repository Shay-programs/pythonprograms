'''Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.'''

def chk_len(s1,s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    elif len(s1) == len(s2):
        print(s1,'\n',s2)
    else:
        pass

s1 = "It's a beautiful world."
s2 = "The sun rises in the east."

chk_len(s1,s2)