#!/usr/bin/env python3
"""Project Euler Problem 057

It is possible to show that the square root of two can 
be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, 
but the eighth expansion, 1393/985, is the first example 
where the number of digits in the numerator exceeds the 
number of digits in the denominator.

In the first one-thousand expansions, how many fractions 
contain a numerator with more digits than denominator?
"""
# Too many levels for recursion.  Unsolved.
# Solved it with Haskell.  Solution 153
from fractions import Fraction

def expand(n):
    if n==0:
        return 1
    else:
        return 1 + Fraction(1,(1+expand(n-1)))

count = 0
for x in range(1,1000):
    target = expand(x)
    if len(str(target.numerator)) > len(str(target.denominator)):
        count += 1

print("Yep, I knew it was",count)