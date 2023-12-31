import re

game_regex = re.compile('Game ([0-9]+): (.*)')

block_re = {
    'red': re.compile('\s*([0-9]+) red'),
    'green': re.compile('\s*([0-9]+) green'),
    'blue': re.compile('\s*([0-9]+) blue')
}

game_sum = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():

        [(game_num, game)] = game_regex.findall(line)

        print(f'Game {game_num}: {game}')

        hands = game.split(';')

        print(hands)

        counters = {color: 0 for color in block_re}

        for hand in hands:
            blocks = hand.split(',')

            for block in blocks:

                for color in block_re:
                    regex = block_re[color]

                    if regex.match(block):
                        [count] = regex.findall(block)
                        print(f'{color} matches {count}')

                        if int(count) > counters[color]:
                            counters[color] = int(count)

        game_sum += counters['red'] * counters['green'] * counters['blue']


print(game_sum)
