#!/usr/bin/env python

class C1:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)

class C2:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)

class C3(C1, C2): pass
I = C3()

I.meth1(); I.metha();
print(I.__dict__)
I.meth2(); I.methb();
