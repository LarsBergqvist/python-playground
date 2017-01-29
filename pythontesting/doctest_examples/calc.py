
"""
>>> get_multiplied_result([5,10])
50
>>> get_multiplied_result([5.5,2])
11.0
>>> get_multiplied_result([5.5,2,3])
33.0
>>> get_multiplied_result([5.5])
5.5
"""
def get_multiplied_result(factors):
    total = 1
    for factor in factors:
        total = total * factor
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()
