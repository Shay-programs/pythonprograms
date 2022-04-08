'''Write a program that asks five times to guess the lucky number'''

import random

number = random.randint(0,10)
play_count = 0

while play_count <=5:
    try:
        answer = int(input("Guess the Lucky Number between (0 to 10) in 5 turns: "))
        play_count += 1

        #if the user guesses the number
        if answer == number:
            print ('Good Guess!', answer , 'is correct!')
            break
        elif play_count == 5:
            print ('Game Over, Sorry but that was not very successful.')  
            break 
        else:
            print ('Try Again')
    except:
        print ('Invalid Input, Game Over!')
        break
        
