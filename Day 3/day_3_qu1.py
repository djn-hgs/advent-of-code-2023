import re

number_re = re.compile(r'[0-9]+')
num_dot_re = re.compile(r'^([0-9]|\.)*$')

file_as_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        file_as_list.append(line.strip())

nums = {}

for i, row in enumerate(file_as_list):

    print(f'row: {i} is {row}')

    matches = number_re.finditer(row)

    for match in matches:
        (start, end) = match.span()

        value = int(match.group(0))

        print(f'{value} start: {start} end: {end}')

        found_symbol = False

        check = ''

        # Left

        if start > 0:
            left = start - 1
            check += row[left]
        else:
            left = start

        # Right

        if end < len(row):
            right = end + 1
            check += row[end]
        else:
            right = end

        # Above

        if i > 0:
            check += file_as_list[i - 1][left: right]

        # Below

        if i < len(file_as_list) - 1:
            check += file_as_list[i + 1][left: right]

        if num_dot_re.match(check):
            print(f'No symbols for {value}')
        else:
            print(f'Adding {value} to total.')

            nums[(i, start)] = value

print(nums)
print(sum(nums.values()))
