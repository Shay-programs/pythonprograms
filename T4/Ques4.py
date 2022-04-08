'''Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.
'''

s = "all-hello-song-happy-joy-world-zeal-pure-care"
l1 = s.split('-')

#sort alphabetically
l1 = sorted(l1)
print('-'.join(l1))