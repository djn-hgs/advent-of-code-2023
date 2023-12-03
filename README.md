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

## Day 3

### Part 1

Oh goody, more parsing with `regex`. So, spent some time thinking how the data might be useful in part 2 and so decided to store all possible information about the values and their locations. Not that it particularly helped. Anyway, it was a fairly easy puzzle to solve and the `regex` tricks that I learned will certainly come in useful.

### Part 2

So this part wasn't much harder than [Part 1]() and a tweak to my slightly mad data structures from the first part enabled me to store the location of all asterisks and all values.

Got the correct value on the demo data after realising one small error in my match spans... and then it failed on the real input.

Tried a few test cases and couldn't solve the problem, so eventually looked down to see what it _wasn't_ spotting. It seemed to be spotting everything that it should.

So then I looked for anything it _was_ spotting that it shouldn't... and realised that my original debug had omitted one `+ 1` which meant that it was over-matching one case (which I thought I had already spotted and sorted and therefore discounted from my testing)... and therefore not including a ratio because I was matching 3 values when it should have been 2.

Doh.
