SOLUTION = '73682'

MAX_NUM = 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
COIN_SUM_CACHE = {}
def coin_sums(total, coins):
    if total == 1:
        return frozenset([(1,)])

    if total in COIN_SUM_CACHE:
        return COIN_SUM_CACHE[total]

    ways_to_sum = list()
    for coin in coins:
        new_total = total - coin

        if new_total == 0:
            ways_to_sum.append(tuple([coin]))
        elif new_total > 0:
            new_coins = coins.copy()
            if new_total < coin:
                new_coins.remove(coin)

            ways_to_subsum = coin_sums(new_total, new_coins)
            for way in ways_to_subsum:
                ways_to_sum.append((coin,) + way)

    ways_to_sum = map(tuple, map(sorted, ways_to_sum))
    ways_to_sum = frozenset(ways_to_sum)

    COIN_SUM_CACHE[total] = ways_to_sum
    return ways_to_sum

def solution_01():
    return len(coin_sums(MAX_NUM, COINS))


COIN_WAYS_CAHCE = {}
def ways(target, avc):
    if avc <= 1:
        return 1

    if (target, avc) in COIN_WAYS_CAHCE:
        return COIN_WAYS_CAHCE[(target, avc)]
    
    res = 0
    while target >= 0:
        res = res + ways(target, avc - 1)
        target = target - COINS[avc-1]

    COIN_WAYS_CAHCE[(target, avc)] = res
    return res


def solution_02():
    print(ways(MAX_NUM, len(COINS)))


def solution_03():
    ways = [0 for _ in range(MAX_NUM+1)]
    ways[0] = 1
    for coin in COINS:
        for j in range(coin, MAX_NUM+1):
            ways[j] = ways[j] + ways[j-coin]
    return ways[MAX_NUM]


def solve():
    return str(solution_03())
