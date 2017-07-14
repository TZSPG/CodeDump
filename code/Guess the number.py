#Guess the number

import random
num = random.randint(0,10)

def Guessing(x):
        try:
                if int(x) > num:
                        Guessing(int(input('Go lower: ')))
                elif int(x) < num:
                         Guessing(int(input('Go higher: ')))
                else:
                        print('Correct!')
                
        except ValueError:
                Guessing(int(input('That\'s not a number!: ')))

guess = input('Enter a number between 1 and 10: ')
Guessing(guess)
