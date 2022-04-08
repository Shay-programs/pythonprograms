## Sample Codes

## 1.---------------------------------------------------------------------
# x = 123 
# for i in x: 
#     print(i)

## The above code will give error as int cannot be iterated

## 2.----------------------------------------------------------------------
i = 0
while i < 5: 
    print(i) 
    i += 1 
    if i == 3: 
        break
    else: 
        print ('error')

## 3.-----------------------------------------------------------------------
count = 0 
while True: 
    print(count) 
    count += 1 
    if count >= 5: 
        break
