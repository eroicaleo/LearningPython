#!/usr/bin/env python3

from unders import *

print(a, c)
'''
NameError: name '_b' is not defined
print(_b)
'''

import unders

print(unders._b)

from all import *

print(a, _c)

'''
NameError: name 'b' is not defined
print(b)
'''

import all
print(all.a, all.b, all._c, all._d)
