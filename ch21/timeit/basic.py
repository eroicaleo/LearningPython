#!/usr/bin/env python3

import timeit

L = list(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=100, repeat=5))
print(L)

m = min(timeit.repeat(number=1000, repeat=4,
    stmt="L = [1, 2, 3, 4, 5]\nfor i in range(5):\n\tL[i] += 1"))
print(m)

m = min(timeit.repeat(number=1000, repeat=4,
    stmt="L = [1, 2, 3, 4, 5]\ni = 0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"))
print(m)

m = min(timeit.repeat(number=1000, repeat=4,
    stmt="L = [1, 2, 3, 4, 5]\nM = [i + 1 for i in L]"))
print(m)

from timeit import repeat

import importlib

m = min(repeat(number=1000, repeat=3,
    setup="vals = list(range(1000))",
    stmt="min(*vals)"))
print(m)

m = min(repeat(number=1000, repeat=3,
    setup="import random\nvals = [random.random() for i in range(1000)]",
    stmt="min(*vals)"))
print(m)

m = timeit.timeit(number=1000,
        stmt="[x ** 2 for x in range(1000)]")
print(m)
m = timeit.Timer(stmt="[x ** 2 for x in range(1000)]").timeit(1000)
print(m)

def testcase():
    y = [x ** 2 for x in range(1000)]
m = timeit.timeit(number=1000,
        stmt=testcase)
print(m)
