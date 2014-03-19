#!/usr/bin/python3.3

def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i, end=":")
print()

x = gensquares(4)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
