from pe.misc import divisors

SOLUTION = "26241"


def solve() -> str:
    odd_num = 1
    diagonal_count = 1
    prime_count = 0

    while True:
        odd_num += 2
        diagonal_count += 4

        reference_corner = odd_num**2
        possible_prime_diagonals = [
            reference_corner - (odd_num - 1),
            reference_corner - (2 * (odd_num - 1)),
            reference_corner - (3 * (odd_num - 1)),
        ]

        prime_diagonals = list(
            filter(lambda x: len(divisors(x)) == 2, possible_prime_diagonals)
        )
        prime_count += len(prime_diagonals)

        prime_ratio = prime_count / diagonal_count
        if prime_ratio < 0.1:
            break

    return str(odd_num)
