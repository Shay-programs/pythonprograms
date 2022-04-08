'''Program on average of 3 nos'''
a = 10
b = 20
c = 30
avg = (a+b+c)/3
print('Avg =', avg)

if ((avg > a) and (avg > b) and (avg > c)):
    print ('Avg is higher than a,b,c.')
elif ((avg > a) and (avg > b)):
    print('Avg is higher than a,b')
elif ((avg > a) and (avg > c)):
    print('Avg is higher than a,c')
elif ((avg > b) and (avg > c)):
    print('Avg is higher than b,c')  
elif (avg > a):
    print('Avg is just higher than a')
elif (avg > b):
    print('Avg is just higher than b')
elif (avg > c):
    print('Avg is just higher than c')
else:
    pass
