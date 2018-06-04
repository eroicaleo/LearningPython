#!/usr/bin/env python

class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

X = Number(5)
Y = X - 2
print(Y.data)
