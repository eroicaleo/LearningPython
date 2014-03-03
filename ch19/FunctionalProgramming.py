#!/usr/local/bin/python3.3

def inc(x): return x + 10

counters = [1, 2, 3, 4]
print(list(map(inc, counters)))

L = list(map(lambda x: x+3, counters))
print(L)

L = list(map(pow, [1, 2, 3], [2, 3, 4]))
print(L)

L = list(map(inc, [1, 2, 3, 4]))
print(L)

L = [inc(x) for x in [1, 2, 3, 4]]
print(L)

L = list(range(-5, 5))
print(L)

L = list(filter(lambda x: x > 0, L))
print(L)

L = [x for x in range(-5, 5) if x > 0]
print(L)

from functools import reduce
L = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(L)
L = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(L)

def myreduce(function, sequence):
    tally = sequence[0]
    for x in sequence[1:]:
        tally = function(tally, x)
    return tally

L = myreduce((lambda x, y: x + y), [1, 2, 3, 4])
print(L)
L = myreduce((lambda x, y: x * y), [1, 2, 3, 4])
print(L)

import functools, operator
L = myreduce(operator.add, [1, 2, 3, 4])
print(L)
