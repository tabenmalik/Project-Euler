SOLUTION = 73682

MAX_NUM = 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
COIN_SUM_CACHE = {}
def coin_sums(total):
    if total == 1:
        return frozenset([(1,)])

    if total in COIN_SUM_CACHE:
        return COIN_SUM_CACHE[total]

    ways_to_sum = list()
    for coin in COINS:
        new_total = total - coin

        if new_total == 0:
            ways_to_sum.append(tuple([coin]))
        elif new_total > 0:
            ways_to_subsum = coin_sums(new_total)
            for way in ways_to_subsum:
                ways_to_sum.append((coin,) + way)

    ways_to_sum = map(tuple, map(sorted, ways_to_sum))
    ways_to_sum = frozenset(ways_to_sum)

    COIN_SUM_CACHE[total] = ways_to_sum
    return ways_to_sum

def solution_01():
    return len(coin_sums(MAX_NUM))
