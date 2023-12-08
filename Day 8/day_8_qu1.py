import re

lr_re = re.compile(r'^([L,R]+)$')
node_re = re.compile(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)')

nodes = {}

with open('input.txt', 'r') as file:
    for line in file.readlines():
        if lr_re.match(line):
            [instructions] = lr_re.findall(line)
            print(instructions)

        if node_re.match(line):
            [(parent, left, right)] = node_re.findall(line)

            print(f'Node {parent}. left: {left}, right: {right}')

            nodes[parent] = {'L': left, 'R': right}

current_node = 'AAA'
cursor = 0
steps = 0

while current_node != 'ZZZ':
    steps += 1
    instruction = instructions[cursor]

    current_node = nodes[current_node][instruction]

    cursor = (cursor + 1) % len(instructions)

    print(steps, cursor)
print(steps)
