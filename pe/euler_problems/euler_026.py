

MAX_NUM = 1000

def long_division(numerator, denominator):
    whole = int(numerator // denominator)
    
    decimals = []
    remainders = set()
    dividend = numerator % denominator * 10
    while True:
        if dividend == 0:
            break

        qoutient = int(dividend // denominator)
        remainder = dividend % denominator

        if (qoutient, remainder) in remainders:
            break

        remainders.add((qoutient, remainder))
        decimals.append(qoutient)
        dividend = remainder * 10

    repeating_decimals = []
    if dividend != 0:
        remainders = set()
        while True:
            if dividend == 0:
                break

            qoutient = int(dividend // denominator)
            remainder = dividend % denominator

            if (qoutient, remainder) in remainders:
                break

            remainders.add((qoutient, remainder))
            repeating_decimals.append(qoutient)
            dividend = remainder * 10

    if len(repeating_decimals) > 0:
        decimals = decimals[:-len(repeating_decimals)]

    return whole, decimals, repeating_decimals
    
def solve():
    lengths = {i: len(long_division(1, i)[2]) for i in range(2, MAX_NUM)}
    max_length = max(lengths, key=lambda k: lengths[k])
    return str(max_length)
