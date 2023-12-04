import re

pile_re = re.compile(r'^Card\s+[0-9]+:\s(.*)\s\|\s(.*)\s')
space_re = re.compile(r'\s*(\d+)\s*')

total = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():

        [(winning_text, my_nums)] = pile_re.findall(line)

        print(f'{winning_text} and {my_nums}')

        winning_split = space_re.findall(winning_text)
        my_split = space_re.findall(my_nums)

        winning_set = {int(v) for v in winning_split}
        my_set = {int(v) for v in my_split}

        intersection = winning_set & my_set

        if intersection:
            total += 2 ** (len(intersection) - 1)

print(total)


