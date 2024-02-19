def find_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 1
    return primes[n - 1]

print(find_primes(10001))