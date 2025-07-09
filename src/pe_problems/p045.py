from pe.sequences import Hexagonals, Pentagonals, Triangulars

SOLUTION = "1533776805"


def solve():
    n = 144
    hexagonals = Hexagonals()
    pentagonals = Pentagonals()
    triangulars = Triangulars()

    while True:
        h = hexagonals[n]
        if hexagonals[n] in pentagonals and h in triangulars:
            return str(h)
        n += 1
