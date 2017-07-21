def find_factors(num):
    """Returns sorted list of the factors of an input"""
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print('{} and {} are factors of {}'.format(i, num // i, num))
            factors.extend([i, num // i])
    print('\n' + 'All factors found.')
    return sorted(factors)

print(find_factors(60))
