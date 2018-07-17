#!/usr/bin/env python

class C: pass
X = C()
print(type(X), type(C))
print(isinstance(X, object))
print(isinstance(C, object))

print(type('spam'), type(str))
print(isinstance('spam', object))
print(isinstance(str, object))

print(type(type), type(object))
print(isinstance(type, object))
print(isinstance(object, type))

print(C.__base__)
print(C().__repr__)
