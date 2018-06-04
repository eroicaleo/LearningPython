#!/usr/bin/env python

class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)

C = Callee()
C(1, 2, 3)
C(1, 2, 3, x=4, y=5)

X = Callee()
X(1, 2)
X(1, 2, 3, 4)
X(a=1, b=2, d=4)
X(*[1, 2], **dict(c=3, d=4))
X(1, *(2,), c=3, **dict(d=4))

def callback(color):
    def oncall():
        print('turn', color)
    return oncall

cb3 = callback('yellow')
cb3()

cb4 = (lambda color='red': 'turn ' + color)
print(cb4())
