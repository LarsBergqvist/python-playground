#!/usr/bin/python3


# zip(). Returns an iterator of tuples where the tuples
# are the combination of the inputs at position i. Stops at the
# length of the shortest input iterable.

x=[(1,2),2,3]
y=[4,5,6,7]
# This returns an iterator of tuples
z=zip(x,y)
print('With zip():')
print(list(z))

# itertools.zip_longest() stops at the length of the
# longest input iterable.
from itertools import zip_longest
z=zip_longest(x,y)
print('With itertools.zip_longest:')
print(list(z))

# cycle() returns an infinite iterator based on a finite iterable
from itertools import cycle
mylist=[1,2,3,4]
iterator=cycle(mylist)
# Though mylist is only 4 items, we can
# iterate on cycle(mylist) forever
# Try looping for a longer range than the length of mylist
for i in range(0,20):
  print(next(iterator))
