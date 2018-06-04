#!/usr/bin/env python

class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        self.val += other
        return self

x = Number(5)
x += 1
x += 1
print(x.val)

y = Number([1])
y += [2]
y += [3]
print(y.val)
