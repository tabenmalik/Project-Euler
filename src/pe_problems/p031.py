SOLUTION: str = "73682"
MAX_NUM: int = 200

COINS: list[int] = [1, 2, 5, 10, 20, 50, 100, 200]


def solve() -> str:
    ways = [0 for _ in range(MAX_NUM + 1)]
    ways[0] = 1
    for coin in COINS:
        for j in range(coin, MAX_NUM + 1):
            ways[j] = ways[j] + ways[j - coin]
    return str(ways[MAX_NUM])
