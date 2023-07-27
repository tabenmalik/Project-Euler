from itertools import permutations, chain

from project_euler.integer import concat, split

SOLUTION = ''

def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)

def knapsacks(nums, t):
    num_sets = 5
    solvedsets = set()
    for outers in permutations(nums, 5):
        lessnums = [n for n in nums if n not in outers]
        for inners in permutations(lessnums):
            sets = []
            for i in range(num_sets):
                subset = (outers[i], inners[i], inners[(i+1)%5])
                if sum(subset) != t:
                    break
                sets.append(subset)
            else:
                if tuple(sorted(sets)) not in solvedsets:
                    yield tuple(sets)
                    solvedsets.add(tuple(sorted(sets)))

def solve():
    maxnum = 0
    for total in range(6, 28):
        for solution in knapsacks(list(range(1, 11)), total):
            digits = list(flatten(map(split, flatten(solution))))
            if len(digits) != 16:
                continue
            num = concat(digits)
            maxnum = max(num, maxnum)

    return maxnum
