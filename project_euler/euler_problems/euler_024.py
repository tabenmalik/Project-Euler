SOLUTION = '2783915460'

def permutations(digits):
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

def solution_01():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i, p in enumerate(permutations(digits), start=1):
        if i == 1_000_000:
            break

    return ''.join(str(i) for i in p)


def solve():
    return str(solution_01())