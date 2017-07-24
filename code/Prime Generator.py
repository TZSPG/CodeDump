def get_primes():
    from itertools import count
    primes = []
    for i in count(2):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            yield i
            primes.append(i)

if __name__ == '__main__':
    for found_prime in get_primes():
        print(found_prime)
