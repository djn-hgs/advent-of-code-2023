import math

stars = []
used_rows = {}
used_columns = {}

# This was 2 in qu 1

gap_height = 2

height = 0
width = 0

with open('input.txt', 'r') as lines:
    for i, line in enumerate(lines):
        height += 1
        width = max(width, len(line))

        for j, symbol in enumerate(line):
            if symbol == '#':
                used_rows[i] = True
                used_columns[j] = True
                stars.append((j, i))


def galaxy_dist(x, y):

    x = abs(x)
    y = abs(y)

    min_diff = min(x, y)
    max_diff = max(x, y)

    if min_diff == 0:
        return max_diff - 1
    elif min_diff == 1:
        return max_diff
    else:

        step_length = math.floor(max_diff / (min_diff - 1))

        achieved = (min_diff - 1) * step_length

        additional = max_diff - achieved

        return (step_length + 1) * (min_diff - 1) + additional


distance_sum = 0

unused_rows = [i for i in range(height) if i not in used_rows]
unused_columns = [j for j in range(width) if j not in used_columns]

for i in range(len(stars) - 1):
    for j in range(i + 1, len(stars)):
        x1, y1 = stars[i]
        x2, y2 = stars[j]

        x1 = x1 + len([j for j in unused_columns if j < x1]) * (gap_height - 1)
        x2 = x2 + len([j for j in unused_columns if j < x2]) * (gap_height - 1)
        y1 = y1 + len([i for i in unused_rows if i < y1]) * (gap_height - 1)
        y2 = y2 + len([i for i in unused_rows if i < y2]) * (gap_height - 1)

        dist = galaxy_dist(x2 - x1, y2 - y1) + 1

        distance_sum += dist

print(distance_sum)
