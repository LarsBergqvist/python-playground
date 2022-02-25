#!/usr/bin/env python3

#
# Examples on generator expression usage
#

symbols = "ABCD"
values = tuple(ord(symbol) for symbol in symbols)
print(values)

# Cartesian product M x N
M = "ABCD"
N = "123"
product = ((m, n) for m in M for n in N)

for item in product:
    print(item)

# Use the % formatting operator for the tuple
product = ((m, n) for m in M for n in N)
for item in product:
    print("(%s,%s)" % item)
