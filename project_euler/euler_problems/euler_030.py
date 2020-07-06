import matplotlib.pyplot as plt

SOLUTION = 443839

def solution_01():
    power = 5

    i = 2
    while True:
        digit_limit = i*(9**power)
        digit_str = [str(9) for _ in range(i)]
        num = int(''.join(digit_str))
        if digit_limit < num:
            break
        i += 1

    limit = digit_limit

    x_s = list(range(10, limit))

    # Compute the digit sums
    x_strs = (str(i) for i in x_s)
    x_digits = map(lambda x: list(map(int, x)), x_strs)
    digit_powers = map(lambda x: [d**power for d in x], x_digits)
    digit_sums = map(sum, digit_powers)
    y_s = list(digit_sums)

    # Plot to show the trend of the sequence
    fig, axis = plt.subplots(figsize=(12, 8))
    _ = axis.plot(x_s, y_s)
    _ = axis.plot(x_s, x_s)
    fig.savefig('./figures/euler_030.png')

    x_y_pairs = zip(x_s, y_s)
    results = list(filter(lambda pair: pair[0] == pair[1], x_y_pairs))
    result = sum(next(iter(zip(*results))))
    return result