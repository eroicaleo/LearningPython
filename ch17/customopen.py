#!/usr/local/bin/python3.3

import builtins

def makeopen(id):
    original = builtins.open
    def custom(*kargs, **pargs):
        print('Custom open call %r:' % id, kargs, pargs)
        return original(*kargs, **pargs)
    builtins.open = custom

print(open('first.py').read(), end='')

makeopen('spam')
F = open('first.py')
print(F.read(), end='')
F.close()

