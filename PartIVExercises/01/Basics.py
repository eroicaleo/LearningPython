#!/usr/bin/env python3

def basic(x):
    print(x)

basic("Hello, world")
basic(1234567)
basic([1, 2, 3])
basic({1:'a', 2:'b', 3:'c'})
basic({1, 2, 1})
# These two will cause problems:
"""
Traceback (most recent call last):
File "./Basics.py", line 11, in <module>
basic()
TypeError: basic() missing 1 required positional argument: 'x'
"""
# basic()
"""
Traceback (most recent call last):
File "./Basics.py", line 11, in <module>
basic(1, 2)
TypeError: basic() takes 1 positional argument but 2 were given
"""
# basic(1, 2)
