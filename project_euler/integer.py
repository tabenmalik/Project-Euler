import math

def is_palindrome(num):
    num_str = str(num)
    reverse_str = num_str[::-1]
    return num_str == reverse_str


def trigonal(n):
    return sum_of_n(n)


def is_trigonal(t):
    n1 = -0.5 + math.sqrt(0.25 + (2 * t))
    n2 = -0.5 - math.sqrt(0.25 + (2 * t))

    result = n1 > 0 and trigonal(int(n1)) == t
    result |= n2 > 0 and trigonal(int(n2)) == t

    return result


def pentagonal(n):
    return (n * ((3 * n) - 1)) // 2


def is_pentagonal(p):
    if p <= 0:
        return False

    n1 = (0.5 + math.sqrt(0.25 + (6*p))) / 3
    n2 = (0.5 - math.sqrt(0.25 + (6*p))) / 3
    
    result = n1 > 0 and pentagonal(int(n1)) == p
    result |= n2 > 0 and pentagonal(int(n2)) == p

    return result


def hexagonal(n):
    return n * ((2*n) - 1)


def is_hexagonal(h):
    if h <= 0:
        return False

    n1 = 0.25 * (1 + math.sqrt(1 + (8*h)))
    n2 = 0.25 * (1 - math.sqrt(1 + (8*h)))

    result = n1 > 0 and hexagonal(int(n1)) == h
    result |= n2 > 0 and hexagonal(int(n2)) == h

    return result 


def sum_of_n(n):
    return int((n * (n + 1)) / 2)


def sum_of_sqrs(n):
    return int((((2 * n) + 1) * (n + 1) * n) / 6)


def sum_of_cubes(n):
    return int(((n * n) * (n + 1) * (n + 1)) / 4)
