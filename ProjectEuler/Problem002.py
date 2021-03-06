#!/usr/bin/env python3
"""Project Euler Problem 002

Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not 
exceed four million.
"""

# First generate a list of fibs in linear time.  Up to 1000 should do.
fibList = [1,1]
for x in range(1000):
    fibList.append(fibList[-2] + fibList[-1])

# Now sum the approriate terms
answer = sum(x for x in fibList if x < 4000000 and x % 2 == 0)

print(answer)
