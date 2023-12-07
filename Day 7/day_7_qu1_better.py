import builtins
import types
import typing
from dataclasses import dataclass
import re

line_split = re.compile(r'(.+)\s(.+)')

CARDS = '23456789TJQKA'

CARD_WEIGHT = {a: CARDS.index(a) + 1 for a in CARDS}

FINGERPRINT_WEIGHT = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5]
]


@dataclass
class Pattern:
    text: str
    value: int

    @property
    def weight(self):
        letters = set(self.text)

        letters_in_order = sorted(letters, key=self.text.count)
        fingerprint = [self.text.count(a) for a in letters_in_order]

        print(letters_in_order, fingerprint)

        return FINGERPRINT_WEIGHT.index(fingerprint)

    def card_values(self):
        return [CARDS.index(a) for a in self.text]

    def __lt__(self, other):
        return (self.weight, self.card_values()) < (other.weight, other.card_values())


patterns = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        [(pattern, value_txt)] = line_split.findall(line)

        value = int(value_txt)

        patterns.append(Pattern(text=pattern, value=value))

print(patterns)

patterns.sort()

total = 0

for i, pattern in enumerate(patterns):
    score = (i + 1) * pattern.value
    print(f'{i + 1} for {pattern.text} with value {pattern.value} so score is {score}')
    total += score

print(total)