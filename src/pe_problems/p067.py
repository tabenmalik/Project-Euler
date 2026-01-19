import os

NUM_FILE: str = "p067.txt"
import pe_problems
from importlib.resources import files

SOLUTION: str = "7273"


def read_number_file() -> list[list[int]]:
    this_dir, _ = os.path.split(__file__)

    num_matrix = []
    lines = files(pe_problems).joinpath("p067.txt").read_text().splitlines()
    for line in lines:
        line = line.rstrip()
        line_nums = list(map(int, line.split(" ")))
        num_matrix.append(line_nums)

    return num_matrix


MAX_PATH_CACHE: dict[tuple[int, int], int] = {}


def max_path(num_triangle: list[list[int]], x: int, y: int) -> int:
    if y == len(num_triangle) - 1:
        return num_triangle[y][x]

    if (x, y) in MAX_PATH_CACHE:
        return MAX_PATH_CACHE[(x, y)]

    max_path_left = max_path(num_triangle, x, y + 1)

    max_path_right = 0
    if x < len(num_triangle[y]):
        max_path_right = max_path(num_triangle, x + 1, y + 1)

    num = num_triangle[y][x]
    max_path_num = max(max_path_left + num, max_path_right + num)
    MAX_PATH_CACHE[(x, y)] = max_path_num
    return max_path_num


def solve() -> str:
    num_triangle = read_number_file()

    return str(max_path(num_triangle, 0, 0))
