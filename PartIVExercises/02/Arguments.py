#!/usr/bin/env python3

def Arguments(x, y):
    return x+y

print(Arguments(1, 2))
print(Arguments("Hello, ", "world!"))
print(Arguments(2.3, 7.2))
print(Arguments([1, 2], [3, 4, 5]))
"""
Traceback (most recent call last):
File "./Arguments.py", line 10, in <module>
print(Arguments({1: 'a'}, {2: 'b'}))
File "./Arguments.py", line 4, in Arguments
return x+y
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
"""
# print(Arguments({1: 'a'}, {2: 'b'}))
