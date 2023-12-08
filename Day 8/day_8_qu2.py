import math
import re

lr_re = re.compile(r'^([L,R]+)$')
node_re = re.compile(r'([A-Z1-9]{3}) = \(([A-Z1-9]{3}), ([A-Z1-9]{3})\)')
a_re = re.compile(r'^[A-Z1-9]{2}A$')
z_re = re.compile(r'^[A-Z1-9]{2}Z$')


nodes = {}

start_nodes = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        if lr_re.match(line):
            [instructions] = lr_re.findall(line)

        if node_re.match(line):
            [(parent, left, right)] = node_re.findall(line)

            nodes[parent] = {'L': left, 'R': right}

            if a_re.match(parent):
                start_nodes.append(parent)


def get_dist(current_node):
    cursor = 0
    steps = 0

    while not z_re.match(current_node):
        steps += 1
        instruction = instructions[cursor]

        current_node = nodes[current_node][instruction]

        cursor = (cursor + 1) % len(instructions)

    return steps


distances = {node: get_dist(node) for node in start_nodes}


print(math.lcm(*distances.values()))