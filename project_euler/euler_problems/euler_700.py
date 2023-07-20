import itertools

def eulercoins():
    a = 1504170715041707
    b = 4503599627370517
    
    yield a
    prev_eulercoin = a

    for n in itertools.count(2):
        seq = ((a % b) * (n % b)) % b
        if seq == a:
            break
        elif seq < prev_eulercoin:
            print(seq)
            yield seq
            prev_eulercoin = seq


def solve():
    print(list(eulercoins()))
    return 0