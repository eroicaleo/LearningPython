#!/usr/bin/env python

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return SquaresIterator(self.start, self.stop)

class SquaresIterator:
    def __init__(self, start, stop):
        self.stop = stop
        self.offset = start
    def __next__(self):
        if self.offset > self.stop:
            raise StopIteration
        else:
            val = self.offset ** 2
            self.offset += 1
            return val

S = Squares(1, 5)
I = iter(S)
print('I:', next(I))
print('I:', next(I))
J = iter(S)
print('J:', next(J))
print('I:', next(I))

for i in S:
    for j in S:
        print('%d:%d' % (i, j), end=' ')
print()


