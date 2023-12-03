import re

number_re = re.compile(r'[0-9]+')
num_dot_re = re.compile(r'^([0-9]|\.)*$')
star_re = re.compile(r'\*')

file_as_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        file_as_list.append(line.strip())

values = {}
stars = {}

for i, row in enumerate(file_as_list):

    values[i] = {}
    stars[i] = {}

    #print(f'row: {i} is {row}')

    num_matches = number_re.finditer(row)

    for match in num_matches:
        (start, end) = match.span()

        value = int(match.group(0))

        #print(f'{value} start: {start} end: {end}')

        values[i][(start, end)]  = value

    star_matches = star_re.finditer(row)

    for match in star_matches:
        (start, end) = match.span()

        value = match.group(0)

        #print(f'{value} start: {start} end: {end}')

        stars[i][(start, end)] = value

sum = 0

for i in stars:
    for (j, k) in stars[i]:

        print(f'Row {i} position {j}')

        ratios = []

        # Left

        if j > 0:
            left = j - 1

            for (start, end) in values[i]:
                if end == j:
                    ratios.append(values[i][(start, end)])

        else:
             left = j

        # Right

        if j < len(file_as_list[i]):
            right = j + 1

            for (start, end) in values[i]:
                if start == j + 1:
                    ratios.append(values[i][(start, end)])

        else:
            right = j

        # Above

        if i > 0:
            for (start, end) in values[i - 1]:
                if end > left and start <= right:
                    ratios.append(values[i - 1][(start, end)])

        # Below

        if i < len(file_as_list):
            for (start, end) in values[i + 1]:
                if end > left and start <= right:
                    ratios.append(values[i + 1][(start, end)])

        print(f'Adjacent values {ratios}')

        if len(ratios) == 2:
            [first, second] = ratios
            print(f'Adding {first} * {second} to total')

            sum += first * second

print(sum)
