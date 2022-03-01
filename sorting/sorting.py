#!/usr/bin/env python3

"""
>>> sort_ascending([6,7,8,1,2])
[1, 2, 6, 7, 8]
>>> sort_descending([6,7,8,1,2])
[8, 7, 6, 2, 1]
>>> sort_ascending(['orange','apple','banana'])
['apple', 'banana', 'orange']
>>> sort_ascending({'orange','apple','banana'})
['apple', 'banana', 'orange']
>>> sort_ascending(('orange','apple','banana'))
['apple', 'banana', 'orange']
>>> sort_ascending_by_word_length(['orange','apple','banana'])
['apple', 'orange', 'banana']
>>> sort_tuples_by_first_asc_then_second_value_desc([('Pelle', 100), ('Pelle', 34),('Olle', 50), ('Olle', 46)])
[('Olle', 50), ('Olle', 46), ('Pelle', 100), ('Pelle', 34)]
"""


def sort_ascending(iterable):
    return sorted(iterable)


def sort_descending(iterable):
    return sorted(iterable, reverse=True)


def sort_ascending_by_word_length(iterable):
    return sorted(iterable, key=len)


def sort_tuples_by_first_asc_then_second_value_desc(iterable):
    return sorted(iterable, key=lambda item: (item[0], -item[1]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
