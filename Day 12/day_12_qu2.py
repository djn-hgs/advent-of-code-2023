import re

spring_re = re.compile(r'^(.+) (.+)$')



def scan(pattern: str, test_pattern: str):
    for i, s in enumerate(test_pattern):

        if i >= len(pattern):
            return False
        elif s == '#' and pattern[i] == '.':
            return False
        elif s == '.' and pattern[i] == '#':
            return False

    return True

def get_combos(pattern: str, lengths: list[int], memo: dict) -> int:

    slack = len(pattern) - sum(lengths) + len(lengths) - 1

    combos = 0

    if len(lengths) == 0:
        test_pattern = '.' * len(pattern)
        if scan(pattern, test_pattern):
            return 1
        else:
            return 0

    elif slack < 0:
        return 0

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

                tuple_lengths = tuple(new_lengths)

                if (new_pattern, tuple_lengths) not in memo:
                    memo[(new_pattern, tuple_lengths)] = get_combos(new_pattern, new_lengths, memo)
                combos += memo[(new_pattern, tuple_lengths)]

    return combos

row_count = 0
rows = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        row_count += 1
        line = line.strip()
        if spring_re.match(line):
            [(pattern_str, lengths_str)] = spring_re.findall(line)

            springs = '?'.join([pattern_str] * 5)
            lengths = [int(v) for v in lengths_str.split(',')] * 5

            rows.append((springs, lengths))

total = 0
memo = {}

for i, (p, l) in enumerate(rows):
    total += get_combos(p, l, memo)
    print(f'Row {i} of {row_count}, running total {total}')

print(total)
print(len(memo))