MAX_NUM = 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def solve():
    ways = [0 for _ in range(MAX_NUM + 1)]
    ways[0] = 1
    for coin in COINS:
        for j in range(coin, MAX_NUM + 1):
            ways[j] = ways[j] + ways[j - coin]
    return str(ways[MAX_NUM])
