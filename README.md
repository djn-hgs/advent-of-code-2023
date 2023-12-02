# Advent of code 2023

## Day 1

### Part 1

An easyish start. Just used the obvious regex, got all matches and then indexed the first and last items. Now I think about it, Part 2 would have gone better had I used a more elegant approach here: it would be sufficient only to find the first and last matches in the first place.

### Part 2

Well, that was going fine: adapted the Part 1 code in the obvious way and then used an easy dictionary to read text digits into numerical digits. The demo text also worked beautifully and so I ran it on the input and got the wrong answer. Eventually I realised that greedy matching was the right approach in the first place, and then all was well. Took too long though.