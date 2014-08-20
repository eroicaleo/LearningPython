#!/usr/bin/env python3

def primes(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime.')

primes(13)
primes(13.0)
primes(15)
primes(15.0)
