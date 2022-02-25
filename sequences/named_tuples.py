#!/usr/bin/env python3

#
# Examples on named tuples usage
#

from collections import namedtuple

book = namedtuple("Book", "name author year")
book1 = book("How to use tuples", "Arne", 2016)
book2 = book("Python is your friend", "Bertil", 2015)
print(book._fields)
print(book1)
print(book2)
print(book1.name)
print(book2.name)
