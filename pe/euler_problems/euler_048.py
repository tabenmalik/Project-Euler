from pe.integer import concat, split




def solve():
    powers = map(lambda x: x**x, range(1, 1000))
    power_sum = sum(powers)

    return str(concat(split(power_sum)[-10:]))
