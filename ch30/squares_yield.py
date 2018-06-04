#!/usr/bin/env python

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for i in range(self.start, self.stop+1):
            yield i ** 2
 

for i in Squares(1, 5):
    print(i, end=' ')
print()

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

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def gen(self):
        for i in range(self.start, self.stop+1):
            yield i ** 2
 

S = Squares(1, 5)
I = iter(S.gen())
print(next(I))
print(next(I))

