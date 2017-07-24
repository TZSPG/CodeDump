def find_factors(num):
    """Returns sorted list of the factors of an input. Returns None if number is prime"""
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print('{} and {} are factors of {}'.format(i, num // i, num))
            factors.extend([i, num // i])
    if len(factors) == 0:
        print('\nThis number is prime')
        return None
    else:
        print('\n' + '{} factors found. Sorting list...'.format(len(factors)))
        return sorted(factors)


if __name__ == '__main__':
    user_num = int(input('What number do you want the factors of: '))
    print(find_factors(user_num))
