#!/usr/bin/env python3

#
# Examples on list comprehension usage
#

symbols = "abcdefg"

# Create a list with list comp
codes = [ord(symbol) for symbol in symbols]
print(codes)

# Create a filtered list with list comp
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 100]
print(codes)

# Python 3 listcomps do not leak variables
x = "my value"
my_list = [x for x in 'LEAK']
print(my_list)
# In Python2 x would have changed to 'K'
# In Python3 x remains as 'my value'
print(x)

# Cartesian product M x N
M = "ABCD"
N = "123"
product = [(m,n) for m in M for n in N]
print(product)
product = [(m,n) for n in N for m in M]
print(product)
