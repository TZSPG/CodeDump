from random import randint

MAXIMUM = int(input('Enter a maximum number: '))
ANSWER = randint(1, MAXIMUM)


def guessing_game(guess, correct=ANSWER):
    try:
        guess = int(guess)
    except ValueError:
        guessing_game(input("That's not a number!: "), correct)
    else:
        if guess > correct:
            guessing_game(input('Go lower: '), correct)
        elif guess < correct:
            guessing_game(input('Go higher: '), correct)
        else:
            print('Correct!')


if __name__ == '__main__':
    first_guess = input('\nEnter a number between 1 and {}: '.format(MAXIMUM))
    guessing_game(first_guess)
