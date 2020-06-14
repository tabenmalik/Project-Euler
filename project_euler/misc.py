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


def is_prime(num):
    """
    Returns True if the given number 
    """
    return len(list(trial_division(num))) == 1


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