#!/usr/bin/env python

class C:
    pass

I = C()
print(type(I), I.__class__)

print(type(C), C.__class__, int.__class__, type(str))

class D:
    pass

c, d = C(), D()
print(type(c) == type(d))
print(type(c), type(d))
print(c.__class__, d.__class__)
c1, c2 = C(), C()
print(type(c1) == type(c2))
