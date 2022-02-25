#!/usr/bin/env python3

"""
>>> iterate_items_and_index([4,5,3,2,2,8])
0 4
1 5
2 3
3 2
4 2
5 8
>>> iterate_items_and_index([4,5,3,2,2,8],3)
3 4
4 5
5 3
6 2
7 2
8 8
"""


def iterate_items_and_index(sequence, start_index=0):
    for index, item in enumerate(sequence, start_index):
        print(index, item)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
