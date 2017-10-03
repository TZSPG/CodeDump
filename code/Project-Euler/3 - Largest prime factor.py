def get_factors(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return sorted(factors)


def largest_prime(lst):
    for factor in lst[::-1]:
        if not get_factors(factor):
            return factor


print(largest_prime(get_factors(600851475143)))
