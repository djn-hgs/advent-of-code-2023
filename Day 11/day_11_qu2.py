import math

stars: [tuple[int, int]] = []
used_rows: {int} = {}
used_columns: {int} = {}

# This was 2 in qu 1. It is the only change

GAP_HEIGHT: int = 1000000

height: int = 0
width: int = 0

with open('input.txt', 'r') as lines:
    for i, line in enumerate(lines):
        height += 1
        width = max(width, len(line))

        for j, symbol in enumerate(line):
            if symbol == '#':
                used_rows[i] = True
                used_columns[j] = True
                stars.append((j, i))


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


distance_sum: int = 0


for i in range(len(stars) - 1):
    for j in range(i + 1, len(stars)):

        distance_sum += raster_dist(*get_pos(*stars[i]), *get_pos(*stars[j]))

print(distance_sum)
