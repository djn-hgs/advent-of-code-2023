def next_value(last_line):
    if any(last_line):
        next_line = [b - a for (a, b) in zip(last_line[:-1], last_line[1:])]

        return last_line[-1] + next_value(next_line)
    else:
        return 0

sum = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        values = [int(v) for v in line.split(' ')]

        sum += next_value(values)

        print(values, next_value(values))

print(sum)
