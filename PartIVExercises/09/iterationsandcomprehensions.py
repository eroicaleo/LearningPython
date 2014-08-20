#!/usr/bin/env python3

import math

L = [1, 4, 9, 16, 25]

L1 = []
for l in L:
    L1.append(math.sqrt(l))
print(L1)

L2 = map(math.sqrt, L)
print(list(L2))

L3 = [math.sqrt(l) for l in L]
print(L3)

L4 = (math.sqrt(l) for l in L)
print(list(L4))
