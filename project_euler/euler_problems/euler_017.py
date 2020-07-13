SOLUTION = '21124'

MAX_NUM = 1000

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
        8: 'eight', 9: 'nine'}
teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}

def num_to_english(n):
    num_eng = ''

    tens_digits = n % 100
    if 0 < tens_digits < 10:    
        num_eng = ones[tens_digits]
    elif 10 < tens_digits < 20:
        num_eng = teens[tens_digits]
    elif tens_digits != 0:
        ones_digit = tens_digits % 10
        tens_digit = tens_digits // 10
        if ones_digit != 0:
            num_eng = ones[ones_digit]

        num_eng = tens[tens_digit] + ' ' + num_eng

    n = n // 100
    hundreds_digit = n % 10
    if hundreds_digit != 0:
        tmp_str = ones[hundreds_digit] + ' hundred'
        if num_eng != '':
            num_eng = tmp_str + ' and ' + num_eng
        else:
            num_eng = tmp_str

    n = n // 10
    thousands_digit = n % 10
    if thousands_digit != 0:
        num_eng = ones[thousands_digit] + ' thousand'
    
    return num_eng

def solution_01():
    eng_strs = map(num_to_english, range(1, MAX_NUM+1))
    removed_spaces = (eng_str.replace(' ', '') for eng_str in eng_strs)
    str_counts = map(len, removed_spaces)
    return sum(str_counts)


def solve():
    return str(solution_01())