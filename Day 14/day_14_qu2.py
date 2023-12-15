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

with open('demo.txt', 'r') as file:
    for line in file.readlines():
        height += 1
        width = max(width, len(line))
        lines.append(line.strip())

lines = tuple(lines)

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


@cache
def score(lines):
    score = 0
    for row in lines:
        for j, c in enumerate(row):
            if c == 'O':
                score += len(row) - j
    return score


def show(rows):
    for row in rows:
        print(row)


lines = rotate(lines)
lines = rotate(lines)

print('Starting here\n')

show(lines)

scores = []

cycle_length = 4
distance = 10000

seeking_cycle_length = True

while seeking_cycle_length:
    i = 0
    print(cycle_length)
    cycle_spot = {}
    score_cycle_spot = {}

    seeking_a_cycle = True

    while seeking_a_cycle and i < distance:
        seeking_a_score_cycle = True

        while seeking_a_score_cycle and i < distance:

            lines = rotate(lines)
            lines = roll(lines)
            score_cycle_spot[i % (cycle_length * 2)] = score(lines)

            #print(score_cycle_spot)

            if i > cycle_length * 2:
                if all(
                        score_cycle_spot[j] == score_cycle_spot[j + cycle_length]
                        for j in range(cycle_length)
                ):
                    seeking_a_score_cycle = False

            i += 1

        for j in range(cycle_length * 2):
            lines = rotate(lines)
            lines = roll(lines)

            cycle_spot[i % (cycle_length * 2)] = lines

            i += 1

        if all(
                cycle_spot[j] == cycle_spot[j + cycle_length]
                for j in range(cycle_length)
        ):
            print(f'Found a cycle of length {cycle_length} after {i} iterations')
            seeking_a_cycle = False
            seeking_cycle_length = False
    if seeking_cycle_length:
        cycle_length += 4

score = score(lines)

lines = rotate(lines)
print(f'Total score {score}')
print(score_cycle_spot)
print(score_cycle_spot[(1000000000 - 1) % cycle_length])
print(score_cycle_spot[(146 - 1) % cycle_length])