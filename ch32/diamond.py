#!/usr/bin/env python

class A: attr = 1
class B(A): pass;
class C(A): attr = 2;
class D(B, C): pass

x = D()
print(x.attr)

class D(B, C): attr = B.attr
x = D()
print(x.attr)

class A:
    def meth(s): print('A.meth')

class C(A):
    def meth(s): print('C.meth')

class B(A): pass

class D(B, C): pass
x = D()
x.meth()
class D(B, C): meth = B.meth
x = D()
x.meth()
