import math


def prime_factorization(n):
    primes = sieve_of_eratosthenes_fast(n)
    prime_divisors = list(filter(lambda x: n % x == 0, primes))

    exps = []
    for prime in prime_divisors:
        exp = 0
        while n % prime == 0:
            exp += 1
            n /= prime
        exps.append(exp)

    return prime_divisors, exps


# def prime_factors(num):
#     return prime_factors_trial_division(num)


def divisors(n, sort=False):
    divisors = [1, n]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.extend([i, int(n / i)])

    if sort:
        divisors = sorted(divisors)

    return tuple(divisors)


PRIME_CACHE = set()
MAX_PRIME = 2

def is_prime(num):
    """
    Returns True if the given number
    """
    global PRIME_CACHE
    global MAX_PRIME

    if num in PRIME_CACHE:
        return True
    elif len(PRIME_CACHE) > 0 and num < MAX_PRIME:
        return False
    elif num <= 1:
        return False

    PRIME_CACHE = set(sieve_of_eratosthenes_fast(3*num))
    MAX_PRIME = max(PRIME_CACHE)
    return num in PRIME_CACHE


def sieve_of_eratosthenes_fast(under):
    sieve_len = int((under - 1) // 2) + 1
    sieve = [False for i in range(0, sieve_len)]

    check_limit = (math.floor(math.sqrt(under)) - 1) // 2
    check_limit = int(check_limit) + 1

    for i in range(1, check_limit):
        if not sieve[i]:
            for j in range(2*i*(i+1), sieve_len, (2*i)+1):
                sieve[j] = True

    primes = [2]
    primes.extend([(2*i) + 1 for i in range(1, sieve_len) if not sieve[i]])

    return primes

def sieve_of_eratosthenes_naive(under):
    bools = [False for i in range(0, under)]
    bools[0] = True
    bools[1] = True

    for i in range(4, under, 2):
        bools[i] = True

    for i in range(3, math.floor(math.sqrt(under))):
        if not bools[i]:
            for j in range(i*i, under, 2*i):
                bools[j] = True

    primes = [i for i, status in enumerate(bools) if not status]

    return primes


def num_to_digits(num):
    return list(map(int, str(num)))


def digits_to_num(digits):
    return int(''.join(str(i) for i in digits))
