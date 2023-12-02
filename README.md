# Advent of code 2023

## Day 1

### Part 1

An easyish start. Just used the obvious `regex`, got all matches and then indexed the first and last items. Now I think about it, Part 2 would have gone better had I used a more elegant approach here: it would be sufficient only to find the first and last matches in the first place.

### Part 2

Well, that was going fine: adapted the Part 1 code in the obvious way and then used an easy dictionary to read text digits into numerical digits. The demo text also worked beautifully and so I ran it on the input and got the wrong answer. Eventually I realised that greedy matching was the right approach in the first place, and then all was well. Took too long though.

## Day 2

### Part 1

I always take a while to remember that splitting on a character is stupidly fiddly in `regex`, but eventually remembered to use `split`. I like to try to go for a nice data structure that preempts all possibilities in the second part, so went for a dictionary with the colours as keys. After a bit of fiddling around with the format of the `regex` the rest dropped out. Not very pretty though.

### Part 2

The choice of data structure in Part 1 paid off. It took about two tweaks to the existing code to finish off Qu2.