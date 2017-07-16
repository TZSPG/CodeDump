from random import randint


def coin_flip(length):
    flips = 0
    coins = [randint(0, 1)]
    while len(coins) < length:
        new_coin = randint(0, 1)
        flips += 1
        print('flip {}: {}'.format(flips, new_coin))
        if new_coin in coins or len(coins) == 0:
            coins.append(new_coin)
        else:
            coins = [new_coin]
    return coins[0], flips


def coin_state(coin_index):
    """Because globals suck"""
    possible_state = ['heads', 'tails']
    return possible_state[coin_index]


if __name__ == '__main__':
    user_max = int(input('How many coins do you want in a row: '))
    coin, flips_taken = coin_flip(user_max)
    message = '\n{} {} were flipped in a row. \nNumber of flips taken: {}'
    print(message.format(user_max, coin_state(coin), flips_taken))
