import re

pattern = re.compile('[0-9]')

total = 0

with open('input1.txt', 'r') as file:
    for line in file.readlines():
        print(line)
        values = pattern.findall(line)
        print(values)
        total += int(values[0] + values[-1])

print(total)
