from itertools import count

primes = {2,3,5,7,11,13,17,19}
tests = {2,3,5,7}


for i in count(2):
    for prime in primes:
        if i % prime != 0:
            break
    else:
        print(i)
        prime_step = i
        break


for i in count(0, prime_step):
    for j in range(2, 21):
        if i % j != 0:
            break
    else:
        print(i)