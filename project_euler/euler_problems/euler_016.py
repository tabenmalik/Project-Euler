def solution_01():
    num = 2 ** 1000
    num_str = str(num)
    digits = list(map(int, num_str))
    return sum(digits)