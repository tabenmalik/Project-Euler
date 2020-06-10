
def solution_01():
    total = 0
    for i in range(0, 10):
        if i % 5 == 0 or i % 3 == 0:
            total += i

    return total
