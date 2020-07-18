import os

from project_euler.integer import sum_of_n

SOLUTION = '162'

def triangle_num_seq(under=None):
    n = 1
    while True:
        yield sum_of_n(n)
        n += 1
        if under is not None and n >= under:
            break


def read_file():
    this_dir, _ = os.path.split(__file__)
    
    words = []
    with open(os.path.join(this_dir, 'euler_042.txt')) as fhdl:
        line = fhdl.read()
        line = line.rstrip()
        line = line.replace('"', '')
        words = line.split(',')

    return words


def letter_value(letter):
    return ord(letter.lower()) - ord('a') + 1


def word_value(word):
    return sum(map(letter_value, word))


def solve():
    words = read_file()
    
    word_values = list(map(word_value, words))
    max_word_value = max(word_values)
    
    triangle_number_set = set(triangle_num_seq(under=max_word_value+1))

    triangle_word_values = list(filter(lambda x: x in triangle_number_set, word_values))

    return str(len(triangle_word_values))