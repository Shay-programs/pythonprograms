''' Create a list of 10 elements of four different data types like int, string, complex and float.'''

numlist = [1,2,3,4,5,6,7,8,9,10]
strlist = ['a','b','c','d','e','f','g','h','i','j']
complist = [(1+2j) , (2+3j), (3+4j),(4+2j) , (5+3j), (6+4j),(7+2j) , (8+3j), (9+4j), (10+10j) ]
floatlist = [1.2,2.3,3.4,4.5,5.6,6.7,7.8,8.9,9.1,10.0]

print(numlist)
print(strlist)
print(complist)
print(floatlist)

#Print real and imaginary part of the first element if the complex number list
print(complist[0].real)
print(complist[0].imag)
