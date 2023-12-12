import re

spring_re = re.compile(r'^(.+) (.+)$')


rows = []

def scan(pattern: str, test_pattern: str):
    for i, s in enumerate(test_pattern):

        if i >= len(pattern):
            return False
        elif s == '#' and pattern[i] == '.':
            return False
        elif s == '.' and pattern[i] == '#':
            return False

    return True

def get_combos(pattern: str, lengths: list[int]) -> list[str]:

    slack = len(pattern) - sum(lengths) + len(lengths) - 1

    combos = []

    if len(lengths) == 0:
        test_pattern = '.' * len(pattern)
        if scan(pattern, test_pattern):
            return [test_pattern]
        else:
            return []

    elif slack < 0:
        return []

    else:
        new_lengths = lengths[1:]

        length = lengths[0]

        for i in range(slack + 1):

            if len(lengths) > 1:
                pattern_length = length + 1

            else:
                pattern_length = length

            test_pattern = ''.join(['#' if i <= j < i + length else '.' for j in range(i + pattern_length)])

            if scan(pattern, test_pattern):

                new_pattern = pattern[i + pattern_length:]

                new_combos = get_combos(new_pattern, new_lengths)

                combos += [test_pattern + c for c in new_combos]

    return combos


with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if spring_re.match(line):
            [(pattern_str, lengths_str)] = spring_re.findall(line)

            springs = pattern_str
            lengths = [int(v) for v in lengths_str.split(',')]

            rows.append((springs, lengths))

all_combos = [(r, get_combos(*r)) for r in rows]

for r, combos in all_combos:
    print(f'Row and pattern: {r}')
    for c in combos:
        print(c)

    print(f'There are {len(combos)} combos')


total_combos = sum(len(c) for (r,c) in all_combos)

print(total_combos)
