#!/usr/bin/env python3
# Various looping techniques are displayed

# When looping through a dictionary, the key and corresponding value
# can be retrieved at the same time using the items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding
# value can be retrieved at the same time using the enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can
# be paired with the zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, use the reversed() function
for i in reversed(range(1, 10, 2)):  # 9-1 in steps of 2
    print(i)

# To loop over a sequence in sorted order, use the sorted() function
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
