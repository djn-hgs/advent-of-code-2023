from dataclasses import dataclass
import re

line_split = re.compile(r'(.+)\s(.+)')

CARDS = '23456789TJQKA'


@dataclass
class Pattern:
    text: str
    value: int

    @property
    def fingerprint(self):
        letters = set(self.text)

        letters_in_order = sorted(letters, key=self.text.count, reverse=True)

        return [self.text.count(a) for a in letters_in_order]

    def card_values(self):
        return [CARDS.index(a) for a in self.text]

    def __lt__(self, other):
        return (self.fingerprint, self.card_values()) < (other.fingerprint, other.card_values())


patterns = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        [(pattern, value_txt)] = line_split.findall(line)

        value = int(value_txt)

        patterns.append(Pattern(text=pattern, value=value))

patterns.sort()

score = sum([(i + 1) * pattern.value for i, pattern in enumerate(patterns)])

print(score)

