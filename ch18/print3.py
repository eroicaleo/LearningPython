#!/usr/local/bin/python3.3

import sys

def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output+end)

print3(1, 2, 3)
print3(1, 2, 3, sep='') # Suppress separator
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...') # Various object types
print3(4, 5, 6, sep='', end='') # Suppress newline
print3(7, 8, 9)
print3() # Add newline (or blank line)
print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr) # Redirect to file

def print3_alt(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output+end)

print3_alt(1, 2, 3)
print3_alt(1, 2, 3, sep='') # Suppress separator
print3_alt(1, 2, 3, sep='...')
print3_alt(1, [2], (3,), sep='...') # Various object types
print3_alt(4, 5, 6, sep='', end='') # Suppress newline
print3_alt(7, 8, 9)
print3_alt() # Add newline (or blank line)
print3_alt(1, 2, 3, sep='??', end='.\n', file=sys.stderr) # Redirect to file
"""
TypeError: print3_alt() got an unexpected keyword argument 'name'
print3_alt(99, name='bob')
"""


