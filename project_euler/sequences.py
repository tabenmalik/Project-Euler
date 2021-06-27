from project_euler.misc import is_prime, divisors

def permutations_seq(digits):
    yield digits.copy()

    largest_index_k = 0
    while largest_index_k != -1:
        largest_index_k = -1
        for i in range(len(digits) - 1):
            if digits[i] < digits[i+1]:
                largest_index_k = i

        if largest_index_k != -1:
            largest_index_l = 0
            for l in range(largest_index_k+1, len(digits)):
                if digits[largest_index_k] < digits[l]:
                    largest_index_l = l

            digits[largest_index_k], digits[largest_index_l] = digits[largest_index_l], digits[largest_index_k]
            digits[largest_index_k+1:] = reversed(digits[largest_index_k+1:])
            yield digits.copy()


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

        if len(divisors(i)) == 2:
            yield i
        i += 2


def fibonacci_seq(under=None):
    """
    A generator of fibonacci numbers
    """
    fib_1 = 1
    fib_2 = 1

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


def even_fibonacci_seq():
    """
    A generator of even fibonacci numbers
    """
    fib_1 = 2
    fib_2 = 8

    yield fib_1
    yield fib_2

    fib_new = 4*fib_2 + fib_1
    while True:
        yield fib_new

        fib_1 = fib_2
        fib_2 = fib_new

        fib_new = 4*fib_2 + fib_1
