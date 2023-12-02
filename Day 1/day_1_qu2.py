import re

digits_as_words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

#

start_regex = re.compile('([0-9]|' + '|'.join(digits_as_words)+').*$')
end_regex = re.compile('^.*([0-9]|' + '|'.join(digits_as_words)+')')

print(start_regex)
print(end_regex)

total = 0

with open('input1.txt', 'r') as file:
    for line in file.readlines():

        print(line)

        [first] = start_regex.findall(line)
        [last] = end_regex.findall(line)

        print(first, last)

        first_digit = digits_as_words[first] if first in digits_as_words else first
        second_digit = digits_as_words[last] if last in digits_as_words else last

        number = int(first_digit + second_digit)

        print(number)

        total += number

print(total)
