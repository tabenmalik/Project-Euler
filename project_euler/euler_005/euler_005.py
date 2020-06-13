MAX_NUM = 20

def is_divisible(i, divisor):
    while divisor > 1:
        if i % divisor != 0:
            return False
        divisor -= 1
    return True

def solution_01():
    num = (MAX_NUM - 1) * MAX_NUM
    while not is_divisible(num, MAX_NUM):
        num += (MAX_NUM - 1) * MAX_NUM

    return num
