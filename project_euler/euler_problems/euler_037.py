from project_euler.misc import prime_seq, num_to_digits, digits_to_num, is_prime, sieve_of_eratosthenes_fast

SOLUTION = '748317'

def is_trucatable_prime(prime):
    single_digit_primes = set([2, 3, 5, 7])
    if prime in single_digit_primes:
        return False

    digits = num_to_digits(prime)
    if digits[0] not in single_digit_primes or digits[-1] not in single_digit_primes:
        return False

    for i in range(1, len(digits)):
        num1 = digits_to_num(digits[i:])
        num2 = digits_to_num(digits[:i])
        
        if not is_prime(num1) or not is_prime(num2):
            return False
    
    return True


def solve():
    limit = 11

    truncatable_primes = []
    for prime in sieve_of_eratosthenes_fast(1000000):
        if is_trucatable_prime(prime):
            truncatable_primes.append(prime)
            if len(truncatable_primes) == limit:
                break

    return str(sum(truncatable_primes))
