"""
>>> 'hello friend'.capitalize()
'Hello friend'

>>> 'Hello friend'.center(20,'*')
'****Hello friend****'

>>> 'Hello friend'.center(10,'*')
'Hello friend'

>>> 'hello friend hello'.count('hello',0,20)
2

>>> 'hello friend hello'.count('hello',0,10)
1

>>> b'hello friend'.decode('UTF-8')
'hello friend'

>>> 'hello friend'.encode('ascii')
b'hello friend'

>>> 'hello friend'.find('hello')
0

>>> 'hello friend'.endswith('friend')
True

>>> 'hello {0} {1}'.format('again','friend')
'hello again friend'

>>> 'ABC123abc'.isalnum()
True

>>> 'ABCabc'.isalpha()
True

>>> '123'.isdigit()
True

>>> 'abc'.islower()
True

>>> 'ABC'.isupper()
True

>>> ' '.join(['word1','word2'])
'word1 word2'

>>> 'hello friend'.partition(' ')
('hello', ' ', 'friend')

>>> 'hello friend'.replace('friend','world')
'hello world'

>>> 'hello friend'.split(' ')
['hello', 'friend']

>>> 'hello\\nfriend'.splitlines()
['hello', 'friend']

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
