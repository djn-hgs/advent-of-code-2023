from functools import cache

directions = {
    0: 'N',
    1: 'W',
    2: 'S',
    3: 'E'
}

lines = []
width = 0
height = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        height += 1
        width = max(width, len(line))
        lines.append(line.strip())

print(f'Width {width}, height {height}')


@cache
def transpose(lines):
    return tuple(''.join(x) for x in zip(*lines))


@cache
def tilt(section):
    zeroes = section.count('O')
    return zeroes * 'O' + (len(section) - zeroes) * '.'


@cache
def roll(rows):
    return tuple('#'.join(tilt(section) for section in row.split('#')) for row in rows)


@cache
def rotate(rows):
    return tuple(''.join(reversed(x)) for x in zip(*rows))


n = 1000000

for i in range(4 * n):
    # print(f'Tilting direction : {directions[i % 4]}')

    # print('Before')
    # for row in lines:
    #     print(row)

    lines = roll(lines)

    # print(f'After rotation {i}, so cycle {i // 4}')

    # for row in lines:
    #     print(row)
    #
    # print()

    lines = rotate(lines)

# print('State of play')
# for row in lines:
#     print(row)


score = 0

for row in lines:
    row_len = len(row)
    searching = True
    cursor = 0
    while searching:
        next_hash = row.find('#', cursor)

        if next_hash == -1:
            seek_point = row_len
        else:
            seek_point = next_hash

        if seek_point > cursor:
            zeroes = row.count('O', cursor, seek_point)
            score += (row_len - cursor - zeroes + 1 + row_len - cursor) * zeroes / 2

        cursor = seek_point + 1

        if cursor > len(row) or next_hash == -1:
            searching = False

print(f'Rotation {i} total score {score}')
