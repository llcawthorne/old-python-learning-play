#!/usr/bin/env python3
"""Project Euler Problem 056

A googol (10^(100)) is a massive number: one followed 
by one-hundred zeros; 100^(100) is almost unimaginably 
large: one followed by two-hundred zeros. Despite their 
size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^(b), 
where a, b < 100, what is the maximum digital sum?
"""

vals = {a**b for a in range(100) for b in range(100)}

greatestSum = 0
for val in vals:
    sum = 0
    for digit in str(val):
        sum += int(digit)
    if sum > greatestSum:
        greatestSum = sum

print('Maximum sum is',greatestSum)
