#!/usr/bin/env python3

def varargs(*args):
    if len(args) == 0:
        return None
    res = args[0]
    for arg in args[1:]:
        res += arg
    return res

print(varargs(1, 2, 3, 4, 5))
print(varargs([1, 2], [3, 4], [5]))
print(varargs())
"""
Traceback (most recent call last):
File "./varargs.py", line 14, in <module>
print(varargs({1: 'a'}, {2: 'b'}))
File "./varargs.py", line 8, in varargs
res += arg
TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
"""
# print(varargs({1: 'a'}, {2: 'b'}))
