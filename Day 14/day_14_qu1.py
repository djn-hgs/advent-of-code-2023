with open('input.txt', 'r') as file:
    lines = file.readlines()

transposed = [''.join(list(x)) for x in zip(*lines)]

score = 0
for row in transposed:
    print(row)
    row_len = len(row)
    searching = True
    cursor = 0
    while searching:
        next_hash = row.find('#', cursor)

        if next_hash == -1:
            seek_point = row_len
        else:
            seek_point = next_hash

        if seek_point > cursor:
            zeroes = row.count('O', cursor, seek_point)
            #print(f'{zeroes} zeroes between {cursor} and {next_hash}')
            score += (row_len - cursor - zeroes + 1 + row_len - cursor) * zeroes / 2

        cursor = seek_point + 1

        if cursor > len(row) or next_hash == -1:
            searching = False
print(score)

