import math
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    result = []
    for i in range(2, n+1):
        if primes[i]:
            result.append(i)

    return result

n = 30
print(sieve_of_eratosthenes(n)) # prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
