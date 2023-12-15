data = []


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


print(sum(pt1_hash(c) for c in data))
