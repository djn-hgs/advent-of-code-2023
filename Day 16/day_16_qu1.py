from dataclasses import dataclass

mirrors: dict[tuple[int, int]: str] = {}

mirror_symbols = ('/', '\\', '|', '-')


def show(trail):
    count = 0

    for j in range(height):

        line = ''

        for i in range(width):
            if (i, j) in mirrors:
                line += mirrors[(i, j)]
            elif ((i, j), N) in trail:
                line += '^'
            elif ((i, j), E) in trail:
                line += '>'
            elif ((i, j), S) in trail:
                line += 'V'
            elif ((i, j), W) in trail:
                line += '<'
            else:
                line += '.'
        print(line)
    print(count)



@dataclass
class Cursor:
    x: int
    y: int
    direction: str

    def check_mirrors(self):
        other = None

        if (self.x, self.y) in mirrors:
            new_directions = step_map[self.direction][mirrors[(self.x, self.y)]]

            self.direction = new_directions[0]

            if len(new_directions) == 2:
                other = Cursor(self.x, self.y, new_directions[1])
        return other

    def update(self):
        dx, dy = directions[self.direction]

        if ((dx == -1 and self.x == 0)
                or (dx == 1 and self.x == width - 1)
                or (dy == -1 and self.y == 0)
                or (dy == 1 and self.y == height - 1)):

            return False

        else:
            self.x += dx
            self.y += dy

            return True

    def breadcrumb(self):
        return (self.x, self.y), self.direction


directions = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

N, E, S, W = directions.keys()

step_map = {N: {
    '-': [E, W],
    '|': [N],
    '/': [E],
    '\\': [W]
}, E: {
    '-': [E],
    '|': [N, S],
    '/': [N],
    '\\': [S]
}, S: {
    '-': [E, W],
    '|': [S],
    '/': [W],
    '\\': [E]
}, W: {
    '-': [W],
    '|': [N, S],
    '/': [S],
    '\\': [N]
}}

width = 0

j = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        width = max(width, len(line))
        for i, c in enumerate(line):
            if c in mirror_symbols:
                mirrors[(i, j)] = c

        j += 1

height = j

been_here_before = []

cursors = [Cursor(0, 0, E)]

while cursors:
    new_cursors = []
    show(been_here_before)
    input()


    for c in cursors:
        if c.breadcrumb() not in been_here_before:
            been_here_before.append(c.breadcrumb())

            another_cursor = c.check_mirrors()

            if another_cursor:
                new_cursors.append(another_cursor)

            new_cursors.append(c)

    cursors = []

    for c in new_cursors:
        if c.update():
            cursors.append(c)


pos = {(x, y) for ((x, y), d) in been_here_before}
show(been_here_before)

print(f'Visited {len(pos) - 1}')

