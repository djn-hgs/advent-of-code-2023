import builtins
import types
import typing
from dataclasses import dataclass
import re

line_split = re.compile(r'(.+)\s(.+)')

cards = '23456789TJQKA'

CARD_WEIGHT = {a: cards.index(a) + 1 for a in cards}

@dataclass
class Rule:
    test: typing.Callable
    label: str
    weight: int


def five(pattern: str):
    return len(set(pattern)) == 1

def four(pattern: str):
    as_set = set(pattern)

    if len(as_set) != 2:
        return False

    [a, b] = list(as_set)

    if pattern.count(a) == 4 or pattern.count(b) == 4:
        return True
    else:
        return False

def full_house(pattern: str):
    as_set = set(pattern)

    if len(as_set) != 2:
        return False

    return 3 in [pattern.count(a) for a in as_set]

def three(pattern: str):
    as_set = set(pattern)

    if len(as_set) != 3:
        return False

    return 3 in [pattern.count(a) for a in as_set]


def two_pair(pattern: str):
    as_set = set(pattern)

    if len(as_set) != 3:
        return False

    return max([pattern.count(a) for a in as_set]) == 2


def one_pair(pattern: str):
    as_set = set(pattern)

    if len(as_set) != 4:
        return False

    return max([pattern.count(a) for a in as_set]) == 2


def high_card(pattern: str):
    return len(set(pattern)) == 5

RULES = [
    Rule(test=five, label='5 of a kind', weight=7),
    Rule(test=four, label='4 of a kind', weight=6),
    Rule(test=full_house, label='Full house', weight=5),
    Rule(test=three, label='Three of a kind', weight=4),
    Rule(test=two_pair, label='Two pair', weight=3),
    Rule(test=one_pair, label='Three of a kind', weight=2),
    Rule(test=high_card, label='High card', weight=1)

]

@dataclass
class Pattern:
    text: str
    value: int

    @property
    def weight(self):
        for rule in RULES:
            if rule.test(self.text):
                return rule.weight

    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        elif self.weight == other.weight:
            i = 0
            while i < 5:
                if CARD_WEIGHT[self.text[i]] < CARD_WEIGHT[other.text[i]]:
                    return True
                elif CARD_WEIGHT[self.text[i]] > CARD_WEIGHT[other.text[i]]:
                    return False

                i += 1
            return False

        else:
            return False

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