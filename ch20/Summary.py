#!/usr/bin/env python3

print([x*x for x in range(10)])

print((x*x for x in range(10)))
print(list(x*x for x in range(10)))

print({x*x for x in range(10)})
print({x: x*x for x in range(10)})

X = 99
print(X)
print([X for X in range(4)])
print(X)
