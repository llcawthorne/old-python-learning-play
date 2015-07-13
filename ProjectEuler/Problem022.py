#!/usr/bin/env python3
"""Project Euler Problem 022

Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working 
out the alphabetical value for each name, multiply this 
value by its alphabetical position in the list to obtain 
a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

for line in open('names.txt'):
    names = line.split(',')

for x in range(len(names)):
    names[x] = names[x][1:-1]

names.sort()

values = []
counter = 1
for name in names:
    value = 0
    for letter in name:
        value += ord(letter) - 64
    values.append(value * counter)
    counter += 1

print('The sum of the name scores is',sum(values))

