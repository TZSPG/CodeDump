primes = [2,3,5]

test_num = 7
while test_num < 2000000:
    for i in range(2, int(test_num**0.5)+1):
        if test_num % i == 0:
            break
    else:
        print(test_num)
        primes.append(test_num)

    test_num += 2

print(sum(primes))