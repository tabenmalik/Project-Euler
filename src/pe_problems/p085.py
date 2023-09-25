def rectangles_in_grid(rows, cols):
    rectangles = 0
    for x in range(1, cols + 1):
        for y in range(1, rows + 1):
            rectangles += (cols - x + 1) * (rows - y + 1)


def solve():
    return ""
