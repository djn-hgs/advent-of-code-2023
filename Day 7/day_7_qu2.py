from dataclasses import dataclass
import re

line_split = re.compile(r'(.+)\s(.+)')

CARDS = 'J23456789TQKA'


@dataclass
class Pattern:
    text: str
    value: int

    @property
    def fingerprint(self):
        letters = set(self.text)

        in_order = sorted(letters, key=self.text.count, reverse=True)

        fingerprint = [self.text.count(a) for a in in_order]

        j_count = self.text.count('J')

        if 0 < j_count < 5:

            without = letters.difference({'J'})

            w_in_order = sorted(without, key=self.text.count, reverse=True)

            fingerprint = [self.text.count(a) for a in w_in_order]

            fingerprint[0] += j_count

        return fingerprint

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

