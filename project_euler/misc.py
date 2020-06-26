import math

def trial_division_naive(num):
    factor = 2

    while num > 1:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 1

def trial_division(num):
    while num % 2 == 0:
        yield 2
        num //= 2
    
    factor = 3
    while factor * factor <= num:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 2

    if num != 1:
        yield num


PRIME_CACHE = set()

def is_prime(num):
    """
    Returns True if the given number 
    """
    global PRIME_CACHE

    if num <= 1:
        return False

    if num in PRIME_CACHE:
        return True

    if len(PRIME_CACHE) > 0 and num < max(PRIME_CACHE):
        return False

    PRIME_CACHE = set(sieve_of_eratosthenes_fast(3*num))
    return num in PRIME_CACHE


def prime_seq(under=None):
    """
    A generator of prime numbers
    """
    if under is None or 2 < under:
        yield 2

    i = 3
    while True:
        if under is not None and i >= under:
            break
        
        if is_prime(i):
            yield i
        i += 2


def fibonacci_seq(under=None):
    """
    A generator of fibonacci numbers
    """
    fib_1 = 1
    fib_2 = 2

    if under is None or fib_1 < under:
        yield fib_1
    
    if under is None or fib_2 < under:
        yield fib_2

    fib_new = fib_2 + fib_1
    while under is None or fib_new < under:
        yield fib_new
        
        fib_1 = fib_2
        fib_2 = fib_new 

        fib_new = fib_2 + fib_1


def even_fibonacci_seq(under=None):
    """
    A generator of even fibonacci numbers
    """
    fib_1 = 2
    fib_2 = 8

    if under is None or fib_1 < under:
        yield fib_1
    
    if under is None or fib_2 < under:
        yield fib_2

    fib_new = 4*fib_2 + fib_1
    while under is None or fib_new < under:
        yield fib_new
        
        fib_1 = fib_2
        fib_2 = fib_new 

        fib_new = 4*fib_2 + fib_1


def sum_of_n(n):
    return int((n * (n + 1)) / 2)


def sum_of_sqrs(n):
    return int((((2 * n) + 1) * (n + 1) * n) / 6)


def sum_of_cubes(n):
    return int(((n * n) * (n + 1) * (n + 1)) / 4)


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


