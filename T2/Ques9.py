'''Guess The Number Game'''
import random

play = True
number = random.randint(0,10)

while play:

    try:
        answer = input("Guess the Lucky Number between (0 to 10): \nEnter 'No' to quit. ")

        if answer.lower().strip() == 'no':
            play = False
            print('Nice Try, the answer was ', number)
        else:
            answer = int(answer)

        #if the user guesses the number
        if answer == number:
            print ('You Win!', answer , 'is correct!')
            play = False
        
    except:
        play = False
        print ('Invalid Input, Game Over!')


