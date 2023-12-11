# This was 2 in qu 1. It is the only change

GAP_HEIGHT: int = 1000000

with open('input.txt', 'r') as lines:
    stars = [(col_num, row_num)
             for row_num, line in enumerate(lines)
             for col_num, symbol in enumerate(line)
             if symbol == '#'
             ]

used_rows = {y for (_, y) in stars}
used_columns = {x for (x, _) in stars}


def taxi_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def get_pos(x, y):
    return (
        x + (x - len([j for j in used_columns if j < x])) * (GAP_HEIGHT - 1),
        y + (y - len([i for i in used_rows if i < y])) * (GAP_HEIGHT - 1)
    )


distance_sum = sum(
    taxi_dist(*get_pos(*s), *get_pos(*t))
    for s in stars
    for t in stars
    if s < t
)

print(distance_sum)
