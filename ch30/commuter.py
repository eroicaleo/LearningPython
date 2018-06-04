#!/usr/bin/env python

class Adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other
    def __str__(self):
        return str(self.data)

x = Adder(5)
x + 2
print(x)
# 2 + x

class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

x = Commuter1(88)
y = Commuter1(99)
print(x+1)
print(1+y)
print(x+y)

class Commuter2:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self.__add__(other)

x = Commuter2(288)
y = Commuter2(299)
print(x+1)
print(1+y)
print(x+y)

class Commuter3:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self + other

x = Commuter3(388)
y = Commuter3(399)
print(x+1)
print(1+y)
print(x+y)

class Commuter4:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    __radd__ = __add__

x = Commuter4(488)
y = Commuter4(499)
print(x+1)
print(1+y)
print(x+y)

class Commuter5:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)
    def __radd__(self, other):
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuter5: %s>' % self.val

x = Commuter5(88)
y = Commuter5(99)
print(x + 10)
print(10 + y)
z = x + y 
print(z)
print(z + 10)
print(z + z)
print(z + z + 1)
