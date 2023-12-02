import re

first_re = re.compile("([0-9]).*$")
last_re = re.compile("^.*([0-9])")

total = 0

with open('input1.txt', 'r') as file:
    for line in file.readlines():
        print(line)
        [first] = first_re.findall(line)
        [last] = last_re.findall(line)
        print(first, last)
        total += int(first + last)

print(total)
