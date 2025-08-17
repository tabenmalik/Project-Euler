import itertools
import os

import pe_problems
from importlib.resources import files

SOLUTION: str = "129448"


def read_number_file() -> list[int]:
    this_dir, _ = os.path.split(__file__)

    nums = []
    line = files(pe_problems).joinpath("p059.txt").read_text()
    nums = list(map(int, line.split(",")))

    return nums


def decrypt(text: list[int], password: tuple[int, int, int]) -> str:
    chunks = [text[i : i + len(password)] for i in range(0, len(text), len(password))]
    decrypted_chunks = []
    for chunk in chunks:
        decrypted_chunks.append(list(map(lambda x, y: x ^ y, chunk, password)))

    flattened_decrypt = [num for chunk in decrypted_chunks for num in chunk]
    decrypted_ascii = list(map(chr, flattened_decrypt))
    return "".join(decrypted_ascii)


def solve() -> str:
    nums = read_number_file()

    lower_case_ascii = [ord("a") + i for i in range(26)]
    passwords = list(itertools.permutations(lower_case_ascii, r=3))

    message = ""
    for password in passwords:
        message = decrypt(nums, password)
        if " the " in message:
            break
    return str(sum(map(ord, message)))
