import re

game_regex = re.compile('Game [0-9]+: (.*)')

red_regex = re.compile('([0-9]+) red')
green_regex = re.compile('([0-9]+) green')
blue_regex = re.compile('([0-9]+) blue')

with open('demo_qu1.txt', 'r') as file:
    for line in file.readlines():
        [game] = game_regex.findall(line)
        print(game)

        hands = game.split(';')

        print(hands)

