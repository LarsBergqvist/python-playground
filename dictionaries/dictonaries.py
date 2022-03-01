#!/usr/bin/env python3

"""
>>> get_dictionary()
{'SEK': 1.3, 'EUR': 1.4}

>>> get_dictionary()
{'SEK': 1.3, 'EUR': 1.4}

>>> get_sorted_tuple_list_from_dictionary(get_dictionary())
[('EUR', 1.4), ('SEK', 1.3)]

>>> get_dictionary_from_dict()
{'Pelle': {'name': 'Pelle', 'age': 36, 'country': 'Denmark'}, 'Ole': {'name': 'Ole', 'age': 22, 'country': 'Norway'}, 'Lisa': {'name': 'Lisa', 'age': 32, 'country': 'Sweden'}}
"""


def get_dictionary():
    dic = {'SEK': 1.3}
    currency = dic.setdefault('SEK', 1.5)
    currency = dic.setdefault('EUR', 1.4)
    return dic


def get_sorted_tuple_list_from_dictionary(dic):
    sorted_list = sorted(dic.items())
    return sorted_list


def get_dictionary_from_dict():
    dic = dict(
        Pelle=dict(name="Pelle", age=36, country="Denmark"),
        Ole=dict(name="Ole", age=22, country="Norway"),
        Lisa=dict(name="Lisa", age=32, country="Sweden"),
    )
    return dic


if __name__ == "__main__":
    import doctest
    doctest.testmod()
