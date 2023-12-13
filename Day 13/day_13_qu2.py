pattern_list = []
reading = False
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if line and not reading:
            pattern = [line]
            reading = True
        elif line and reading:
            pattern.append(line)
        elif not line and reading:
            pattern_list.append(pattern)
            reading = False

pattern_list.append(pattern)


def vertical(pattern):
    width = max(len(line) for line in pattern)

    ready = ((line, line[::-1]) for line in pattern)

    columns = set(range(1, width))

    for (pattern, backward) in ready:
        for column in range(width):
            focus = min(column, width - column)
            forward_slice = pattern[max(0, column - focus):column]
            reverse_slice = backward[max(0, width - column - focus):width - column]

            if forward_slice != reverse_slice:
                columns.discard(column)
    return columns


def horizontal(pattern):
    return vertical(transpose(pattern))


def transpose(pattern):
    width = max(len(l) for l in pattern)
    height = len(pattern)

    return [''.join(pattern[j][i] for j in range(height)) for i in range(width)]

total = 0

for p in pattern_list:
    found = False

    old_v = vertical(p)
    old_h = horizontal(p)

    for i in range(len(p)):
        for j in range(len(p[0])):
            new_p = p.copy()
            the_chr = p[i][j]

            if the_chr == '.':
                the_chr = '#'
            else:
                the_chr = '.'

            new_p[i] = p[i][:j] + the_chr + p[i][j + 1:]
            v = vertical(new_p)
            h = horizontal(new_p)
            print((i, j), v, h, p[i], new_p[i])
            if v - old_v or h - old_h:
                found = True
                break
        if found:
            break

    v -= old_v
    h -= old_h
    print(found, (i, j), the_chr, v, h)

    if v:
        x = v.pop()
        total += x
    if h:
        y = h.pop()
        total += 100 * y

print(total)