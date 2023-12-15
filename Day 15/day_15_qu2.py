import re
from dataclasses import dataclass

data = []

remove_re = re.compile(r'([a-z]+)-')
focal_length_re = re.compile(r'([a-z]+)=([0-9]+)')

@dataclass
class Lens:
    label: str
    focal_length: int

def pt1_hash(step):
    current = 0

    for c in step:
        current += ord(c)
        current *= 17
        current %= 256

    return current


with open('input.txt', 'r') as file:
    for line in file.readlines():
        data += line.strip().split(',')

boxes = [[] for i in range(256)]

for step in data:
    if remove_re.match(step):
        [label] = remove_re.findall(step)
        box = pt1_hash(label)

        print(f'Removing {label} from box {box}')

        labels = [lens.label for lens in boxes[box]]

        if label in labels:
            pos = labels.index(label)
            boxes[box].pop(pos)
    if focal_length_re.match(step):

        [(label, focal_length)] = focal_length_re.findall(step)

        box = pt1_hash(label)

        print(f'Adding {label} with focal length {focal_length}')

        labels = [lens.label for lens in boxes[box]]

        if label in labels:
            pos = labels.index(label)

            boxes[box][pos].focal_length = int(focal_length)
        else:

            boxes[box].append(Lens(label, int(focal_length)))

total = 0

for i, box in enumerate(boxes):
    if box:
        for j, lens in enumerate(box):
            print(f'Box {i}, lens {j} {lens}')

            total += (i + 1) * (j + 1) * lens.focal_length

print(total)
