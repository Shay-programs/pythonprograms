'''Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).
'''

def sq_tup(num):
    t = [n**2 for n in range(1,num+1)]
    t = tuple(t)
    print(t)

sq_tup(20)
