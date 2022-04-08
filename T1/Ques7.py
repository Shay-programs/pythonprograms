'''. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.'''

def change_format(format_type = "lower", inputstr = 'Sample'):
    if format_type.lower() == 'upper': print (inputstr.upper())
    if format_type.lower() == 'lower': print (inputstr.lower())
    if (format_type.lower() == 'camelcase') or (format_type.lower() == 'uppercamel'):  
        inputstr = inputstr.title()
        inputstr = inputstr.replace(' ','')
        print(''.join(inputstr))
    if format_type.lower() == 'snakecase': 
        inputstr = inputstr.lower()
        inputstr = inputstr.replace(' ','_')
        print(inputstr)
    if format_type.lower() == 'lowercamel':  
        inputstr = inputstr.title()
        inputstr = inputstr.replace(' ','')
        print(''.join([inputstr[0].lower() , inputstr[1:]]))
    

change_format('camelcase','HeLLO there')
