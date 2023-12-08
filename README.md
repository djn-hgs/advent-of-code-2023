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

## Day 4

### Part 1

Yet more `regex` to sort the parsing. Quite enjoyed that. Whoop. Realised that the problem was then solved with some set intersections and that was that.

### Part 2

If I'd created the dictionary that I'd thought of creating in [Part 1]() then this would have been trivial. As it was, following the explanation on the site suggested a simple, non-recursive, solution that worked perfectly... or would have done if I hadn't messed up my indexing AGAIN. Lesson learned.

## Note about `input.txt` files

Just read the post about not including my inputs in my repos so time to fiddle with some `.gitignore` files.

## Day 5

### Part 1

Had some fun using dictionaries to store the transformations and then applied these in sequence to work out the answer.

### Part 2

The solution here was fairly obvious: store the ranges in the question and then map those using the described transformations. It got quite fiddly using dictionaries, so I used some dataclasses to store things nicely and to make debugging easier. Managed to get myself confused by the possibility of overlapping ranges - which didn't occur in the question - and once I'd discounted this the code ran straight through.

## Day 6

I feel slightly guilty here: rather than using Python to produce all possible matches by sieving, I just solved a quadratic and then adjusted for the case where we had integer limits (so the discriminant was a perfect square). On that basis, part 2 was no harder than part 1.

## Day 7

### Part 1

Confused myself by trying to work out how to regex the various hands and then gave up and just wrote some rough and ready functions that matched them. With that in place it was then just a case of sorting on the basis of the "weights" of the various hands and then working out the right way to handle a tie-breaker. I realised, whilst doing part 2, that the whole thing was trivial if we just created a histogram of letter frequencies and then sorted lexicographically on that. Hey ho.

### Part 2

Initially I just worked out the effect of substituting the known number of 'J' cards for the dominant other card, but then realised that calculating a histogram with and without the 'J' present then allowed us to work out the additional score that could be achieved by using it as a wildcard.

## Day 8

### Part 1

Initially it looked like a `Tree` class might be the way in, but then I realised that this was better understood as something akin to a Lindenmayer 'L-System'. Then it was just a case of tracking the journey of a node starting at 'AAA' until it landed at 'ZZZ'

### Part 2

Once I'd understood the scenario, a small amount of `regex` enabled me to tweak the previous code to find all the starting nodes and to match all the ending nodes. It was pretty obvious that we wanted to use `lcm` rather than trying to traverse them all simultaneously.

## Update on `input.txt`

Just realised that `.gitignore` parses wildcards in the obvious way, so this is now the only line in my `.gitignore` file:

```
/*/input.txt
```