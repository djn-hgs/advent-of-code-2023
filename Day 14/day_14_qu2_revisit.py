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
#lines = rotate(lines)

print('Starting here\n')

show(lines)

scores = []

n = 1000000000

for i in range(1):
    #print(f'\nTilting direction : {directions[i % 4]}\n')

    lines = rotate(lines)
    lines = roll(lines)

    #show(lines)


    #scores.append(score(lines))

    # if scores[-4:] == scores[-8:-4]:
    #     print('Here')

score = score(lines)

lines = rotate(lines)
print('\nFinal\n')
show(lines)
print('Boo')
print(f'Total score {score}')
