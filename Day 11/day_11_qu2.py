import math

stars: [tuple[int, int]] = []
used_rows: {int} = {}
used_columns: {int} = {}

# This was 2 in qu 1. It is the only change

GAP_HEIGHT: int = 1000000

height: int = 0
width: int = 0

with open('input.txt', 'r') as lines:
    for row_num, line in enumerate(lines):
        height += 1
        width = max(width, len(line))

        for col_num, symbol in enumerate(line):
            if symbol == '#':
                used_rows[row_num] = True
                used_columns[col_num] = True
                stars.append((col_num, row_num))


def raster_dist(x1: int, y1: int, x2: int, y2: int):
    min_diff = min(abs(x2 - x1), abs(y2 - y1))
    max_diff = max(abs(x2 - x1), abs(y2 - y1))

    if min_diff == 0:
        return max_diff

    elif min_diff == 1:
        return max_diff + 1

    else:
        step_length: int = math.floor(max_diff / (min_diff - 1))

        additional: int = max_diff - (min_diff - 1) * step_length

        return (step_length + 1) * (min_diff - 1) + additional + 1


def get_pos(x, y):
    return (
        x + (x - len([j for j in used_columns if j < x])) * (GAP_HEIGHT - 1),
        y + (y - len([i for i in used_rows if i < y])) * (GAP_HEIGHT - 1)
    )


distance_sum = sum(
    raster_dist(*get_pos(*s), *get_pos(*t))
    for s in stars
    for t in stars
    if s < t
)

print(distance_sum)
