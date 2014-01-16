#!/usr/local/bin/python3.3

import sys

print(len(dir(sys)))

print(len([x for x in dir(sys) if not x.startswith('__')]))
print(len([x for x in dir(sys) if not x[0] == '_']))

print('Attibute of list type:')
print(dir([]))
print('Attibute of string type:')
print(dir(''))

def dir1(x): return [a for a in dir(x) if not a.startswith('__')]

print(dir1(tuple))
print(dir1(str))
