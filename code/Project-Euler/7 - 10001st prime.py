primes = [2,3]


test_num = 5

while len(primes) < 10001:
    for i in primes:
        if test_num % i == 0:
            break
    else:
        primes.append(test_num)

    test_num += 2


print(primes[-1])