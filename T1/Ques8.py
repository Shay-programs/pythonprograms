"""If one data type value is assigned to a variable and then a 
different data type value is assigned to a
again. Will it change the value? If Yes then Why?
"""
a = "Welcome"
print(type(a))

a = 123
print(type(a))

''' Answer - Yes, it will change the value as well as data type for
the same variable as re-assigning a variable is allowed in Python and the 
most recent assigment(or last defination) is its current value and datatype.'''