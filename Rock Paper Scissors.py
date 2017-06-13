from random import randint

choices = ['rock', 'scissors', 'paper']  # Notice that in index form, 0 beats 1, 1 beats 2, and 2 beats 0


def rps_game(player_input):
    if player_input in choices:
        choice_index = choices.index(player_input)
        computer_choice = int(randint(0, 2))

        if choice_index + 1 == computer_choice or choice_index - 2 == computer_choice:
            rps_game(input('Player wins!\n \n').lower())

        elif choice_index - 1 == computer_choice or choice_index + 2 == computer_choice:
            rps_game(input('Computer wins!\n \n').lower())

        elif choice_index == computer_choice:
            rps_game(input('Tie!\n \n').lower())
    else:
        rps_game(input('Please choose Rock, Paper or Scissors:  ').lower())


rps_game(input('Rock, paper or scissors?:  ').lower())
