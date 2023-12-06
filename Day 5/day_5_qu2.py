import re
from dataclasses import dataclass

seed_re = re.compile(r'seeds:\s(.*)')
space_re = re.compile(r'\s*(\d+)\s+(\d+)\s*')
map_re = re.compile(r'([a-z]+)-to-([a-z]+)\smap:')
range_re = re.compile(r'(\d+)\s(\d+)\s(\d+)')

@dataclass
class Frame:
    start: int
    stop: int
    type: str

@dataclass
class Transform:
    source_type: str
    start: int
    stop: int
    target_type: str
    target_start: int

with open('input.txt', 'r') as file:
    first_line = file.readline()

    [seeds_list] = seed_re.findall(first_line)
    start_seeds_text = space_re.findall(seeds_list)

    source_frames = [Frame(start=int(v), stop =int(v) + int(r), type='seed') for (v, r) in start_seeds_text]

    transforms = []

    source = None
    target = None

    for line in file.readlines():
        if map_re.match(line):

            [(source, target)] = map_re.findall(line)

        elif range_re.match(line):
            [(target_index, source_index, length)] = range_re.findall(line)

            transforms.append(
                Transform(start=int(source_index),
                          stop=int(source_index) + int(length),
                          source_type=source,
                          target_type=target,
                          target_start=int(target_index)
                          )
            )

print(source_frames)
print(transforms)

chain = {
    'seed': 'soil',
    'soil': 'fertilizer',
    'fertilizer': 'water',
    'water': 'light',
    'light': 'temperature',
    'temperature': 'humidity',
    'humidity': 'location'
}

source = 'seed'

while source != 'location':

    target = chain[source]

    print(f'Source {source}, target {target}')

    target_frames = []

    for transform in transforms:
        if transform.source_type == source:
            print(f'{transform}')
            print(source_frames)

            spare_source_frames = []

            for frame in source_frames:
                print(f'Frame {frame}')

                if frame.start < transform.start <= frame.stop:
                    left_frame = Frame(start=frame.start, stop=transform.start, type=source)

                    spare_source_frames.append(left_frame)

                    frame.start = transform.start

                    print(f'Left {frame}')

                if frame.start < transform.stop < frame.stop:
                    right_frame = Frame(start=transform.stop, stop=frame.stop, type=source)

                    spare_source_frames.append(right_frame)

                    frame.stop = transform.stop

                    print(f'Right {frame}')

                if transform.start <= frame.start < frame.stop <= transform.stop:
                    offset = transform.target_start - transform.start

                    new_frame = Frame(
                        start=frame.start + offset,
                        stop=frame.stop + offset,
                        type=target
                    )

                    target_frames.append(new_frame)

                    print(f'Contained {frame} so mapped to {new_frame}')

                else:
                    spare_source_frames.append(frame)

                    print(f'Spare {frame}')

            source_frames = spare_source_frames

    for frame in source_frames:
        new_frame = Frame(start=frame.start, stop=frame.stop, type=target)

        target_frames.append(new_frame)

    source = target
    source_frames = target_frames

print(source_frames)

print(min([frame.start for frame in source_frames]))