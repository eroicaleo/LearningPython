#!/usr/bin/env python3

def countdown(n):
    if n <= 0:
        print()
        return
    print(n, end=' ')
    countdown(n-1)

countdown(5)

print(list(range(5, 0, -1)))

print(list(x for x in range(5, 0, -1)))

def countdown2(n):
    if n <= 0:
        yield 'stop'
    else:
        yield n
        for i in countdown2(n-1): yield i

print(list(countdown2(5)))
