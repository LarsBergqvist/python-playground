#!/usr/bin/env python3

"""
>>> a=[1,2,3]
>>> b=['a','b','c']
>>> list(zip(a,b))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> a=[1,2,3]
>>> b=['a','b']
>>> list(zip(a,b))
[(1, 'a'), (2, 'b')]
>>> zipped=zip([1,2],['a','b'])
>>> a1, b1 = zip(*zipped)
>>> print(a1)
(1, 2)
>>> print(b1)
('a', 'b')
>>> print(list(a1))
[1, 2]
>>> print(list(b1))
['a', 'b']
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
