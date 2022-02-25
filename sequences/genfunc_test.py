#!/usr/bin/env python3


"""
>>> for i in fibonacci(6): print(i)
1
1
2
3
5
8
"""


def fibonacci(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
