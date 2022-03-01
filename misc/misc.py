#!/usr/bin/env python3

# Conditionally select one of two items
# by using a list and an index
# Works as True == 1 and False == 0
"""
>>> b=True
>>> ['apple','orange'][b]
'orange'
>>> b=False
>>> ['apple','orange'][b]
'apple'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
