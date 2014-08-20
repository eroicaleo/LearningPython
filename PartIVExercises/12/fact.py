#!/usr/bin/env python3

import timeit
from functools import reduce
import math

def fact1(N):
    if N == 1: return N
    else: return N*fact1(N-1)

def fact2(N):
    return reduce((lambda x, y: x * y), range(N, 1, -1))

def fact3(N):
    prod = 1
    for i in range(N, 1, -1):
        prod *= i
    return prod

print(fact1(3))
print(fact2(3))
print(fact3(3))

m = timeit.timeit(number=10000, stmt='fact1(3)', setup='from __main__ import fact1')
print(m)

m = timeit.timeit(number=10000, stmt='fact2(3)', setup='from __main__ import fact2')
print(m)

m = timeit.timeit(number=10000, stmt='fact3(3)', setup='from __main__ import fact3')
print(m)

m = timeit.timeit(number=10000, stmt='math.factorial(3)', setup='import math')
print(m)
