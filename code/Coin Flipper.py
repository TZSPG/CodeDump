from random import randint


exit_loop = int(input('How many coins do you want in a row: '))
flips = 0
coins = []


while len(coins) < exit_loop:
    new_coin = randint(0,1)
    print('flip {}: {}'.format(flips, new_coin))
    flips += 1          # Kept outside following if statement to follow DRY principle
    if new_coin in coins or len(coins) == 0:
        coins.append(new_coin)
    else:
        coins = []

def coin_state():
    """Because globals suck"""
    possible_state = ['heads', 'tails']
    return possible_state[coins[0] - 1]


message = '\n{} {} were flipped in a row. \nNumber of flips taken: {}'
print(message.format(len(coins), coin_state(), flips - 1))
