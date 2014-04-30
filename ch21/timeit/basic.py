#!/usr/bin/env python3

import timeit

L = list(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=100, repeat=5))
print(L)
