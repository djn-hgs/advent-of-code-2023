import re

seed_re = re.compile(r'seeds:\s(.*)')
space_re = re.compile(r'\s*(\d+)\s*')
map_re = re.compile(r'([a-z]+)-to-([a-z]+)\smap:')
range_re = re.compile(r'(\d+)\s(\d+)\s(\d+)')

range_dict = {}

with open('input.txt', 'r') as file:
    first_line = file.readline()

    [seeds_list] = seed_re.findall(first_line)
    start_seeds_text = space_re.findall(seeds_list)

    start_seeds = {int(v): None for v in start_seeds_text}

    source = None
    target = None

    for line in file.readlines():
        if map_re.match(line):

            [(source, target)] = map_re.findall(line)

            range_dict[source] = {target: {}}

        elif range_re.match(line):
            [(target_index, source_index, length)] = range_re.findall(line)

            range_dict[source][target][int(source_index)] = (int(target_index), int(length))

print(range_dict)

for seed_index in start_seeds:
    source = 'seed'

    cursor = seed_index

    while source != 'location':
        for target in range_dict[source]:
            print(f'Source {source} Target {target} Cursor {cursor}')
            for source_index in range_dict[source][target]:
                target_index, length = range_dict[source][target][source_index]

                offset = cursor - source_index

                if 0 <= offset < length:
                    print(f'Adjusting {source_index} to {target_index} (length {length})')
                    cursor = target_index + offset
                    break

            print(f'Adjusted cursor {cursor}')

        source = target

    print(f'Seed {seed_index} ends up at location {cursor}\n')
    start_seeds[seed_index] = cursor

print(min(start_seeds.values()))
