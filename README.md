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

## Day 9

No parsing!

But a good chance to combine some list comprehension and recursion. Judicious combination of the `zip` function with some slicing meant that the two parts just dropped.

Next job is to do this in Haskell. But I'm not taking up Mr Dales' to tackle them all in Haskell henceforth!

### Update

Haskell solution also included. Had to do quite a lot of work to understand how to achieve the text splitting, so it was good fun. Notes are in the folder [here](Day 9/day9-haskell/README.md).

## Day 10

### Part 1

Yay, no parsing once more. So this was obviously going to come from a Depth First Traversal, and thus I implemented the usual stack-based DFT and got the wrong answer... I was marking nodes as "visited" at the wrong time and so miscounting badly. Did a bit of thinking and then all was well. My code is nasty and I'm not very happy with it.

### Part 2

After considering some classic flood-fill algorithms, I then realised that this was just a parity game. All was going well until I fell down a rabbit-hole trying to replace the `S` symbol with the correct symbol for the pipe it was representing. For the sake of my sanity I eventually just looked at my own input file and realised that it was a `|` symbol but there is a little bit of work to be done coming up with a quick way to do this properly... but not now.

## Day 11

### Part 1

Spent far too long trying to debug my raster-distance calculations only to realise that I hadn't read the question properly: I'd doubled distances vertically but not horizontally. Once this was tweaked, the calculations dropped out nicely.

### Part 2

Pay-back for using a calculated approach in [part 1](). All I had to do was replace the number `2` with `1000000`.

## Day 12

### Part 1

Had a nice recursive approach here, but tied myself in knots trying to deal with base-cases. Got there in the end and it worked just fine. Having used lists to store the spring patterns, I hit a problem with hashing and thus flipped back to using strings. I was desperately hoping that part 2 wasn't going to be a scaled up version...

### Part 2

Oh well... I really couldn't see how to get the code to optimise, but a hint to use memoization sent me in the right direction. Had a slight issue because I needed to memo-ize against patterns and lists, but that was easily resolved by converting my length lists to tuples. The memo dictionary was pretty huge: 154748 items.

I definitely learned something today about using types that hash nicely. And the importance of hashing and memoization in problems that are likely to see a great deal of repetition in their recursion.

## Day 13

### Part 1

After Day 12, I was worried that any not-too elegant solution might lead to pain in Part 2, so I spent a bit too long worrying about finding the most efficient approach. I also interpreted the question to mean that there may be more than one mirror line to deal with. In the end it was enough just to do some slicing and proceed by removing lines of non-symmetry.

### Part 2

Again, I was worried that I might be hitting complexity issues and started wondering how to come up with the most efficient approach. In the end a simple linear search was easily fast enough. The only sticking point was that I forgot a copy of a list of strings would not clone the strings, so a judicious application of `.copy()` sorted that. Not the most elegant code, but the underlying algorithms are ok.

## Day 14

### Part 1

This was ok. I was a bit nervous as to where we were headed with Part 2 and therefore tried to come up wih the most "hashable" and time efficient approach, rotating the list (using the cute `zip` trick) and then performing the required operations using text slicing and a lot of `@cache` just in case.

### Part 2

This was pretty much what I was expecting, and the idea was to find a looping sequence. I wrote a reasonably nice algorithm that found cycles by first spotting cycles in the scores and then checking that these were true cycles in the configurations. Annoyingly, having found the cycle, my actual calculation was wrong...

There followed a lot of confused fiddling and, in the end, I altered my calculation code and used the knowledge about the cycle length to get the correct repeating sequence. Once I'd rememberd that 1000000000 cycles corresponded to 1000000000x4 rotations, it all worked.
 
## Day 15

Part 1 was worryingly easy and had me scared that Part 2 was going to have a sting in the tale. I was a little worried about the time complexity of my approach to Part 2 (lists of lists with deletion) but it all worked fine first time.