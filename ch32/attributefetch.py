#!/usr/bin/env python

class C:
    data = 'spam'
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)
    def __len__(self): return len(self.data)

X = C()
print(X)
print(len(X))
# Exception
# X[0]

class C: pass
X = C()
X.normal = lambda: 99
print(X.normal())
X.__add__ = lambda y: 88 + y
print(X.__add__(1))
# Exception
# print(X + 1)

class C:
    def __getattr__(self, name):
        print(name)
X = C()
X.normal
X.__add__
# Exception
# X + 1

class C:
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)

X = C()
print(X.__getitem__(1))
# Exception
# X[1]
# type(X).__getitem__(X, 1)
print(X.__add__('eggs'))
print(X)
# Exception
# X + 'eggs'
# type(X).__add__(X, 'eggs')

class C:
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)
    def __getitem__(self, i):
        print('getitem: ' + str(i))
        return self.data[i]
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)

X = C()
print(X.upper)
print(X.upper())
print(X[1])
type(X).__getitem__(X, 1)
print(X + 'eggs')
print(type(X).__add__(X, 'eggs'))
print(X.__add__('eggs'))
