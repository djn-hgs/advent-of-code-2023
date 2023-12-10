# Day 9 - Haskell

## Dependencies and coding

I needed to split the text on the `" "` character, which is weird because everything else is easy. The solution was to use the `Data.List.Split` module, but that then led to a rabbit-hole trying to understand how I could effectively manage the installation of packages... on a mac.

In addition, I was really fed-up with doing all my Haskell development from the command line.

The recommended solution seemed to be to use the IntelliJ IDE and to manage the Haskell via the relevant plugin, which all worked most nicely using the `stack` system. After some tweaking I got this one working.

The question is whether this is a repeatable experiment...

Seemingly IntelliJ isn't too happy with creating the `Stack` environment, but it's pretty trivial to create from the command line and then import into IntelliJ. So that'll do for now.

## Coding

I'm still learning...

- I keep on rediscovering the `zipwith` function, which is super helpful.
- I want to get better at using guards in recursive functions, and this worked well here.
- When using `zip` on two lists, the zipping is only as long as the shorter list, which is neat.
- Separating the input file into distinct lines is easy using the `lines` function.
- Separating an individual line on a character (such as `" "`) is hard, which is why I ended up using `Data.List.Split` and then the `splitOn` function.

