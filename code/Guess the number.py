from random import randint


def guessing_game(guess, highest):
    try:
        guess = int(guess)
    except ValueError:
        guessing_game(input("That's not a number!: "), highest)
    else:
        if guess > answer:
            guessing_game(input('Go lower: '), highest)
        elif guess < answer:
            guessing_game(input('Go higher: '), highest)
        else:
            print('Correct!')


if __name__ == '__main__':
    maximum = int(input('Enter a maximum number: '))
    answer = randint(1, maximum)
    first_guess = input('\nEnter a number between 1 and {}: '.format(maximum))
    guessing_game(first_guess, maximum)
