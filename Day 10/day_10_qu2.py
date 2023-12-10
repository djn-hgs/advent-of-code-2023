import math

the_graph = {}
the_symbol = {}

start = None
width = 0

with open('input.txt', 'r') as file:
    i = 0

    for line in file.readlines():
        width = max(len(line), width)

        for j, pipe in enumerate(line):
            the_graph[(i, j)] = []

            the_symbol[(i, j)] = pipe

            if pipe == '-':
                if j > 0:
                    the_graph[(i, j)].append((i, j - 1))

                if j < width:
                    the_graph[(i, j)].append((i, j + 1))

            if pipe == '|':
                if i > 0:
                    the_graph[(i, j)].append((i - 1, j))

                the_graph[(i, j)].append((i + 1, j))

            if pipe == 'L':
                if i > 0:
                    the_graph[(i, j)].append((i - 1, j))
                if j < width:
                    the_graph[(i, j)].append((i, j + 1))

            if pipe == 'J':
                if i > 0:
                    the_graph[(i, j)].append((i - 1, j))
                if j > 0:
                    the_graph[(i, j)].append((i, j - 1))

            if pipe == '7':
                if j > 0:
                    the_graph[(i, j)].append((i, j - 1))
                the_graph[(i, j)].append((i + 1, j))

            if pipe == 'F':
                if j < width:
                    the_graph[(i, j)].append((i, j + 1))
                the_graph[(i, j)].append((i + 1, j))

            if pipe == 'S':
                start = (i, j)
                if i > 0:
                    the_graph[(i, j)].append((i - 1, j))
                if j > 0:
                    the_graph[(i, j)].append((i, j - 1))
                if j < width:
                    the_graph[(i, j)].append((i, j + 1))
                the_graph[(i, j)].append((i + 1, j))

        i += 1

height = i

distance = {n: math.inf for n in the_graph}
distance[start] = 0

predecessor = {n: None for n in the_graph}

loop_length = None

visited = [start]
stack = [start]

target = None

while stack and not target:
    node = stack.pop()
    visited.append(node)

    for neighbour in the_graph[node]:
        if neighbour == start and distance[node] > 1:
            print('Here')
            loop_length = distance[node] + 1
            target = node
            break

        if neighbour not in visited:
            predecessor[neighbour] = node
            distance[neighbour] = distance[node] + 1
            stack.append(neighbour)

cursor = target

loop = []

while cursor:
    loop.append(cursor)
    cursor = predecessor[cursor]

print(loop)

inside_points = []

for i in range(height):
    outside = True
    on_loop = False
    entry_symbol = None

    for j in range(width):
        if (i, j) in loop:
            pipe = the_symbol[(i, j)]

            if pipe == 'S':
                pipe = '|'

            if pipe == '|':
                on_loop = True
                outside = not outside

            elif pipe == 'L':
                on_loop = True
                entry_symbol = 'L'

            elif pipe == 'F':
                on_loop = True
                entry_symbol = 'F'

            elif pipe == 'J':
                if entry_symbol == 'F':
                    outside = not outside

            elif pipe == '7':
                if entry_symbol == 'L':
                    outside = not outside

        else:
            on_loop = False

        if not (on_loop or outside):
            inside_points.append((i, j))


for i in range(height):
    line = ''

    for j in range(width):
        if (i, j) in loop:
            line += the_symbol[(i, j)]
        elif (i, j) in inside_points:
            line += 'I'
        else:
            line += '.'

    print(line)

print(f'There are {len(inside_points)} inside')
