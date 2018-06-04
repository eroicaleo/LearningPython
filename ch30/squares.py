#!/usr/bin/env python

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):
    print(i, end=' ')
print()

X = Squares(1, 5)
I = iter(X)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))

X = Squares(1, 5)
print(list(X)[1])
print(':'.join(map(str, Squares(1, 5))))

# generator implementation
def gsquares(start, stop):
    for i in range(start, stop+1):
        yield i ** 2

for i in gsquares(1, 5):
    print(i, end=' ')
print()

for i in (x ** 2 for x in range(1, 6)):
    print(i, end=' ')
print()

S = 'ace'
for x in S:
    for y in S:
        print(x+y, end=' ')
print()
