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

scores = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        height += 1
        width = max(width, len(line))
        lines.append(line.strip())

lines = tuple(lines)

print(f'Width {width}, height {height}')



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


@cache
def score(rows):
    total = 0
    for row in rows:
        for j, c in enumerate(row):
            if c == 'O':
                total += len(row) - j
    return total


def show(rows):
    for row in rows:
        print(row)


lines = rotate(lines)
lines = rotate(lines)
lines = rotate(lines)

cycle_length = 36
line_register = [0 for i in range(cycle_length * 2)]
score_register = [0 for i in range(cycle_length * 2)]

for i in range(10000):
    line_register[i % (cycle_length * 2)] = lines
    #score_register[i % (cycle_length * 2)] = score(lines)

    if line_register[:cycle_length] == line_register[cycle_length:]:
        print(f'Cycle when i={i}')
        break

    for j in range(4):
        if (i % 4) == j:
            lines = roll(lines)

        lines = rotate(lines)


print([score(lines) for lines in line_register])

our_choice = line_register[(1000000000 * 4) % cycle_length]
print(score(our_choice))

