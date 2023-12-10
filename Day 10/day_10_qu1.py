import math

the_graph = {}

start = None
width = 0

with open('input.txt', 'r') as file:
    i = 0

    for line in file.readlines():
        width = max(len(line), width)

        for j, pipe in enumerate(line):
            the_graph[(i, j)] = []

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

print(math.ceil(loop_length / 2))
cursor = target

journey = []

while cursor:
    journey.append(cursor)
    cursor = predecessor[cursor]

print(len(journey))
