#!/usr/local/bin/python3.3

def f(a, b, c):
    print(a, b, c)
    return

f(1, 2, 3)

f(c=1, b=2, a=3)

f(1, b=2, c=3)

"""
This is wrong:
f(1, b=2, a=3)
will get
TypeError: f() got multiple values for argument 'a'
"""

def f(a, b=99, c=100):
    print(a, b, c)
    return

f(1)
f(2, 35, 46)
f(1, c=6)

def f(**args):
    print(args)
    return

f(a=1, b=2)

def f(a, *pargs, **kargs):
    print(a, pargs, kargs)
    return

f(1, 2, 3, x=4, y=5)

def f(a, b, c, d):
    print(a, b, c, d)
    return

f(**{'a': 1, 'b': 2, 'c': 3, 'd': 4})
f(*[1, 2], **{'c': 3, 'd': 4})
f(1, *(2, 3), **{'d': 4})
f(1, c=3, *(2,), **{'d': 4})
f(1, c=3, *[2], **{'d': 4})

def Tracer(func, *pargs, **kargs):
    print('Calling: ', func.__name__)
    return func(*pargs, **kargs)

def func(a, b, c, d):
    print(a+b+c+d)
    return

Tracer(func, 1, 2, c=3, d=4)

def kwonly(a, *b, c):
    print(a, b, c)
    return

kwonly(1, 2, c=3)
kwonly(1, c=3)
"""
TypeError: kwonly() missing 1 required keyword-only argument: 'c'
kwonly(1, 2, 3)
"""

def f(a, *b, c=6, **d):
    print(a, b, c, d)
    return

f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=5, c=7)
f(1, 2, 3, c=7, x=4, y=5)
