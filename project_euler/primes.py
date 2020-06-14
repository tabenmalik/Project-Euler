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
    i = 2
    while True:
        if under is not None and i >= under:
            break
        
        if is_prime(i):
            yield i
        i += 1