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
    return len(list(trial_division(num))) == 1


def prime_seq(under=None):
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
    fib_1 = 1
    fib_2 = 2

    yield fib_1
    yield fib_2

    while under is None or fib_2 < under:
        fib_new = fib_2 + fib_1
        
        yield fib_new
        
        fib_1 = fib_2
        fib_2 = fib_new 


def even_fibonacci_seq(under=None):
    fib_1 = 2
    fib_2 = 8

    yield fib_1
    yield fib_2

    while under is None or fib_2 < under:
        fib_new = 4*fib_2 + fib_1
        
        yield fib_new
        
        fib_1 = fib_2
        fib_2 = fib_new 