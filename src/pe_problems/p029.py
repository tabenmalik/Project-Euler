SOLUTION: str = "9183"
MAX_NUM: int = 100


def solve() -> str:
    powers = {a**b for a in range(2, MAX_NUM + 1) for b in range(2, MAX_NUM + 1)}
    return str(len(powers))
