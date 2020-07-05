import itertools

from project_euler.misc import num_to_digits, digits_to_num

SOLUTION = 932718654

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


def contains_multiples(num, digits):
    digits = digits.copy()
    multiplier = 1

    while len(digits) > 0:
        multiple = num * multiplier
        multiple_digits = num_to_digits(multiple)

        sub_digits = digits[:len(multiple_digits)]
        if multiple_digits != sub_digits:
            return False

        digits = digits[len(multiple_digits):]
        multiplier += 1   
    
    return True

def solution_01():
    pandigitals = reversed(list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    
    for pandigital in pandigitals:
        for i in range(1, 5):
            if contains_multiples(digits_to_num(pandigital[:i]), pandigital):
                return digits_to_num(pandigital)

