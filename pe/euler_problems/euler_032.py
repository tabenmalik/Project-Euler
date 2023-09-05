import itertools
from pprint import pprint

from pe.misc import divisors, sieve_of_eratosthenes_fast




def solve():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # digits = [1, 2, 3, 4]
    all_perms = list(itertools.permutations(digits))
    perms_columns = list(zip(*all_perms))
    
    products = set()
    for i in range(1, 5):
        for j in range(i+1, 6):
            a = zip(*perms_columns[0:i])
            b = zip(*perms_columns[i:j])
            product = zip(*perms_columns[j:])

            a = map(lambda x: list(map(str, x)), a)
            b = map(lambda x: list(map(str, x)), b)
            product = map(lambda x: list(map(str, x)), product)
            
            a = map(lambda x: ''.join(x), a)
            b = map(lambda x: ''.join(x), b)
            product = map(lambda x: ''.join(x), product)
            
            a = map(int, a)
            b = map(int, b)
            product = map(int, product)
            
            actual_products = filter(lambda trip: trip[0] == trip[1] * trip[2], zip(product, a, b))
            actual_products = list(zip(*actual_products))
            if len(actual_products) > 0:
                products.update(actual_products[0])

    return str(sum(products))
