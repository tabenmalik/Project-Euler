from project_euler.sequences import Pentagonals

SOLUTION = '5482660'


def solve():
    max_num = 10000
    pentagonals = Pentagonals()

    for i in range(1, max_num):
        for j in range(i + 1, max_num):
            pi = pentagonals[i]
            pj = pentagonals[j]
            
            p_sum = pi + pj
            p_diff = pj - pi

            if p_sum in pentagonals and p_diff in pentagonals:
                return str(p_diff)

    
