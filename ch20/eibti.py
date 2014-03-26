#!/usr/bin/python3.3

import math

print(math.factorial(10))

from permute import permute2
seq = list(range(10))
p2 = permute2(seq)
print(next(p2))
print(next(p2))

seq = list(range(50))
p3 = permute2(seq)
print(next(p3))

import random

seq = list(range(20))
p4 = permute2(seq)
print(next(p4))
print(next(p4))

random.shuffle(seq)
print(next(p4))
print(next(p4))
