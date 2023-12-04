import re

pile_re = re.compile(r'^Card\s+([0-9]+):\s(.*)\s\|\s(.*)\s')
space_re = re.compile(r'\s*(\d+)\s*')

total = 0

match_dict = {}

with open('input.txt', 'r') as file:
    for line in file.readlines():

        [(card_num,
          winning_text,
          my_nums)] = pile_re.findall(line)

        winning_split = space_re.findall(winning_text)
        my_split = space_re.findall(my_nums)

        winning_set = {int(v) for v in winning_split}
        my_set = {int(v) for v in my_split}

        intersection = winning_set & my_set

        match_dict[int(card_num)] = len(intersection)

        print(f'Card {card_num}: {len(intersection)}')


print(match_dict)

card_nums = sorted(list(match_dict))

my_cards = {i: 1 for i in card_nums}

for i in card_nums:
    print(my_cards)

    print(f'Processing card {i} with {match_dict[i]} matches ({my_cards[i]} repetitions)')

    if match_dict[i] == 0:
        print('Nothing to do: no winning numbers.')
    else:

        for j in range(match_dict[i]):
            if i + j + 1 in my_cards:
                print(f'Card {i + j + 1} times {my_cards[i]}')
                my_cards[i + j + 1] += my_cards[i]
            else:
                print('Doh: nowhere to look.')

print(sum(my_cards.values()))





