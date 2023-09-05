from pe.misc import sieve_of_eratosthenes_fast




def solve():
    primes = sieve_of_eratosthenes_fast(1_000_000)
    primes_set = set(primes)

    prime_sums = []
    for window_size in range(2, len(primes)):
        for start in range(0, len(primes) - window_size):
            num = sum(primes[start:start+window_size])
            
            if num > primes[-1]:
                break

            if num in primes_set:
                prime_sums.append((num, window_size))

    longest_sum = max(prime_sums, key=lambda x: x[1])
    return str(longest_sum[0])